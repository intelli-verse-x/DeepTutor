"""Auth router — login, logout, status, registration, and user-management endpoints."""

from contextvars import Token as _CtxToken
import logging

from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    Header,
    HTTPException,
    Response,
    WebSocket,
    status,
)
from pydantic import BaseModel, field_validator

from deeptutor.services.config import load_auth_settings

# SameSite=None lets the cookie work when the browser accesses the frontend via
# 127.0.0.1 and the backend via localhost (different origins on the same machine).
# Browsers require Secure=True for SameSite=None, but that needs HTTPS — so in
# local dev we fall back to SameSite=Lax and tell users to use localhost:// URLs.
_SECURE = bool(load_auth_settings()["cookie_secure"])
_SAMESITE = "none" if _SECURE else "lax"

from deeptutor.multi_user.context import set_current_user, user_from_token_payload
from deeptutor.multi_user.paths import local_admin_user
from deeptutor.services.auth import (
    AUTH_ENABLED,
    POCKETBASE_ENABLED,
    TOKEN_EXPIRE_HOURS,
    TokenPayload,
    add_user,
    authenticate,
    authenticate_pb,
    create_token,
    decode_token,
    delete_user,
    is_first_user,
    list_users,
    register_pb,
    set_role,
)

logger = logging.getLogger(__name__)

router = APIRouter()

_COOKIE_NAME = "dt_token"
_COOKIE_MAX_AGE = TOKEN_EXPIRE_HOURS * 3600


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------


class LoginRequest(BaseModel):
    """Payload for the POST /login endpoint."""

    username: str
    password: str


class RegisterRequest(BaseModel):
    """Payload for the POST /register endpoint."""

    username: str
    password: str

    @field_validator("username")
    @classmethod
    def username_valid(cls, v: str) -> str:
        import re

        v = v.strip()
        if not v:
            raise ValueError("Email cannot be empty")
        # Accept standard email addresses (used by PocketBase mode) or plain
        # usernames (used by the built-in SQLite/JSON auth mode).
        email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        plain_re = re.compile(r"^[A-Za-z0-9_\-.]{3,64}$")
        if not email_re.match(v) and not plain_re.match(v):
            raise ValueError("Enter a valid email address")
        return v

    @field_validator("password")
    @classmethod
    def password_valid(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v


class SetRoleRequest(BaseModel):
    """Payload for the PUT /users/{username}/role endpoint."""

    role: str

    @field_validator("role")
    @classmethod
    def role_valid(cls, v: str) -> str:
        if v not in ("admin", "user"):
            raise ValueError("Role must be 'admin' or 'user'")
        return v


class AuthStatusResponse(BaseModel):
    """Response body for the GET /status endpoint."""

    enabled: bool
    authenticated: bool
    user_id: str | None = None
    username: str | None = None
    role: str | None = None
    is_admin: bool = False


class UserInfo(BaseModel):
    """Single user record returned by the GET /users endpoint."""

    id: str = ""
    username: str
    role: str
    created_at: str
    disabled: bool = False


# ---------------------------------------------------------------------------
# Shared helper — extract token from cookie or Bearer header
# ---------------------------------------------------------------------------


def _bearer_token_from_header(authorization: str | None) -> str | None:
    """Parse ``Authorization: Bearer <token>`` without using ``HTTPBearer``.

    ``HTTPBearer`` is a class-based dependency whose ``__call__`` is annotated
    ``request: Request``. FastAPI doesn't inject a Request into WebSocket
    dependency resolution, which makes ``HTTPBearer`` raise ``TypeError`` the
    moment a router with this dep mounts a WS endpoint. Doing the parse by
    hand keeps ``require_auth`` HTTP/WS-symmetric.
    """
    if not authorization:
        return None
    parts = authorization.split(None, 1)
    if len(parts) == 2 and parts[0].lower() == "bearer":
        token = parts[1].strip()
        return token or None
    return None


def _extract_token(authorization: str | None, dt_token: str | None) -> str | None:
    return _bearer_token_from_header(authorization) or dt_token


# ---------------------------------------------------------------------------
# Dependencies — reusable auth guards for other routers
# ---------------------------------------------------------------------------


def _install_current_user(payload: TokenPayload | None) -> _CtxToken:
    """Install the request-local current-user ContextVar from an auth result.

    Single point of truth for ``payload → CurrentUser`` so HTTP and WebSocket
    entry points produce identical user objects. ``payload is None`` means
    "no JWT was required" (AUTH_ENABLED=false) and resolves to the local
    admin user; a non-None payload resolves through ``user_from_token_payload``.

    Returns the ContextVar reset token. HTTP callers ignore it (the request
    ends with the task, so the var is GC'd with the task context). WebSocket
    callers keep it and call ``reset_current_user`` in their ``finally`` block,
    because a WS connection outlives the dependency-resolution task.

    ⚠ Invariant: every authenticated entry point MUST call this before the
    handler runs. Skipping it leaves ``get_current_path_service()`` falling
    back to the admin workspace — the silent-routing root cause of #481.
    """
    user = local_admin_user() if payload is None else user_from_token_payload(payload)
    return set_current_user(user)


def _install_noauth_user(x_user_id: str) -> _CtxToken:
    """Install the current user from the ``x-user-id`` header when AUTH is off.

    The fork drives multi-tenancy from ``x-user-id`` instead of upstream's login.
    When ``AUTH_ENABLED=false`` we must still give each tenant its OWN per-user
    scope, otherwise every request resolves to the local-admin workspace and all
    users silently share one global store (cross-user leak across memory /
    knowledge / books). An empty / missing id keeps the legacy single-user
    behaviour (admin workspace), so CLI usage is unchanged.
    """
    from deeptutor.multi_user.models import LOCAL_ADMIN_ID, CurrentUser
    from deeptutor.multi_user.paths import scope_for_user

    uid = (x_user_id or "").strip()
    if not uid or uid == LOCAL_ADMIN_ID:
        return set_current_user(local_admin_user())
    user = CurrentUser(
        id=uid,
        username=uid,
        role="user",
        scope=scope_for_user(uid, is_admin=False),
    )
    return set_current_user(user)


async def require_auth(
    authorization: str | None = Header(default=None, alias="Authorization"),
    dt_token: str | None = Cookie(default=None),
    x_user_id: str = Header(default="", alias="x-user-id"),
) -> TokenPayload | None:
    """
    FastAPI dependency that enforces authentication when AUTH_ENABLED=true.

    Accepts the JWT from either:
      - Authorization: Bearer <token> header
      - dt_token cookie

    ``Header`` and ``Cookie`` are kept here in place of ``HTTPBearer`` so the
    function stays usable from WebSocket call sites that don't go through
    FastAPI's standard HTTP request lifecycle.

    Returns the authenticated TokenPayload, or None if auth is disabled.
    Raises HTTP 401 if auth is enabled but the token is missing or invalid.

    Declared ``async def`` so the ``set_current_user`` call runs in the same
    asyncio context as the endpoint. A sync dependency is dispatched via
    ``anyio.to_thread.run_sync``, which executes the function in a worker
    thread under a *copy* of the request context; any ``ContextVar.set``
    inside that thread is discarded when the thread returns, leaving the
    endpoint to read the unset default. That regression was the root cause
    of #481.
    """
    if not AUTH_ENABLED:
        _install_noauth_user(x_user_id)
        return None

    token = _extract_token(authorization, dt_token)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    _install_current_user(payload)
    return payload


class _WsAuthFailed:
    """Sentinel: ws_require_auth failed and closed the WebSocket."""


ws_auth_failed: _WsAuthFailed = _WsAuthFailed()


async def ws_require_auth(ws: WebSocket) -> _CtxToken | _WsAuthFailed:
    """Authenticate a WebSocket connection and set the user ContextVar.

    Must be called **before** ``ws.accept()`` so the server can reject
    unauthenticated upgrades cleanly.

    Returns a ContextVar reset token on success, or ``ws_auth_failed``
    on failure (the WebSocket is already closed — the caller should
    ``return`` immediately).

    Usage::

        user_token = await ws_require_auth(ws)
        if user_token is ws_auth_failed:
            return
        await ws.accept()
        try:
            ...
        finally:
            reset_current_user(user_token)
    """
    if not AUTH_ENABLED:
        # Browsers cannot set custom headers on WebSocket upgrades, so the SPA
        # passes the tenant as a query param (?user_id=). Fall back to the
        # x-user-id header for non-browser clients.
        uid = (
            ws.query_params.get("user_id")
            or ws.query_params.get("x_user_id")
            or ws.headers.get("x-user-id")
            or ""
        )
        return _install_noauth_user(uid)

    token = ws.query_params.get("token") or ws.cookies.get("dt_token")
    payload = decode_token(token) if token else None
    if not payload:
        await ws.close(code=4001)
        return ws_auth_failed

    return _install_current_user(payload)


async def require_admin(
    payload: TokenPayload | None = Depends(require_auth),
) -> TokenPayload:
    """
    FastAPI dependency that requires the caller to be an admin.

    Raises HTTP 403 if the authenticated user is not an admin.
    When AUTH_ENABLED=false, all requests are treated as admin.

    ``async def`` mirrors ``require_auth`` so the dependency chain stays on
    the event loop and the user ContextVar set by ``require_auth`` is visible
    to the endpoint.
    """
    if not AUTH_ENABLED:
        return _local_admin_token_payload()

    if payload is None or payload.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return payload


def _local_admin_token_payload() -> TokenPayload:
    """Synthetic admin payload used when AUTH_ENABLED=false.

    Mirrors the local admin identity (LOCAL_ADMIN_USERNAME / LOCAL_ADMIN_ID)
    so audit logs and self-reference checks behave the same as in multi-user
    mode. Values are kept aligned with ``local_admin_user()`` in
    ``deeptutor/multi_user/paths.py``.
    """
    from deeptutor.multi_user.models import LOCAL_ADMIN_ID, LOCAL_ADMIN_USERNAME

    return TokenPayload(
        username=LOCAL_ADMIN_USERNAME,
        role="admin",
        user_id=LOCAL_ADMIN_ID,
    )


# ---------------------------------------------------------------------------
# Public endpoints (no auth required)
# ---------------------------------------------------------------------------


@router.get("/status", response_model=AuthStatusResponse)
async def auth_status(
    authorization: str | None = Header(default=None, alias="Authorization"),
    dt_token: str | None = Cookie(default=None),
) -> AuthStatusResponse:
    """Return whether auth is enabled and whether the current request is authenticated."""
    if not AUTH_ENABLED:
        return AuthStatusResponse(
            enabled=False,
            authenticated=True,
            user_id="local-admin",
            username="local",
            role="admin",
            is_admin=True,
        )

    token = _extract_token(authorization, dt_token)
    payload = decode_token(token) if token else None
    return AuthStatusResponse(
        enabled=True,
        authenticated=payload is not None,
        user_id=payload.user_id if payload else None,
        username=payload.username if payload else None,
        role=payload.role if payload else None,
        is_admin=payload.role == "admin" if payload else False,
    )


@router.post("/login")
async def login(body: LoginRequest, response: Response) -> dict:
    """Validate credentials and set a JWT cookie."""
    if not AUTH_ENABLED:
        return {"ok": True, "message": "Auth is disabled — no login required."}

    if POCKETBASE_ENABLED:
        # PocketBase mode: email = username field for backwards-compat with the
        # existing LoginRequest schema; users can pass their email as "username".
        pb_result = authenticate_pb(body.username, body.password)
        if not pb_result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
        payload, pb_token = pb_result
        response.set_cookie(
            key=_COOKIE_NAME,
            value=pb_token,
            httponly=True,
            samesite=_SAMESITE,
            max_age=_COOKIE_MAX_AGE,
            secure=_SECURE,
        )
        logger.info(f"User '{payload.username}' logged in via PocketBase (role={payload.role!r})")
        return {
            "ok": True,
            "user_id": payload.user_id,
            "username": payload.username,
            "role": payload.role,
            "is_admin": payload.role == "admin",
        }

    # Standard JWT + bcrypt mode
    result = authenticate(body.username, body.password)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = create_token(result.username, result.role, result.user_id)
    response.set_cookie(
        key=_COOKIE_NAME,
        value=token,
        httponly=True,
        samesite=_SAMESITE,
        max_age=_COOKIE_MAX_AGE,
        secure=_SECURE,
    )

    logger.info(f"User '{result.username}' logged in (role={result.role!r})")
    return {
        "ok": True,
        "user_id": result.user_id,
        "username": result.username,
        "role": result.role,
        "is_admin": result.role == "admin",
    }


@router.post("/logout")
async def logout(response: Response) -> dict:
    """Clear the JWT cookie."""
    response.delete_cookie(key=_COOKIE_NAME, samesite=_SAMESITE)
    return {"ok": True}


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest) -> dict:
    """
    Bootstrap-only registration.

    Public endpoint that creates the *first* admin account when the user store
    is empty. Once an admin exists, this endpoint is closed; further accounts
    must be created by an admin via ``POST /api/v1/auth/users``.

    Only available when AUTH_ENABLED=true.
    """
    if not AUTH_ENABLED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Auth is disabled — registration is not available.",
        )

    if POCKETBASE_ENABLED:
        # PocketBase deployments are documented as single-user. Keep registration
        # closed and require admins to provision users in the PocketBase admin UI.
        if not is_first_user():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Self-registration is closed. Ask an administrator to create your account.",
            )
        result = register_pb(username=body.username, email=body.username, password=body.password)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Registration failed — username or email may already be taken.",
            )
        logger.info(f"First user registered via PocketBase: '{body.username}'")
        return {
            "ok": True,
            "user_id": result.get("id", ""),
            "username": body.username,
            "role": "user",
            "is_first_user": True,
            "is_admin": False,
        }

    # Standard mode — only allowed before the first admin exists.
    if not is_first_user():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Self-registration is closed. Ask an administrator to create your account.",
        )

    existing = {u["username"] for u in list_users()}
    if body.username in existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken",
        )

    add_user(body.username, body.password)
    user_id = ""
    role = "user"
    for item in list_users():
        if item.get("username") == body.username:
            user_id = str(item.get("id") or "")
            role = str(item.get("role") or "user")
            break
    logger.info(f"First user (admin) registered: '{body.username}'")
    return {
        "ok": True,
        "user_id": user_id,
        "username": body.username,
        "role": role,
        "is_first_user": True,
        "is_admin": role == "admin",
    }


@router.get("/is_first_user")
async def check_is_first_user() -> dict:
    """Return whether the user store is empty (used by the register UI)."""
    return {"is_first_user": is_first_user() if AUTH_ENABLED else False}


# ---------------------------------------------------------------------------
# Admin-only endpoints
# ---------------------------------------------------------------------------


@router.get("/users", response_model=list[UserInfo])
async def get_users(_: TokenPayload = Depends(require_admin)) -> list[UserInfo]:
    """List all registered users. Requires admin role."""
    return [UserInfo(**u) for u in list_users()]


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def admin_create_user(
    body: RegisterRequest,
    current: TokenPayload = Depends(require_admin),
) -> dict:
    """Admin-only: create a new user account.

    Replaces the public ``/register`` flow once the first admin exists. The
    new account is always created with role=``user``; admins can promote
    later via ``PUT /users/{username}/role``.
    """
    if not AUTH_ENABLED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Auth is disabled — user creation is not available.",
        )

    if POCKETBASE_ENABLED:
        result = register_pb(username=body.username, email=body.username, password=body.password)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Failed to create user — username may already be taken.",
            )
        logger.info(
            f"Admin '{current.username if current else 'local'}' created PocketBase user "
            f"'{body.username}'"
        )
        return {
            "ok": True,
            "user_id": result.get("id", ""),
            "username": body.username,
            "role": "user",
            "is_admin": False,
        }

    existing = {u["username"] for u in list_users()}
    if body.username in existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken",
        )

    add_user(body.username, body.password)
    user_id = ""
    role = "user"
    for item in list_users():
        if item.get("username") == body.username:
            user_id = str(item.get("id") or "")
            role = str(item.get("role") or "user")
            break
    logger.info(
        f"Admin '{current.username if current else 'local'}' created user '{body.username}' "
        f"(role={role!r})"
    )
    return {
        "ok": True,
        "user_id": user_id,
        "username": body.username,
        "role": role,
        "is_admin": role == "admin",
    }


@router.delete("/users/{username}", status_code=status.HTTP_200_OK)
async def remove_user(
    username: str,
    current: TokenPayload = Depends(require_admin),
) -> dict:
    """Delete a user. Admins cannot delete their own account."""
    if current and username == current.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot delete your own account",
        )

    removed = delete_user(username)
    if not removed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    logger.info(f"Admin '{current.username if current else 'local'}' deleted user '{username}'")
    return {"ok": True}


@router.put("/users/{username}/role", status_code=status.HTTP_200_OK)
async def update_user_role(
    username: str,
    body: SetRoleRequest,
    current: TokenPayload = Depends(require_admin),
) -> dict:
    """Change a user's role. Admins cannot change their own role."""
    if current and username == current.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot change your own role",
        )

    updated = set_role(username, body.role)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    logger.info(
        f"Admin '{current.username if current else 'local'}' set '{username}' role to {body.role!r}"
    )
    return {"ok": True, "username": username, "role": body.role}


# ===========================================================================
# Anonymous bearer-token issuance (BUG-101) — preserved from fork prod main.
#
# Coexists with the session-cookie auth above. Clients may keep sending a raw
# ``x-user-id`` header while ``DEEPTUTOR_REQUIRE_AUTH`` is unset; these
# endpoints let the TutorX SPA / Unity / RN clients mint + refresh a stdlib
# HS256 JWT with zero new dependencies. The routes (/anonymous, /refresh,
# /whoami) do not collide with the session routes above, and the helper
# symbols (encode_token, decode_and_verify, ...) are unique to this block.
# ===========================================================================

import base64
import hashlib
import hmac
import json
import os
import time
import uuid
from typing import Optional

from deeptutor.api.middleware.tenant import get_current_user_id

DEFAULT_TTL_SECONDS = 7 * 24 * 60 * 60  # 7 days


# ---------------------------------------------------------------------------
# Stdlib HS256 JWT (encode + decode + verify) — zero new dependencies.
# Layout: header.payload.signature, each url-safe-base64 (no padding).
# ---------------------------------------------------------------------------

def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(data: str) -> bytes:
    pad = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + pad)


def _hs256_sign(secret: str, signing_input: bytes) -> bytes:
    return hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()


def _ttl_seconds() -> int:
    raw = os.getenv("DEEPTUTOR_AUTH_TOKEN_TTL_SECONDS", "").strip()
    if not raw:
        return DEFAULT_TTL_SECONDS
    try:
        v = int(raw)
        if 60 <= v <= 30 * 24 * 60 * 60:  # 1 minute .. 30 days
            return v
    except ValueError:
        pass
    return DEFAULT_TTL_SECONDS


def _get_secret() -> str:
    secret = os.getenv("DEEPTUTOR_JWT_SECRET", "").strip()
    if not secret:
        # Fail closed: refuse to mint OR verify when the secret is unset.
        raise HTTPException(
            status_code=503,
            detail=(
                "Auth temporarily unavailable. DEEPTUTOR_JWT_SECRET is not "
                "configured on this deployment."
            ),
        )
    if len(secret) < 32:
        # Cheap belt-and-braces check; HS256 secrets shorter than 256 bits are
        # an immediate red flag.
        raise HTTPException(
            status_code=503,
            detail="Auth misconfigured: DEEPTUTOR_JWT_SECRET is too short.",
        )
    return secret


def encode_token(sub: str, ttl_seconds: Optional[int] = None) -> dict:
    """Mint an HS256 token for ``sub``. Returns ``{token, expires_at}``."""
    secret = _get_secret()
    now = int(time.time())
    ttl = ttl_seconds if ttl_seconds is not None else _ttl_seconds()
    exp = now + ttl
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "sub": sub,
        "iat": now,
        "exp": exp,
        "iss": "deeptutor-auth",
    }
    h = _b64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    p = _b64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{h}.{p}".encode("ascii")
    sig = _b64url_encode(_hs256_sign(secret, signing_input))
    return {"token": f"{h}.{p}.{sig}", "expires_at": exp}


def decode_and_verify(token: str) -> dict:
    """Verify ``token`` and return the decoded payload.

    Raises :class:`HTTPException` on every failure mode.
    """
    secret = _get_secret()
    parts = token.split(".")
    if len(parts) != 3:
        raise HTTPException(status_code=401, detail="Malformed token")
    h_b64, p_b64, sig_b64 = parts
    try:
        header = json.loads(_b64url_decode(h_b64))
        payload = json.loads(_b64url_decode(p_b64))
        sig = _b64url_decode(sig_b64)
    except Exception as exc:  # noqa: BLE001
        logger.debug("Token decode failed: %s", type(exc).__name__)
        raise HTTPException(status_code=401, detail="Malformed token") from None
    if header.get("alg") != "HS256" or header.get("typ") != "JWT":
        raise HTTPException(status_code=401, detail="Unsupported token algorithm")
    expected = _hs256_sign(secret, f"{h_b64}.{p_b64}".encode("ascii"))
    if not hmac.compare_digest(expected, sig):
        raise HTTPException(status_code=401, detail="Bad signature")
    if int(payload.get("exp", 0)) < int(time.time()):
        raise HTTPException(status_code=401, detail="Token expired")
    sub = str(payload.get("sub", "")).strip()
    if not sub:
        raise HTTPException(status_code=401, detail="Token missing subject")
    return payload


# ---------------------------------------------------------------------------
# Pydantic request / response models.
# ---------------------------------------------------------------------------

class AnonymousAuthRequest(BaseModel):
    # Optional client hint (e.g. existing localStorage user_id) — accepted only
    # when it is a v4 UUID. Otherwise we mint a fresh one.
    preferred_user_id: Optional[str] = None


class TokenResponse(BaseModel):
    user_id: str
    token: str
    expires_at: int
    token_type: str = "Bearer"
    issued_at: int


class RefreshRequest(BaseModel):
    token: str


class WhoAmIResponse(BaseModel):
    user_id: str
    authenticated: bool


_UUID_V4_RE = __import__("re").compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    __import__("re").IGNORECASE,
)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/anonymous", response_model=TokenResponse)
async def anonymous(body: Optional[AnonymousAuthRequest] = None) -> TokenResponse:
    """Mint a JWT for an anonymous browser session.

    If ``preferred_user_id`` is supplied AND looks like a UUID v4, we re-use
    it (so a returning client preserves its identity across token rotations).
    Otherwise a fresh UUID is minted server-side. **No PII is recorded.**
    """
    sub: Optional[str] = None
    if body and body.preferred_user_id:
        candidate = body.preferred_user_id.strip()
        if _UUID_V4_RE.match(candidate):
            sub = candidate
    if not sub:
        sub = str(uuid.uuid4())
    issued = encode_token(sub)
    return TokenResponse(
        user_id=sub,
        token=issued["token"],
        expires_at=issued["expires_at"],
        issued_at=int(time.time()),
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh(body: RefreshRequest) -> TokenResponse:
    """Re-sign the supplied token's subject with a fresh expiry.

    The submitted token must still be valid (non-expired and well-signed).
    Identity (``sub``) is preserved verbatim.
    """
    payload = decode_and_verify(body.token)
    sub = payload["sub"]
    issued = encode_token(sub)
    return TokenResponse(
        user_id=sub,
        token=issued["token"],
        expires_at=issued["expires_at"],
        issued_at=int(time.time()),
    )


@router.get("/whoami", response_model=WhoAmIResponse)
async def whoami(authorization: Optional[str] = Header(default=None)) -> WhoAmIResponse:
    """Cheap echo endpoint for debugging the auth path.

    Returns the resolved user id from the request context. ``authenticated``
    is ``True`` only when a valid bearer token is also present.
    """
    authenticated = False
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1].strip()
        try:
            decode_and_verify(token)
            authenticated = True
        except HTTPException:
            authenticated = False
    return WhoAmIResponse(
        user_id=get_current_user_id(),
        authenticated=authenticated,
    )

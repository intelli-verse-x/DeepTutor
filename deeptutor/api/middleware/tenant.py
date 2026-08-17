"""Multi-tenant user identification middleware.

Identity is derived **server-side** from a signature-verified bearer token and
stored in a ContextVar so any downstream service can call
`get_current_user_id()` without threading it through every function signature.

Nothing here reads a caller-supplied identity header. The `x-user-id` header
used to be the tenant key, which meant any HTTP client could name itself as any
learner and read/write that learner's tutor history, notebooks, memory,
knowledge bases and exam records. A header is not a credential: it is chosen by
the caller. Identity now comes only from a token this service signed (or, when
`AUTH_ENABLED=true`, from the session JWT), so the caller cannot pick it.

Two accepted token shapes, both verified, neither forgeable without the signing
secret:

* the fork's anonymous HS256 token (`POST /api/v1/auth/anonymous`), whose `sub`
  is the tenant id — see `deeptutor.api.routers.auth.decode_and_verify`;
* the session JWT issued by `deeptutor.services.auth` when `AUTH_ENABLED=true`.

When a request carries neither, the ContextVar holds `_UNVERIFIED` and every
resolver raises 401. It does **not** fall back to a default tenant: guessing an
identity is what made this forgeable in the first place, and a shared fallback
bucket silently mixes different people's data.

For CLI / single-user mode the middleware never runs, so the ContextVar keeps
its `DEEPTUTOR_DEFAULT_USER_ID` default and behaviour is unchanged.
"""

from __future__ import annotations

import contextvars
import os

from fastapi import HTTPException

_DEFAULT_USER_ID = os.getenv("DEEPTUTOR_DEFAULT_USER_ID", "default")

# Stored on the ContextVar for HTTP/WebSocket requests that carried no
# verifiable identity. Deliberately not a legal user id (NUL byte) so it can
# never be mistaken for a tenant key, and never used as a path segment, if some
# future call site reads the ContextVar directly instead of via the accessors.
_UNVERIFIED = "\x00unverified"

_UNAUTHENTICATED_DETAIL = (
    "Not authenticated: a verified bearer token is required. "
    "Mint one with POST /api/v1/auth/anonymous."
)

current_user_id: contextvars.ContextVar[str] = contextvars.ContextVar(
    "current_user_id", default=_DEFAULT_USER_ID
)


def subject_from_authorization(authorization: str | None) -> str | None:
    """Return the verified subject of a bearer token, or ``None``.

    ``None`` covers every failure mode — absent header, wrong scheme, malformed
    token, bad signature, expired, no subject. Callers must treat it as "no
    identity" and refuse, never as "use a default".

    Both verifiers are signature-checked. Imports are local because
    ``deeptutor.api.routers.auth`` imports this module at module scope.
    """
    if not authorization:
        return None
    parts = authorization.split(None, 1)
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None
    token = parts[1].strip()
    if not token:
        return None

    # Session JWT (AUTH_ENABLED=true). Returns None when auth is off or the
    # signing secret is unset, so this is a no-op in anonymous deployments.
    try:
        from deeptutor.services.auth import decode_token

        payload = decode_token(token)
        if payload is not None:
            subject = str(payload.user_id or payload.username or "").strip()
            if subject:
                return subject
    except Exception:  # noqa: BLE001 — fall through to the anonymous verifier
        pass

    # Fork's anonymous HS256 token. Raises HTTPException on every failure mode
    # (including 503 when DEEPTUTOR_JWT_SECRET is unset); swallow it here so the
    # ASGI middleware never raises outside the router, where FastAPI's exception
    # handlers cannot turn it into a response.
    try:
        from deeptutor.api.routers.auth import decode_and_verify

        claims = decode_and_verify(token)
    except HTTPException:
        return None
    except Exception:  # noqa: BLE001 — never let auth plumbing 500 a request
        return None

    subject = str(claims.get("sub", "")).strip()
    return subject or None


def require_identity_enforced() -> bool:
    """Whether an identity-less HTTP/WebSocket request must be refused outright.

    Set ``DEEPTUTOR_REQUIRE_IDENTITY=true`` on any shared or internet-facing
    deployment. **This is required to fully close the tenancy hole.**

    The tenant-scoped resolvers above always fail closed, so no caller can reach
    another *named* learner regardless of this flag. But upstream's
    ``AUTH_ENABLED=false`` mode resolves an identity-less request to the local
    admin workspace, and roughly two dozen routers (chat, knowledge, book, …)
    take their scope from that context rather than calling ``require_user_id``.
    On a single-user localhost install that is correct and is upstream's whole
    design. On a shared deployment it means an anonymous caller reads and writes
    the admin workspace.

    Defaulting to off keeps upstream's local single-user product working
    unchanged; a deployment that serves more than one person must turn it on.
    """
    return os.getenv("DEEPTUTOR_REQUIRE_IDENTITY", "").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def get_current_user_id() -> str:
    """Return the verified user_id for the current request.

    Raises 401 when the request carried no verifiable identity. Raising (rather
    than returning a default) is what makes the indirect resolvers in
    ``knowledge/tenant_manager.py``, ``services/notebook/pg_manager.py`` and
    ``services/session/pg_store.py`` fail closed without each needing its own
    check — they resolve tenancy through this function.
    """
    uid = current_user_id.get()
    if uid == _UNVERIFIED:
        raise HTTPException(status_code=401, detail=_UNAUTHENTICATED_DETAIL)
    return uid


def get_current_user_id_or_none() -> str | None:
    """Non-raising variant for diagnostics (``/auth/whoami``)."""
    uid = current_user_id.get()
    return None if uid == _UNVERIFIED else uid


def _bridge_upstream_user(uid: str):
    """Mirror the verified subject into upstream's ``multi_user`` context.

    Upstream v1.4 scopes per-user data (memory, knowledge, workspaces) via its
    own ``CurrentUser`` ContextVar + ``PathService``. The fork drives tenancy
    from the verified token subject instead of upstream's login system, so we
    bridge the two: every request populates upstream's context from the same
    id. This makes upstream's per-user isolation work without enabling
    upstream's auth (``require_auth`` stays a no-op when ``AUTH_ENABLED=false``).

    Returns ``(token, reset_fn)`` or ``(None, None)`` if multi_user is absent.
    """
    try:
        from deeptutor.multi_user.context import (
            reset_current_user,
            set_current_user,
        )
        from deeptutor.multi_user.models import CurrentUser
        from deeptutor.multi_user.paths import scope_for_user
    except Exception:  # noqa: BLE001 — multi_user optional; tenancy still works via fork ctx
        return None, None

    try:
        user = CurrentUser(
            id=uid,
            username=uid,
            role="user",
            scope=scope_for_user(uid, is_admin=False),
        )
        return set_current_user(user), reset_current_user
    except Exception:  # noqa: BLE001
        return None, None


class TenantMiddleware:
    """Pure-ASGI middleware that binds the per-request tenant.

    Implemented as raw ASGI (NOT ``BaseHTTPMiddleware``) on purpose: Starlette's
    ``BaseHTTPMiddleware`` runs the endpoint in a separate task, so ContextVars
    set inside its ``dispatch`` are **not** visible to route handlers. That
    silently broke per-user isolation — ``set_current_user`` had no effect on the
    handler's context, so every tenant fell back to the shared global workspace
    (cross-user data leak across memory / knowledge / books).

    A pure-ASGI middleware sets the ContextVars in the *same* task that runs the
    downstream app, so both the fork's ``current_user_id`` and upstream's
    ``multi_user`` context propagate correctly. It also covers ``websocket``
    scopes (chat / question / book streams), which ``BaseHTTPMiddleware`` skips.

    Unverified requests are bound to ``_UNVERIFIED`` rather than rejected here:
    a raw-ASGI middleware sits outside FastAPI's exception handlers, so raising
    would surface as a 500. The resolvers raise a clean 401 instead, and public
    routes (``/auth/*``, health, the diag-bank secret routes) keep working
    because they never resolve a tenant.
    """

    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        authorization = None
        for key, value in scope.get("headers", []):
            if key == b"authorization":
                authorization = value.decode("latin-1")
                break

        uid = subject_from_authorization(authorization)
        if uid is None and scope["type"] == "websocket":
            # Browsers cannot set headers on a WebSocket upgrade, so the token
            # travels as a query param. Still signature-verified — only the
            # transport differs.
            uid = _subject_from_ws_query(scope)

        token = current_user_id.set(uid or _UNVERIFIED)
        upstream_token, upstream_reset = (
            _bridge_upstream_user(uid) if uid else (None, None)
        )
        try:
            await self.app(scope, receive, send)
        finally:
            current_user_id.reset(token)
            if upstream_reset is not None and upstream_token is not None:
                upstream_reset(upstream_token)


def _subject_from_ws_query(scope) -> str | None:
    """Verify a WebSocket ``?token=`` query parameter."""
    from urllib.parse import parse_qs

    raw = scope.get("query_string") or b""
    try:
        params = parse_qs(raw.decode("latin-1"))
    except Exception:  # noqa: BLE001
        return None
    values = params.get("token") or []
    if not values:
        return None
    return subject_from_authorization(f"Bearer {values[0]}")


async def require_user_id() -> str:
    """FastAPI dependency — the verified tenant id for this request.

    Use as ``Depends(require_user_id)``. Raises 401 when the caller presented no
    verifiable identity. Takes no parameters on purpose: there is no
    caller-supplied input that can influence the answer.
    """
    return get_current_user_id()

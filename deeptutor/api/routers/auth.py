"""Anonymous bearer-token issuance for the TutorX SPA / mobile clients.

This router closes the BUG-101 loop end-to-end: clients call
``POST /api/v1/auth/anonymous`` once, get back a signed HS256 JWT, then send
it as ``Authorization: Bearer <jwt>`` on every subsequent call. When ops is
ready they flip ``DEEPTUTOR_REQUIRE_AUTH=true`` and the tenant middleware
starts rejecting requests that lack a matching token (the ``sub`` claim must
match the ``x-user-id`` header).

Design choices that protect this rollout:

* **Zero new deps.** HS256 is implemented with ``hmac`` / ``hashlib`` /
  ``base64`` from the standard library so deploy doesn't need a new
  ``pip install``.
* **Backwards compatible.** Until ops sets ``DEEPTUTOR_REQUIRE_AUTH=true``,
  clients can ignore these endpoints and continue sending raw ``x-user-id``.
  Existing TutorX SPA + Unity + RN apps keep working.
* **Idempotent refresh.** ``POST /auth/refresh`` re-signs the same ``sub``
  with a fresh expiry — does not rotate the user identity.
* **Predictable expiry.** Default 7 days, override with
  ``DEEPTUTOR_AUTH_TOKEN_TTL_SECONDS``. Refresh is allowed any time the
  caller still holds a valid (non-expired) token.

Endpoints
---------
``POST /api/v1/auth/anonymous`` → mint a fresh anonymous identity.
``POST /api/v1/auth/refresh``    → extend an existing valid token's exp.
``GET  /api/v1/auth/whoami``     → echo the resolved user id (debug).
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import logging
import os
import time
import uuid
from typing import Optional

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

from deeptutor.api.middleware.tenant import get_current_user_id

logger = logging.getLogger("api.auth")

router = APIRouter()

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

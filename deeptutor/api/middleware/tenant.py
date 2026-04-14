"""Multi-tenant user identification middleware.

Extracts `x-user-id` from request headers, stores it in a ContextVar so
any downstream service can call `get_current_user_id()` without passing
it through every function signature.

For CLI / single-user mode, falls back to a configurable default.
"""

from __future__ import annotations

import contextvars
import os

from fastapi import Header, Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

_DEFAULT_USER_ID = os.getenv("DEEPTUTOR_DEFAULT_USER_ID", "default")

current_user_id: contextvars.ContextVar[str] = contextvars.ContextVar(
    "current_user_id", default=_DEFAULT_USER_ID
)


def get_current_user_id() -> str:
    """Return the user_id for the current request (or the CLI default)."""
    return current_user_id.get()


class TenantMiddleware(BaseHTTPMiddleware):
    """Starlette middleware that sets current_user_id from the x-user-id header."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        uid = request.headers.get("x-user-id", "").strip() or _DEFAULT_USER_ID
        token = current_user_id.set(uid)
        try:
            return await call_next(request)
        finally:
            current_user_id.reset(token)


async def require_user_id(x_user_id: str = Header(default="")) -> str:
    """FastAPI dependency — use as `Depends(require_user_id)` on routes
    that must have an explicit user id.  Falls back to the context var."""
    uid = x_user_id.strip()
    if uid:
        return uid
    return get_current_user_id()

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


def _bridge_upstream_user(uid: str):
    """Mirror the fork's ``x-user-id`` into upstream's ``multi_user`` context.

    Upstream v1.4 scopes per-user data (memory, knowledge, workspaces) via its
    own ``CurrentUser`` ContextVar + ``PathService``. The fork drives tenancy
    from the ``x-user-id`` header instead of upstream's login system, so we
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


class TenantMiddleware(BaseHTTPMiddleware):
    """Starlette middleware that sets current_user_id from the x-user-id header.

    Also bridges the id into upstream's ``multi_user`` context so upstream's
    per-user scoping (memory/knowledge/workspaces) follows the same tenant.
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        uid = request.headers.get("x-user-id", "").strip() or _DEFAULT_USER_ID
        token = current_user_id.set(uid)
        upstream_token, upstream_reset = _bridge_upstream_user(uid)
        try:
            return await call_next(request)
        finally:
            current_user_id.reset(token)
            if upstream_reset is not None and upstream_token is not None:
                upstream_reset(upstream_token)


async def require_user_id(x_user_id: str = Header(default="")) -> str:
    """FastAPI dependency — use as `Depends(require_user_id)` on routes
    that must have an explicit user id.  Falls back to the context var."""
    uid = x_user_id.strip()
    if uid:
        return uid
    return get_current_user_id()

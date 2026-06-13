"""Reusable FastAPI dependency that gates endpoints on LLM-capability access.

A user with no granted LLM model cannot meaningfully use a feature that depends
on one. This guard turns that into an explicit, typed ``403``
(``code: "NO_MODEL_ACCESS"``) instead of a confusing downstream failure, and it
mirrors :func:`has_capability_access` so the server-side gate agrees with the
frontend lock.

Attach at the endpoint (or router) that actually consumes an LLM::

    @router.post("/run", dependencies=[Depends(require_llm_access)])

Admins always pass (they manage the catalog directly).

Note: as of the multi-user release only the LLM capability is grantable per
user — embedding/search are shared admin infrastructure and are not gated.
"""

from __future__ import annotations

from fastapi import Depends, HTTPException, status

from deeptutor.api.routers.auth import require_auth
from deeptutor.services.auth import TokenPayload

from .model_access import has_capability_access


def _require(capability: str) -> None:
    if has_capability_access(capability):
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "code": "NO_MODEL_ACCESS",
            "capability": capability,
            "message": (
                "Your account doesn't have an LLM model assigned. "
                "Please contact your administrator."
            ),
        },
    )


async def require_llm_access(
    _: TokenPayload | None = Depends(require_auth),
) -> None:
    # ``Depends(require_auth)`` keeps the same ordering guarantees as
    # ``require_admin``: the user ContextVar is installed before the guard reads
    # it.
    _require("llm")

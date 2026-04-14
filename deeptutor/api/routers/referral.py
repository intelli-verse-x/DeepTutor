"""
Proxy router for fetching a user's referral code/URL from the
Intelliverse-X User Backend (api.intelli-verse-x.ai).

Reuses the same Cognito S2S OAuth credentials that external_notes uses,
but targets the User API host instead of the AI API host.

Env vars (shared with external_notes):
  COGNITO_OAUTH2_URL        - Cognito token endpoint
  COGNITO_S2S_CLIENT_ID     - Cognito app-client ID
  COGNITO_S2S_CLIENT_SECRET - Cognito app-client secret

Env vars (specific to this router):
  INTELLIVERSE_USER_API_URL - User API base URL
                              (default: https://api.intelli-verse-x.ai)
"""

from __future__ import annotations

import logging
import os
from typing import Any

import httpx
from fastapi import APIRouter, Depends

from deeptutor.api.middleware.tenant import require_user_id
from deeptutor.api.routers.external_notes import _build_auth_headers

logger = logging.getLogger(__name__)

router = APIRouter()

_USER_API_URL = os.getenv(
    "INTELLIVERSE_USER_API_URL", "https://api.intelli-verse-x.ai"
)
_TIMEOUT = 15.0


@router.get("/url")
async def get_referral_url(
    user_id: str = Depends(require_user_id),
) -> dict[str, Any]:
    """Fetch the real referral code and URL for a user."""
    url = f"{_USER_API_URL}/api/user/referral/url"
    headers = await _build_auth_headers()
    headers["x-user-id"] = user_id

    try:
        async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
            resp = await client.get(url, headers=headers)
            resp.raise_for_status()
            body = resp.json()

        data = body.get("data") or body
        referral_code = data.get("referralCode", "")
        referral_url = data.get("referralUrl", "")

        if referral_code and not referral_url:
            referral_url = (
                f"https://intelli-verse-x.ai/auth?mode=signup&ref={referral_code}"
            )

        return {
            "referralCode": referral_code,
            "referralUrl": referral_url,
            "source": "intelliverse-x",
        }
    except httpx.HTTPStatusError as e:
        logger.warning("Referral URL fetch failed (HTTP %s): %s", e.response.status_code, e)
        return {
            "referralCode": "",
            "referralUrl": "",
            "error": f"Upstream HTTP {e.response.status_code}",
            "source": "intelliverse-x",
        }
    except Exception as e:
        logger.warning("Referral URL fetch failed: %s", e)
        return {
            "referralCode": "",
            "referralUrl": "",
            "error": str(e),
            "source": "intelliverse-x",
        }

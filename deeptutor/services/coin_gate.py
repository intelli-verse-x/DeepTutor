"""
TutorX Coin Gate Service
========================

Manages daily free tier + coin gating for DeepTutor AI features via Nakama RPCs.

Flow:
1. Before AI call → check_allowance(user_id, game_id)
2. If allowed → process AI
3. After success → record_usage(user_id, game_id)
"""

import os
import httpx
from dataclasses import dataclass
from deeptutor.logging import get_logger

logger = get_logger("CoinGate")

NAKAMA_SERVER_KEY = os.getenv("NAKAMA_SERVER_KEY", "defaultkey")
NAKAMA_HTTP_URL = os.getenv("NAKAMA_HTTP_URL", "http://localhost:7350")


@dataclass
class AllowanceStatus:
    can_use: bool
    free_remaining: int
    coin_balance: int
    cost_per_msg: int
    used_today: int
    error: str | None = None

    @property
    def is_free_tier(self) -> bool:
        return self.free_remaining > 0

    @property
    def requires_coins(self) -> bool:
        return not self.is_free_tier and self.coin_balance >= self.cost_per_msg

    @property
    def is_blocked(self) -> bool:
        return not self.is_free_tier and self.coin_balance < self.cost_per_msg


async def check_allowance(
    user_id: str | None,
    game_id: str | None,
    auth_token: str | None = None,
) -> AllowanceStatus:
    """
    Check if user can use TutorX AI.
    
    Returns AllowanceStatus with can_use=True if:
    - Free tier remaining > 0, OR
    - Coin balance >= cost_per_msg
    """
    if not user_id or not game_id:
        logger.debug("No user_id/game_id - allowing anonymous usage")
        return AllowanceStatus(
            can_use=True,
            free_remaining=3,
            coin_balance=0,
            cost_per_msg=5,
            used_today=0,
        )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            url = f"{NAKAMA_HTTP_URL}/v2/rpc/tutorx_check_allowance"
            headers = {
                "Authorization": f"Basic {NAKAMA_SERVER_KEY}",
                "Content-Type": "application/json",
            }
            if auth_token:
                headers["Authorization"] = f"Bearer {auth_token}"

            payload = {"gameId": game_id}
            resp = await client.post(url, json=payload, headers=headers)

            if resp.status_code != 200:
                logger.warning(f"Nakama RPC failed: {resp.status_code} - {resp.text}")
                return AllowanceStatus(
                    can_use=True,
                    free_remaining=3,
                    coin_balance=0,
                    cost_per_msg=5,
                    used_today=0,
                    error=f"RPC failed: {resp.status_code}",
                )

            data = resp.json().get("payload", {})
            if isinstance(data, str):
                import json
                data = json.loads(data)

            return AllowanceStatus(
                can_use=data.get("canUse", True),
                free_remaining=data.get("freeRemaining", 3),
                coin_balance=data.get("coinBalance", 0),
                cost_per_msg=data.get("costPerMsg", 5),
                used_today=data.get("usedToday", 0),
            )

    except Exception as e:
        logger.error(f"check_allowance error: {e}")
        return AllowanceStatus(
            can_use=True,
            free_remaining=3,
            coin_balance=0,
            cost_per_msg=5,
            used_today=0,
            error=str(e),
        )


async def record_usage(
    user_id: str | None,
    game_id: str | None,
    auth_token: str | None = None,
) -> bool:
    """Record successful AI usage for coin deduction tracking."""
    if not user_id or not game_id:
        return True

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            url = f"{NAKAMA_HTTP_URL}/v2/rpc/tutorx_record_usage"
            headers = {
                "Authorization": f"Basic {NAKAMA_SERVER_KEY}",
                "Content-Type": "application/json",
            }
            if auth_token:
                headers["Authorization"] = f"Bearer {auth_token}"

            payload = {"gameId": game_id}
            resp = await client.post(url, json=payload, headers=headers)

            if resp.status_code != 200:
                logger.warning(f"record_usage RPC failed: {resp.status_code}")
                return False

            return True

    except Exception as e:
        logger.error(f"record_usage error: {e}")
        return False

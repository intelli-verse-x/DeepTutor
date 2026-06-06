"""
Rate Limiting Middleware for DeepTutor API
==========================================

Implements token bucket algorithm for rate limiting.
Tracks requests per IP address and user ID.
"""

import time
from collections import defaultdict
from typing import Callable

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

import logging

logger = logging.getLogger("RateLimiter")


class TokenBucket:
    """Token bucket implementation for rate limiting."""

    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize token bucket.
        
        Args:
            capacity: Maximum number of tokens
            refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens from bucket.
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            True if tokens available, False otherwise
        """
        now = time.time()
        elapsed = now - self.last_refill
        
        # Refill tokens based on elapsed time
        self.tokens = min(
            self.capacity,
            self.tokens + (elapsed * self.refill_rate)
        )
        self.last_refill = now

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


class RateLimiterMiddleware(BaseHTTPMiddleware):
    """
    Rate limiting middleware with different limits per endpoint type.
    
    Limits:
    - Vision endpoints: 10 requests/minute (expensive AI calls)
    - Chat/Solve endpoints: 30 requests/minute
    - Other endpoints: 60 requests/minute
    """

    def __init__(self, app, enable: bool = True):
        super().__init__(app)
        self.enable = enable
        
        # Store buckets per client (IP + user_id)
        self.buckets: dict[str, dict[str, TokenBucket]] = defaultdict(dict)
        
        # Define rate limits for different endpoint categories
        self.rate_limits = {
            "vision": {"capacity": 10, "refill_rate": 10/60},  # 10 per minute
            "chat": {"capacity": 30, "refill_rate": 30/60},    # 30 per minute
            "solve": {"capacity": 30, "refill_rate": 30/60},   # 30 per minute
            "default": {"capacity": 60, "refill_rate": 60/60}, # 60 per minute
        }

    def _get_client_id(self, request: Request) -> str:
        """Get unique client identifier from IP and user ID."""
        ip = request.client.host if request.client else "unknown"
        user_id = request.headers.get("x-user-id", "anonymous")
        return f"{ip}:{user_id}"

    def _get_endpoint_category(self, path: str) -> str:
        """Determine endpoint category for rate limiting."""
        if "/vision/" in path:
            return "vision"
        elif "/chat" in path or "/solve" in path:
            return "chat"
        else:
            return "default"

    def _get_or_create_bucket(self, client_id: str, category: str) -> TokenBucket:
        """Get or create token bucket for client and category."""
        if category not in self.buckets[client_id]:
            limits = self.rate_limits[category]
            self.buckets[client_id][category] = TokenBucket(
                capacity=limits["capacity"],
                refill_rate=limits["refill_rate"]
            )
        return self.buckets[client_id][category]

    async def dispatch(self, request: Request, call_next: Callable):
        """Process request with rate limiting."""
        if not self.enable:
            return await call_next(request)

        # Skip rate limiting for health checks and system endpoints
        if request.url.path in ["/", "/health", "/api/v1/system/status"]:
            return await call_next(request)

        # Get client identifier and endpoint category
        client_id = self._get_client_id(request)
        category = self._get_endpoint_category(request.url.path)
        
        # Get token bucket for this client and category
        bucket = self._get_or_create_bucket(client_id, category)

        # Try to consume token
        if not bucket.consume():
            logger.warning(
                f"Rate limit exceeded: {client_id} on {category} endpoint {request.url.path}"
            )
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "Rate limit exceeded",
                    "message": f"Too many requests to {category} endpoints. Please try again later.",
                    "retry_after": int(1 / self.rate_limits[category]["refill_rate"]),
                    "category": category,
                }
            )

        # Process request
        response = await call_next(request)
        
        # Add rate limit headers
        response.headers["X-RateLimit-Limit"] = str(self.rate_limits[category]["capacity"])
        response.headers["X-RateLimit-Remaining"] = str(int(bucket.tokens))
        response.headers["X-RateLimit-Category"] = category
        
        return response


# Cleanup old buckets periodically (run this in background task)
def cleanup_old_buckets(middleware: RateLimiterMiddleware, max_age_seconds: int = 3600):
    """Remove buckets that haven't been used in max_age_seconds."""
    now = time.time()
    clients_to_remove = []
    
    for client_id, categories in middleware.buckets.items():
        # Check if any bucket has been used recently
        recent_activity = False
        for bucket in categories.values():
            if (now - bucket.last_refill) < max_age_seconds:
                recent_activity = True
                break
        
        if not recent_activity:
            clients_to_remove.append(client_id)
    
    for client_id in clients_to_remove:
        del middleware.buckets[client_id]
    
    if clients_to_remove:
        logger.info(f"Cleaned up {len(clients_to_remove)} inactive rate limit buckets")

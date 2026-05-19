"""
LLM Retry Utilities
===================

Production-ready retry logic for LLM API calls with exponential backoff.
"""

import asyncio
import logging
from typing import Any, Callable, TypeVar

from deeptutor.logging import get_logger

logger = get_logger("LLMRetry")

T = TypeVar('T')


class RetryableError(Exception):
    """Error that can be retried."""
    pass


class NonRetryableError(Exception):
    """Error that should not be retried."""
    pass


async def retry_with_exponential_backoff(
    func: Callable[..., Any],
    *args,
    max_retries: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    timeout: float | None = None,
    on_retry: Callable[[int, Exception], None] | None = None,
    **kwargs,
) -> Any:
    """
    Retry an async function with exponential backoff.
    
    Args:
        func: Async function to retry
        *args: Positional arguments to pass to func
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        exponential_base: Base for exponential backoff
        timeout: Optional timeout in seconds for the entire operation
        on_retry: Optional callback when retry happens (retry_count, exception)
        **kwargs: Keyword arguments to pass to func
        
    Returns:
        Result from successful function call
        
    Raises:
        Exception: Last exception if all retries fail
    """
    last_exception = None
    delay = initial_delay
    
    async def execute_with_timeout():
        for attempt in range(max_retries + 1):
            try:
                return await func(*args, **kwargs)
            except NonRetryableError:
                # Don't retry non-retryable errors
                raise
            except Exception as e:
                last_exception = e
                
                if attempt >= max_retries:
                    # No more retries
                    logger.error(
                        f"All {max_retries} retry attempts failed for {func.__name__}: {e}"
                    )
                    raise
                
                # Check if error is retryable
                if _is_retryable_error(e):
                    # Log retry
                    logger.warning(
                        f"Retry {attempt + 1}/{max_retries} for {func.__name__} "
                        f"after {delay:.1f}s due to: {type(e).__name__}: {str(e)[:100]}"
                    )
                    
                    # Call retry callback if provided
                    if on_retry:
                        try:
                            on_retry(attempt + 1, e)
                        except Exception as callback_error:
                            logger.error(f"Error in retry callback: {callback_error}")
                    
                    # Wait before retry
                    await asyncio.sleep(delay)
                    
                    # Update delay for next retry
                    delay = min(delay * exponential_base, max_delay)
                else:
                    # Non-retryable error
                    logger.error(f"Non-retryable error in {func.__name__}: {e}")
                    raise
    
    # Execute with overall timeout if specified
    if timeout:
        try:
            return await asyncio.wait_for(execute_with_timeout(), timeout=timeout)
        except asyncio.TimeoutError:
            logger.error(f"Operation timed out after {timeout}s")
            raise TimeoutError(f"Operation timed out after {timeout}s")
    else:
        return await execute_with_timeout()


def _is_retryable_error(error: Exception) -> bool:
    """
    Determine if an error is retryable.
    
    Args:
        error: Exception to check
        
    Returns:
        True if error should be retried
    """
    error_str = str(error).lower()
    error_type = type(error).__name__
    
    # Network errors (retryable)
    retryable_errors = [
        "timeout",
        "connection",
        "connect",
        "timed out",
        "rate limit",
        "429",  # Too many requests
        "500",  # Internal server error
        "502",  # Bad gateway
        "503",  # Service unavailable
        "504",  # Gateway timeout
        "network",
        "unreachable",
    ]
    
    # Client errors (non-retryable)
    non_retryable_errors = [
        "400",  # Bad request
        "401",  # Unauthorized
        "403",  # Forbidden
        "404",  # Not found
        "invalid",
        "unauthorized",
        "forbidden",
        "authentication",
    ]
    
    # Check non-retryable first
    if any(err in error_str for err in non_retryable_errors):
        return False
    
    # Check retryable
    if any(err in error_str for err in retryable_errors):
        return True
    
    # Default: retry network-related exceptions
    if error_type in ["TimeoutError", "ConnectionError", "asyncio.TimeoutError"]:
        return True
    
    # Default: don't retry unknown errors
    return False


def mask_sensitive_data(text: str, patterns: list[str] | None = None) -> str:
    """
    Mask sensitive data in text (API keys, tokens, etc.).
    
    Args:
        text: Text to mask
        patterns: Optional list of patterns to mask
        
    Returns:
        Text with sensitive data masked
    """
    import re
    
    if not text:
        return text
    
    # Default patterns
    default_patterns = [
        # API keys (various formats)
        (r'(api[_-]?key["\s:=]+)([a-zA-Z0-9_-]{20,})', r'\1***\2[-8:]'),
        (r'(bearer\s+)([a-zA-Z0-9_-]{20,})', r'\1***'),
        (r'(sk-[a-zA-Z0-9]{20,})', r'sk-***'),
        (r'(password["\s:=]+)([^\s"]+)', r'\1***'),
        (r'(token["\s:=]+)([a-zA-Z0-9_-]{20,})', r'\1***'),
    ]
    
    masked = text
    for pattern, replacement in default_patterns:
        masked = re.sub(pattern, replacement, masked, flags=re.IGNORECASE)
    
    return masked


__all__ = [
    "retry_with_exponential_backoff",
    "mask_sensitive_data",
    "RetryableError",
    "NonRetryableError",
]

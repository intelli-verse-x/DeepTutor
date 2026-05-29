# LLM Factory API

## Import
```python
from deeptutor.services.llm import complete, stream
```

## Instantiation
No instantiation needed. `complete` and `stream` are module-level async functions that auto-resolve config from `get_llm_config()` (global settings). Pass overrides as kwargs.

## Call Method
```python
# Non-streaming completion
response = await complete(
    prompt="Explain photosynthesis",
    system_prompt="You are a helpful tutor.",
)

# Streaming completion
async for chunk in stream(
    prompt="Explain photosynthesis",
    system_prompt="You are a helpful tutor.",
):
    print(chunk, end="")

# With explicit overrides (model, api_key, base_url, binding)
response = await complete(
    prompt="Hello",
    system_prompt="You are helpful.",
    model="gpt-4o",
    api_key="sk-...",
    base_url="https://api.openai.com/v1",
    binding="openai",
)

# With pre-built messages list (bypasses prompt/system_prompt)
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Hello"},
]
response = await complete(prompt="", system_prompt="", messages=messages)
```

## Function Signatures
```python
async def complete(
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    api_version: str | None = None,
    binding: str | None = None,
    messages: list[dict[str, Any]] | None = None,
    max_retries: int = DEFAULT_MAX_RETRIES,
    retry_delay: float = DEFAULT_RETRY_DELAY,
    exponential_backoff: bool = DEFAULT_EXPONENTIAL_BACKOFF,
    **kwargs: Any,  # extra_headers, reasoning_effort, image_data, response_format
) -> str

async def stream(
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    api_version: str | None = None,
    binding: str | None = None,
    messages: list[dict[str, Any]] | None = None,
    max_retries: int = DEFAULT_MAX_RETRIES,
    retry_delay: float = DEFAULT_RETRY_DELAY,
    exponential_backoff: bool = DEFAULT_EXPONENTIAL_BACKOFF,
    **kwargs: Any,
) -> AsyncGenerator[str, None]
```

## Return Type
- `complete()` returns `str` (the full response content).
- `stream()` returns `AsyncGenerator[str, None]` yielding content chunks as strings.

## Notes
- `LLMFactory` class exists but is a thin legacy shim — only has `get_provider(config)`. Prefer `complete()`/`stream()`.
- Config resolution: if `model`+`api_key`+(`base_url` or `binding`) are all passed, they form an explicit config; otherwise falls back to global `get_llm_config()`.
- Provider routing is automatic based on model name, URL patterns, or explicit `binding` string.

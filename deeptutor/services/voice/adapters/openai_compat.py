"""OpenAI-compatible HTTP adapters for TTS and STT.

A single pair of adapters covers the whole OpenAI-`/v1/audio/*` cluster —
OpenAI, Groq, SiliconFlow, OpenRouter, Azure OpenAI and local vLLM/LM Studio —
by varying ``base_url`` / ``api_key`` / ``model`` and a couple of config flags
(``auth_style``, ``api_version``, ``request_style``). Genuinely bespoke
providers (DashScope native, ElevenLabs, Gemini, Deepgram) get their own
adapters keyed in ``adapters/__init__.py``.
"""

from __future__ import annotations

import base64
import logging
from typing import Any

import httpx

from deeptutor.services.voice.base import (
    BaseSTTAdapter,
    BaseTTSAdapter,
    VoiceProviderError,
    build_auth_headers,
    join_audio_path,
)
from deeptutor.services.voice.config import STT_BASE64_JSON, STTConfig, TTSConfig

logger = logging.getLogger(__name__)

_FORMAT_CONTENT_TYPES = {
    "mp3": "audio/mpeg",
    "opus": "audio/opus",
    "aac": "audio/aac",
    "flac": "audio/flac",
    "wav": "audio/wav",
    "pcm": "audio/pcm",
}


def _raise_for_provider(resp: httpx.Response, action: str) -> None:
    """Surface a provider error with a trimmed body for diagnostics."""
    if resp.status_code < 400:
        return
    body = resp.text or ""
    detail = body.strip()[:400]
    raise VoiceProviderError(
        f"{action} failed with HTTP {resp.status_code}" + (f": {detail}" if detail else ".")
    )


class OpenAICompatTTSAdapter(BaseTTSAdapter):
    """POST ``{base}/audio/speech`` with a JSON body, returning raw audio bytes."""

    async def synthesize(self, text: str, config: TTSConfig) -> tuple[bytes, str]:
        if not config.base_url:
            raise VoiceProviderError("No endpoint URL configured for TTS.")
        url = join_audio_path(config.base_url, "audio/speech")
        headers = {
            "Content-Type": "application/json",
            **build_auth_headers(config.auth_style, config.api_key),
            **(config.extra_headers or {}),
        }
        response_format = (config.response_format or "mp3").lower()
        payload: dict[str, Any] = {
            "model": config.model,
            "input": text,
            "response_format": response_format,
        }
        if config.voice:
            payload["voice"] = config.voice
        if config.speed is not None:
            payload["speed"] = config.speed

        logger.debug(
            "TTS synthesize url=%s model=%s voice=%s fmt=%s chars=%d",
            url,
            config.model,
            config.voice,
            response_format,
            len(text),
        )
        try:
            async with httpx.AsyncClient(timeout=config.request_timeout) as client:
                resp = await client.post(url, headers=headers, json=payload)
        except httpx.HTTPError as exc:
            raise VoiceProviderError(f"TTS request error: {exc}") from exc
        _raise_for_provider(resp, "TTS synthesis")
        audio = resp.content
        if not audio:
            raise VoiceProviderError("TTS provider returned empty audio.")
        content_type = resp.headers.get("content-type") or _FORMAT_CONTENT_TYPES.get(
            response_format, "application/octet-stream"
        )
        # Some gateways return JSON content-type with audio; trust the format map.
        if "json" in content_type:
            content_type = _FORMAT_CONTENT_TYPES.get(response_format, "audio/mpeg")
        return audio, content_type


class OpenAICompatSTTAdapter(BaseSTTAdapter):
    """POST ``{base}/audio/transcriptions``.

    Multipart ``file`` upload by default; OpenRouter uses a base64-JSON body
    (``request_style == "base64_json"``) sharing the same path.
    """

    async def transcribe(
        self,
        audio: bytes,
        config: STTConfig,
        *,
        filename: str = "audio.webm",
        content_type: str = "application/octet-stream",
    ) -> str:
        if not config.base_url:
            raise VoiceProviderError("No endpoint URL configured for STT.")
        if not audio:
            raise VoiceProviderError("No audio data to transcribe.")
        url = join_audio_path(config.base_url, "audio/transcriptions")
        auth = build_auth_headers(config.auth_style, config.api_key)

        try:
            async with httpx.AsyncClient(timeout=config.request_timeout) as client:
                if config.request_style == STT_BASE64_JSON:
                    resp = await self._post_base64(client, url, auth, audio, filename, config)
                else:
                    resp = await self._post_multipart(
                        client, url, auth, audio, filename, content_type, config
                    )
        except httpx.HTTPError as exc:
            raise VoiceProviderError(f"STT request error: {exc}") from exc
        _raise_for_provider(resp, "Transcription")
        return self._parse_text(resp)

    async def _post_multipart(
        self,
        client: httpx.AsyncClient,
        url: str,
        auth: dict[str, str],
        audio: bytes,
        filename: str,
        content_type: str,
        config: STTConfig,
    ) -> httpx.Response:
        files = {"file": (filename, audio, content_type or "application/octet-stream")}
        data: dict[str, str] = {"model": config.model, "response_format": "json"}
        if config.language:
            data["language"] = config.language
        headers = {**auth, **(config.extra_headers or {})}
        return await client.post(url, headers=headers, files=files, data=data)

    async def _post_base64(
        self,
        client: httpx.AsyncClient,
        url: str,
        auth: dict[str, str],
        audio: bytes,
        filename: str,
        config: STTConfig,
    ) -> httpx.Response:
        fmt = filename.rsplit(".", 1)[-1].lower() if "." in filename else "webm"
        body: dict[str, Any] = {
            "model": config.model,
            "input_audio": {"data": base64.b64encode(audio).decode("ascii"), "format": fmt},
        }
        if config.language:
            body["language"] = config.language
        headers = {"Content-Type": "application/json", **auth, **(config.extra_headers or {})}
        return await client.post(url, headers=headers, json=body)

    @staticmethod
    def _parse_text(resp: httpx.Response) -> str:
        content_type = resp.headers.get("content-type", "")
        if "json" in content_type:
            data = resp.json()
            if isinstance(data, dict):
                text = data.get("text")
                if isinstance(text, str):
                    return text.strip()
                # OpenRouter/chat-style fallback.
                choices = data.get("choices")
                if isinstance(choices, list) and choices:
                    message = (choices[0] or {}).get("message") or {}
                    if isinstance(message.get("content"), str):
                        return message["content"].strip()
            raise VoiceProviderError("Transcription response had no `text` field.")
        # response_format=text returns a bare string.
        return (resp.text or "").strip()


__all__ = ["OpenAICompatTTSAdapter", "OpenAICompatSTTAdapter"]

# Block A: Fix _call_llm fail-open → fail-closed

## Problem (Codex audit finding)

`_call_llm()` catches LLM exceptions and returns `{"error": "LLM call failed: ..."}`. This error JSON is then parsed by `_safe_json_parse()` as valid data, and the stage handler unconditionally calls `advance_stage()`. Result: a failed LLM call corrupts progress with garbage data and advances the stage.

Example flow:
```
_call_llm fails → returns {"error": "LLM call failed: timeout"}
  → _safe_json_parse({"error": ...}) → {"error": "LLM call failed: timeout"}
  → data.get("questions", []) → []
  → progress.diagnostic = DiagnosticResult(total_questions=0)
  → advance_stage(DIAGNOSTIC_PHASE2)  ← BUG: stage advanced with garbage data
```

## Fix

### 1. Change `_call_llm` to raise on failure (NOT return error JSON)

Delete the try/except that catches Exception. Let the exception propagate.

```python
async def _call_llm(self, system_prompt: str, user_message: str) -> str:
    from deeptutor.services.llm import complete
    rag_context = await self._retrieve_context(user_message)
    if rag_context:
        system_prompt = system_prompt + rag_context
    response = await complete(prompt=user_message, system_prompt=system_prompt)
    return response
```

(Remove the `try/except` wrapper and the `return json.dumps({"error": ...})` fallback)

### 2. `run()` catches exception and streams error

Add exception handling in `run()` that sends error to stream:

```python
async def run(self, context: UnifiedContext, stream: StreamBus) -> None:
    book_id = self._resolve_book_id(context)
    progress = self._service.get_or_create(book_id)
    stage = progress.current_stage
    handler = self._STAGE_HANDLERS.get(stage)
    if handler is None:
        if stage == LearningStage.COMPLETED:
            async with stream.stage("completed", source=self.manifest.name):
                await stream.content("学习流程已完成。进入复习阶段。")
        return
    try:
        await handler(self, progress, context, stream)
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Stage {stage} failed: {e}")
        async with stream.stage("error", source=self.manifest.name):
            await stream.content(f"阶段执行失败: {e}。进度已保存，下次将继续此阶段。")
    finally:
        self._service.save(progress)
```

This means: if LLM fails → stage handler crashes → exception caught → error streamed to user → progress saved WITHOUT advancing stage → next invocation retries same stage.

### 3. Update tests that expected error JSON return

`test_llm_integration.py` has `test_call_llm_network_error` that expects `_call_llm` to return `{"error": "..."}`. Change it to expect exception:

```python
@pytest.mark.asyncio
async def test_call_llm_network_error(self):
    """_call_llm raises on failure, does not return error JSON."""
    cap = GuidedLearningCapability()
    with patch("deeptutor.capabilities.guided_learning.complete",
               new_callable=AsyncMock, side_effect=Exception("Network down")):
        with pytest.raises(Exception, match="Network down"):
            await cap._call_llm("system", "user")
```

## 验收

```bash
cd D:\Project\DeepTutor && .venv\Scripts\python.exe -m pytest deeptutor/learning/tests/ -v
# 预期: 64 passed (12 integration + 52 original — test_call_llm_network_error updated)
```

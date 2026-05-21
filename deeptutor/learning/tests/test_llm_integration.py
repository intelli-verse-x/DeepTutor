"""Integration tests for guided_learning LLM + RAG integration."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import LearningProgress, LearningStage


class TestLLMIntegration:
    """Verify _call_llm calls real LLM factory."""

    @pytest.mark.asyncio
    async def test_call_llm_calls_complete(self):
        """_call_llm should call deeptutor.services.llm.complete."""
        cap = GuidedLearningCapability()
        with patch("deeptutor.capabilities.guided_learning.complete",
                   new_callable=AsyncMock) as mock_complete:
            mock_complete.return_value = "LLM response"
            result = await cap._call_llm("system", "user")
            mock_complete.assert_called_once()
            assert result == "LLM response"

    @pytest.mark.asyncio
    async def test_call_llm_network_error(self):
        """_call_llm raises on failure, does not return error JSON."""
        cap = GuidedLearningCapability()
        with patch("deeptutor.capabilities.guided_learning.complete",
                   new_callable=AsyncMock, side_effect=Exception("Network down")):
            with pytest.raises(Exception, match="Network down"):
                await cap._call_llm("system", "user")

    def test_call_llm_exists_and_is_async(self):
        """_call_llm should be an async method."""
        import inspect
        cap = GuidedLearningCapability()
        assert hasattr(cap, "_call_llm")
        assert inspect.iscoroutinefunction(cap._call_llm)


class TestRAGIntegration:
    """Verify RAG retrieval is called and injected."""

    @pytest.mark.asyncio
    async def test_retrieve_context_no_kb(self):
        """Without kb_name, _retrieve_context returns (content, error) tuple with empty strings."""
        cap = GuidedLearningCapability()
        result = await cap._retrieve_context("test query")
        assert result == ("", "")

    def test_kb_params_stored(self):
        """kb_name and kb_base_dir should be stored as instance attrs."""
        cap = GuidedLearningCapability(kb_name="my_kb", kb_base_dir="/tmp/kb")
        assert cap._kb_name == "my_kb"
        assert cap._kb_base_dir == "/tmp/kb"

    def test_default_kb_is_none(self):
        """Default kb_name should be None."""
        cap = GuidedLearningCapability()
        assert cap._kb_name is None
        assert cap._kb_base_dir is None

    @pytest.mark.asyncio
    async def test_call_llm_injects_rag_context(self):
        """_call_llm should call _retrieve_context and inject results."""
        cap = GuidedLearningCapability(kb_name="test_kb")
        with patch.object(cap, "_retrieve_context", new_callable=AsyncMock,
                         return_value=("\n\n参考教材内容：\nSome content", "")) as mock_rag:
            with patch("deeptutor.capabilities.guided_learning.complete",
                      new_callable=AsyncMock) as mock_complete:
                mock_complete.return_value = "response"
                await cap._call_llm("system", "user")
                mock_rag.assert_called_once_with("user")
                # The system_prompt passed to complete should contain RAG context
                called_system = mock_complete.call_args[1]["system_prompt"]
                assert "参考教材内容" in called_system
                assert "Some content" in called_system


class TestNoMockRemnants:
    """Verify no _mock_llm code remains."""

    def test_no_mock_llm_on_instance(self):
        """_mock_llm should not exist on any instance."""
        cap = GuidedLearningCapability()
        assert not hasattr(cap, "_mock_llm")

    def test_no_mock_llm_in_source(self):
        """_mock_llm should not appear anywhere in the module source."""
        import inspect
        src = inspect.getsource(GuidedLearningCapability)
        assert "_mock_llm" not in src


class TestJSONParse:
    """Existing _safe_json_parse should still work."""

    def test_valid_json(self):
        cap = GuidedLearningCapability()
        result = cap._safe_json_parse('{"key": "value"}')
        assert result == {"key": "value"}

    def test_invalid_json_fallback(self):
        cap = GuidedLearningCapability()
        result = cap._safe_json_parse("not json", default={"fallback": True})
        assert result == {"fallback": True}

    def test_invalid_json_empty_default(self):
        cap = GuidedLearningCapability()
        result = cap._safe_json_parse("garbage")
        assert result == {}

from __future__ import annotations

import asyncio
import json
from pathlib import Path

from deeptutor.knowledge.add_documents import DocumentAdder


def _write_provider_version(kb_dir: Path, provider: str) -> None:
    version_dir = kb_dir / "version-1"
    version_dir.mkdir(parents=True)
    if provider == "pageindex":
        (version_dir / "pageindex_docs.json").write_text(
            json.dumps({"provider": "pageindex", "docs": {"doc.pdf": {"doc_id": "doc-1"}}}),
            encoding="utf-8",
        )
    elif provider == "graphrag":
        output_dir = version_dir / "output"
        output_dir.mkdir()
        (output_dir / "entities.parquet").write_bytes(b"placeholder")
    else:
        (version_dir / "docstore.json").write_text("{}", encoding="utf-8")
        (version_dir / "index_store.json").write_text("{}", encoding="utf-8")
    (version_dir / "meta.json").write_text(
        json.dumps(
            {
                "provider": provider,
                "signature": provider,
                "version": "version-1",
            }
        ),
        encoding="utf-8",
    )


def test_document_adder_reads_provider_from_kb_config_when_metadata_missing(
    tmp_path: Path,
) -> None:
    kb_dir = tmp_path / "page-kb"
    (kb_dir / "raw").mkdir(parents=True)
    _write_provider_version(kb_dir, "pageindex")
    (tmp_path / "kb_config.json").write_text(
        json.dumps(
            {"knowledge_bases": {"page-kb": {"path": "page-kb", "rag_provider": "pageindex"}}}
        ),
        encoding="utf-8",
    )

    adder = DocumentAdder(kb_name="page-kb", base_dir=str(tmp_path))

    assert adder.rag_provider == "pageindex"


def test_document_adder_preserves_explicit_bound_provider(tmp_path: Path) -> None:
    kb_dir = tmp_path / "graph-kb"
    (kb_dir / "raw").mkdir(parents=True)
    _write_provider_version(kb_dir, "graphrag")

    adder = DocumentAdder(
        kb_name="graph-kb",
        base_dir=str(tmp_path),
        rag_provider="graphrag",
    )

    assert adder.rag_provider == "graphrag"


def test_process_new_documents_returns_failures_without_marking_processed(
    monkeypatch, tmp_path: Path
) -> None:
    kb_dir = tmp_path / "kb"
    raw_dir = kb_dir / "raw"
    raw_dir.mkdir(parents=True)
    _write_provider_version(kb_dir, "llamaindex")
    doc = raw_dir / "bad.txt"
    doc.write_text("hello", encoding="utf-8")

    class _FailingRagService:
        def __init__(self, *_args, **_kwargs) -> None:
            pass

        async def add_documents(self, *_args, **_kwargs) -> bool:
            raise RuntimeError("provider exploded")

    monkeypatch.setattr(
        "deeptutor.knowledge.add_documents.RAGService",
        _FailingRagService,
    )

    adder = DocumentAdder(kb_name="kb", base_dir=str(tmp_path))
    result = asyncio.run(adder.process_new_documents([doc]))

    assert result.processed_files == []
    assert result.failed_count == 1
    assert "provider exploded" in result.failure_summary()
    assert adder.get_ingested_hashes() == {}

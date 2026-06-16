from __future__ import annotations

import zipfile

import pytest

from deeptutor.services.parsing.engines import factory
from deeptutor.services.parsing.types import ParserError


def test_known_engines() -> None:
    assert factory.KNOWN_ENGINES == {"text_only", "mineru", "docling", "markitdown"}


def test_list_engines_reports_metadata_and_availability() -> None:
    engines = {entry["id"]: entry for entry in factory.list_engines()}
    assert set(engines) == {"text_only", "mineru", "docling", "markitdown"}
    assert engines["text_only"]["available"] is True
    assert engines["text_only"]["needs_local_models"] is False
    # MinerU is an external CLI / hosted API — the adapter is always available;
    # readiness (not availability) gates actual use.
    assert engines["mineru"]["available"] is True
    assert engines["mineru"]["needs_local_models"] is True
    assert engines["markitdown"]["needs_local_models"] is False


def test_get_parser_unknown_raises() -> None:
    with pytest.raises(ParserError):
        factory.get_parser("nope")


def test_text_only_parser_extracts_docx_text(tmp_path) -> None:
    parser = factory.get_parser("text_only")
    assert type(factory.get_parser("text-only")) is type(parser)
    docx = tmp_path / "lesson.docx"
    with zipfile.ZipFile(docx, "w") as zf:
        zf.writestr(
            "word/document.xml",
            """
            <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
              <w:body>
                <w:p><w:r><w:t>Hello DeepTutor</w:t></w:r></w:p>
              </w:body>
            </w:document>
            """.strip(),
        )

    workdir = tmp_path / "parsed"
    workdir.mkdir()
    parser.parse(docx, workdir, config={})

    assert (workdir / "lesson.md").read_text(encoding="utf-8") == "Hello DeepTutor"


def test_mineru_signature_distinguishes_local_and_cloud() -> None:
    parser = factory.get_parser("mineru")
    from deeptutor.services.parsing.engines.mineru.config import MinerUConfig

    local = parser.signature(MinerUConfig(mode="local")).hash()
    cloud = parser.signature(MinerUConfig(mode="cloud")).hash()
    assert local != cloud


def test_mineru_cloud_readiness_needs_token() -> None:
    from deeptutor.services.parsing.engines.mineru.config import MinerUConfig
    from deeptutor.services.parsing.engines.mineru.readiness import mineru_readiness

    assert mineru_readiness(MinerUConfig(mode="cloud", api_token="")).reason == "not_configured"
    assert mineru_readiness(MinerUConfig(mode="cloud", api_token="tok")).ready is True


def test_mineru_local_model_download_gate(monkeypatch: pytest.MonkeyPatch) -> None:
    from deeptutor.services.parsing.engines.mineru import backend
    from deeptutor.services.parsing.engines.mineru import readiness as rd
    from deeptutor.services.parsing.engines.mineru.config import MinerUConfig

    monkeypatch.setattr(
        backend,
        "local_cli_probe",
        lambda p="": {"found": True, "command": "mineru", "path": "", "source": "path"},
    )
    monkeypatch.setattr(rd, "mineru_models_ready", lambda source="huggingface": False)

    # Models missing + auto-download off → gated.
    blocked = rd.mineru_readiness(MinerUConfig(mode="local", allow_local_model_download=False))
    assert blocked.ready is False
    assert blocked.reason == "models_missing"

    # Explicit opt-in → allowed.
    allowed = rd.mineru_readiness(MinerUConfig(mode="local", allow_local_model_download=True))
    assert allowed.ready is True

    # CLI missing → distinct gate.
    monkeypatch.setattr(
        backend,
        "local_cli_probe",
        lambda p="": {"found": False, "command": "", "path": "", "source": "path"},
    )
    no_cli = rd.mineru_readiness(MinerUConfig(mode="local"))
    assert no_cli.reason == "cli_missing"

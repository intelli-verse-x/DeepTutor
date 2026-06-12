"""
Skill hub providers
===================

Import skills from external registries ("hubs") into the local skill layer.

A hub skill is the same artefact DeepTutor already speaks natively — a
directory with a ``SKILL.md`` (YAML frontmatter + markdown playbook) plus
optional support files — so importing is a fetch + adapt + install pipeline,
not a format translation:

1. **verify** — ask the hub for its security verdict on the package. A
   ``suspicious`` verdict aborts the install unless the caller explicitly
   opts out (registries of this kind have shipped malware before).
2. **fetch** — download and safely extract the package into a temp dir
   (zip-slip / zip-bomb guards live here).
3. **install** — :meth:`SkillService.install_tree` applies the import
   policy (frontmatter adaptation, ``always`` stripping, suffix whitelist)
   and records provenance in ``.hub-lock.json``.

Providers are addressed as ``<hub>:<slug>[@version]`` (e.g.
``clawhub:gh-release-notes@1.2.0``; the hub prefix defaults to ``clawhub``).
Two provider shapes ship in v1:

* :class:`ClawHubProvider` — speaks the ClawHub HTTP API directly (search /
  download / verify), so no Node toolchain is required;
* :class:`CommandProvider` — wraps an arbitrary fetch command for registries
  that only publish a CLI. The command must drop the package into the
  directory given as ``{dest}``; everything after that goes through the same
  verify-less install gate (verdict is ``unknown``).

Extra hubs are declared in ``settings/skill_hubs.json``::

    {
      "hubs": {
        "myhub": {"type": "command", "fetch_cmd": "myhub pull {slug} --out {dest}"},
        "mirror": {"type": "clawhub", "base_url": "https://mirror.example/api/v1"}
      }
    }
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tempfile
from typing import Any, Protocol
import zipfile

import httpx

from deeptutor.services.path_service import get_path_service

from .service import SkillImportError, SkillInstallResult, SkillService

logger = logging.getLogger(__name__)

DEFAULT_HUB = "clawhub"
_CLAWHUB_BASE_URL = "https://clawhub.ai/api/v1"
_HUBS_SETTINGS_FILE = "skill_hubs"

_REF_RE = re.compile(
    r"^(?:(?P<hub>[a-z0-9][a-z0-9-]{0,31}):)?"
    r"(?P<slug>[a-z0-9][a-z0-9._-]{0,127})"
    r"(?:@(?P<version>[A-Za-z0-9][A-Za-z0-9._-]{0,63}))?$"
)

# Extraction bounds for a downloaded package archive. Structural safety only —
# the per-file suffix whitelist is applied later by ``install_tree``.
_ZIP_MAX_ENTRIES = 600
_ZIP_MAX_ENTRY_BYTES = 4_000_000
_ZIP_MAX_TOTAL_BYTES = 40_000_000
_ZIP_MAX_RATIO = 200.0

_HTTP_TIMEOUT = 30.0
_FETCH_CMD_TIMEOUT = 120.0


class HubError(Exception):
    """A hub interaction failed (network, protocol, or configuration)."""


@dataclass(slots=True)
class HubSkillRef:
    """One hub listing: enough to show a search row and stamp provenance."""

    hub: str
    slug: str
    display_name: str = ""
    summary: str = ""
    version: str = ""


@dataclass(slots=True)
class HubVerdict:
    """Hub security verdict, collapsed to a tri-state.

    ``ok`` — the hub vouches for the package; ``suspicious`` — the hub
    flags it (install is refused without an explicit override);
    ``unknown`` — the hub has no verdict surface or the call failed,
    so the caller should warn rather than block.
    """

    status: str  # "ok" | "suspicious" | "unknown"
    detail: str = ""


@dataclass(slots=True)
class FetchedSkill:
    """A downloaded package on local disk, pending install."""

    ref: HubSkillRef
    root: Path  # directory containing SKILL.md
    cleanup_dir: Path  # temp tree to remove once installed

    def cleanup(self) -> None:
        shutil.rmtree(self.cleanup_dir, ignore_errors=True)


@dataclass(slots=True)
class HubInstallOutcome:
    """Everything the caller needs to report an install."""

    result: SkillInstallResult
    ref: HubSkillRef
    verdict: HubVerdict


class SkillHubProvider(Protocol):
    name: str

    def search(self, query: str, *, limit: int = 10) -> list[HubSkillRef]: ...

    def fetch(self, slug: str, *, version: str | None = None) -> FetchedSkill: ...

    def verify(self, slug: str, *, version: str | None = None) -> HubVerdict: ...


# ── ref parsing ──────────────────────────────────────────────────────────


def parse_hub_ref(ref: str) -> tuple[str, str, str | None]:
    """Split ``<hub>:<slug>[@version]`` into its parts; hub defaults."""
    match = _REF_RE.match((ref or "").strip())
    if match is None:
        raise HubError(f"Invalid skill reference `{ref}`. Expected <hub>:<slug>[@version].")
    return (
        match.group("hub") or DEFAULT_HUB,
        match.group("slug"),
        match.group("version"),
    )


# ── safe archive extraction (directory-preserving) ──────────────────────


def _extract_skill_zip(zip_path: Path, dest: Path) -> None:
    """Extract a package zip preserving subdirectories, defensively.

    The KB upload extractor (:func:`safe_extract_zip`) flattens paths, which
    would destroy a skill's ``references/`` layout — so this sibling keeps
    relative paths and instead rejects traversal segments outright. Bomb
    guards mirror the extractor's posture. Members are streamed through
    ``ZipFile.open``, so no permission bits or links materialise.
    """
    dest.mkdir(parents=True, exist_ok=True)
    dest_root = dest.resolve()
    total = 0
    try:
        archive = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile as exc:
        raise SkillImportError(f"Downloaded package is not a valid zip: {exc}") from exc
    with archive:
        members = [info for info in archive.infolist() if not info.is_dir()]
        if len(members) > _ZIP_MAX_ENTRIES:
            raise SkillImportError("Package archive has too many entries.")
        for info in members:
            raw = info.filename.replace("\\", "/")
            rel = Path(raw)
            if rel.is_absolute() or ".." in rel.parts:
                raise SkillImportError(f"Illegal path in package archive: {raw}")
            if raw.startswith("__MACOSX/") or rel.name.startswith("."):
                continue
            if info.file_size > _ZIP_MAX_ENTRY_BYTES:
                raise SkillImportError(f"Package entry too large: {raw}")
            if info.compress_size > 0:
                if info.file_size / info.compress_size > _ZIP_MAX_RATIO:
                    raise SkillImportError(f"Suspicious compression ratio: {raw}")
            total += info.file_size
            if total > _ZIP_MAX_TOTAL_BYTES:
                raise SkillImportError("Package archive exceeds the size limit.")
            target = (dest_root / rel).resolve()
            if not target.is_relative_to(dest_root):  # defense in depth
                raise SkillImportError(f"Illegal path in package archive: {raw}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, open(target, "wb") as sink:
                shutil.copyfileobj(source, sink, length=1 << 16)
            if target.stat().st_size > info.file_size:
                target.unlink(missing_ok=True)
                raise SkillImportError(f"Entry decompressed past declared size: {raw}")


def _locate_package_root(extracted: Path) -> Path:
    """Find the directory holding ``SKILL.md`` (top level or one wrapper deep).

    Hub zips routinely wrap the package in a single named folder; anything
    deeper or ambiguous is rejected rather than guessed at.
    """
    if (extracted / "SKILL.md").is_file():
        return extracted
    subdirs = [p for p in extracted.iterdir() if p.is_dir()]
    if len(subdirs) == 1 and (subdirs[0] / "SKILL.md").is_file():
        return subdirs[0]
    raise SkillImportError("Package does not contain a SKILL.md.")


# ── providers ─────────────────────────────────────────────────────────────


class ClawHubProvider:
    """ClawHub registry over its public read-only HTTP API.

    Speaking HTTP directly (instead of shelling out to the ``clawhub`` npm
    CLI) keeps the pipeline free of a Node toolchain dependency and lets the
    security verdict gate run inside our install path.
    """

    def __init__(
        self,
        name: str = DEFAULT_HUB,
        *,
        base_url: str = _CLAWHUB_BASE_URL,
        client: httpx.Client | None = None,
    ) -> None:
        self.name = name
        self._base_url = base_url.rstrip("/")
        self._client = client or httpx.Client(timeout=_HTTP_TIMEOUT, follow_redirects=True)

    def _get(self, path: str, **params: Any) -> httpx.Response:
        url = f"{self._base_url}{path}"
        try:
            response = self._client.get(
                url, params={k: v for k, v in params.items() if v is not None}
            )
        except httpx.HTTPError as exc:
            raise HubError(f"{self.name}: request failed: {exc}") from exc
        if response.status_code == 404:
            raise HubError(f"{self.name}: not found: {path}")
        if response.status_code >= 400:
            raise HubError(
                f"{self.name}: HTTP {response.status_code} for {path}: {response.text[:200]}"
            )
        return response

    def search(self, query: str, *, limit: int = 10) -> list[HubSkillRef]:
        response = self._get("/search", q=query, limit=limit)
        try:
            payload = response.json()
        except ValueError as exc:
            raise HubError(f"{self.name}: search returned invalid JSON") from exc
        rows = payload if isinstance(payload, list) else None
        if rows is None and isinstance(payload, dict):
            for key in ("results", "items", "skills"):
                if isinstance(payload.get(key), list):
                    rows = payload[key]
                    break
        if rows is None:
            raise HubError(f"{self.name}: unrecognised search response shape")
        refs: list[HubSkillRef] = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            slug = str(row.get("slug") or "").strip()
            if not slug:
                continue
            refs.append(
                HubSkillRef(
                    hub=self.name,
                    slug=slug,
                    display_name=str(row.get("displayName") or row.get("name") or slug),
                    summary=str(row.get("summary") or row.get("description") or ""),
                    version=str(row.get("version") or ""),
                )
            )
        return refs

    def verify(self, slug: str, *, version: str | None = None) -> HubVerdict:
        try:
            response = self._get(
                f"/skills/{slug}/verify", version=version, tag=None if version else "latest"
            )
            payload = response.json()
        except (HubError, ValueError) as exc:
            return HubVerdict(status="unknown", detail=str(exc))
        if not isinstance(payload, dict):
            return HubVerdict(status="unknown", detail="unrecognised verify response")
        decision = str(payload.get("decision") or "").strip().lower()
        if payload.get("ok") is True:
            return HubVerdict(status="ok", detail=decision)
        return HubVerdict(status="suspicious", detail=decision or "hub flagged this package")

    def fetch(self, slug: str, *, version: str | None = None) -> FetchedSkill:
        response = self._get(
            "/download", slug=slug, version=version, tag=None if version else "latest"
        )
        tmp = Path(tempfile.mkdtemp(prefix="deeptutor-skill-"))
        try:
            zip_path = tmp / "package.zip"
            zip_path.write_bytes(response.content)
            extracted = tmp / "extracted"
            _extract_skill_zip(zip_path, extracted)
            root = _locate_package_root(extracted)
        except Exception:
            shutil.rmtree(tmp, ignore_errors=True)
            raise
        resolved_version = version or self._latest_version(slug)
        return FetchedSkill(
            ref=HubSkillRef(hub=self.name, slug=slug, version=resolved_version),
            root=root,
            cleanup_dir=tmp,
        )

    def _latest_version(self, slug: str) -> str:
        """Resolve the version actually served by an untagged download."""
        try:
            payload = self._get(f"/skills/{slug}").json()
        except (HubError, ValueError):
            return ""
        if not isinstance(payload, dict):
            return ""
        latest = payload.get("latestVersion") or payload.get("latest_version")
        if isinstance(latest, dict):
            latest = latest.get("version")
        if latest is None and isinstance(payload.get("skill"), dict):
            latest = payload["skill"].get("latestVersion")
        return str(latest or "").strip()


class CommandProvider:
    """Generic fetch-by-command provider for registries without a public API.

    The configured ``fetch_cmd`` template receives ``{slug}``, ``{version}``
    (empty string when unpinned) and ``{dest}`` — it must leave the package
    (a ``SKILL.md`` tree, or a zip we can extract) under ``{dest}``. The
    command runs without a shell; pipes and substitutions won't work, which
    is the point.
    """

    def __init__(self, name: str, *, fetch_cmd: str) -> None:
        self.name = name
        self._fetch_cmd = fetch_cmd

    def search(self, query: str, *, limit: int = 10) -> list[HubSkillRef]:
        raise HubError(f"{self.name}: this hub does not support search.")

    def verify(self, slug: str, *, version: str | None = None) -> HubVerdict:
        return HubVerdict(status="unknown", detail="command hubs have no verdict API")

    def fetch(self, slug: str, *, version: str | None = None) -> FetchedSkill:
        tmp = Path(tempfile.mkdtemp(prefix="deeptutor-skill-"))
        dest = tmp / "fetched"
        dest.mkdir()
        argv = [
            part.format(slug=slug, version=version or "", dest=str(dest))
            for part in shlex.split(self._fetch_cmd)
        ]
        try:
            completed = subprocess.run(
                argv,
                cwd=str(tmp),
                capture_output=True,
                text=True,
                timeout=_FETCH_CMD_TIMEOUT,
                check=False,
            )
            if completed.returncode != 0:
                raise HubError(
                    f"{self.name}: fetch command failed "
                    f"({completed.returncode}): {(completed.stderr or completed.stdout)[:300]}"
                )
            root = self._resolve_fetched_root(dest, tmp)
        except Exception:
            shutil.rmtree(tmp, ignore_errors=True)
            raise
        return FetchedSkill(
            ref=HubSkillRef(hub=self.name, slug=slug, version=version or ""),
            root=root,
            cleanup_dir=tmp,
        )

    @staticmethod
    def _resolve_fetched_root(dest: Path, tmp: Path) -> Path:
        """Accept either an extracted tree or a single zip in ``dest``."""
        zips = sorted(dest.glob("*.zip"))
        if len(zips) == 1 and not (dest / "SKILL.md").is_file():
            extracted = tmp / "extracted"
            _extract_skill_zip(zips[0], extracted)
            return _locate_package_root(extracted)
        return _locate_package_root(dest)


# ── provider registry ─────────────────────────────────────────────────────


def _load_hub_settings() -> dict[str, dict[str, Any]]:
    try:
        path = get_path_service().get_settings_file(_HUBS_SETTINGS_FILE)
    except Exception:
        return {}
    if not isinstance(path, Path) or not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        logger.warning("skill_hubs settings file is unreadable; ignoring it")
        return {}
    hubs = data.get("hubs") if isinstance(data, dict) else None
    if not isinstance(hubs, dict):
        return {}
    return {str(name): value for name, value in hubs.items() if isinstance(value, dict)}


def get_hub_provider(name: str) -> SkillHubProvider:
    """Resolve a hub name to a provider: built-in ``clawhub`` plus settings."""
    hub = (name or DEFAULT_HUB).strip().lower()
    configured = _load_hub_settings().get(hub)
    if configured is not None:
        kind = str(configured.get("type") or "").strip().lower()
        if kind == "clawhub":
            return ClawHubProvider(
                hub, base_url=str(configured.get("base_url") or _CLAWHUB_BASE_URL)
            )
        if kind == "command":
            fetch_cmd = str(configured.get("fetch_cmd") or "").strip()
            if not fetch_cmd:
                raise HubError(f"Hub `{hub}` is missing fetch_cmd in skill_hubs settings.")
            return CommandProvider(hub, fetch_cmd=fetch_cmd)
        raise HubError(f"Hub `{hub}` has unknown type `{kind}` in skill_hubs settings.")
    if hub == DEFAULT_HUB:
        return ClawHubProvider()
    raise HubError(
        f"Unknown hub `{hub}`. Configure it in settings/skill_hubs.json or use `clawhub:`."
    )


# ── orchestration ─────────────────────────────────────────────────────────


def install_from_hub(
    ref: str,
    *,
    service: SkillService,
    rename_to: str | None = None,
    force: bool = False,
    allow_unverified: bool = False,
    provider: SkillHubProvider | None = None,
) -> HubInstallOutcome:
    """One-shot pipeline: verify → fetch → install → record provenance.

    ``suspicious`` verdicts abort unless ``allow_unverified`` is set;
    ``unknown`` verdicts install but are stamped into provenance so the
    caller can warn. ``provider`` is injectable for tests.
    """
    hub, slug, version = parse_hub_ref(ref)
    resolved = provider or get_hub_provider(hub)

    verdict = resolved.verify(slug, version=version)
    if verdict.status == "suspicious" and not allow_unverified:
        raise SkillImportError(
            f"{hub} flags `{slug}` as suspicious"
            + (f" ({verdict.detail})" if verdict.detail else "")
            + ". Pass --allow-unverified to install anyway."
        )

    fetched = resolved.fetch(slug, version=version)
    try:
        result = service.install_tree(
            fetched.root,
            rename_to=rename_to,
            fallback_description=fetched.ref.summary or None,
            force=force,
            origin={
                "hub": hub,
                "slug": slug,
                "version": fetched.ref.version or version or "",
                "verdict": verdict.status,
                "installed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            },
        )
    finally:
        fetched.cleanup()
    return HubInstallOutcome(result=result, ref=fetched.ref, verdict=verdict)


__all__ = [
    "DEFAULT_HUB",
    "ClawHubProvider",
    "CommandProvider",
    "FetchedSkill",
    "HubError",
    "HubInstallOutcome",
    "HubSkillRef",
    "HubVerdict",
    "SkillHubProvider",
    "get_hub_provider",
    "install_from_hub",
    "parse_hub_ref",
]

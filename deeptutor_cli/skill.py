"""
CLI Skill Commands
==================

Manage local skills and install packages from external hubs (ClawHub, …).

Hub references use ``<hub>:<slug>[@version]``; the hub prefix defaults to
``clawhub``. Installs run the full import gate: hub security verdict →
safe extraction → frontmatter adaptation (``always`` stripped, flat
``bins``/``env`` folded into ``requires``) → provenance in ``.hub-lock.json``.

In a multi-user deployment this CLI operates the owner (admin) workspace, so
an installed skill lands in the admin catalog and stays invisible to other
users until a grant assigns it.
"""

from __future__ import annotations

from rich.table import Table
import typer

from .common import console


def register(app: typer.Typer) -> None:
    @app.command("search")
    def skill_search(
        query: str = typer.Argument(..., help="Natural-language search query."),
        hub: str = typer.Option("clawhub", "--hub", help="Hub to search."),
        limit: int = typer.Option(10, "--limit", min=1, max=50, help="Max results."),
    ) -> None:
        """Search a skill hub."""
        from deeptutor.services.skill.hub import HubError, get_hub_provider

        try:
            refs = get_hub_provider(hub).search(query, limit=limit)
        except HubError as exc:
            console.print(f"[bold red]Search failed:[/] {exc}")
            raise typer.Exit(code=1)
        if not refs:
            console.print("[dim]No skills matched.[/]")
            return
        table = Table(title=f"{hub}: {query}")
        table.add_column("Ref", style="bold")
        table.add_column("Version")
        table.add_column("Summary")
        for ref in refs:
            table.add_row(
                f"{ref.hub}:{ref.slug}",
                ref.version or "-",
                ref.summary[:100] or ref.display_name,
            )
        console.print(table)
        console.print("[dim]Install with: deeptutor skill install <ref>[/]")

    @app.command("install")
    def skill_install(
        ref: str = typer.Argument(..., help="Skill ref: <hub>:<slug>[@version]."),
        name: str | None = typer.Option(
            None, "--name", help="Install under a different local skill name."
        ),
        force: bool = typer.Option(
            False, "--force", help="Overwrite an existing skill with the same name."
        ),
        allow_unverified: bool = typer.Option(
            False,
            "--allow-unverified",
            help="Install even when the hub flags the package as suspicious.",
        ),
    ) -> None:
        """Install a skill from a hub into the local skill library."""
        from deeptutor.services.skill.hub import HubError, install_from_hub
        from deeptutor.services.skill.service import (
            InvalidSkillNameError,
            SkillExistsError,
            SkillImportError,
            get_skill_service,
        )

        service = get_skill_service()
        try:
            outcome = install_from_hub(
                ref,
                service=service,
                rename_to=name,
                force=force,
                allow_unverified=allow_unverified,
            )
        except SkillExistsError as exc:
            console.print(
                f"[bold red]Skill `{exc}` already exists.[/] Re-run with --force to replace it."
            )
            raise typer.Exit(code=1)
        except (HubError, SkillImportError, InvalidSkillNameError) as exc:
            console.print(f"[bold red]Install failed:[/] {exc}")
            raise typer.Exit(code=1)

        info = outcome.result.info
        verdict = outcome.verdict
        verdict_style = {"ok": "green", "suspicious": "red"}.get(verdict.status, "yellow")
        console.print(
            f"[bold green]Installed[/] [bold]{info.name}[/]"
            + (f" [dim]({outcome.ref.hub}@{outcome.ref.version})[/]" if outcome.ref.version else "")
        )
        console.print(
            f"  verdict: [{verdict_style}]{verdict.status}[/]"
            + (f" [dim]{verdict.detail}[/]" if verdict.detail else "")
        )
        if verdict.status != "ok":
            console.print(
                f"  [yellow]Review before use:[/] [dim]{service.root / info.name / 'SKILL.md'}[/]"
            )
        for entry in service.summary_entries():
            if entry.name == info.name and not entry.available:
                console.print(f"  [yellow]unavailable until:[/] {', '.join(entry.missing)}")
        for rel, reason in outcome.result.skipped:
            console.print(f"  [dim]skipped {rel} — {reason}[/]")

    @app.command("list")
    def skill_list() -> None:
        """List local skills, including hub provenance."""
        from deeptutor.services.skill.service import get_skill_service

        service = get_skill_service()
        table = Table(title="Skills")
        table.add_column("Name", style="bold")
        table.add_column("Source")
        table.add_column("Origin")
        table.add_column("Description")
        for info in service.list_skills():
            origin = service.hub_origin(info.name)
            origin_label = "-"
            if origin:
                version = str(origin.get("version") or "").strip()
                origin_label = str(origin.get("hub") or "hub") + (f"@{version}" if version else "")
            table.add_row(info.name, info.source, origin_label, info.description[:80])
        console.print(table)

    @app.command("remove")
    def skill_remove(
        name: str = typer.Argument(..., help="Skill name to remove."),
    ) -> None:
        """Remove a user-layer skill (builtin skills are read-only)."""
        from deeptutor.services.skill.service import (
            InvalidSkillNameError,
            SkillNotFoundError,
            SkillReadOnlyError,
            get_skill_service,
        )

        try:
            get_skill_service().delete(name)
        except (SkillNotFoundError, InvalidSkillNameError):
            console.print(f"[bold red]Skill not found:[/] {name}")
            raise typer.Exit(code=1)
        except SkillReadOnlyError as exc:
            console.print(f"[bold red]{exc}[/]")
            raise typer.Exit(code=1)
        console.print(f"[green]Removed[/] {name}")

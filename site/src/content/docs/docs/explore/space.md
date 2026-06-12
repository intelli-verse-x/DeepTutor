---
title: Space
description: "Manage reusable context: skills, personas, notebooks, chat history, and question assets."
---

Space is the library layer for reusable context. It is where you manage assets that can shape future Chat turns, Partner behavior, Co-Writer drafts, and Book generation.

![Space workspace](/screenshots/space.png)

## What belongs in Space

| Asset | Use it for |
| --- | --- |
| **Skills** | `SKILL.md` files that teach DeepTutor a workflow, style, or domain behavior. |
| **Personas** | Role/voice instructions that can be selected in Chat or copied into Partners. |
| **Notebooks** | Durable records saved from Chat, Research, Co-Writer, or manual Markdown import. |
| **Chat History** | Resumable sessions and past context. |
| **Question assets** | Practice material that can be referenced later. |

## Skills

Skills live under the user workspace and can be tagged, edited, previewed, or kept read-only if they are built in. A good skill is specific: it tells the agent when to use it, what inputs it expects, and what output shape is useful.

You don't have to write every skill yourself: DeepTutor skills share their format with the wider Agent-Skills ecosystem, and `deeptutor skill install clawhub:<slug>` imports a community skill from [ClawHub](https://clawhub.ai/) through a security gate — hub verdict check, safe extraction, no binaries, no prompt self-injection. See [CLI commands](/docs/cli/commands/) for the full flow.

## Personas and Partners

Personas are lightweight role definitions. Partners have a stronger `SOUL.md`, but personas are a good starting point: create or refine a persona in Space, then use it while creating a Partner.

## Notebooks

Notebooks are the easiest way to turn an answer into durable context. Save summaries, research outputs, writing drafts, or book reading notes, then attach them later from Chat or CLI.

## See also

- [Chat Workspace](/docs/explore/chat-workspace/) — attach Space context to turns
- [Partners](/docs/explore/partners/) — assign skills/notebooks to partners
- [Co-Writer](/docs/explore/co-writer/) — save drafts to notebooks

---
title: Interactive REPL
description: A long-running terminal chat session with inline /slash commands for switching capabilities, tools, KBs, and more.
---

`deeptutor chat` opens an interactive REPL — useful for **exploratory work**, **multi-turn debugging**, and **driving DeepTutor with your hands** instead of with `run` calls.

## Launching

```bash
# Default — chat capability, no KBs, no extra tools
deeptutor chat

# Pre-attach a KB and pre-enable a tool
deeptutor chat --kb physics --tool rag --tool reason

# Start in a specific capability (e.g., always use Deep Solve)
deeptutor chat --capability deep_solve

# Resume a prior session
deeptutor chat --session sess_abc123

# Hand it preferences via flags (same as run)
deeptutor chat --language zh --kb papers --history-ref sess_old_xyz
```

## What the REPL looks like

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ DeepTutor CLI                                                      ┃
┃ Type a message to chat. Commands:                                 ┃
┃   /quit  /session  /new                                           ┃
┃   /regenerate (alias /retry) — re-run the last user message       ┃
┃   /tool on|off <name>                                             ┃
┃   /cap <name>                                                     ┃
┃   /kb <name>|none                                                 ┃
┃   /history add <id> | /history clear                              ┃
┃   /notebook add <ref> | /notebook clear                           ┃
┃   /show last|<n> — expand a truncated tool result                 ┃
┃   /refs  /config show|set|clear                                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
[dim]session=(new) capability=chat tools=[] kb=[] history=[] notebook_refs=[] language=en config={}[/]
You> _
```

The dimmed status line shows everything that will be sent on your next turn: session id, capability, tools, attached KBs, history references, notebook references, language, and config.

## A typical session

```text
You> What is the chain rule?

▶ thinking
  [dim]The user is asking about a foundational calculus concept...[/]

▶ responding
The **chain rule** says that to differentiate a composite function `f(g(x))`, you multiply...

[dim]session=sess_abc123 turn=turn_xyz789 capability=chat[/]

You> /tool on rag
[dim]session=sess_abc123 capability=chat tools=[rag] kb=[] ...[/]

You> /kb math
[dim]session=sess_abc123 capability=chat tools=[rag] kb=[math] ...[/]

You> Now with a worked example from chapter 3 of the textbook

▶ retrieving
  ● rag_search(query="chain rule worked example")
  │ Example: differentiate sin(x²) using the chain rule...
  └ #1 rag — +3 more lines

▶ responding
Here's the example from chapter 3:

Take `y = sin(x²)`. Let `u = x²`...

You> /quit
$
```

## All slash commands

### Session

| Command | Effect |
|---------|--------|
| `/quit` | Exit the REPL |
| `/session` | Print the current session id |
| `/new` | Start a fresh session, clearing the id |
| `/regenerate` (or `/retry`) | Re-run the last user message with the current config |

### Capability switching

| Command | Effect |
|---------|--------|
| `/cap <name>` | Switch to a different capability |

Valid names: `chat`, `deep_solve`, `deep_question`, `deep_research`, `math_animator`, `visualize`, `auto`. CLI aliases also work (e.g., `solve` → `deep_solve`, `quiz` → `deep_question`).

```text
You> /cap deep_solve
[dim]capability=deep_solve ...[/]
You> Find d/dx [sin(x²)]
```

### Tools

```text
/tool on <name>     # Enable a tool for next turn
/tool off <name>    # Disable it
```

Valid tool names: `rag`, `web_search`, `code_execution`, `reason`, `brainstorm`, `paper_search`. Some tools (like `read_memory`, `web_fetch`) are always-on and don't need to be explicitly toggled.

### Knowledge Bases

```text
/kb <name>          # Attach a KB (replaces any current attachment)
/kb none            # Detach
```

### History references

Tell the model about prior sessions it should treat as context (without copy-pasting):

```text
/history add sess_prior_xyz
/history clear
```

This is how you build cross-session context — perfect for "follow-up" research turns.

### Notebook references

Bring in specific records from your notebooks:

```text
/notebook add my-notes:rec_abc123,rec_def456
/notebook clear
```

### Config overrides

Per-capability config that applies to subsequent turns:

```text
/config show                       # Print current config
/config set num_questions 5
/config set difficulty=hard
/config set difficulty hard
/config clear                      # Reset to defaults
```

For example, with `--capability deep_question`:

```text
You> /config set num_questions 8
You> /config set question_types '["short_answer","mcq"]'
You> Generate questions on linear regression
```

### Inspecting tool results

Tool results in the REPL are truncated to first 10 lines / 240 chars per line to keep the display clean. To expand a specific one:

```text
/show last          # Last tool result
/show 3             # The third tool result in this session
```

Up to 32 results are buffered in memory for expansion.

### `/refs`

Print everything that will go into the next turn:

```text
You> /refs
[bold]Current state:[/]
  session     sess_abc123
  capability  chat
  tools       [rag, reason]
  kb          [physics, math]
  history     [sess_old_xyz]
  notebooks   [my-notes:rec_abc123]
  language    en
  config      {"difficulty": "hard", "num_questions": 5}
```

## How streaming works in the REPL

Each turn is rendered stage by stage. You'll see, in order:

| Indicator | Meaning |
|-----------|---------|
| `▶ <stage>` | A new pipeline stage just started (e.g., `retrieving`, `reasoning`, `writing`) |
| `  [dim]…[/]` | Intermediate thinking — model's chain-of-thought-ish reasoning |
| `  ● <tool>(...)` | A tool was just invoked |
| `  │ <line>` | A line of tool output |
| `  └ #N <tool> — +M more lines; run /show N to expand` | Tool result was truncated |
| *plain text* | Final markdown response, rendered |

## Tips

### Multi-line input

For multi-line messages (code snippets, long prompts), end each line with a backslash `\` and press Enter:

```text
You> Please review this Python code:\
def fib(n):\
    if n < 2: return n\
    return fib(n-1) + fib(n-2)
```

### Switching capabilities mid-session

You can freely switch capabilities within a session — DeepTutor keeps the conversation context. A common pattern:

```text
You> /cap deep_research
You> /config set mode=report
You> /config set depth=standard
You> Survey recent papers on RAG (2024–2026)
[long research turn]

You> /cap chat
You> Now write a 3-paragraph summary suitable for a non-technical audience

You> /cap deep_question
You> /config set num_questions 5
You> Generate quiz questions about those papers
```

All three turns share the same memory and reference each other automatically.

### Saving the session log

Sessions are stored in the shared session database. To export a clean markdown transcript:

```bash
deeptutor session show sess_abc123 --format json | \
  jq -r '.messages[] | "**" + .role + "**: " + .content + "\n"' > transcript.md
```

### Going from REPL → notebook

Like a turn? Save it to a notebook:

```bash
# In the REPL
You> /quit

# Then from shell, capture the assistant's last message
deeptutor session show sess_abc123 --format json | \
  jq -r '.messages[-1].content' > my-answer.md

deeptutor notebook add-md my-notes my-answer.md --title "Chain rule explanation"
```

## See also

- [**Commands**](/docs/cli/commands/) — full reference for `run`, `kb`, `bot`, etc.
- [**Agent handoff**](/docs/cli/agent-handoff/) — letting an agent do this for you

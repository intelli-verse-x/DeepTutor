# DeepTutor Local Patch Notes

> Local fixes applied on top of mainstream v1.1.0.
> Re-apply these after syncing from upstream (https://github.com/HKUDS/DeepTutor).

---

## Fix 1: Deep Research — "settings are incomplete" guard

**Problem:** When Deep Research mode is active but the research config hasn't been fully initialized yet, `buildResearchWSConfig()` throws and the message gets swallowed — the user sees nothing happen when they hit send.

**Root cause:** `handleSend()` unconditionally called `buildResearchWSConfig(researchConfig)` even when `researchConfig` fields like `depth` were empty strings. The validation check existed in the UI (composer shows disabled state) but was not enforced at send time — a race condition / edge case.

**Files affected:**

| File | Change |
|---|---|
| `web/app/(workspace)/chat/[[...sessionId]]/page.tsx` | Added `if (!researchValidation.valid) return;` guard before `buildResearchWSConfig(researchConfig)` call (line ~555) |
| `web/app/(workspace)/chat/[[...sessionId]]/page.tsx` | Added `researchValidation` to the `useCallback` dependency array (line ~570) |

**Diff snippet:**

```typescript
// BEFORE
if (isResearchMode) config = buildResearchWSConfig(researchConfig);

// AFTER
if (isResearchMode) {
  if (!researchValidation.valid) return;
  config = buildResearchWSConfig(researchConfig);
}
```

**Re-apply after sync:** Search for `isResearchMode` in `page.tsx` — the guard must be placed before `buildResearchWSConfig`. If the upstream changed the variable name (`researchValidation` / `researchConfig`), adapt accordingly.

---

## Fix 2: Windows GBK encoding crash (emoji in print())

**Problem:** Backend crashes with `'gbk' codec can't encode character '\U0001f500'` when running on Windows (Chinese/Japanese locale). The emoji characters in `decompose_agent.py` `print()` statements cannot be encoded to the Windows default GBK code page.

**Root cause:** `sys.stdout` on Windows defaults to the system locale encoding (e.g. `gbk` on zh-CN Windows). Emoji characters (🔄, ✅, ❌, etc.) are outside the GBK character set. When `print()` tries to write them to stdout, Python throws `UnicodeEncodeError`.

**Files affected:**

| File | Change |
|---|---|
| `deeptutor/api/run_server.py` | Added `encoding="utf-8"` to both `sys.stdout.reconfigure()` and `sys.stderr.reconfigure()` calls |
| `start_backend.bat` | Added `set PYTHONIOENCODING=utf-8` and `set PYTHONUTF8=1` before launching Python |

**Diff snippet (`run_server.py`):**

```python
# BEFORE
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(line_buffering=True)

# AFTER
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(line_buffering=True, encoding="utf-8")
```

**Diff snippet (`start_backend.bat`):**

```batch
@echo off
cd /d "%~dp0"

REM Set UTF-8 encoding for stdout to support emoji characters
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

call .venv\Scripts\activate.bat
python -m deeptutor.api.run_server
pause
```

**Source of the emoji:** `deeptutor/agents/research/agents/decompose_agent.py` line ~131 has `print()` calls with emoji characters. On Linux/Mac these work fine (UTF-8 by default); on Windows they fail.

**Re-apply after sync:** Two changes needed:
1. Add `encoding="utf-8"` to `sys.stdout.reconfigure()` and `sys.stderr.reconfigure()` in `run_server.py`
2. Add `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1` in the startup script

---

## Fix 3: Notebook service module not importable

**Problem:** Frontend "Save to Notebook" modal shows "No Notebooks found" even though notebooks exist. The `/api/v1/notebook/list` API endpoint either returns empty or errors silently.

**Root cause discovered so far:** The `deeptutor/services/notebook/` directory was missing from the working tree (possibly deleted or not checked out properly). Restored from git HEAD. Also, the `deeptutor/services/__init__.py` was missing a lazy import for `notebook_manager`, so `from deeptutor.services import notebook_manager` would fail at runtime if the directory existed but the import wasn't wired.

**Files affected:**

| File | Change |
|---|---|
| `deeptutor/services/notebook/` | Restored entire directory from git HEAD (service.py, __init__.py) |
| `deeptutor/services/__init__.py` | Added lazy import for `notebook_manager` and added `"notebook"` to `__all__` |

**Diff snippet (`services/__init__.py`):**

```python
# In __all__ — added "notebook"
__all__ = [
    ...
    "notebook",       # NEW
    ...
]

# In __getattr__ — added notebook_manager lazy import
if name == "notebook_manager":
    from .notebook import notebook_manager
    return notebook_manager
```

**Re-apply after sync:**
1. Verify `deeptutor/services/notebook/` exists with `service.py` and `__init__.py`
2. Add the `notebook_manager` lazy import in `deeptutor/services/__init__.py` (and `"notebook"` to `__all__`)
3. Test with: `python -c "from deeptutor.services import notebook_manager; print(notebook_manager)"`

---

## Fix 4 (Unconfirmed): SaveToNotebookModal — image model crash

**Problem (reported but root cause not yet confirmed):** When using "Save to Notebook" from a chat record that includes an image attachment, the `NotebookSummarizeAgent` tries to generate a summary. The agent uses the LLM model (likely `gpt-4o-mini`), and if the model doesn't support image input, it fails with an error like "Cannot read image.png (this model does not support image input)".

**Speculative:** The `_build_record_summary` function in `deeptutor/api/routers/notebook.py` passes the record to `NotebookSummarizeAgent.summarize()`, which sends the raw `output` (which may include image references) to the LLM. If the output contains image URLs/data that the LLM cannot process, it throws.

**No fix applied yet** — needs investigation.

---

## Startup scripts (new files)

These are convenience scripts created for local use, not in the upstream repo:

| File | Description |
|---|---|
| `start_backend.bat` | Activates venv, sets UTF-8 encoding, starts `python -m deeptutor.api.run_server` |
| `start_frontend.bat` | Runs `npm run dev -- -p 3782` in the `web/` directory |

---

## Verification checklist

After re-syncing from upstream, run these checks:

```bash
# 1. Check Deep Research guard
grep -n "isResearchMode" web/app/(workspace)/chat/[[...sessionId]]/page.tsx

# 2. Check UTF-8 encoding in run_server.py
grep -n "encoding" deeptutor/api/run_server.py

# 3. Check notebook import
python -c "from deeptutor.services import notebook_manager; print('OK:', notebook_manager)"

# 4. Test notebook list API
curl -s http://localhost:8001/api/v1/notebook/list | python -m json.tool
```

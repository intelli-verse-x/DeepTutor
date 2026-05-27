# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and usage patterns.

## exec — Shell Execution

- The shell execution tool is disabled unless an administrator explicitly enables it.
- When enabled, commands have a configurable timeout (default 60s).
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.).
- Output is truncated at 10,000 characters.
- File access is restricted to the workspace by default.

## cron — Scheduled Reminders

- Please refer to cron skill for usage.

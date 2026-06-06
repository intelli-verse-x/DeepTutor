---
title: Email
description: TutorBot over email — IMAP polling + SMTP replies, with explicit consent and full body parsing.
---

The Email channel turns your TutorBot into an asynchronous email correspondent. Users send mail to a configured inbox, the bot reads via IMAP, replies via SMTP. Useful for **async help desks** and for users who prefer email.

## What you need

- An email account (Gmail, Outlook, your own SMTP/IMAP server, etc.)
- App-password access *(or OAuth, see below)*
- 5 minutes of config

## Step 1 — Configure mail credentials

For **Gmail**:

1. Enable 2FA on the account
2. Create an [**App Password**](https://myaccount.google.com/apppasswords) (16-character single-use password)
3. Use that as the password in the config below

For **Outlook / Office 365**: Either an App Password (with 2FA enabled) or OAuth. App Passwords are simpler for personal use.

For **self-hosted** (Postfix, Maddy, etc.): use the account credentials directly.

## Step 2 — Configure

```yaml
channels:
  email:
    enabled: true
    consent_granted: true              # MUST be explicit — privacy safeguard

    # IMAP (inbound)
    imap_host: "imap.gmail.com"
    imap_port: 993
    imap_username: "tutor@example.com"
    imap_password: "YOUR_APP_PASSWORD"
    imap_mailbox: "INBOX"
    imap_use_ssl: true

    # SMTP (outbound)
    smtp_host: "smtp.gmail.com"
    smtp_port: 587
    smtp_username: "tutor@example.com"
    smtp_password: "YOUR_APP_PASSWORD"
    smtp_use_tls: true
    smtp_use_ssl: false
    from_address: "tutor@example.com"

    # Behavior
    auto_reply_enabled: true
    poll_interval_seconds: 30          # IMAP check frequency
    mark_seen: true                    # mark messages as read after processing
    max_body_chars: 12000
    subject_prefix: "Re: "
    allow_from:                        # email addresses; [] = open, ["x@..."] = allowlist
      - "student@example.com"
```

## Step 3 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:email → connecting (imap.gmail.com:993)
[bot:my-math-tutor] channel:email → ready, polling every 30s
```

Send an email to `tutor@example.com` from your allowed address — within 30 seconds (or the next poll), you get an automated reply.

## Why `consent_granted` is required

Reading email is sensitive. The channel **refuses to start** unless `consent_granted: true` is set explicitly — a hard gate to prevent accidental email reading. This is a deliberate privacy safeguard.

## Config reference

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `enabled` | bool | yes | `false` |
| `consent_granted` | bool | yes | `false` — must explicitly set `true` |
| `imap_host` | string | yes | — |
| `imap_port` | int | yes | `993` |
| `imap_username` | string | yes | — |
| `imap_password` | string | yes | — |
| `imap_mailbox` | string | optional | `"INBOX"` |
| `imap_use_ssl` | bool | optional | `true` |
| `smtp_host` | string | yes | — |
| `smtp_port` | int | yes | `587` |
| `smtp_username` | string | yes | — |
| `smtp_password` | string | yes | — |
| `smtp_use_tls` | bool | optional | `true` |
| `smtp_use_ssl` | bool | optional | `false` |
| `from_address` | string | optional | = `smtp_username` |
| `auto_reply_enabled` | bool | optional | `true` |
| `poll_interval_seconds` | int | optional | `30` |
| `mark_seen` | bool | optional | `true` |
| `max_body_chars` | int | optional | `12000` |
| `subject_prefix` | string | optional | `"Re: "` |
| `allow_from` | list[string] | optional | `[]` (open to anyone) |

## Capabilities on Email

| Feature | Supported |
|---------|-----------|
| Plain text bodies | ✅ |
| HTML bodies | ✅ *(converted to markdown)* |
| Attachments inbound | ✅ *(PDFs, images, text files)* |
| Attachments outbound | ✅ *(reply with files via SMTP)* |
| Threading | ✅ *(via `In-Reply-To` headers)* |
| Subject prefixing | ✅ *(`Re: ` by default)* |
| LaTeX in body | ⚠️ rendered as plain text; consider converting to PDF for math-heavy responses |

## Session model

Each unique sender email is treated as a separate session. Replies in the same email thread (matched by `In-Reply-To`) continue the same session.

This means a single user emailing from `student@example.com` always lands in the same DeepTutor session — perfect for ongoing async help.

## Keep-alive specifics

The Email channel uses a **background polling loop**:

- Every `poll_interval_seconds`, the channel logs in via IMAP, fetches unseen messages, processes them, marks them seen
- On IMAP disconnect, auto-reconnects on next poll
- SMTP connection is opened per-send (no persistent connection)

For high-volume use, set `poll_interval_seconds: 15` or lower. Below 10 seconds you may hit your provider's rate limits.

## Common issues

### Won't start — "consent_granted is required"

You forgot to set:

```yaml
consent_granted: true
```

This is intentional friction. Set it consciously.

### "Authentication failed" on Gmail / Outlook

You used your account password instead of an App Password. With 2FA enabled, regular passwords are blocked for IMAP/SMTP — must use a 16-char App Password.

### Too many replies / loop with another auto-responder

If two auto-responders email each other, you get a feedback loop. The channel detects loops by checking the `Auto-Submitted:` header — but if the other side doesn't set it, loops are possible. Defensive measures:

- Use `allow_from` to restrict who the bot replies to
- Set `auto_reply_enabled: false` and manually trigger replies from CLI

### IMAP folder not found

Some providers use different mailbox names (`INBOX` vs `Inbox` vs `[Gmail]/All Mail`). Check via the provider's webmail and update `imap_mailbox`.

### Replies marked as spam

Add a proper `from_address`, set up SPF/DKIM/DMARC records for your domain if self-hosted, or use a trusted SMTP relay (SendGrid, Mailgun) for outbound only.

## See also

- [**WhatsApp**](/docs/tutorbot/whatsapp/) — another bridge-style channel
- [**Explore TutorBot**](/docs/tutorbot/) — architecture

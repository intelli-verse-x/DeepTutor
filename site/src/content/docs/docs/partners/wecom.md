---
title: WeCom (WeChat Work)
description: Configure Enterprise WeChat / WeCom AI Bot delivery for a Partner.
---

<img src="/channel-icons/wecom.svg" alt="" width="40" height="40" />

Use `wecom` for Enterprise WeChat / WeChat Work. It connects through the WeCom AI Bot WebSocket long connection and is different from personal [WeChat (`weixin`)](/docs/partners/weixin/).

![WeCom channel configuration](/screenshots/partners-channel-wecom.png)

## Requirements

- A WeCom organization with admin access.
- The `wecom-aibot-sdk` Python package. Install via the Partners extra or directly if needed.

```bash
pip install -e ".[partners]"
python -c "import wecom_aibot_sdk; print('ok')"
```

## Create the bot in WeCom

1. Sign in to <https://work.weixin.qq.com/>.
2. Open **Applications & Mini Programs -> AI Bot Platform**.
3. Create an **AI Bot** application.
4. Configure name, description, visible departments/users, and any required approval settings.
5. Copy **Bot ID** and **Secret**.

## Configure DeepTutor

Open **Partners -> your partner -> Channels -> WeCom** and fill:

| Field | Notes |
| --- | --- |
| `enabled` | Start this channel when the partner starts. |
| `bot_id` | Bot ID from WeCom AI Bot platform. |
| `secret` | Secret from WeCom. Treat it as a credential. |
| `allow_from` | User ids allowed to talk to this partner. Empty denies access; `*` opens it where supported by the base channel policy. |
| `welcome_message` | Optional text sent when a user opens the chat. |
| `send_progress` / `send_tool_hints` | Delivery switches for narration and one-line tool calls. |

## Access control and visibility

WeCom has two layers of access control:

1. WeCom application visibility controls who can open the AI Bot inside the organization.
2. DeepTutor `allow_from` controls which sender ids are allowed into the Partner runtime.

During first setup, keep the WeCom visible range small and set `allow_from` explicitly once you know the sender ids from logs.

## Start and test

```bash
deeptutor partner start <partner-id>
```

The server log should show a WeCom WebSocket connection and authentication. Then open the AI Bot in WeCom and send a short message.

## Troubleshooting

- **`ImportError: wecom_aibot_sdk`** — install `wecom-aibot-sdk` or the Partners extra in the same environment running DeepTutor.
- **Connects but no reply** — check `allow_from`, department visibility, and whether the sender is allowed to use the AI Bot application.
- **Disconnects** — transient disconnects auto-reconnect. If it stays offline, verify Bot ID / Secret and outbound network access to WeCom.

---
title: Feishu
description: Configure the Feishu / Lark channel for a Partner — Open Platform app setup, WebSocket long connection, and CardKit streaming cards.
---

<img src="/channel-icons/feishu.svg" alt="" width="40" height="40" />

The `feishu` channel connects a Partner to a Feishu (飞书) or Lark custom app through the official `lark-oapi` SDK over a **WebSocket long connection**: DeepTutor dials out to Feishu's servers, so you need no public IP, no webhook URL, and no reverse proxy. The same channel serves both mainland Feishu (`open.feishu.cn`) and international Lark (`open.larksuite.com`) apps, which makes it the natural choice for a workplace tutor inside a Chinese organization.

The channel also supports **Streaming**: with the switch on, replies render as CardKit streaming cards that fill in with a live typewriter effect while the answer is generated.

![Feishu channel configuration](/screenshots/partners-channel-feishu.png)

## Install requirements

Feishu support ships with the Partners extra; the underlying client is the official `lark-oapi` SDK — nothing extra to install.

```bash
pip install -e ".[partners]"
# or, from an installed release when partners extras are available:
pip install "deeptutor[partners]"
```

## Create an app on the Open Platform

1. Open the [Feishu Open Platform](https://open.feishu.cn/) (or the [Lark Open Platform](https://open.larksuite.com/) for international tenants), go to the **Developer Console**, and create a **Custom App** with a name, description, and icon.
2. On **Credentials & Basic Info**, copy the **App ID** (`cli_...`) and **App Secret** — they go into the channel card.
3. **Features -> Bot**: enable the bot capability and give the bot a display name and avatar.
4. **Events & Callbacks**: switch the subscription mode to **Long Connection** so events arrive over WebSocket instead of a webhook, then subscribe to the `im.message.receive_v1` event.
5. **Permissions & Scopes**: grant the messaging scopes — at minimum `im:message` (read and send as bot); add `im:resource` if images, files, and audio should flow through.
6. **Create a version and release it.** For internal apps this is an internal release plus admin approval. Until a version is released, the bot receives nothing — this is the single most common setup mistake.

If you enable event encryption on the platform (under Events & Callbacks), also note the **Encrypt Key** and **Verification Token**; they must be mirrored into the channel card.

## Configure the channel card

Open **Partners -> your partner -> Channels -> Feishu**.

| Field | What to enter |
| --- | --- |
| **Streaming** | Off by default. Streams the reply live into a CardKit card with a typewriter effect. Requires **Send Progress**: narration rounds stream as they happen. |
| **Send Progress** | Keep on while testing. It delivers narration updates during long turns. |
| **Send Tool Hints** | Keep on for debugging; turn off if users should not see one-line tool calls. |
| **Enabled** | Turn on only when you are ready to start the channel. |
| **App Id** | The `cli_...` App ID from Credentials & Basic Info. |
| **App Secret** | The App Secret from the same page. Stored as a secret and masked after save. |
| **Encrypt Key** | Only needed when event encryption is enabled on the platform. Leave blank otherwise. |
| **Verification Token** | The event Verification Token from the platform; used to verify event signatures. Leave blank if you did not configure one. |
| **Allow From** | One value per line. Use `*` for an open test bot, or `ou_...` open ids (copy them from the partner logs after a first message). Empty denies everyone. |
| **React Emoji** | The reaction the bot adds to every message it accepts, as an instant acknowledgement. Default `THUMBSUP`; other common types: `OK`, `EYES`, `DONE`, `OnIt`, `HEART`. |
| **Group Policy** | `mention` (default): in groups the bot only answers when @mentioned. `open`: it answers every group message. DMs always get a response. |

DeepTutor picks the outbound message format automatically: short plain text goes out as a text message, link-only content as a rich-text post, and anything with headings, code blocks, lists, or tables as an interactive card. Feishu allows one table per card, so multi-table replies are split across several cards.

## After you save

1. Click **Save**, then turn **Enabled** on.
2. Start the partner (or restart it / use the reload action on the Channels panel if it is already running).
3. From an allowed account, open a DM with the bot in Feishu and send a short message.
4. Watch the partner logs: you should see the inbound event, and your message should receive the React Emoji reaction almost immediately.
5. Once you have confirmed the `ou_...` sender id in the logs, replace `*` in **Allow From** with real ids.

## Verify it is healthy

- The logs show `Feishu bot started with WebSocket long connection` and no repeated `Feishu WebSocket error` lines (the channel auto-reconnects every 5 seconds if the connection drops).
- Your test message gets the React Emoji reaction right away — that confirms both inbound events and outbound API credentials work.
- The reply arrives; with **Streaming** on, you see a card filling in live instead of a single final message.

## Troubleshooting

### The bot receives nothing

Three gates must all be open: the app version is **released** (not draft), the `im.message.receive_v1` event is subscribed, and the subscription mode is **Long Connection**. A missing release is the most common cause — re-check it first.

### Messages arrive but replies fail

Usually a missing scope. Make sure `im:message` is granted (plus `im:resource` for media), then **release a new version** — scope changes only take effect after release. The exact API error code appears in the partner logs.

### Events fail after enabling encryption

If you configured an Encrypt Key on the platform, the same value must be in the channel card (along with the Verification Token), and vice versa. After rotating either value on the platform, update the card and restart the partner.

### Streaming cards never stream

**Streaming** requires **Send Progress** to be on. If CardKit card creation fails (look for `Failed to create Feishu streaming card` in the logs), the channel falls back to sending a regular card at the end of the turn — the reply still arrives, just without the typewriter effect.

## See also

- [Channel Matrix](/docs/partners/channels/) — all channels at a glance
- [DingTalk](/docs/partners/dingtalk/) — the other major Chinese workplace chat, similar no-webhook model

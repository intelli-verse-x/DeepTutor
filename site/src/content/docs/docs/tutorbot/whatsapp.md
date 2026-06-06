---
title: WhatsApp
description: TutorBot on WhatsApp — requires a separate Node.js bridge running Baileys (WhatsApp Web protocol).
---

WhatsApp is the odd one out. The official WhatsApp Business API has substantial friction (verified business, monthly fees, application process). Instead, DeepTutor's WhatsApp channel connects to a **separate Node.js bridge** that speaks WhatsApp Web's protocol — fast to set up, free, and doesn't require business verification.

## What you need

- A Node.js 18+ host (can be the same machine as DeepTutor, or separate)
- A WhatsApp account on a real phone
- ~5 minutes for the QR-code pairing flow

## Step 1 — Run the bridge

DeepTutor's repo includes a sample bridge under `multi-user/whatsapp-bridge/` using [@whiskeysockets/baileys](https://github.com/WhiskeySockets/Baileys). Or run any compatible bridge that exposes a WebSocket on a known port.

A minimal bridge looks like:

```javascript
// bridge.js
const { default: makeWASocket, useMultiFileAuthState } = require('@whiskeysockets/baileys')
const WebSocket = require('ws')

const wss = new WebSocket.Server({ port: 3001 })
let waSocket = null

async function start() {
  const { state, saveCreds } = await useMultiFileAuthState('./auth')
  waSocket = makeWASocket({ auth: state, printQRInTerminal: true })
  waSocket.ev.on('creds.update', saveCreds)
  waSocket.ev.on('messages.upsert', ({ messages }) => {
    wss.clients.forEach(client => client.send(JSON.stringify(messages[0])))
  })
}

wss.on('connection', (ws) => {
  ws.on('message', (raw) => {
    const { jid, text } = JSON.parse(raw)
    waSocket?.sendMessage(jid, { text })
  })
})

start()
```

Start it:

```bash
cd multi-user/whatsapp-bridge
npm install
node bridge.js
```

A QR code appears in the terminal. Open WhatsApp on your phone → **Settings → Linked devices → Link a device** → scan. Done.

## Step 2 — Configure DeepTutor

```yaml
channels:
  whatsapp:
    enabled: true
    bridge_url: "ws://localhost:3001"   # where the bridge listens
    bridge_token: ""                    # optional, if your bridge requires auth
    allow_from:                          # phone numbers in E.164 format
      - "+85291234567"
```

## Step 3 — Start the bot

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:whatsapp → connecting (ws://localhost:3001)
[bot:my-math-tutor] channel:whatsapp → ready
```

Send a message to the **same phone number** that's logged into the bridge — the bridge relays it to DeepTutor, the bot replies through the bridge, the reply lands in WhatsApp.

## Config reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `enabled` | bool | yes | |
| `bridge_url` | url | yes | WebSocket URL of the bridge |
| `bridge_token` | string | optional | Auth token if your bridge requires it |
| `allow_from` | list[string] | optional | Phone numbers (E.164); `["*"]` = open |

## Capabilities on WhatsApp

| Feature | Supported |
|---------|-----------|
| Direct messages | ✅ |
| Group messages | ✅ *(bridge must support group routing)* |
| Markdown | ⚠️ basic — WhatsApp only renders `*bold*`, `_italic_`, `~strike~`, `` ` ` `` |
| File / image / audio | ✅ *(via bridge)* |
| LaTeX math | ❌ rendered as plain text |
| Voice notes | ✅ *(transcribed if `TRANSCRIPTION_API_KEY` is set)* |

## Keep-alive specifics

WhatsApp Web tokens expire periodically — typically when the phone is offline for ~2 weeks. When that happens:

- The bridge prints a new QR code
- You re-scan from your phone
- Sessions resume

Run the bridge as a managed process (`pm2`, systemd, supervisor) so it restarts on crash. The DeepTutor side auto-reconnects to the bridge's WebSocket if it drops.

## Why a bridge instead of the official API?

| Option | Friction | Cost | Restrictions |
|--------|----------|------|--------------|
| WhatsApp Business API (official) | Verified business + Meta approval | $0.005–0.10 per message | Template-only outbound outside 24h windows |
| WhatsApp Web bridge (this) | One QR scan | Free | Phone must stay online ~weekly |

The bridge is great for personal use and small teams. For production-grade business messaging, consider Twilio or 360dialog (official API resellers).

## Risks and policy

WhatsApp Web's terms allow automation of your own account, but they technically frown on bot-like usage. Practical risks:

- **Account ban** — rare for low-volume use; common if you spam
- **Rate limits** — WhatsApp may flag accounts sending too many messages per minute

If you're using DeepTutor's WhatsApp channel for any non-trivial deployment, use a dedicated phone number you control, not your personal one.

## Common issues

### Bridge keeps printing QR codes

The auth state isn't being persisted. Check that `./auth` directory is writable and isn't being wiped between restarts.

### "Bridge unreachable"

```bash
curl http://localhost:3001 2>&1 | head -1
# Should at least respond, even with 400 (it's a WS endpoint)
```

If `connection refused`, the bridge isn't running. If `cannot resolve host`, your `bridge_url` is wrong.

### Messages send but never arrive

Check the bridge's logs (`node bridge.js` stdout). WhatsApp Web sometimes silently drops messages when the bridge sends them too fast — add throttling in the bridge.

## See also

- [**Email**](/docs/tutorbot/email/) — another bridge-style integration (IMAP/SMTP)
- [Baileys docs](https://github.com/WhiskeySockets/Baileys) — bridge library reference

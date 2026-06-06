---
title: WhatsApp
description: 在 WhatsApp 上跑 TutorBot —— 需要单独跑一个 Node.js 桥接器（基于 Baileys，走 WhatsApp Web 协议）。
---

WhatsApp 是个特殊存在。官方的 WhatsApp Business API 摩擦不小（企业认证、月费、申请流程）。所以 DeepTutor 的 WhatsApp 渠道连的是一个 **独立的 Node.js 桥接器**，桥接器讲 WhatsApp Web 的协议 —— 上手快、免费、不用做企业认证。

## 你需要准备

- 一台跑 Node.js 18+ 的机器（可以和 DeepTutor 同一台，也可以分开）
- 一个真实手机上的 WhatsApp 账号
- ~5 分钟扫码配对

## Step 1 —— 跑桥接器

DeepTutor 仓库里在 `multi-user/whatsapp-bridge/` 下有一个示例桥接器，用的是 [@whiskeysockets/baileys](https://github.com/WhiskeySockets/Baileys)。或者你也可以跑任何兼容的桥接器，只要它在已知端口上暴露一个 WebSocket。

最小桥接器长这样：

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

启动：

```bash
cd multi-user/whatsapp-bridge
npm install
node bridge.js
```

终端会出一个二维码。在手机上打开 WhatsApp → **设置 → 已链接的设备 → 链接设备** → 扫码。搞定。

## Step 2 —— 配置 DeepTutor

```yaml
channels:
  whatsapp:
    enabled: true
    bridge_url: "ws://localhost:3001"   # 桥接器监听地址
    bridge_token: ""                    # 可选，桥接器要求鉴权时用
    allow_from:                          # 手机号，E.164 格式
      - "+85291234567"
```

## Step 3 —— 启动 bot

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:whatsapp → connecting (ws://localhost:3001)
[bot:my-math-tutor] channel:whatsapp → ready
```

发消息给 **桥接器登录的那个手机号** —— 桥接器把消息转给 DeepTutor，bot 通过桥接器回，回复落到 WhatsApp。

## 配置参考

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `enabled` | bool | 是 | |
| `bridge_url` | url | 是 | 桥接器的 WebSocket URL |
| `bridge_token` | string | 可选 | 桥接器要求鉴权时用 |
| `allow_from` | list[string] | 可选 | 手机号（E.164）；`["*"]` 全开 |

## WhatsApp 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 私聊 | ✅ |
| 群消息 | ✅ *（桥接器要支持群路由）* |
| Markdown | ⚠️ 基础 —— WhatsApp 只渲染 `*bold*`、`_italic_`、`~strike~`、`` ` ` `` |
| 文件 / 图片 / 音频 | ✅ *（通过桥接器）* |
| LaTeX 数学公式 | ❌ 当纯文本渲染 |
| 语音 | ✅ *（设了 `TRANSCRIPTION_API_KEY` 就转写）* |

## 保活机制

WhatsApp Web 的 token 会定期失效 —— 一般是手机离线 ~2 周。失效时：

- 桥接器会打印新的二维码
- 你用手机重新扫
- 会话恢复

把桥接器跑在受管的进程下（`pm2`、systemd、supervisor），crash 时自动重启。DeepTutor 这边在桥接器 WebSocket 断开时会自动重连。

## 为什么用桥接器而不是官方 API？

| 方案 | 摩擦 | 成本 | 限制 |
|------|------|------|------|
| WhatsApp Business API（官方） | 企业认证 + Meta 审批 | 每条消息 $0.005–0.10 | 24 小时窗口外只能发模板消息 |
| WhatsApp Web 桥接器（这个） | 扫一次码 | 免费 | 手机要 ~每周保持在线 |

桥接器很适合个人和小团队用。生产级的商用消息，考虑 Twilio 或 360dialog（官方 API 的代理商）。

## 风险与政策

WhatsApp Web 的条款允许自动化自己的账号，但严格说不太欢迎类 bot 的用法。实际风险：

- **封号** —— 低量使用很少；刷消息容易踩
- **限流** —— WhatsApp 会标记每分钟发消息过多的账号

如果你要把 DeepTutor 的 WhatsApp 渠道用在任何非玩具部署，请用你掌控的专属手机号，不要用个人号。

## 常见问题

### 桥接器一直打印二维码

auth state 没有被持久化。检查 `./auth` 目录可写、并且不会在重启时被清掉。

### "Bridge unreachable"

```bash
curl http://localhost:3001 2>&1 | head -1
# 至少应该有响应，哪怕是 400（这是 WS 端点）
```

如果是 `connection refused`，桥接器没跑。如果是 `cannot resolve host`，你的 `bridge_url` 写错了。

### 消息发出去但对方收不到

看桥接器日志（`node bridge.js` 的 stdout）。WhatsApp Web 有时候在桥接器发太快时会静默丢消息 —— 在桥接器里加节流。

## 另请参阅

- [**电子邮件**](/zh-cn/docs/tutorbot/email/) —— 另一种桥接式集成（IMAP/SMTP）
- [Baileys 文档](https://github.com/WhiskeySockets/Baileys) —— 桥接库参考

---
title: WeChat (Personal Weixin)
description: Configure the personal WeChat channel for a Partner using QR-code login and HTTP long polling.
---

<img src="/channel-icons/weixin.svg" alt="" width="40" height="40" />

The `weixin` channel connects a Partner to a personal WeChat account through the iLink long-poll API. It is different from **WeCom**: use this page for normal personal WeChat, and [WeCom](/docs/partners/wecom/) for Enterprise WeChat / WeChat Work.

![WeChat channel configuration](/screenshots/partners-channel-weixin.png)

## Install requirements

Personal WeChat support is included with the Partners extra. The QR-code terminal rendering also uses `qrcode`.

```bash
pip install -e ".[partners]"
# or, from an installed release when partners extras are available:
pip install "deeptutor[partners]"
```

## Configure the channel card

Open **Partners -> your partner -> Channels -> WeChat**.

| Field | What to enter |
| --- | --- |
| **Send Progress** | Keep on while testing. It sends narration updates during long turns. |
| **Send Tool Hints** | Keep on for debugging; turn off if you do not want users to see one-line tool calls. |
| **Enabled** | Turn on only when you are ready to login/start the channel. |
| **Allow From** | One value per line. Use `*` for an open test channel, or specific WeChat user ids once you know them. Empty denies access. |
| **Base Url** | Default: `https://ilinkai.weixin.qq.com`. Usually leave unchanged. |
| **Cdn Base Url** | Default: `https://novac2c.cdn.weixin.qq.com/c2c`. Used for media upload/download. |
| **Route Tag** | Optional Tencent route tag. Leave blank unless your deployment requires it. |
| **Token** | Optional bot token. Leave blank for QR-code login; the channel saves the token after a successful scan. |
| **State Dir** | Optional custom state directory. Blank means DeepTutor uses `data/partners/<id>/runtime/weixin/` for `account.json`. |
| **Poll Timeout** | Long-poll timeout in seconds. `35` is the default and works for most networks. |

## Login flow

1. Save the channel with **Enabled** on and **Token** empty.
2. Start the partner from the UI or CLI.
3. Watch the terminal that runs `deeptutor start`; it prints a QR code / scan URL for WeChat login.
4. Open the link or scan the terminal QR code with WeChat.
5. After confirmation, DeepTutor stores `account.json` in the WeChat state directory and begins long polling.
6. Send a short message from an allowed account.

```bash
deeptutor partner start <partner-id>
```

If the terminal says the session expired, restart the partner and scan the refreshed code. The implementation refreshes expired QR codes a few times, but it cannot complete login without a human scan.

## Verify it is healthy

A healthy WeChat channel has three signs:

- the terminal shows QR login success and a saved account state;
- `data/partners/<partner-id>/runtime/weixin/account.json` exists in the mounted `data/` tree;
- a short message from an allowed sender produces a Partner reply.

For Docker, make sure `data/partners/` is persisted. Otherwise every container restart can require a fresh scan.

## Access control

`Allow From` is enforced before messages enter the partner brain. During the first test, `*` is fine. For production, replace it with specific user ids after you observe inbound sender ids in logs.

## Troubleshooting

### The channel starts but asks for QR login every time

Check whether `State Dir` points to a writable location. If blank, DeepTutor writes under the partner runtime directory. If that directory is not persisted in Docker, the token disappears on restart.

### Messages arrive but replies fail

WeChat replies require a recent `context_token` from inbound messages. If the account has been idle for too long, send a fresh inbound message and let DeepTutor refresh the context before replying.

### Too many progress messages

Disable **Send Progress** or **Send Tool Hints** on the channel card. This does not change the partner's reasoning; it only changes what is delivered to WeChat.

---
title: 电子邮件
description: 通过邮件跑 TutorBot —— IMAP 轮询 + SMTP 回信，显式授权与完整正文解析。
---

Email 渠道把你的 TutorBot 变成一个异步的邮件对话方。用户给指定邮箱发信，bot 通过 IMAP 读取，通过 SMTP 回信。适合 **异步答疑** 以及更偏好邮件的用户群体。

## 你需要准备

- 一个邮箱账号（Gmail、Outlook、你自建的 SMTP/IMAP 服务器等）
- App-password 访问 *（或 OAuth，见下文）*
- 5 分钟配置

## Step 1 —— 准备邮箱凭证

**Gmail**：

1. 在账号上启用 2FA
2. 创建 [**App Password**](https://myaccount.google.com/apppasswords)（16 字符一次性密码）
3. 把它作为下面配置里的密码

**Outlook / Office 365**：要么 App Password（启用 2FA）要么 OAuth。个人用 App Password 更简单。

**自建**（Postfix、Maddy 等）：直接用账号密码。

## Step 2 —— 配置

```yaml
channels:
  email:
    enabled: true
    consent_granted: true              # 必须显式 —— 隐私保护

    # IMAP（入站）
    imap_host: "imap.gmail.com"
    imap_port: 993
    imap_username: "tutor@example.com"
    imap_password: "YOUR_APP_PASSWORD"
    imap_mailbox: "INBOX"
    imap_use_ssl: true

    # SMTP（出站）
    smtp_host: "smtp.gmail.com"
    smtp_port: 587
    smtp_username: "tutor@example.com"
    smtp_password: "YOUR_APP_PASSWORD"
    smtp_use_tls: true
    smtp_use_ssl: false
    from_address: "tutor@example.com"

    # 行为
    auto_reply_enabled: true
    poll_interval_seconds: 30          # IMAP 检查频率
    mark_seen: true                    # 处理后标记为已读
    max_body_chars: 12000
    subject_prefix: "Re: "
    allow_from:                        # 邮箱地址；[] = 全开；["x@..."] = 白名单
      - "student@example.com"
```

## Step 3 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:email → connecting (imap.gmail.com:993)
[bot:my-math-tutor] channel:email → ready, polling every 30s
```

从你允许的地址给 `tutor@example.com` 发邮件 —— 30 秒内（或下一次 poll），你会收到自动回复。

## 为什么 `consent_granted` 必须设

读邮件很敏感。渠道在没有显式 `consent_granted: true` 的情况下 **拒绝启动** —— 一个硬卡点，防止误读邮件。这是有意为之的隐私保护。

## 配置参考

| 字段 | 类型 | 必填 | 默认值 |
|------|------|------|--------|
| `enabled` | bool | 是 | `false` |
| `consent_granted` | bool | 是 | `false` —— 必须显式设为 `true` |
| `imap_host` | string | 是 | —— |
| `imap_port` | int | 是 | `993` |
| `imap_username` | string | 是 | —— |
| `imap_password` | string | 是 | —— |
| `imap_mailbox` | string | 可选 | `"INBOX"` |
| `imap_use_ssl` | bool | 可选 | `true` |
| `smtp_host` | string | 是 | —— |
| `smtp_port` | int | 是 | `587` |
| `smtp_username` | string | 是 | —— |
| `smtp_password` | string | 是 | —— |
| `smtp_use_tls` | bool | 可选 | `true` |
| `smtp_use_ssl` | bool | 可选 | `false` |
| `from_address` | string | 可选 | = `smtp_username` |
| `auto_reply_enabled` | bool | 可选 | `true` |
| `poll_interval_seconds` | int | 可选 | `30` |
| `mark_seen` | bool | 可选 | `true` |
| `max_body_chars` | int | 可选 | `12000` |
| `subject_prefix` | string | 可选 | `"Re: "` |
| `allow_from` | list[string] | 可选 | `[]`（对所有人开放） |

## 邮件上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 纯文本正文 | ✅ |
| HTML 正文 | ✅ *（转成 markdown）* |
| 入站附件 | ✅ *（PDF、图片、文本文件）* |
| 出站附件 | ✅ *（通过 SMTP 带附件回复）* |
| 邮件 thread | ✅ *（通过 `In-Reply-To` header）* |
| 主题前缀 | ✅ *（默认 `Re: `）* |
| 正文里的 LaTeX | ⚠️ 当纯文本渲染；数学密集的回复考虑转 PDF |

## 会话模型

每个独立的发件人邮箱被视为一个独立 session。同一邮件 thread 内的回复（按 `In-Reply-To` 匹配）继续同一 session。

意思就是 `student@example.com` 发的所有邮件总会落到同一个 DeepTutor session —— 非常适合持续的异步答疑。

## 保活机制

Email 渠道用一个 **后台轮询循环**：

- 每 `poll_interval_seconds` 秒，渠道通过 IMAP 登录、拉未读邮件、处理、标已读
- IMAP 掉线时，下一次 poll 自动重连
- SMTP 是每次发信开新连接（不维持长连接）

高量使用就把 `poll_interval_seconds: 15` 或更低。低于 10 秒可能撞 provider 限流。

## 常见问题

### 启动失败 —— "consent_granted is required"

你忘了设：

```yaml
consent_granted: true
```

这是有意的摩擦。请有意识地打开。

### Gmail / Outlook "Authentication failed"

你用了账号密码而不是 App Password。启用 2FA 后，IMAP/SMTP 是不接收常规密码的 —— 必须用 16 字符的 App Password。

### 和另一个自动回复器互相循环

两个自动回复器互发邮件就会陷入回环。渠道通过检查 `Auto-Submitted:` header 来检测回环 —— 但如果对方不设这个 header，回环还是可能。防御措施：

- 用 `allow_from` 限制 bot 回复的对象
- 设 `auto_reply_enabled: false`，从 CLI 手动触发回复

### IMAP 文件夹找不到

有些 provider mailbox 名字不一样（`INBOX` vs `Inbox` vs `[Gmail]/All Mail`）。在 provider 的 webmail 里查清楚，改 `imap_mailbox`。

### 回复被标垃圾邮件

填一个像样的 `from_address`；自建邮件服务器记得配 SPF/DKIM/DMARC；或者出站用受信的 SMTP relay（SendGrid、Mailgun）。

## 另请参阅

- [**WhatsApp**](/zh-cn/docs/tutorbot/whatsapp/) —— 另一个桥接式渠道
- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 架构

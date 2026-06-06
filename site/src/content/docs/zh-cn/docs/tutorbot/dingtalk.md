---
title: 钉钉
description: 在钉钉上跑 TutorBot —— 阿里的企业聊天，走 Stream Mode 连接。
---

钉钉是阿里的企业即时通信产品。DeepTutor 通过官方 `dingtalk-stream` SDK 走 **Stream Mode** —— 不需要公网 webhook。

## 你需要准备

- 一个有管理员权限的钉钉组织
- 访问 [**钉钉开放平台**](https://open.dingtalk.com/)

## Step 1 —— 创建应用

1. 登录 <https://open.dingtalk.com/>
2. **应用开发** → **创建应用**
3. 选 **企业内部机器人** 类型
4. 填名字、描述、图标
5. 创建后在凭证页复制 **AppKey（Client ID）** 和 **AppSecret（Client Secret）**

## Step 2 —— 启用 Stream Mode

1. 在应用设置 → **Stream 模式** → **启用**
2. 这样就不需要公网 webhook URL 了

## Step 3 —— 权限

申请这些权限：
- 发消息
- 读消息内容
- （可选）语音转文字

## Step 4 —— 配置

```yaml
channels:
  dingtalk:
    enabled: true
    client_id: "dingxxxxxxxxxxxxxxxx"
    client_secret: "YOUR_CLIENT_SECRET"
    allow_from: []
```

## Step 5 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:dingtalk → connecting (stream mode)
[bot:my-math-tutor] channel:dingtalk → ready
```

## 配置参考

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `enabled` | bool | 是 | |
| `client_id` | string | 是 | 钉钉的 AppKey |
| `client_secret` | string | 是 | AppSecret |
| `allow_from` | list[string] | 可选 | 钉钉 user id |

## 钉钉上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 私聊 | ✅ |
| 群聊 | ✅ |
| Markdown / 富文本 | ✅ |
| 动作卡片（可交互按钮） | ✅ |
| 文件上传 | ✅ |
| **语音 → 文字转写** | ✅ *（内置钉钉的语音识别）* |
| @ 寻址 | ✅ |

## 保活机制

dingtalk-stream SDK 负责 long-poll 回调连接。断线时自动重连。

## 常见问题

### "Invalid client_secret"

去钉钉开放平台 → 你的应用 → 凭证 核对。Secret 可以被轮换。

### Bot 在线但不回复

确认 bot 已经为目标用户 / 部门安装。在钉钉里，机器人必须先被显式加到组织里才能聊天。

### Stream 模式连不上

Stream 模式要求 bot 已发布（不是 draft 状态）。在钉钉应用页点 **发布**。

## 另请参阅

- [**飞书**](/zh-cn/docs/tutorbot/feishu/) —— 国内另一个主流企业聊天
- [**企业微信**](/zh-cn/docs/tutorbot/wecom/) —— 腾讯的企业即时通信

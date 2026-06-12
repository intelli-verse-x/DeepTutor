---
title: WeCom（企业微信）
description: 为 Partner 配置企业微信 / WeChat Work AI Bot 渠道。
---

<img src="/channel-icons/wecom.svg" alt="" width="40" height="40" />

`wecom` 用于企业微信 / WeChat Work。它通过企业微信 AI Bot WebSocket 长连接接入，和个人 [WeChat (`weixin`)](/zh-cn/docs/partners/weixin/) 不同。

![WeCom 渠道配置](/screenshots/partners-channel-wecom.png)

## 前置条件

- 有企业微信组织管理员权限。
- 安装 `wecom-aibot-sdk`。可以通过 Partners extra 安装，必要时也可单独安装。

```bash
pip install -e ".[partners]"
python -c "import wecom_aibot_sdk; print('ok')"
```

## 在企业微信创建 AI Bot

1. 登录 <https://work.weixin.qq.com/>。
2. 打开 **应用管理 / 小程序 -> AI Bot 平台**。
3. 创建 **AI Bot** 应用。
4. 配置名称、描述、可见部门/用户和审批设置。
5. 复制 **Bot ID** 和 **Secret**。

## 配置 DeepTutor

打开 **Partners -> 你的 partner -> Channels -> WeCom**，填写：

| 字段 | 说明 |
| --- | --- |
| `enabled` | partner 启动时是否启动该渠道。 |
| `bot_id` | 企业微信 AI Bot 平台里的 Bot ID。 |
| `secret` | 企业微信 Secret，按凭证处理。 |
| `allow_from` | 允许访问的用户 id。空列表拒绝访问；基础 channel policy 支持时，`*` 表示开放。 |
| `welcome_message` | 用户打开会话时发送的可选欢迎语。 |
| `send_progress` / `send_tool_hints` | 是否投递过程 narration 和一行工具调用提示。 |

## 访问控制和可见范围

WeCom 有两层访问控制：

1. 企业微信应用可见范围决定组织内谁能打开这个 AI Bot。
2. DeepTutor 的 `allow_from` 决定哪些 sender ids 可以进入 Partner runtime。

首次配置时，建议把企业微信可见范围设小；从日志确认 sender ids 后，再显式填写 `allow_from`。

## 启动和测试

```bash
deeptutor partner start <partner-id>
```

服务端日志应显示 WeCom WebSocket connected/authenticated。然后在企业微信里打开 AI Bot，发送一条短消息测试。

## 常见问题

- **`ImportError: wecom_aibot_sdk`** —— 在运行 DeepTutor 的同一个环境里安装 `wecom-aibot-sdk` 或 Partners extra。
- **连接成功但不回复** —— 检查 `allow_from`、部门可见范围，以及发送者是否有权限使用该 AI Bot。
- **断线** —— 短暂断线会自动重连；持续离线时检查 Bot ID / Secret 和服务器到企业微信的出站网络。

---
title: 飞书 / Lark
description: 在飞书（国内）/ Lark（海外）上跑 TutorBot —— 走 lark-oapi SDK 的 WebSocket 长连。
---

飞书是国内最流行的办公聊天工具；Lark 是它的海外对应版本。两者 API 一致。DeepTutor 通过官方 `lark-oapi` SDK，用一条长连 WebSocket 同时支持。

## 你需要准备

- 飞书 / Lark 开发者账号
- 访问 [**飞书开放平台**](https://open.feishu.cn/)（国内）或 [**Lark Open Platform**](https://open.larksuite.com/)（海外）
- 可选：一个你能装 bot 的飞书 / Lark 组织

## Step 1 —— 创建应用

1. 打开对应平台 → **创建应用** → **自建应用**
2. 填基本信息（名称、描述、图标）
3. 创建后在 **凭证与基础信息** 页复制：
   - **App ID**
   - **App Secret**
   - **Verification Token**
   - **Encrypt Key**

## Step 2 —— 开启机器人能力

1. 左侧栏 → **应用能力** → **机器人** → **启用**
2. 配置机器人的显示名和头像

## Step 3 —— 配置事件订阅

1. 左侧栏 → **事件订阅** → **订阅事件**
2. 添加你关心的事件：
   - `im.message.receive_v1` —— 接收消息
   - `im.message.message_read_v1` —— 已读回执（可选）
3. **启用长连接模式**，这样就不用公网 webhook URL 了。打开后 bot 走 WebSocket 而不是 webhook。

## Step 4 —— 加权限

左侧栏 → **权限管理**：

- `im:message:send_as_bot` —— 发消息
- `im:resource` —— 读多媒体附件
- `contact:user.id:readonly` —— 解析 user id

然后 **发布** 版本 *（自建应用走内部发布）*。

## Step 5 —— 配置 DeepTutor

```yaml
channels:
  feishu:
    enabled: true
    app_id: "cli_xxxxxxxxxxxxxxxx"
    app_secret: "YOUR_APP_SECRET"
    verification_token: "YOUR_VERIFICATION_TOKEN"
    encrypt_key: "YOUR_ENCRYPT_KEY"
    allow_from: []
    group_policy: "mention"
```

## Step 6 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:feishu → connecting (long-connection)
[bot:my-math-tutor] channel:feishu → ready (app_id=cli_xxx)
```

## 配置参考

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `enabled` | bool | 是 | |
| `app_id` | string | 是 | `cli_...` |
| `app_secret` | string | 是 | |
| `verification_token` | string | 是 | 用于事件签名校验 |
| `encrypt_key` | string | 是 | 用于解密入站事件 |
| `allow_from` | list[string] | 可选 | User id 列表；`["*"]` 全开 |
| `group_policy` | `"mention" \| "open"` | 可选 | 默认 `"mention"` |

## 飞书上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 私聊 | ✅ |
| 群聊 | ✅ |
| **交互卡片** | ✅ *（带按钮的飞书富卡片消息）* |
| Markdown | ✅ |
| 文件 / 图片上传 / 下载 | ✅ |
| 语音转写 | ✅ *（设了 `transcription_api_key`）* |
| 表情反应 | ⚠️ 只支持发出方向 |
| @ 寻址 | ✅ |

## 长连模式 vs webhook 模式

飞书支持两种投递方式：

| 模式 | 优点 | 缺点 |
|------|------|------|
| **长连接** *（推荐）* | 不需要公网 IP；哪都能用 | 一个 app 对一个 DeepTutor 实例 |
| Webhook | 多个端点；标准请求/响应 | 需要 HTTPS 公网 URL |

DeepTutor 默认走长连。要切到 webhook（有负载均衡需求时），需要自己跑一个 webhook 接收器 —— 目前 DeepTutor 内置不支持。

## 保活机制

lark-oapi SDK 负责 WebSocket 自动重连。后台线程跑 WebSocket 监听器，把事件转给 DeepTutor 的 async 总线。

如果 bot 在飞书里掉线了（状态显示 offline）：

```bash
deeptutor bot stop my-math-tutor
deeptutor bot start my-math-tutor
```

要长期稳定，配 systemd 或 Docker `restart: unless-stopped`。

## 常见问题

### 启动报 "Invalid app_secret"

去飞书凭证页核对 **App Secret** —— 它可以被轮换。也确认你在正确的平台（国内是 `open.feishu.cn`，海外是 `open.larksuite.com` —— 两边的 secret 不通用）。

### Bot 说自己在线但收不到消息

两件事检查：

1. **权限** —— `im:message:send_as_bot` 和事件订阅都加了，并且 **发布** 了新版本
2. 事件订阅里 **长连接模式** 开了

### Verification token 不匹配

如果你在飞书里重新生成了 verification token，更新配置并重启 bot。这个 token 被签到每个入站事件里做完整性校验。

### Encrypt key 不匹配

同上 —— 你在飞书（设置 → 事件订阅）重新生成 encrypt key 后，要更新配置并重启。

## 另请参阅

- [**企业微信**](/zh-cn/docs/tutorbot/wecom/) —— 腾讯的企业聊天平台，注册 UX 类似
- [**钉钉**](/zh-cn/docs/tutorbot/dingtalk/) —— 阿里在企业聊天领域的对位产品

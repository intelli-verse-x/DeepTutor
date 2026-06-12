---
title: WeChat（个人微信）
description: 使用扫码登录和 HTTP long-poll 为 Partner 配置个人微信渠道。
---

<img src="/channel-icons/weixin.svg" alt="" width="40" height="40" />

`weixin` channel 用 iLink long-poll API 把 Partner 接到个人微信账号。它和 **WeCom 企业微信** 不一样：普通个人微信看本页，企业微信 / WeChat Work 看 [WeCom](/zh-cn/docs/partners/wecom/)。

![WeChat 渠道配置](/screenshots/partners-channel-weixin.png)

## 安装依赖

个人微信支持在 Partners extra 里；终端二维码渲染还会用到 `qrcode`。

```bash
pip install -e ".[partners]"
# 或发布包支持 extras 时：
pip install "deeptutor[partners]"
```

## 配置 channel card

打开 **Partners -> 你的 partner -> Channels -> WeChat**。

| 字段 | 怎么填 |
| --- | --- |
| **Send Progress** | 测试时建议开启。长任务会把过程 narration 发到微信。 |
| **Send Tool Hints** | 调试时建议开启；如果不想让用户看到一行工具调用，生产环境可关闭。 |
| **Enabled** | 准备登录/启动时再打开。 |
| **Allow From** | 一行一个值。测试可填 `*` 表示开放；上线后换成具体微信用户 id。空列表通常表示拒绝所有人。 |
| **Base Url** | 默认 `https://ilinkai.weixin.qq.com`，一般不用改。 |
| **Cdn Base Url** | 默认 `https://novac2c.cdn.weixin.qq.com/c2c`，用于媒体上传/下载。 |
| **Route Tag** | 可选腾讯路由标签。没有特殊部署要求就留空。 |
| **Token** | 可选 bot token。扫码登录时留空；扫码成功后 channel 会保存 token。 |
| **State Dir** | 可选状态目录。留空时使用 `data/partners/<id>/runtime/weixin/` 存 `account.json`。 |
| **Poll Timeout** | long-poll 超时时间，单位秒。默认 `35`，多数网络可用。 |

## 登录流程

1. 保存 channel，**Enabled** 打开，**Token** 留空。
2. 从 UI 或 CLI 启动 partner。
3. 查看运行 `deeptutor start` 的终端；那里会打印微信登录二维码 / 扫码链接。
4. 用微信扫码，或在浏览器打开终端给出的链接后扫码确认。
5. 成功后，DeepTutor 会在 WeChat state directory 写入 `account.json`，然后开始 long polling。
6. 用允许的账号发一条短消息测试。

```bash
deeptutor partner start <partner-id>
```

如果终端提示二维码过期，重启 partner 或等待刷新后重新扫码。实现会自动刷新几次二维码，但登录必须人工扫码完成。

## 如何确认健康

健康的 WeChat channel 通常有三个迹象：

- 终端显示扫码登录成功，并保存了账号状态；
- 挂载的 `data/` 目录里存在 `data/partners/<partner-id>/runtime/weixin/account.json`；
- 允许的发送者发一条短消息后，Partner 能正常回复。

Docker 部署必须持久化 `data/partners/`，否则每次容器重启都可能需要重新扫码。

## 访问控制

消息进入 partner brain 之前会先检查 `Allow From`。第一次测试填 `*` 可以；生产环境建议从日志里确认 sender id 后换成明确 allowlist。

## 常见问题

### 每次启动都要求重新扫码

检查 `State Dir` 是否可写、是否持久化。留空时 DeepTutor 写到 partner runtime 目录；如果 Docker 没挂载该目录，重启后 token 会丢失。

### 收得到消息但回不了

微信回复依赖最近入站消息带来的 `context_token`。如果账号空闲太久，先从微信发一条新消息，让 DeepTutor 刷新 context 后再回复。

### 过程消息太多

在 channel card 里关闭 **Send Progress** 或 **Send Tool Hints**。这不会改变 partner 推理，只改变微信里看到的投递内容。

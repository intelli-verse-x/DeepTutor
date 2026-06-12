---
title: Partners 伙伴
description: 运行在同一 Chat agent loop 上的、可接入 IM 渠道的持久学习伙伴。
---

Partners 是拥有独立身份、Soul、模型策略、资源库和渠道配置的持久学习伙伴。它替代了旧 TutorBot 引擎：每条来自网页或 IM 的消息都会进入与主 Chat 相同的 `ChatOrchestrator -> AgenticChatPipeline`。

![Partners 工作台](/screenshots/partners.png)

## 心智模型

一个 Partner 是 `data/partners/<id>/workspace/` 下的 **synthetic user workspace**。里面有 partner 的 soul、复制过来的知识库、技能、Notebook、Memory 和渠道运行状态。因为这个布局和 Chat 工作区一致，RAG、`read_skill`、Notebook、Memory、MCP deferred tools 都可以直接复用，不需要另一套 bot 引擎。

![Partners 架构](/screenshots/partners-architecture.png)

## 创建 Partner

打开 **Partners -> New partner**，按向导完成：

![Partner 创建向导：Identity 步骤](/screenshots/partners-new.png)

1. **Identity** —— 名称、头像、描述、默认回复语言。
2. **Soul** —— partner 的角色和表达方式，会写入 `SOUL.md`。
3. **Mind** —— 模型选择、系统工具、MCP 工具和投递偏好。
4. **Library** —— 分配知识库、技能和 Notebook。它们会被复制进 partner 工作区，避免原始资源变化影响运行时上下文。
5. **Review** —— 启动前确认工作区与渠道配置。

![Partner 详情](/screenshots/partners-detail.png)

向导里选的内容之后都可以改：partner 详情页除了网页 **Chat** 视图，还有覆盖 identity、soul、mind、library 的 **Configure** tab，以及配置投递的 **Channels** tab。

![Partner 详情：Configure tab](/screenshots/partners-configure.png)

## 渠道通用字段

每个 channel card 都是同一个 partner brain 的投递适配器。大多数字段含义一致：

| 字段 | 含义 |
| --- | --- |
| **Enabled** | 是否启动这个渠道。配置凭证前可以先关闭。 |
| **Send Progress** | 是否把长任务过程中的 narration/progress 发到 IM。长回答等待较久时建议开启。 |
| **Send Tool Hints** | 是否发送一行工具调用提示，例如 `rag(query=...)`。生产群里想安静一点可以关掉。 |
| **Allow From** | 允许访问的用户 id、群 id、邮箱或 `*`。空列表通常表示拒绝所有人；`*` 表示开放。 |

每个 channel 都有专属配置页，包含凭证、接入步骤和排错说明——完整清单见 [**Channel Matrix**](/zh-cn/docs/partners/channels/)。个人微信看 [**WeChat**](/zh-cn/docs/partners/weixin/)，企业微信看 [**WeCom**](/zh-cn/docs/partners/wecom/)，QQ 官方 bot 和 NapCat 看 [**QQ / NapCat**](/zh-cn/docs/partners/qq/)。

## CLI 对应命令

```bash
deeptutor partner list
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor partner start math-tutor
deeptutor partner stop math-tutor
```

CLI 适合做 smoke test；实际配置渠道时更推荐 Web UI，因为它会遮盖 secret，并按 channel schema 渲染字段。

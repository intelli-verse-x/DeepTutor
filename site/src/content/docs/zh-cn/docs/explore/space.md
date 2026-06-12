---
title: Space 空间
description: 管理可复用上下文：skills、personas、notebooks、chat history 和题目资产。
---

Space 是可复用上下文的资源库层。你在这里管理会影响未来 Chat、Partner、Co-Writer 和 Book 的资产。

![Space 工作台](/screenshots/space.png)

## Space 里有什么

| 资产 | 用途 |
| --- | --- |
| **Skills** | `SKILL.md` 文件，用来教 DeepTutor 一个 workflow、风格或领域行为。 |
| **Personas** | 可在 Chat 选择、也可复制到 Partners 的角色/语气说明。 |
| **Notebooks** | 从 Chat、Research、Co-Writer 保存，或从 Markdown 导入的长期记录。 |
| **Chat History** | 可恢复 session 和历史上下文。 |
| **Question assets** | 之后可以引用的练习材料。 |

## Skills

Skills 位于用户 workspace 下，可以加标签、编辑、预览；内置 skill 可以只读。一个好的 skill 应该具体说明何时使用、需要什么输入、输出应该长什么样。

不是每个 skill 都得自己写：DeepTutor 的 skill 格式与更大的 Agent-Skills 生态互通，`deeptutor skill install clawhub:<slug>` 一条命令就能从 [ClawHub](https://clawhub.ai/) 导入社区 skill，且全程过安全门 —— hub 安全裁定、防御式解压、二进制进不来、不能自我注入 system prompt。完整流程见 [CLI 命令](/zh-cn/docs/cli/commands/)。

## Personas 和 Partners

Personas 是较轻量的角色定义。Partners 有更强的 `SOUL.md`，但 persona 是很好的起点：先在 Space 里创建/打磨 persona，再在创建 Partner 时使用。

## Notebooks

Notebook 是把一次回答变成长期上下文的最简单方式。可以保存 summary、research output、writing draft 或 book reading note，之后在 Chat 或 CLI 里重新挂载。

## 相关页面

- [聊天工作台](/zh-cn/docs/explore/chat-workspace/) —— 把 Space context 挂到 turn 上
- [Partners](/zh-cn/docs/explore/partners/) —— 给 partner 分配 skills/notebooks
- [Co-Writer](/zh-cn/docs/explore/co-writer/) —— 把 draft 保存到 Notebook

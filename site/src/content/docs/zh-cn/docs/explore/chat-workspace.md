---
title: 聊天工作台
description: DeepTutor 默认 agent loop：工具、RAG、附件、Memory、Notebook 和深层 capability 都在同一线程中运行。
---

Chat 是大多数工作开始的地方。它不是普通聊天框，而是默认 agent loop：可以调用工具、读取 source、搜索知识库、写 Notebook、向用户追问，并在同一个 session 里切换到更深的 capability。

![Chat 工作台](/screenshots/chat.png)

## 页面区域

| 区域 | 作用 |
| --- | --- |
| **左侧栏** | 主界面：Chat、Partners、Co-Writer、Book、Knowledge、Space、Memory、Settings。Recents 可恢复历史 session。 |
| **Composer** | 输入框、capability 选择、文件/上下文附件、persona、模型选择和发送按钮。 |
| **Activity panel** | 工具调用、中间进度、source 预览和生成 artifact。 |
| **Notebook / Markdown 操作** | 把重要 turn 保存到 Notebook，或导出整个 session 为 Markdown。 |

## Agent loop

![Chat agent loop](/screenshots/chat-agent-loop.png)

一次 turn 可能有多轮：

1. 模型先生成回答或工具计划。
2. 如果需要工具，DeepTutor 执行工具并把 observation 写回上下文。
3. 模型基于证据继续。
4. 最后一轮不再调用工具时，输出最终答案。

`ask_user` 是特殊工具：它会暂停 turn，提出结构化澄清问题，等你回答后继续。

## Chat 里可启动的能力

| Capability | 适合做什么 |
| --- | --- |
| `chat` | 普通答疑、开放对话、轻量工具调用。 |
| `deep_solve` | 分步解题、复杂推理、验证。 |
| `deep_question` | 生成练习题、quiz、mimic-source。 |
| `deep_research` | 拆分子问题，结合 RAG/web/arXiv 生成带引用报告。 |
| `visualize` | SVG、Chart.js、Mermaid、HTML，以及路由到动画输出。 |
| `math_animator` | 以 Manim 为核心的数学动画工作流。 |
| `auto` | 让 DeepTutor 自动选择 capability。 |
| `mastery_path` | 学习路径与掌握度规划。 |

## 工具

Settings 里用户可切换的工具是 `brainstorm`、`web_search`、`paper_search`、`reason`。按上下文自动挂载的工具包括：`rag`、`read_source`、`read_memory`、`write_memory`、`read_skill`、`load_tools`、`exec`、`web_fetch`、`ask_user`、`list_notebook`、`write_note`、`github`。

## 实用例子

```text
挂载一个 KB 后问："Explain chapter 4 and quiz me on the weak spots."
```

```text
上传 PDF 后问："Extract the assumptions and save the final summary to my notebook."
```

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb signals
deeptutor chat --capability deep_research --kb papers
```

## 相关页面

- [Partners](/zh-cn/docs/explore/partners/) —— 同一个 loop 接入 IM 伙伴
- [Knowledge](/zh-cn/docs/explore/knowledge/) —— 为 Chat 提供 RAG grounding
- [Memory](/zh-cn/docs/explore/memory/) —— 可审计的个性化记忆
- [CLI](/zh-cn/docs/cli/) —— 从终端运行同样的 turn

---
title: Book Engine
description: 多 agent 流水线把你的材料编译成可交互的「活书」，13 种 block 类型。
---

给 DeepTutor 一个主题，让它指向你的知识库，**Book Engine** 就会产出一本结构化、可交互的书 —— 不是一份静态导出，而是一本可读、可自测、可在上下文里讨论的活书。

## 工作原理

幕后是一条多 agent 流水线在干重活：

1. **Outline proposal** —— 给定主题 + KB，提出章节结构
2. **Source retrieval** —— 从 KB 中拉相关段落
3. **Chapter tree synthesis** —— 装配层级化的章节提纲
4. **Page planning** —— 给每页规划放哪些 block
5. **Block compilation** —— 逐个生成 block（正文、quiz、代码、figure、……）

你始终掌控全局：review 提案、重排章节、在任意页面旁边开聊天。

## 13 种 block 类型

页面由 13 种 block 装配而成，每种用自己的交互组件渲染：

| Block | 说明 |
|-------|------|
| **Text** | 标准散文段落 |
| **Callout** | Tip / Warning / Note / Important —— 带色边的提示框 |
| **Quiz** | 内嵌交互题；答案与期望答复校验 |
| **Flash cards** | 正反翻转卡，用于间隔重复 |
| **Code** | 语法高亮的代码片段，可选可执行运行时 |
| **Figure** | 带 caption 和 alt text 的图片 |
| **Deep dive** | 可折叠区块，用于进阶 / 可选材料 |
| **Animation** | Manim 渲染的视频 |
| **Interactive demo** | 内嵌的交互式 HTML（包括用于数学的 **GeoGebra viewer**） |
| **Timeline** | 纵向事件时间线 |
| **Concept graph** | 展示概念间关系的迷你知识图谱 |
| **Section** | 用于嵌套 block 的分组容器 |
| **User note** | 给读者自己记笔记用的可编辑富文本 |

## KB 指纹与漂移检测

Book 的每一页都会 **对其源 KB 做指纹**。当源文档变了：

- `deeptutor book health <book_id>` 会报告漂移（哪些页面已经过期）
- `deeptutor book refresh-fingerprints <book_id>` 在你确认过变更之后清掉 stale-page 标记

所以即便 KB 在持续演化，用 Book Engine 也是安全的 —— 你会知道哪一页已经和源不同步。

## 在 Web UI 里使用

1. 左侧栏点 **Book**
2. **+ New book** → 选主题、挂 KB
3. Review 并编辑生成的提纲
4. 确认 —— 流水线开始逐页编译
5. 打开页面，可阅读、可自测、可旁边聊天

## 在 CLI 里

```bash
deeptutor book list                                   # 工作区里所有的 book
deeptutor book health <book_id>                       # KB 漂移报告
deeptutor book refresh-fingerprints <book_id>         # 把 stale 页面标记为已确认
```

health 的 JSON 输出：

```json
{
  "kb_drift": {
    "kb_name": "physics",
    "stale_pages": ["page_abc", "page_def"],
    "drift_ratio": 0.12
  },
  "log_health": {
    "last_compile": "2026-05-20T14:23:01Z",
    "errors": []
  }
}
```

## 与之搭配的

- **Knowledge** —— 一本书的质量取决于其 KB 的质量。从这里开始。
- **Page 旁边的聊天** —— 每一页都有一个绑定到它的聊天 composer；可以基于页面内容追问。
- **Notebooks** —— 把阅读 book 时的聊天要点存到 notebook，方便日后回顾。

## 另见

- [**知识库**](/zh-cn/docs/explore/knowledge/) —— 搭好支撑一本书的 KB
- [**Space → Notebooks**](/zh-cn/docs/explore/space/) —— 把 book 的讨论存下来
- [**CLI → book commands**](/zh-cn/docs/cli/commands/)

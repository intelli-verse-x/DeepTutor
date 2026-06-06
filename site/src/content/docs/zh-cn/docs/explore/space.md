---
title: Space 空间
description: 你的个人学习资料库 —— Chat History、Notebooks、Question Bank、Skills，全在一个地方。
---

Space 是与活跃界面相对的 **阅读 / 回顾** 端。Chat / Co-Writer / Book 是你 *产出* 的地方，Space 则是你产出的所有东西的归宿 —— 可搜索、可回放。

## Space 里有什么

Space 在一套导航下集成了四个子界面：

| 子界面 | 内容 |
|--------|------|
| **Chat History** | 所有模式下的每段对话（Chat / Solve / Quiz / Research / Visualize） |
| **Notebooks** | 分类、配色的 notebook，承载来自 Chat、Research、Co-Writer 的记录 |
| **Question Bank** | 自动生成过的全部 quiz 题 —— 可收藏，可在聊天里 @ 引用 |
| **Skills** | 用户自己编写的 `SKILL.md` 文件，定义教学人设 |

## Chat History

每一段对话，支持：

- **标题重命名** —— 把自动生成的标题改成你能搜到的样子
- **删除** —— 删掉一个 session（连同它的 memory trace）
- **继续** —— 在新 tab 打开 session，或附加到当前 tab
- **逐回合删除** —— 每个入口都支持（chat、solve、quiz、research、visualize）

顶部浏览器搜索框会跨所有标题和正文做过滤 —— 想不起来某事是在哪个 session 里聊的时候很有用。

## Notebooks

Notebook 是 **你想留存的产出的持久化存储**。一个 notebook 包含：

- 一个名字 + 描述 + 颜色标签
- 一组记录（每条记录是一份 Markdown 文档）
- 反向链接到来源的聊天 session / Co-Writer 文档

### 存到 notebook

大部分界面都有 **Save to Notebook** 动作：

| 界面 | 存下的内容 |
|------|------------|
| **Chat** *（任意模式）* | 当前回合 + 其引用 |
| **Co-Writer** | 当前文档 |
| **Quiz** | 题目 + 你的答案 + 评分结果 |
| **Research** | 完整报告 + 提纲 + 引用 |

### 在聊天里用 notebook

Notebook 可以通过 `list_notebook` 和 `write_note` 工具在聊天里查询（至少存在 1 个 notebook 时会自动挂上）。也可以通过 composer 的 Space 选择器把具体记录挂到某个回合。

### CLI 镜像

```bash
deeptutor notebook list
deeptutor notebook create research-notes --description "Daily reading log"
deeptutor notebook show research-notes
deeptutor notebook add-md research-notes ./paper-summary.md
deeptutor notebook replace-md research-notes <record_id> ./updated.md
deeptutor notebook remove-record research-notes <record_id>
```

## Question Bank

**Quiz** 模式生成的每道自动校验题都会落到这里：

- **收藏** —— 标记一道题以便日后复习
- **分类** —— 题目会按来源继承一个主题标签
- **在聊天里 @ 引用** —— 在新回合里引用过去的题（「@question 47，为什么 B 是对的？」）

Question Bank 让间隔重复成为一个真实可用的工作流：把昨天做错的题重新生成、获取讲解、再做一次。

## Skills

Skills 是 **用户编写的人设定义** —— 按特定 schema 写的 `SKILL.md` 文件。当一个 skill 激活时：

- 它的人设会在生效期间 **注入聊天 system prompt**
- 它的 trigger 可以让它自动激活（比如你提到特定主题时）

### Skill schema

```markdown
---
name: socratic-tutor
description: Teach by asking probing questions instead of giving direct answers
triggers:
  - "explain"
  - "what is"
  - "teach me"
---

You are a Socratic tutor. Instead of giving direct answers:

1. Ask probing questions that reveal what the student already knows.
2. Guide them to discover the answer themselves.
3. Confirm understanding with a follow-up question.

Use clear, encouraging language. Never lecture.
```

DeepTutor 自带几个原型 —— Socratic、鼓励型、严格型 —— 你也可以在 Skills 这个 tab 里写自己的。

### Skill 存在哪里

- **个人 skills** —— `data/user/workspace/skills/*.md`
- **项目作用域 skills** —— `.deeptutor/skills/*.md` *（如果你在用项目工作区）*

## 与之搭配的

- **Chat** —— 把 notebook 记录 / 过去的 session 拉进当前回合做上下文
- **TutorBot** —— Bot 同样能使用 Skills（按 bot 单独配置）
- **Memory** —— Notebook 会成为 `notebook` surface 下的 L1 trace，最终被合并进 L3

## 另见

- [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) —— 产出 Space 所存的内容
- [**记忆系统**](/zh-cn/docs/explore/memory/) —— Space 的内容如何喂给记忆流水线
- [**探索 TutorBot**](/zh-cn/docs/tutorbot/) —— bot 同样使用 Skills

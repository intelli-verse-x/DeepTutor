---
title: 从 PyPI 安装
description: 选项 1 —— 最顺滑的安装方式。pip install deeptutor，然后 init、start。
---

PyPI 安装是最顺滑的路径：**完整本地 Web 应用 + CLI，无需 clone**。需要 **Python 3.11+** 以及 PATH 上的 **Node.js 20+** —— `deeptutor start` 会拉起内置的 Next.js standalone 服务器。

## 安装

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # 提示输入端口 + LLM 提供商 + 可选 embedding
deeptutor start    # 同时启动后端 + 前端；保持终端开着
```

`deeptutor init` 会询问：

- **后端端口**（默认 `8001`）
- **前端端口**（默认 `3782`）
- **LLM 提供商** / base URL / API key / 模型
- **可选 embedding 提供商**（用于 RAG / 知识库）

`deeptutor start` 之后，打开终端里打印的前端地址 —— 默认是 <http://127.0.0.1:3782>。按 `Ctrl+C` 同时停掉后端和前端。

> 跳过 `deeptutor init` 也行，应用会以默认端口和空配置启动，进 **设置 → LLM** 再配也可以。

## 试用 v1.4.0 beta

PyPI 把 `1.4.0-beta` 规范化为 `1.4.0b0`，所以普通 `pip install -U deeptutor` 不会跳到 beta：

```bash
pip install --pre -U deeptutor
# 或精确锁定：
pip install -U deeptutor==1.4.0b0
```

## 文件存在哪里

工作区位于运行命令时所在的目录（首次启动会在那里创建 `data/` 目录）。覆盖位置：

```bash
DEEPTUTOR_HOME=/opt/deeptutor deeptutor start
# 或：
deeptutor start --home /opt/deeptutor
```

首次 init 后的目录结构：

```text
my-deeptutor/
└── data/
    └── user/
        ├── settings/
        │   ├── system.json
        │   ├── auth.json
        │   ├── integrations.json
        │   ├── interface.json
        │   ├── model_catalog.json
        │   ├── main.yaml
        │   └── agents.yaml
        ├── memory/
        └── workspace/
```

各配置文件的含义在下面 [**配置参考**](#datausersettings-配置文件) 一节。

## 安装之后能直接用什么

不用离开工作区，随时进 CLI：

```bash
deeptutor chat                                          # 交互式 REPL
deeptutor run chat "解释一下傅里叶变换"                   # 单次执行
deeptutor kb create my-kb --doc textbook.pdf            # 建一个知识库
deeptutor memory show                                   # 查看记忆
deeptutor config show                                   # 查看当前配置
```

完整命令面：[**DeepTutor CLI**](/zh-cn/docs/cli/)。

## 升级

```bash
pip install --upgrade deeptutor
deeptutor start
```

工作区会在升级中保留。

## `data/user/settings/` 配置文件

`data/user/settings/` 下的所有文件都是纯 JSON / YAML。浏览器里的 **设置** 页是推荐的编辑入口。

| 文件 | 用途 |
|------|------|
| `model_catalog.json` | LLM / embedding / 搜索 provider 配置；API key；当前激活模型 |
| `system.json` | 后端 / 前端端口、对外 API base、CORS、SSL 校验、附件目录 |
| `auth.json` | 可选的认证开关、用户名、密码哈希、token / cookie 设置 |
| `integrations.json` | 可选的 PocketBase 与 sidecar 集成设置 |
| `interface.json` | UI 语言 / 主题 / 侧边栏偏好 |
| `main.yaml` | 运行时默认行为与路径注入 |
| `agents.yaml` | 各 capability / 工具的温度和 token 设置 |

> 项目根目录的 `.env` **不会** 被当作应用配置加载。建议从浏览器里 **设置 → LLM** 配置，或直接编辑 `model_catalog.json`。

## 常见错误

### macOS 上 `python: command not found`

```bash
python3 -m pip install -U deeptutor
python3 -m deeptutor init   # 或者，如果 entry point 在 PATH 上，直接 `deeptutor init`
```

### Node.js 不在 PATH 上

`deeptutor start` 会拉起内置 Next.js 服务器，需要 PATH 上有 `node`。从 <https://nodejs.org> 装 Node 20+，或 `brew install node@22`。

### 端口 `3782` 或 `8001` 被占用

```bash
lsof -i :3782          # macOS
ss -ltnp | grep :3782  # Linux
```

杀掉占用进程，或重跑 `deeptutor init` 改端口。

### LLM provider 401 Unauthorized

API key 被 provider 拒绝。在 **设置 → LLM** 重新输入，或：

```bash
deeptutor init   # 重跑向导，工作区会保留
```

更多问题：[**故障排查**](/zh-cn/docs/get-started/troubleshooting/)。

## 下一步

- [**探索 DeepTutor**](/zh-cn/docs/explore/) —— 看看跑起来的应用
- [**多用户部署**](/zh-cn/docs/get-started/multi-user/) —— 部署成团队服务器

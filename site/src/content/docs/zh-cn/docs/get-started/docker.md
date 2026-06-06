---
title: Docker
description: 选项 3 —— 一个容器跑完整 Web 应用，镜像来自 GHCR。
---

一个容器跑完整 Web 应用。镜像在 GitHub Container Registry 上：

- `ghcr.io/hkuds/deeptutor:latest` —— 稳定版
- `ghcr.io/hkuds/deeptutor:pre` —— 预发布版（如有）

## 运行

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **`3782` 和 `8001` 都要映射。** 端口 `3782` 提供 Web UI；端口 `8001` 是 FastAPI 后端，浏览器会直接调它 —— 容器里没有 in-container proxy。漏掉 `8001` 的映射，页面依然能加载，但 **设置** 会显示 "Backend unreachable" 然后没法用。

打开 <http://127.0.0.1:3782>。容器首次启动时会创建 `/app/data/user/settings/*.json`；从 Web 的设置页面里配置模型 provider。配置、API key、日志、工作区文件、记忆、知识库全部持久化在 `deeptutor-data` volume 里。

## 后台模式

加 `-d` 让它在后台跑：

```bash
docker run -d --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest

docker logs -f deeptutor      # 跟踪日志
docker stop deeptutor         # 停止
docker rm deeptutor           # 删除（volume 仍保留）
```

`deeptutor-data` volume 会在 `stop` / `rm` 之间保留设置和工作区。如果真要从头来：`docker volume rm deeptutor-data`。

## 改宿主机端口

改 `-p host:container` 映射的左边即可：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:8088:3782 \
  -p 127.0.0.1:8089:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

如果你在 `/app/data/user/settings/system.json` 里改了容器侧端口，重启并把每条映射右侧同步改掉。

## 连本地 LLM（Ollama / LM Studio / llama.cpp / vLLM）

Docker 里的 `localhost` 指的是容器本身，不是宿主机。要访问宿主机上跑的模型服务，用 host gateway：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

然后在 **设置 → LLM**（或 **Embedding**）里，把 provider Base URL 指到 `host.docker.internal`：

| 服务 | Base URL |
|------|----------|
| Ollama LLM | `http://host.docker.internal:11434/v1` |
| Ollama embedding | `http://host.docker.internal:11434/api/embed` |
| LM Studio | `http://host.docker.internal:1234/v1` |
| llama.cpp | `http://host.docker.internal:8080/v1` |

Docker Desktop（macOS / Windows）通常**不需要** `--add-host` 就能解析 `host.docker.internal`。Linux 上，这个 flag 是在现代 Docker Engine 上创建这个 hostname 的可移植方式。

### Linux 替代方案 —— host networking

加 `--network=host`，去掉 `-p` flags：

```bash
docker run --rm --name deeptutor \
  --network=host \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

容器直接共享宿主机网络，所以打开 <http://127.0.0.1:3782>（或 `system.json` 里的 `frontend_port`），宿主机服务也能用普通的 localhost URL 访问，比如 `http://127.0.0.1:11434/v1`。

> Host networking 把容器端口直接暴露在宿主机上，可能跟已有服务冲突。

## 升级

```bash
docker pull ghcr.io/hkuds/deeptutor:latest
docker rm -f deeptutor 2>/dev/null
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

volume 会保留 —— 你的设置、KB、记忆都能撑过升级。

## 常见错误

### `Bind for 0.0.0.0:3782 failed: port is already allocated`

```bash
lsof -i :3782          # macOS
ss -ltnp | grep :3782  # Linux
```

干掉冲突进程，或者在 `-p` 映射里换一个宿主机端口。

### 容器立刻退出

```bash
docker logs deeptutor | tail -30
```

最常见原因：首次启动时 LLM API key 配错（后端会 fail fast）。先在 Web UI 的 **设置 → LLM** 里把 LLM 配好再说，或者从 volume 里删掉错的凭证：

```bash
docker run --rm -v deeptutor-data:/app/data alpine \
  sh -c 'rm /app/data/user/settings/model_catalog.json'
docker run ... ghcr.io/hkuds/deeptutor:latest    # 用干净的 catalog 重启
```

### 前端能加载但 API 调用 404（远程 / 在反向代理后）

显式设置外部 API base。在 volume 里的 `data/user/settings/system.json`，把 `public_api_base` 设成对外可达的 URL。重启。

### Docker 里的多用户模式

直接在 volume 的 `data/user/settings/auth.json` 里把 auth 开关打开（`"enabled": true`），然后重启。容器会自动 pick up。完整配置见 [**多用户部署**](/zh-cn/docs/get-started/multi-user/)。

更多：[**故障排查**](/zh-cn/docs/get-started/troubleshooting/)。

## 下一步

- [**多用户部署**](/zh-cn/docs/get-started/multi-user/) —— 团队配置
- [**探索 DeepTutor**](/zh-cn/docs/explore/) —— 看看跑起来的应用

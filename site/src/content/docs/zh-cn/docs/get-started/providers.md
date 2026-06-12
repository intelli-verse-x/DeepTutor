---
title: Provider 配置
---


DeepTutor 当前内置 33 个 LLM provider 绑定、12 个 embedding provider 绑定和 7 个激活的搜索 provider（外加显式的 `none` 选项）。可以通过 Web 设置页面、`deeptutor init`、`data/user/settings/model_catalog.json` 或进程环境变量来配置。项目根目录的 `.env` 文件**不会**被运行时自动加载。


## 配置入口和优先级

推荐优先用 **设置 -> LLM / Embedding / Search**，因为 Web UI 会写入 `data/user/settings/model_catalog.json` 并触发运行时 apply。`deeptutor init` 适合首次初始化；环境变量适合容器编排或一次性覆盖。项目根目录 `.env` 文件不会被自动读取，如果要用环境变量，请在启动 `deeptutor start` 的进程环境里显式 export。

多用户部署里，API key 和 provider base URL 只属于 admin workspace。普通用户只拿到 admin 分配的逻辑模型 ID，看不到密钥。

## LLM Providers

| Provider                | Binding               | 默认 Base URL                                             |
| :---------------------- | :-------------------- | :-------------------------------------------------------- |
| <img src="/provider-icons/aihubmix-color.svg" alt="" width="16" height="16" /> AiHubMix | `aihubmix` | `https://aihubmix.com/v1`                                |
| <img src="/provider-icons/anthropic.svg" alt="" width="16" height="16" /> Anthropic | `anthropic` | `https://api.anthropic.com/v1`                           |
| <img src="/provider-icons/azure-color.svg" alt="" width="16" height="16" /> Azure OpenAI | `azure_openai` | —                                                        |
| <img src="/provider-icons/bytedance-color.svg" alt="" width="16" height="16" /> BytePlus | `byteplus` | `https://ark.ap-southeast.bytepluses.com/api/v3`         |
| <img src="/provider-icons/bytedance-color.svg" alt="" width="16" height="16" /> BytePlus Coding Plan | `byteplus_coding_plan` | `https://ark.ap-southeast.bytepluses.com/api/coding/v3`  |
| Custom (OpenAI-compat)  | `custom`              | —                                                        |
| <img src="/provider-icons/anthropic.svg" alt="" width="16" height="16" /> Custom Anthropic | `custom_anthropic` | —                                                        |
| <img src="/provider-icons/qwen-color.svg" alt="" width="16" height="16" /> DashScope (Qwen) | `dashscope` | `https://dashscope.aliyuncs.com/compatible-mode/v1`      |
| <img src="/provider-icons/deepseek-color.svg" alt="" width="16" height="16" /> DeepSeek | `deepseek` | `https://api.deepseek.com`                               |
| <img src="/provider-icons/gemini-color.svg" alt="" width="16" height="16" /> Gemini | `gemini` | `https://generativelanguage.googleapis.com/v1beta/openai/`|
| <img src="/provider-icons/githubcopilot.svg" alt="" width="16" height="16" /> GitHub Copilot | `github_copilot` | `https://api.githubcopilot.com`                          |
| <img src="/provider-icons/groq.svg" alt="" width="16" height="16" /> Groq | `groq` | `https://api.groq.com/openai/v1`                         |
| Lemonade                | `lemonade`            | `http://localhost:13305/api/v1`                          |
| llama.cpp               | `llama_cpp`           | `http://localhost:8080/v1`                               |
| <img src="/provider-icons/lmstudio.svg" alt="" width="16" height="16" /> LM Studio | `lm_studio` | `http://localhost:1234/v1`                               |
| <img src="/provider-icons/minimax-color.svg" alt="" width="16" height="16" /> MiniMax | `minimax` | `https://api.minimax.io/v1`                              |
| <img src="/provider-icons/minimax-color.svg" alt="" width="16" height="16" /> MiniMax Anthropic | `minimax_anthropic` | `https://api.minimax.io/v1`                              |
| <img src="/provider-icons/mistral-color.svg" alt="" width="16" height="16" /> Mistral | `mistral` | `https://api.mistral.ai/v1`                              |
| <img src="/provider-icons/moonshot.svg" alt="" width="16" height="16" /> Moonshot (Kimi) | `moonshot` | `https://api.moonshot.ai/v1`                             |
| <img src="/provider-icons/ollama.svg" alt="" width="16" height="16" /> Ollama | `ollama` | `http://localhost:11434/v1`                              |
| <img src="/provider-icons/nvidia-color.svg" alt="" width="16" height="16" /> NVIDIA NIM | `nvidia_nim` | —                                                        |
| <img src="/provider-icons/openai.svg" alt="" width="16" height="16" /> OpenAI | `openai` | `https://api.openai.com/v1`                              |
| <img src="/provider-icons/openai.svg" alt="" width="16" height="16" /> OpenAI Codex | `openai_codex` | `https://chatgpt.com/backend-api`                        |
| <img src="/provider-icons/openrouter.svg" alt="" width="16" height="16" /> OpenRouter | `openrouter` | `https://openrouter.ai/api/v1`                           |
| OpenVINO Model Server   | `ovms`                | `http://localhost:8000/v3`                               |
| <img src="/provider-icons/baiducloud-color.svg" alt="" width="16" height="16" /> Qianfan (Ernie) | `qianfan` | `https://qianfan.baidubce.com/v2`                        |
| <img src="/provider-icons/siliconcloud-color.svg" alt="" width="16" height="16" /> SiliconFlow | `siliconflow` | `https://api.siliconflow.cn/v1`                          |
| <img src="/provider-icons/stepfun-color.svg" alt="" width="16" height="16" /> Step Fun | `stepfun` | `https://api.stepfun.com/v1`                             |
| <img src="/provider-icons/vllm-color.svg" alt="" width="16" height="16" /> vLLM | `vllm` | `http://localhost:8000/v1`                               |
| <img src="/provider-icons/volcengine-color.svg" alt="" width="16" height="16" /> VolcEngine | `volcengine` | `https://ark.cn-beijing.volces.com/api/v3`               |
| <img src="/provider-icons/volcengine-color.svg" alt="" width="16" height="16" /> VolcEngine Coding Plan | `volcengine_coding_plan` | `https://ark.cn-beijing.volces.com/api/coding/v3`       |
| <img src="/provider-icons/xiaomimimo.svg" alt="" width="16" height="16" /> Xiaomi MIMO | `xiaomi_mimo` | `https://api.xiaomimimo.com/v1`                          |
| <img src="/provider-icons/zhipu-color.svg" alt="" width="16" height="16" /> Zhipu AI (GLM) | `zhipu` | `https://open.bigmodel.cn/api/paas/v4`                   |

### 配置

```dotenv
LLM_BINDING=openai
LLM_MODEL=gpt-4o-mini
LLM_API_KEY=sk-xxx
LLM_HOST=https://api.openai.com/v1
```

:::tip
任何 OpenAI 兼容的 API 都能配合 `openai` 或 `custom` binding 使用。把 `LLM_HOST` 设成你 provider 的 base URL 即可。
:::

## Embedding Providers

| Provider             | Binding       | 模型示例                  | 默认维度    |
| :------------------- | :------------ | :------------------------ | :---------: |
| <img src="/provider-icons/openai.svg" alt="" width="16" height="16" /> OpenAI | `openai` | `text-embedding-3-large`  |    3072     |
| <img src="/provider-icons/gemini-color.svg" alt="" width="16" height="16" /> Gemini | `gemini` | `gemini-embedding-001`   |    3072     |
| <img src="/provider-icons/azure-color.svg" alt="" width="16" height="16" /> Azure OpenAI | `azure_openai` | 部署名称                  |      —      |
| <img src="/provider-icons/cohere-color.svg" alt="" width="16" height="16" /> Cohere | `cohere` | `embed-v4.0`              |    1024     |
| <img src="/provider-icons/jina.svg" alt="" width="16" height="16" /> Jina | `jina` | `jina-embeddings-v3`      |    1024     |
| <img src="/provider-icons/ollama.svg" alt="" width="16" height="16" /> Ollama | `ollama` | `nomic-embed-text`        |     768     |
| <img src="/provider-icons/vllm-color.svg" alt="" width="16" height="16" /> vLLM / LM Studio | `vllm` | 任意 embedding 模型       |      —      |
| <img src="/provider-icons/siliconcloud-color.svg" alt="" width="16" height="16" /> SiliconFlow | `siliconflow` | `Qwen/Qwen3-Embedding-8B` |    4096     |
| <img src="/provider-icons/qwen-color.svg" alt="" width="16" height="16" /> Aliyun DashScope | `aliyun` | `qwen3-vl-embedding`     |    2560     |
| <img src="/provider-icons/openrouter.svg" alt="" width="16" height="16" /> OpenRouter | `openrouter` | 取决于 provider           |      —      |
| 任意 OpenAI 兼容     | `custom`      | —                         |      —      |
| Custom OpenAI SDK    | `custom_openai_sdk` | —                    |      —      |

### 配置

`EMBEDDING_HOST` 必须是完整的 embedding endpoint URL，而不仅仅是 provider 的 base URL。

```dotenv
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=text-embedding-3-large
EMBEDDING_API_KEY=sk-xxx
EMBEDDING_HOST=https://api.openai.com/v1/embeddings
EMBEDDING_DIMENSION=
```

:::caution
建好知识库之后再换 embedding 模型会引发维度不匹配。DeepTutor 会检测到并提醒你 —— 换了模型就要把知识库重建。
:::

## 搜索 Providers

| Provider    | 环境变量 Key         | 备注                             |
| :---------- | :------------------- | :------------------------------- |
| <img src="/provider-icons/brave.svg" alt="" width="16" height="16" /> Brave | `BRAVE_API_KEY` | 推荐，有免费额度                 |
| <img src="/provider-icons/tavily-color.svg" alt="" width="16" height="16" /> Tavily | `TAVILY_API_KEY` |                                  |
| Serper      | `SERPER_API_KEY`     |                                  |
| <img src="/provider-icons/jina.svg" alt="" width="16" height="16" /> Jina | `JINA_API_KEY` |                                  |
| <img src="/provider-icons/searxng.svg" alt="" width="16" height="16" /> SearXNG | — | 自部署，不需要 API key           |
| <img src="/provider-icons/duckduckgo.svg" alt="" width="16" height="16" /> DuckDuckGo | — | 不需要 API key                   |
| <img src="/provider-icons/perplexity-color.svg" alt="" width="16" height="16" /> Perplexity | `PERPLEXITY_API_KEY` | 需要 API key                     |
| None        | —                    | 显式关闭网页搜索                 |

### 配置

```dotenv
SEARCH_PROVIDER=brave
SEARCH_API_KEY=your-api-key
```

搜索是可选的 —— DeepTutor 不配搜索也能跑。配了之后，`web_search` 工具会在 Chat 和其他 capability 里可用。旧的 `exa`、`baidu`、`openrouter` 搜索设置只作为弃用的兼容值保留，不推荐作为新选择。

## 本地模型

DeepTutor 通过若干 provider 支持本地托管的模型。Docker 里连接宿主机模型时，`localhost` 指容器自身；请用 `host.docker.internal` 或参考 [Docker 文档](/zh-cn/docs/get-started/docker/#连本地-llmollama--lm-studio--llamacpp--vllm)。

### Ollama

```dotenv
LLM_BINDING=ollama
LLM_MODEL=llama3.1
LLM_HOST=http://localhost:11434/v1
LLM_API_KEY=ollama

EMBEDDING_BINDING=ollama
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_HOST=http://localhost:11434/v1
EMBEDDING_API_KEY=ollama
EMBEDDING_DIMENSION=768
```

### LM Studio

```dotenv
LLM_BINDING=lm_studio
LLM_MODEL=your-model-name
LLM_HOST=http://localhost:1234/v1
LLM_API_KEY=lm-studio
```

### vLLM

```dotenv
LLM_BINDING=vllm
LLM_MODEL=your-model-name
LLM_HOST=http://localhost:8000/v1
LLM_API_KEY=token-abc123
```

### llama.cpp

```dotenv
LLM_BINDING=llama_cpp
LLM_MODEL=your-model-name
LLM_HOST=http://localhost:8080/v1
LLM_API_KEY=not-needed
```

### Lemonade

```dotenv
LLM_BINDING=lemonade
LLM_MODEL=your-model-name
LLM_HOST=http://localhost:13305/api/v1
LLM_API_KEY=not-needed
```

---
title: Provider Configuration
---


DeepTutor currently ships 33 LLM provider bindings, 12 embedding provider bindings, and 7 active search providers (plus an explicit `none` option). Configure them through the Web Settings page, `deeptutor init`, `data/user/settings/model_catalog.json`, or process environment variables. Project-root `.env` files are not auto-loaded by the runtime.


## Configuration surfaces and precedence

Prefer **Settings -> LLM / Embedding / Search** for normal use because the Web UI writes `data/user/settings/model_catalog.json` and applies the runtime change. `deeptutor init` is best for first boot; environment variables are best for orchestrated containers or one-off overrides. Project-root `.env` files are not auto-loaded, so export variables in the process environment that starts `deeptutor start`.

In multi-user deployments, API keys and provider base URLs belong to the admin workspace. Ordinary users only receive granted logical model IDs; credentials are never returned to them.

## LLM Providers

| Provider                | Binding               | Default Base URL                                          |
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

### Configuration

```dotenv
LLM_BINDING=openai
LLM_MODEL=gpt-4o-mini
LLM_API_KEY=sk-xxx
LLM_HOST=https://api.openai.com/v1
```

:::tip
Any OpenAI-compatible API works with the `openai` or `custom` binding. Set `LLM_HOST` to your provider's base URL.
:::

## Embedding Providers

| Provider             | Binding       | Model Example             | Default Dim |
| :------------------- | :------------ | :------------------------ | :---------: |
| <img src="/provider-icons/openai.svg" alt="" width="16" height="16" /> OpenAI | `openai` | `text-embedding-3-large`  |    3072     |
| <img src="/provider-icons/gemini-color.svg" alt="" width="16" height="16" /> Gemini | `gemini` | `gemini-embedding-001`   |    3072     |
| <img src="/provider-icons/azure-color.svg" alt="" width="16" height="16" /> Azure OpenAI | `azure_openai` | deployment name           |      —      |
| <img src="/provider-icons/cohere-color.svg" alt="" width="16" height="16" /> Cohere | `cohere` | `embed-v4.0`              |    1024     |
| <img src="/provider-icons/jina.svg" alt="" width="16" height="16" /> Jina | `jina` | `jina-embeddings-v3`      |    1024     |
| <img src="/provider-icons/ollama.svg" alt="" width="16" height="16" /> Ollama | `ollama` | `nomic-embed-text`        |     768     |
| <img src="/provider-icons/vllm-color.svg" alt="" width="16" height="16" /> vLLM / LM Studio | `vllm` | Any embedding model       |      —      |
| <img src="/provider-icons/siliconcloud-color.svg" alt="" width="16" height="16" /> SiliconFlow | `siliconflow` | `Qwen/Qwen3-Embedding-8B` |    4096     |
| <img src="/provider-icons/qwen-color.svg" alt="" width="16" height="16" /> Aliyun DashScope | `aliyun` | `qwen3-vl-embedding`     |    2560     |
| <img src="/provider-icons/openrouter.svg" alt="" width="16" height="16" /> OpenRouter | `openrouter` | provider-dependent        |      —      |
| Any OpenAI-compatible| `custom`      | —                         |      —      |
| Custom OpenAI SDK    | `custom_openai_sdk` | —                    |      —      |

### Configuration

`EMBEDDING_HOST` must be the full embedding endpoint URL, not just the provider base URL.

```dotenv
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=text-embedding-3-large
EMBEDDING_API_KEY=sk-xxx
EMBEDDING_HOST=https://api.openai.com/v1/embeddings
EMBEDDING_DIMENSION=
```

:::caution
Changing the embedding model after creating a knowledge base will cause a mismatch. DeepTutor detects this and warns you — rebuild the knowledge base if you switch models.
:::

## Search Providers

| Provider    | Env Key              | Notes                            |
| :---------- | :------------------- | :------------------------------- |
| <img src="/provider-icons/brave.svg" alt="" width="16" height="16" /> Brave | `BRAVE_API_KEY` | Recommended, free tier available |
| <img src="/provider-icons/tavily-color.svg" alt="" width="16" height="16" /> Tavily | `TAVILY_API_KEY` |                                  |
| Serper      | `SERPER_API_KEY`     |                                  |
| <img src="/provider-icons/jina.svg" alt="" width="16" height="16" /> Jina | `JINA_API_KEY` |                                  |
| <img src="/provider-icons/searxng.svg" alt="" width="16" height="16" /> SearXNG | — | Self-hosted, no API key needed   |
| <img src="/provider-icons/duckduckgo.svg" alt="" width="16" height="16" /> DuckDuckGo | — | No API key needed                |
| <img src="/provider-icons/perplexity-color.svg" alt="" width="16" height="16" /> Perplexity | `PERPLEXITY_API_KEY` | Requires API key                 |
| None        | —                    | Explicitly disables web search   |

### Configuration

```dotenv
SEARCH_PROVIDER=brave
SEARCH_API_KEY=your-api-key
```

Search is optional — DeepTutor works without it. When configured, the `web_search` tool becomes available in Chat and other capabilities. Older `exa`, `baidu`, and `openrouter` search settings are treated as deprecated compatibility values rather than recommended new choices.

## Local Models

DeepTutor works with locally-hosted models through several providers. In Docker, `localhost` means the container itself; use `host.docker.internal` or the pattern in the [Docker guide](/docs/get-started/docker/#connecting-to-a-local-llm-ollama--lm-studio--llamacpp--vllm) when the model server runs on the host.

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

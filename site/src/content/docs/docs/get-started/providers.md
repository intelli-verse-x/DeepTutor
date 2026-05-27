---
title: Provider Configuration
---


DeepTutor currently ships 32 LLM provider bindings, 12 embedding provider bindings, and 7 active search providers (plus an explicit `none` option). Configure them through the Web Settings page, `deeptutor init`, `data/user/settings/model_catalog.json`, or process environment variables. Project-root `.env` files are not auto-loaded by the runtime.

## LLM Providers

| Provider                | Binding               | Default Base URL                                          |
| :---------------------- | :-------------------- | :-------------------------------------------------------- |
| AiHubMix                | `aihubmix`            | `https://aihubmix.com/v1`                                |
| Anthropic               | `anthropic`           | `https://api.anthropic.com/v1`                           |
| Azure OpenAI            | `azure_openai`        | —                                                        |
| BytePlus                | `byteplus`            | `https://ark.ap-southeast.bytepluses.com/api/v3`         |
| BytePlus Coding Plan    | `byteplus_coding_plan`| `https://ark.ap-southeast.bytepluses.com/api/coding/v3`  |
| Custom (OpenAI-compat)  | `custom`              | —                                                        |
| Custom Anthropic        | `custom_anthropic`    | —                                                        |
| DashScope (Qwen)        | `dashscope`           | `https://dashscope.aliyuncs.com/compatible-mode/v1`      |
| DeepSeek                | `deepseek`            | `https://api.deepseek.com`                               |
| Gemini                  | `gemini`              | `https://generativelanguage.googleapis.com/v1beta/openai/`|
| GitHub Copilot          | `github_copilot`      | `https://api.githubcopilot.com`                          |
| Groq                    | `groq`                | `https://api.groq.com/openai/v1`                         |
| llama.cpp               | `llama_cpp`           | `http://localhost:8080/v1`                               |
| LM Studio               | `lm_studio`           | `http://localhost:1234/v1`                               |
| MiniMax                 | `minimax`             | `https://api.minimax.io/v1`                              |
| MiniMax Anthropic       | `minimax_anthropic`   | `https://api.minimax.io/v1`                              |
| Mistral                 | `mistral`             | `https://api.mistral.ai/v1`                              |
| Moonshot (Kimi)         | `moonshot`            | `https://api.moonshot.ai/v1`                             |
| Ollama                  | `ollama`              | `http://localhost:11434/v1`                              |
| NVIDIA NIM              | `nvidia_nim`          | —                                                        |
| OpenAI                  | `openai`              | `https://api.openai.com/v1`                              |
| OpenAI Codex            | `openai_codex`        | `https://chatgpt.com/backend-api`                        |
| OpenRouter              | `openrouter`          | `https://openrouter.ai/api/v1`                           |
| OpenVINO Model Server   | `ovms`                | `http://localhost:8000/v3`                               |
| Qianfan (Ernie)         | `qianfan`             | `https://qianfan.baidubce.com/v2`                        |
| SiliconFlow             | `siliconflow`         | `https://api.siliconflow.cn/v1`                          |
| Step Fun                | `stepfun`             | `https://api.stepfun.com/v1`                             |
| vLLM                    | `vllm`                | `http://localhost:8000/v1`                               |
| VolcEngine              | `volcengine`          | `https://ark.cn-beijing.volces.com/api/v3`               |
| VolcEngine Coding Plan  | `volcengine_coding_plan`| `https://ark.cn-beijing.volces.com/api/coding/v3`       |
| Xiaomi MIMO             | `xiaomi_mimo`         | `https://api.xiaomimimo.com/v1`                          |
| Zhipu AI (GLM)          | `zhipu`               | `https://open.bigmodel.cn/api/paas/v4`                   |

### Configuration

```dotenv
LLM_BINDING=openai
LLM_MODEL=gpt-4o-mini
LLM_API_KEY=sk-xxx
LLM_HOST=https://api.openai.com/v1
```

::: tip
Any OpenAI-compatible API works with the `openai` or `custom` binding. Set `LLM_HOST` to your provider's base URL.
:::

## Embedding Providers

| Provider             | Binding       | Model Example             | Default Dim |
| :------------------- | :------------ | :------------------------ | :---------: |
| OpenAI               | `openai`      | `text-embedding-3-large`  |    3072     |
| Gemini               | `gemini`      | `gemini-embedding-001`   |    3072     |
| Azure OpenAI         | `azure_openai`| deployment name           |      —      |
| Cohere               | `cohere`      | `embed-v4.0`              |    1024     |
| Jina                 | `jina`        | `jina-embeddings-v3`      |    1024     |
| Ollama               | `ollama`      | `nomic-embed-text`        |     768     |
| vLLM / LM Studio     | `vllm`        | Any embedding model       |      —      |
| SiliconFlow          | `siliconflow` | `Qwen/Qwen3-Embedding-8B` |    4096     |
| Aliyun DashScope     | `aliyun`      | `qwen3-vl-embedding`     |    2560     |
| OpenRouter           | `openrouter`  | provider-dependent        |      —      |
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

::: warning
Changing the embedding model after creating a knowledge base will cause a mismatch. DeepTutor detects this and warns you — rebuild the knowledge base if you switch models.
:::

## Search Providers

| Provider    | Env Key              | Notes                            |
| :---------- | :------------------- | :------------------------------- |
| Brave       | `BRAVE_API_KEY`      | Recommended, free tier available |
| Tavily      | `TAVILY_API_KEY`     |                                  |
| Serper      | `SERPER_API_KEY`     |                                  |
| Jina        | `JINA_API_KEY`       |                                  |
| SearXNG     | —                    | Self-hosted, no API key needed   |
| DuckDuckGo  | —                    | No API key needed                |
| Perplexity  | `PERPLEXITY_API_KEY` | Requires API key                 |
| None        | —                    | Explicitly disables web search   |

### Configuration

```dotenv
SEARCH_PROVIDER=brave
SEARCH_API_KEY=your-api-key
```

Search is optional — DeepTutor works without it. When configured, the `web_search` tool becomes available in Chat and other capabilities. Older `exa`, `baidu`, and `openrouter` search settings are treated as deprecated compatibility values rather than recommended new choices.

## Local Models

DeepTutor works with locally-hosted models through several providers:

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

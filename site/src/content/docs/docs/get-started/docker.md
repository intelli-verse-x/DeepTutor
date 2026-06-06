---
title: Docker
description: Option 3 — one container for the full Web app, from the GHCR image.
---

One container for the full Web app. Images on GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — stable release
- `ghcr.io/hkuds/deeptutor:pre` — pre-release, when available

## Run

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Map both `3782` and `8001`.** Port `3782` serves the Web UI; port `8001` is the FastAPI backend that your browser calls directly — there is no in-container proxy. Skip the `8001` mapping and the page still loads, but **Settings** shows "Backend unreachable" and stays unusable.

Open <http://127.0.0.1:3782>. The container creates `/app/data/user/settings/*.json` on first boot; configure model providers from the Web Settings page. Config, API keys, logs, workspace files, memory, and knowledge bases all persist in the `deeptutor-data` volume.

## Detached mode

Add `-d` to run in the background:

```bash
docker run -d --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest

docker logs -f deeptutor      # follow logs
docker stop deeptutor         # stop
docker rm deeptutor           # remove (volume persists)
```

The `deeptutor-data` volume keeps your settings and workspace across `stop` / `rm` cycles. To truly start over: `docker volume rm deeptutor-data`.

## Remote Docker / reverse proxy

The Web UI runs in the user's browser, not inside the container. If someone
opens DeepTutor through a remote hostname, the browser needs a backend URL it
can reach.

For remote servers, open **Settings -> Network** or edit
`data/user/settings/system.json` in the mounted volume:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` is accepted as a compatibility alias and is normalized into
`next_public_api_base_external` on save. Leave the field blank for local Docker
on the same machine.

CORS is separate from the API base:

- `next_public_api_base_external` tells the browser where to send API and
  WebSocket calls.
- `cors_origins` lists the frontend page origins allowed to call the backend.
- With auth disabled, DeepTutor permits normal HTTP/HTTPS browser origins by
  default.
- With auth enabled, set exact frontend origins such as
  `https://deeptutor.example.com`.

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

## Different host ports

Change the left side of each `-p host:container` mapping:

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:8088:3782 \
  -p 127.0.0.1:8089:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

If you change container-side ports in `/app/data/user/settings/system.json`, restart and update the right side of each mapping to match.

## Connecting to a local LLM (Ollama / LM Studio / llama.cpp / vLLM)

Inside Docker, `localhost` is the container itself, not your host machine. To reach a model service running on the host, use the host gateway:

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Then in **Settings → LLM** (or **Embedding**), point the provider Base URL at `host.docker.internal`:

| Service | Base URL |
|---------|----------|
| Ollama LLM | `http://host.docker.internal:11434/v1` |
| Ollama embedding | `http://host.docker.internal:11434/api/embed` |
| LM Studio | `http://host.docker.internal:1234/v1` |
| llama.cpp | `http://host.docker.internal:8080/v1` |

Docker Desktop (macOS / Windows) usually resolves `host.docker.internal` **without** `--add-host`. On Linux, the flag is the portable way to create that hostname on modern Docker Engine.

### Linux alternative — host networking

Add `--network=host` and drop the `-p` flags:

```bash
docker run --rm --name deeptutor \
  --network=host \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

The container shares the host network directly, so open <http://127.0.0.1:3782> (or the `frontend_port` in `system.json`), and host services can be reached with normal localhost URLs like `http://127.0.0.1:11434/v1`.

> Host networking exposes container ports directly on the host and may conflict with existing services.

## Updating

```bash
docker pull ghcr.io/hkuds/deeptutor:latest
docker rm -f deeptutor 2>/dev/null
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

The volume persists — your settings, KBs, memory all survive the upgrade.

## Common errors

### `Bind for 0.0.0.0:3782 failed: port is already allocated`

```bash
lsof -i :3782          # macOS
ss -ltnp | grep :3782  # Linux
```

Kill the conflicting process, or choose different host ports in your `-p` mapping.

### Container exits immediately

```bash
docker logs deeptutor | tail -30
```

Most common: bad LLM API key on first boot (the backend fails fast). Open **Settings → LLM** in the Web UI before configuring an LLM, or remove the bad credential from the volume:

```bash
docker run --rm -v deeptutor-data:/app/data alpine \
  sh -c 'rm /app/data/user/settings/model_catalog.json'
docker run ... ghcr.io/hkuds/deeptutor:latest    # restart with clean catalog
```

### Frontend loads but API calls 404 (remote / behind a reverse proxy)

Set the explicit external API base. In `data/user/settings/system.json` inside
the volume, set `next_public_api_base_external` to the externally-reachable URL
and restart. `public_api_base` is still accepted as a compatibility alias.

### Multi-user mode in Docker

Just toggle auth in the volume's `data/user/settings/auth.json` (`"enabled": true`) and restart. The container picks it up. See [**Multi-User Deployment**](/docs/get-started/multi-user/) for the full setup.

More: [**Troubleshooting**](/docs/get-started/troubleshooting/).

## Next

- [**Multi-User Deployment**](/docs/get-started/multi-user/) — team setup
- [**Explore DeepTutor**](/docs/explore/) — tour the running app

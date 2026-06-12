/**
 * Cloudflare Worker — serves the static site (assets binding) plus two
 * dynamic endpoints used by the landing-page footer heartbeat:
 *
 *   GET /api/traffic  zone-wide unique visitors + total requests, summed
 *                     over Cloudflare's GraphQL Analytics retention window
 *                     (30 days on free plan). Edge-cached 5 minutes.
 *   GET /api/release  latest non-draft GitHub release. Edge-cached 30 min.
 *
 * Static requests never reach this script — the assets router answers them
 * first; only unmatched paths (i.e. /api/*) invoke the Worker.
 *
 * Config (wrangler.jsonc / dashboard → Settings):
 *   - CF_ZONE_ID    deeptutor.info zone id (vars)
 *   - CF_API_TOKEN  API token with `Zone Analytics: Read` (secret)
 *   - GITHUB_TOKEN  optional read-only PAT, bumps rate limit (secret)
 */

interface Env {
  ASSETS: { fetch(request: Request): Promise<Response> };
  CF_ZONE_ID?: string;
  CF_API_TOKEN?: string;
  GITHUB_TOKEN?: string;
}

interface ExecutionContextLike {
  waitUntil(promise: Promise<unknown>): void;
}

export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContextLike,
  ): Promise<Response> {
    const { pathname } = new URL(request.url);
    if (request.method === "GET" && pathname === "/api/traffic") {
      return withEdgeCache(request, ctx, () => traffic(env));
    }
    if (request.method === "GET" && pathname === "/api/release") {
      return withEdgeCache(request, ctx, () => release(env));
    }
    if (request.method === "GET" && pathname === "/api/stars") {
      return withEdgeCache(request, ctx, () => stars(env));
    }
    return env.ASSETS.fetch(request);
  },
};

/**
 * Serve from the colo-local edge cache when fresh; otherwise compute and
 * cache the 200 response (TTL comes from its own Cache-Control header).
 */
async function withEdgeCache(
  request: Request,
  ctx: ExecutionContextLike,
  compute: () => Promise<Response>,
): Promise<Response> {
  const cache = caches.default;
  const hit = await cache.match(request);
  if (hit) return hit;

  const response = await compute();
  if (response.status === 200) {
    ctx.waitUntil(cache.put(request, response.clone()));
  }
  return response;
}

// ───────────────────────── /api/traffic ─────────────────────────

interface AnalyticsGroup {
  sum: { requests: number; bytes: number };
  uniq?: { uniques?: number };
}

interface GraphqlResponse {
  data?: {
    viewer?: {
      zones?: { httpRequests1dGroups?: AnalyticsGroup[] }[];
    };
  };
  errors?: { message: string }[];
}

// Cloudflare's free-plan retention is 30 days, so the effective scope is
// "since launch, capped at 30 days back". No date dimension/orderBy — the
// API then returns a single group aggregated over the whole window (orderBy
// without a selected dimension is a GraphQL syntax error).
const TRAFFIC_QUERY = `
  query Total($zoneTag: String!, $since: Date!) {
    viewer {
      zones(filter: { zoneTag: $zoneTag }) {
        httpRequests1dGroups(limit: 30, filter: { date_geq: $since }) {
          sum { requests bytes }
          uniq { uniques }
        }
      }
    }
  }
`;

async function traffic(env: Env): Promise<Response> {
  if (!env.CF_API_TOKEN || !env.CF_ZONE_ID) {
    return json({ error: "not_configured" }, 503);
  }

  const since = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
    .toISOString()
    .slice(0, 10);

  try {
    const upstream = await fetch(
      "https://api.cloudflare.com/client/v4/graphql",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${env.CF_API_TOKEN}`,
        },
        body: JSON.stringify({
          query: TRAFFIC_QUERY,
          variables: { zoneTag: env.CF_ZONE_ID, since },
        }),
      },
    );

    if (!upstream.ok) {
      return json({ error: "upstream_status", status: upstream.status }, 502);
    }

    const payload = (await upstream.json()) as GraphqlResponse;
    if (payload.errors?.length) {
      return json(
        { error: "graphql_error", detail: payload.errors[0].message },
        502,
      );
    }

    const groups = payload.data?.viewer?.zones?.[0]?.httpRequests1dGroups ?? [];
    const totals = groups.reduce(
      (acc, g) => ({
        requests: acc.requests + (g.sum?.requests ?? 0),
        bytes: acc.bytes + (g.sum?.bytes ?? 0),
        uniques: acc.uniques + (g.uniq?.uniques ?? 0),
      }),
      { requests: 0, bytes: 0, uniques: 0 },
    );

    return json(
      {
        window: "total",
        requests: totals.requests,
        bytes: totals.bytes,
        uniques: totals.uniques,
      },
      200,
      "public, max-age=300, s-maxage=300, stale-while-revalidate=600",
    );
  } catch (err) {
    return json({ error: "fetch_failed", detail: String(err) }, 502);
  }
}

// ───────────────────────── /api/release ─────────────────────────

interface GithubRelease {
  tag_name: string;
  name: string | null;
  html_url: string;
  published_at: string;
  prerelease: boolean;
  draft: boolean;
}

const RELEASES_ENDPOINT =
  "https://api.github.com/repos/HKUDS/DeepTutor/releases?per_page=5";

function ghHeaders(env: Env): Record<string, string> {
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
    "User-Agent": "deeptutor-info-worker",
    "X-GitHub-Api-Version": "2022-11-28",
  };
  if (env.GITHUB_TOKEN) {
    headers.Authorization = `Bearer ${env.GITHUB_TOKEN}`;
  }
  return headers;
}

async function release(env: Env): Promise<Response> {
  try {
    const upstream = await fetch(RELEASES_ENDPOINT, { headers: ghHeaders(env) });
    if (!upstream.ok) {
      return json({ error: "upstream_status", status: upstream.status }, 502);
    }

    const releases = (await upstream.json()) as GithubRelease[];
    const latest = releases.find((r) => !r.draft) ?? null;
    if (!latest) {
      return json({ error: "no_release" }, 404);
    }

    return json(
      {
        tag: latest.tag_name,
        name: latest.name ?? latest.tag_name,
        url: latest.html_url,
        published_at: latest.published_at,
        prerelease: latest.prerelease,
      },
      200,
      "public, max-age=1800, s-maxage=1800, stale-while-revalidate=3600",
    );
  } catch (err) {
    return json({ error: "fetch_failed", detail: String(err) }, 502);
  }
}

// ───────────────────────── /api/stars ─────────────────────────

const REPO_ENDPOINT = "https://api.github.com/repos/HKUDS/DeepTutor";

async function stars(env: Env): Promise<Response> {
  try {
    const upstream = await fetch(REPO_ENDPOINT, { headers: ghHeaders(env) });
    if (!upstream.ok) {
      return json({ error: "upstream_status", status: upstream.status }, 502);
    }
    const repo = (await upstream.json()) as { stargazers_count?: number };
    if (typeof repo.stargazers_count !== "number") {
      return json({ error: "bad_payload" }, 502);
    }
    return json(
      { stars: repo.stargazers_count },
      200,
      "public, max-age=1800, s-maxage=1800, stale-while-revalidate=3600",
    );
  } catch (err) {
    return json({ error: "fetch_failed", detail: String(err) }, 502);
  }
}

function json(body: unknown, status = 200, cache?: string): Response {
  const headers: Record<string, string> = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
  };
  if (cache) headers["Cache-Control"] = cache;
  return new Response(JSON.stringify(body), { status, headers });
}

/**
 * Cloudflare Pages Function — cumulative-since-launch traffic summary for
 * the landing-page heartbeat. Queries Cloudflare's GraphQL Analytics API
 * over the full retention window (30 days on free, 6 months on Pro).
 *
 * Env vars (Pages → Settings → Environment variables):
 *   - CF_API_TOKEN  API token with `Zone Analytics: Read` (scoped to deeptutor.info).
 *   - CF_ZONE_ID    deeptutor.info zone id (Cloudflare → Overview → API).
 *
 * Edge-cached 1 hour. Returns `{ error }` with a useful status when the
 * upstream is unreachable so the client can hide the heartbeat row.
 */

interface Env {
  CF_API_TOKEN?: string;
  CF_ZONE_ID?: string;
}

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

// `httpRequests1dGroups` with `limit: 30` — Cloudflare's free-plan retention
// is 30 days. Upstream returns whatever exists within the window, so the
// effective scope is "since launch, capped at 30 days back".
const QUERY = `
  query Total($zoneTag: String!, $since: Date!) {
    viewer {
      zones(filter: { zoneTag: $zoneTag }) {
        httpRequests1dGroups(
          limit: 30
          filter: { date_geq: $since }
          orderBy: [date_DESC]
        ) {
          sum { requests bytes }
          uniq { uniques }
        }
      }
    }
  }
`;

export const onRequestGet: PagesFunction<Env> = async ({ env }) => {
  if (!env.CF_API_TOKEN || !env.CF_ZONE_ID) {
    return json({ error: "not_configured" }, 503);
  }

  const since = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
    .toISOString()
    .slice(0, 10);

  try {
    const upstream = await fetch("https://api.cloudflare.com/client/v4/graphql", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${env.CF_API_TOKEN}`,
      },
      body: JSON.stringify({
        query: QUERY,
        variables: { zoneTag: env.CF_ZONE_ID, since },
      }),
    });

    if (!upstream.ok) {
      return json({ error: "upstream_status", status: upstream.status }, 502);
    }

    const payload = (await upstream.json()) as GraphqlResponse;
    if (payload.errors?.length) {
      return json({ error: "graphql_error", detail: payload.errors[0].message }, 502);
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
      "public, max-age=3600, s-maxage=3600, stale-while-revalidate=7200",
    );
  } catch (err) {
    return json({ error: "fetch_failed", detail: String(err) }, 502);
  }
};

function json(body: unknown, status = 200, cache?: string): Response {
  const headers: Record<string, string> = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
  };
  if (cache) headers["Cache-Control"] = cache;
  return new Response(JSON.stringify(body), { status, headers });
}

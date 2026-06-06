/**
 * Cloudflare Pages Function — most recent GitHub release for HKUDS/DeepTutor.
 *
 * Returns the FIRST item from `/releases` (most recently published,
 * including prereleases) so that `v1.4.0-beta`-style tags surface on the
 * landing page immediately instead of waiting for the next stable.
 *
 * Optional env var:
 *   - GITHUB_TOKEN  any read-only PAT, bumps rate limit to 5k/h.
 *                   Not required for current traffic (unauth = 60/h, plenty
 *                   given the 30-min edge cache).
 */

interface Env {
  GITHUB_TOKEN?: string;
}

interface GithubRelease {
  tag_name: string;
  name: string | null;
  html_url: string;
  published_at: string;
  prerelease: boolean;
  draft: boolean;
}

const ENDPOINT =
  "https://api.github.com/repos/HKUDS/DeepTutor/releases?per_page=5";

export const onRequestGet: PagesFunction<Env> = async ({ env }) => {
  try {
    const headers: Record<string, string> = {
      Accept: "application/vnd.github+json",
      "User-Agent": "deeptutor-info-pages",
      "X-GitHub-Api-Version": "2022-11-28",
    };
    if (env.GITHUB_TOKEN) {
      headers.Authorization = `Bearer ${env.GITHUB_TOKEN}`;
    }

    const upstream = await fetch(ENDPOINT, { headers });
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
};

function json(body: unknown, status = 200, cache?: string): Response {
  const headers: Record<string, string> = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
  };
  if (cache) headers["Cache-Control"] = cache;
  return new Response(JSON.stringify(body), { status, headers });
}

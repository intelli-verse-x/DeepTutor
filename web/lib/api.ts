// API configuration and utility functions.
//
// The frontend bundle is now URL-agnostic: the browser issues requests against
// the frontend origin (`:3782/api/...` and `:3782/api/.../ws`), and
// `web/proxy.ts` rewrites `/api/*` and `/ws/*` to the configured backend on
// every request. This means there is no build-time or runtime URL substitution
// in the bundle, and no placeholder token to keep alive. `apiUrl` and `wsUrl`
// stay as one-liner pass-throughs so the dozens of existing call sites continue
// to compile and work without modification.

/**
 * Construct a full API URL from a path.
 *
 * Pass-through: returns the path unchanged. The actual backend URL is
 * determined at request time by `web/proxy.ts`, which reads
 * `DEEPTUTOR_API_BASE_URL` (exported by the container entrypoint from
 * `data/user/settings/system.json`).
 *
 * @param path - API path (e.g., '/api/v1/knowledge/list')
 * @returns The same path, unchanged
 */
export function apiUrl(path: string): string {
  return path;
}

/**
 * Construct a WebSocket URL from a path.
 *
 * Pass-through: returns the path unchanged. `proxy.ts` rewrites `/ws/*` to
 * the configured backend, and the runtime upgrades to `ws://` /
 * `wss://` based on the backend's scheme.
 *
 * @param path - WebSocket path (e.g., '/api/v1/solve')
 * @returns The same path, unchanged
 */
export function wsUrl(path: string): string {
  return path;
}

/**
 * Parse a "DEEPTUTOR_AUTH_ENABLED"-style flag at runtime.
 *
 * Used by both `apiFetch` (frontend) and `web/proxy.ts` (auth redirect) to
 * decide whether to gate requests. Evaluated with a runtime regex so the
 * value can be set by the container entrypoint on every start (no build-time
 * inlining).
 */
export function parseAuthEnabled(raw: string | undefined): boolean {
  return /^(1|true|yes|on)$/i.test((raw ?? "").trim());
}

const AUTH_ENABLED = parseAuthEnabled(process.env.DEEPTUTOR_AUTH_ENABLED);

/**
 * Authenticated fetch wrapper. Behaves identically to `fetch` but automatically
 * redirects to /login when the backend returns 401 (expired / invalid token).
 *
 * Pass `skipAuthRedirect: true` for endpoints where a 401 is an expected,
 * recoverable response that the caller wants to handle inline — most notably
 * the login/register endpoints, where 401 means "wrong credentials" and must
 * surface as a form error rather than reload the page.
 */
export async function apiFetch(
  input: RequestInfo | URL,
  init?: RequestInit & { skipAuthRedirect?: boolean },
): Promise<Response> {
  const { skipAuthRedirect, ...fetchInit } = init ?? {};
  const res = await fetch(input, { credentials: "include", ...fetchInit });

  if (
    res.status === 401 &&
    AUTH_ENABLED &&
    !skipAuthRedirect &&
    typeof window !== "undefined"
  ) {
    const next = encodeURIComponent(window.location.pathname);
    window.location.href = `/login?next=${next}`;
    return new Promise(() => {});
  }

  return res;
}

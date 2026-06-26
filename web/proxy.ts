import { NextRequest, NextResponse } from "next/server";
import { parseAuthEnabled } from "./lib/api";

// Backend base URL for `/api/*` and `/ws/*` rewrites. The container
// entrypoint exports `DEEPTUTOR_API_BASE_URL` from `data/user/settings/system.json`
// (preferring `next_public_api_base`, then `next_public_api_base_external`,
// then `http://localhost:${BACKEND_PORT}`). In dev (`deeptutor start`) it
// defaults to `http://localhost:8001`.
const API_BASE_URL =
  process.env.DEEPTUTOR_API_BASE_URL ?? "http://localhost:8001";

const AUTH_ENABLED = parseAuthEnabled(process.env.DEEPTUTOR_AUTH_ENABLED);
const LOGIN_PATH = "/login";
const COOKIE_NAME = "dt_token";

export function proxy(req: NextRequest) {
  const { pathname, search } = req.nextUrl;

  // Forward all backend-relative paths to the configured backend. The browser
  // fetches against the frontend origin (e.g. `:3782/api/v1/...` or
  // `:3782/api/v1/.../ws`); the rewrite is what bridges the origin gap and
  // keeps the URL knowledge in one place (the entrypoint + system.json) rather
  // than baked into the frontend bundle.
  if (pathname.startsWith("/api/") || pathname.startsWith("/ws/")) {
    return NextResponse.rewrite(new URL(pathname + search, API_BASE_URL));
  }

  // Auth is disabled (default) — let everything else through
  if (!AUTH_ENABLED) return NextResponse.next();

  // Always allow auth pages and Next.js internals
  if (
    pathname.startsWith(LOGIN_PATH) ||
    pathname.startsWith("/register") ||
    pathname.startsWith("/_next") ||
    pathname.startsWith("/favicon")
  ) {
    return NextResponse.next();
  }

  const token = req.cookies.get(COOKIE_NAME)?.value;

  // No token — redirect to login, preserving the intended destination
  if (!token) {
    const loginUrl = req.nextUrl.clone();
    loginUrl.pathname = LOGIN_PATH;
    loginUrl.searchParams.set("next", pathname);
    return NextResponse.redirect(loginUrl);
  }

  // Verify token structure (JWT: header.payload.signature)
  const parts = token.split(".");
  if (parts.length !== 3) {
    const loginUrl = req.nextUrl.clone();
    loginUrl.pathname = LOGIN_PATH;
    loginUrl.searchParams.set("next", pathname);
    const response = NextResponse.redirect(loginUrl);
    response.cookies.delete(COOKIE_NAME);
    return response;
  }

  // Check expiry from payload (base64url-decoded JSON)
  try {
    const payload = JSON.parse(
      Buffer.from(parts[1], "base64url").toString("utf-8"),
    );
    if (payload.exp && Date.now() >= payload.exp * 1000) {
      const loginUrl = req.nextUrl.clone();
      loginUrl.pathname = LOGIN_PATH;
      loginUrl.searchParams.set("next", pathname);
      const response = NextResponse.redirect(loginUrl);
      response.cookies.delete(COOKIE_NAME);
      return response;
    }
  } catch {
    // Malformed payload — treat as invalid
    const loginUrl = req.nextUrl.clone();
    loginUrl.pathname = LOGIN_PATH;
    loginUrl.searchParams.set("next", pathname);
    const response = NextResponse.redirect(loginUrl);
    response.cookies.delete(COOKIE_NAME);
    return response;
  }

  return NextResponse.next();
}

export const config = {
  // Run on every request except Next.js internals and the favicon. The /api/*
  // and /ws/* paths are explicitly handled above (rewritten to the backend).
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};

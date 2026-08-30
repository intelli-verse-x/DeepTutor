"""Tenancy must come from a verified token, never from a caller-supplied value.

Regression cover for the ``x-user-id`` impersonation hole: the header was the
tenant key, so any HTTP client could name itself as any learner and read or
write that learner's tutor sessions, notebooks, memory, knowledge bases and exam
records.

The properties pinned here are the ones that made it exploitable, so each is
asserted directly rather than inferred from a single happy path:

1. a forged identity header grants nothing;
2. a request with no verifiable identity is refused, not defaulted (a fallback
   tenant is the same hole with extra steps);
3. a verified token resolves to its own subject;
4. a header cannot override or shadow a verified subject;
5. ``POST /auth/anonymous`` cannot be steered to mint a token for a chosen
   subject — otherwise requiring tokens would only add a round trip to the
   attack;
6. the rate-limit bucket is not caller-partitionable (that cap fronts paid
   models);
7. an unverifiable WebSocket upgrade resolves to no identity.
"""

from __future__ import annotations

import pytest

pytest.importorskip("fastapi")

from fastapi import Depends, FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from deeptutor.api.middleware.tenant import (  # noqa: E402
    TenantMiddleware,
    _subject_from_ws_query,
    require_user_id,
    subject_from_authorization,
)

# 32+ chars: _get_secret() rejects anything shorter as a misconfiguration.
_TEST_SECRET = "test-secret-for-identity-tests-0123456789"

VICTIM = "11111111-1111-4111-8111-111111111111"
ATTACKER = "22222222-2222-4222-8222-222222222222"


@pytest.fixture(autouse=True)
def _jwt_secret(monkeypatch):
    monkeypatch.setenv("DEEPTUTOR_JWT_SECRET", _TEST_SECRET)


@pytest.fixture
def client() -> TestClient:
    app = FastAPI()
    app.add_middleware(TenantMiddleware)

    @app.get("/tenant")
    async def _tenant(user_id: str = Depends(require_user_id)):
        return {"user_id": user_id}

    return TestClient(app)


def _mint(sub: str) -> str:
    from deeptutor.api.routers.auth import encode_token

    return encode_token(sub)["token"]


def _bearer(sub: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {_mint(sub)}"}


# ---------------------------------------------------------------------------
# 1-2. The header grants nothing, and absence is refused rather than defaulted.
# ---------------------------------------------------------------------------


def test_forged_identity_header_is_ignored(client: TestClient) -> None:
    res = client.get("/tenant", headers={"x-user-id": VICTIM})
    assert res.status_code == 401
    assert VICTIM not in res.text


@pytest.mark.parametrize(
    "headers",
    [
        {},
        {"x-user-id": VICTIM},
        {"Authorization": "Bearer not.a.token"},
        {"Authorization": f"Basic {VICTIM}"},
        {"Authorization": ""},
    ],
    ids=["no-headers", "forged-header", "malformed-token", "wrong-scheme", "empty"],
)
def test_unverifiable_request_is_refused(client: TestClient, headers) -> None:
    """No tenant is invented for an unverifiable caller.

    A default/shared fallback tenant would silently mix different people's data
    and keep the header path effectively alive.
    """
    assert client.get("/tenant", headers=headers).status_code == 401


def test_bad_signature_is_refused(client: TestClient) -> None:
    token = _mint(ATTACKER)
    head, payload, sig = token.split(".")
    tampered = f"{head}.{payload}.{'A' * len(sig)}"
    res = client.get("/tenant", headers={"Authorization": f"Bearer {tampered}"})
    assert res.status_code == 401


def test_token_signed_with_another_secret_is_refused(
    client: TestClient, monkeypatch
) -> None:
    token = _mint(ATTACKER)
    monkeypatch.setenv("DEEPTUTOR_JWT_SECRET", "a-completely-different-secret-0123456789")
    res = client.get("/tenant", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 401


# ---------------------------------------------------------------------------
# 3-4. A verified token resolves to its own subject and cannot be shadowed.
# ---------------------------------------------------------------------------


def test_verified_token_resolves_its_subject(client: TestClient) -> None:
    res = client.get("/tenant", headers=_bearer(ATTACKER))
    assert res.status_code == 200
    assert res.json()["user_id"] == ATTACKER


def test_header_cannot_override_verified_subject(client: TestClient) -> None:
    """The original bug shape: caller authenticates as itself, names a victim."""
    headers = _bearer(ATTACKER) | {"x-user-id": VICTIM}
    res = client.get("/tenant", headers=headers)
    assert res.status_code == 200
    assert res.json()["user_id"] == ATTACKER


def test_resolver_only_reads_the_authorization_value() -> None:
    """``subject_from_authorization`` has no other input to be confused by."""
    assert subject_from_authorization(None) is None
    assert subject_from_authorization(f"Bearer {_mint(VICTIM)}") == VICTIM


# ---------------------------------------------------------------------------
# 5. The mint endpoint is not an impersonation oracle.
# ---------------------------------------------------------------------------


@pytest.fixture
def auth_client() -> TestClient:
    from deeptutor.api.routers import auth as auth_router

    app = FastAPI()
    app.include_router(auth_router.router, prefix="/api/v1/auth")
    return TestClient(app)


@pytest.mark.parametrize(
    "body",
    [None, {}, {"preferred_user_id": VICTIM}, {"preferred_user_id": "not-a-uuid"}],
    ids=["no-body", "empty", "requests-victim", "requests-garbage"],
)
def test_anonymous_never_mints_a_caller_chosen_subject(auth_client, body) -> None:
    res = auth_client.post("/api/v1/auth/anonymous", json=body)
    assert res.status_code == 200
    minted = res.json()["user_id"]
    assert minted != VICTIM
    # And the token really carries the server-chosen subject.
    assert subject_from_authorization(f"Bearer {res.json()['token']}") == minted


def test_anonymous_subjects_are_distinct_per_call(auth_client) -> None:
    first = auth_client.post("/api/v1/auth/anonymous", json={}).json()["user_id"]
    second = auth_client.post("/api/v1/auth/anonymous", json={}).json()["user_id"]
    assert first != second


# ---------------------------------------------------------------------------
# 6. Rate-limit buckets are not caller-partitionable.
# ---------------------------------------------------------------------------


def test_rate_limit_bucket_ignores_the_identity_header() -> None:
    """Varying the header must not hand the caller a fresh quota.

    These buckets cap the chat / vision routes, which reach paid models.
    """
    from deeptutor.api.middleware.rate_limiter import RateLimiterMiddleware

    limiter = RateLimiterMiddleware.__new__(RateLimiterMiddleware)

    class _Req:
        def __init__(self, headers):
            self.headers = headers
            self.client = type("C", (), {"host": "203.0.113.7"})()

    a = limiter._get_client_id(_Req({"x-user-id": "aaa"}))
    b = limiter._get_client_id(_Req({"x-user-id": "bbb"}))
    assert a == b

    # A verified subject still gets its own bucket.
    verified = limiter._get_client_id(
        _Req({"authorization": f"Bearer {_mint(ATTACKER)}"})
    )
    assert verified != a
    assert ATTACKER in verified


# ---------------------------------------------------------------------------
# 7. WebSocket upgrades: identity in a URL is not identity.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "query",
    [
        f"user_id={VICTIM}",
        f"x_user_id={VICTIM}",
        "token=not.a.token",
        "",
    ],
    ids=["user_id-param", "x_user_id-param", "malformed-token", "no-query"],
)
def test_ws_query_identity_is_not_accepted(query: str) -> None:
    assert _subject_from_ws_query({"query_string": query.encode()}) is None


def test_ws_verified_token_query_resolves() -> None:
    scope = {"query_string": f"token={_mint(ATTACKER)}".encode()}
    assert _subject_from_ws_query(scope) == ATTACKER


# ---------------------------------------------------------------------------
# Shared-deployment enforcement: no identity means no service, not admin.
# ---------------------------------------------------------------------------


@pytest.fixture
def enforced(monkeypatch):
    monkeypatch.setenv("DEEPTUTOR_REQUIRE_IDENTITY", "true")


def _auth_dep_app():
    """App whose route resolves scope via ``require_auth`` only.

    This is the shape of the ~24 routers mounted with ``dependencies=[require_auth]``
    that never call ``require_user_id``: with auth disabled they take their
    workspace from the ContextVar that ``require_auth`` installs.
    """
    from deeptutor.api.routers.auth import require_auth

    app = FastAPI()

    @app.get("/scoped", dependencies=[Depends(require_auth)])
    async def _scoped():
        return {"ok": True}

    return app


def test_identityless_request_is_refused_when_enforced(enforced) -> None:
    res = TestClient(_auth_dep_app()).get("/scoped")
    assert res.status_code == 401


def test_verified_request_is_served_when_enforced(enforced) -> None:
    res = TestClient(_auth_dep_app()).get("/scoped", headers=_bearer(ATTACKER))
    assert res.status_code == 200


def test_identityless_request_keeps_single_user_behaviour_when_not_enforced(
    monkeypatch,
) -> None:
    """Upstream's localhost single-user install must not start needing tokens."""
    monkeypatch.delenv("DEEPTUTOR_REQUIRE_IDENTITY", raising=False)
    res = TestClient(_auth_dep_app()).get("/scoped")
    assert res.status_code == 200


def test_admin_routes_refuse_when_enforced_and_auth_disabled(enforced) -> None:
    """Anonymous tokens carry a subject and no role, so admin cannot be proven."""
    from deeptutor.api.routers.auth import require_admin

    app = FastAPI()

    @app.get("/admin-only", dependencies=[Depends(require_admin)])
    async def _admin_only():
        return {"ok": True}

    client = TestClient(app)
    assert client.get("/admin-only").status_code in (401, 403)
    assert client.get("/admin-only", headers=_bearer(ATTACKER)).status_code == 403

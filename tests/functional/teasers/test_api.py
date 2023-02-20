from teasers.choices import StatusChoices
from users.models import Author


def test_get_teasers(client, db, bake_authors, bake_teasers):
    bake_teasers(bake_authors)

    response = client.get("/api/teasers/")
    assert response.status_code == 200
    response_json = response.json()

    teasers_num = 6
    assert len(response_json) == teasers_num
    for i, response_teaser in enumerate(response_json, start=1):
        assert response_teaser["title"] == f"title_{i}"
        assert response_teaser["status"] == StatusChoices.pending


def test_pay_for_teasers(client, db, bake_authors, bake_teasers):
    bake_teasers(bake_authors)
    response = client.patch(
        "/api/teasers/paid",
        # pay for every odd teaser: author_1(1, 3), author_2(5)
        data={"ids": list(range(1, 7, 2))},
        content_type="application/json",
    )
    assert response.status_code == 200
    response_json = response.json()
    for teaser in response_json:
        assert teaser["status"] == StatusChoices.paid if teaser["id"] % 2 == 1 else StatusChoices.pending
    for author in Author.objects.all():
        assert author.account.current_balance == 200 if author.user.id % 2 == 1 else 100


def test_deny_teasers(client, db, bake_authors, bake_teasers):
    bake_teasers(bake_authors)
    response = client.patch(
        "/api/teasers/denied",
        # deny every odd teaser: 1, 3, 5
        data={"ids": list(range(1, 7, 2))},
        content_type="application/json",
    )
    assert response.status_code == 200
    response_json = response.json()
    for teaser in response_json:
        assert teaser["status"] == StatusChoices.denied if teaser["id"] % 2 == 1 else StatusChoices.pending

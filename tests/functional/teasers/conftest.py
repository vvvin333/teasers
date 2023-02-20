import pytest
from django.contrib.auth.models import User
from model_bakery import baker

from accounts.models import TeaserPrice, Account
from teasers.models import Teaser
from users.models import Author


@pytest.fixture(scope="function")
def bake_authors() -> list[Author]:
    authors = []
    authors_num = 2
    t_price = 100
    teaser_price = TeaserPrice.objects.create(
        price=t_price,
    )
    for i in range(1, authors_num + 1):
        django_user = User.objects.create(
            username=f"user_{i}",
        )
        author = Author.objects.create(
            first_name=f"fname_{i}",
            last_name=f"lname_{i}",
            user=django_user,
        )
        Account.objects.create(
            teaser_price=teaser_price,
            author=author,
        )
        authors.append(author)
    return authors


@pytest.fixture(scope="function")
def bake_teasers():
    def func(authors: list[Author]) -> list[Teaser]:
        teasers = []
        teasers_per_author_num = 3
        count = 0
        for author in authors:
            count += 1
            for _ in range(teasers_per_author_num):
                baker.make(
                    Teaser,
                    title=f"title_{count}",
                    author=author,
                )
        return teasers

    return func

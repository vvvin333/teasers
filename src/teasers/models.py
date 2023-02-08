from django.db import models

from teasers.choices import StatusChoices
from users.models import Author


class Teaser(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=32)
    status = models.CharField(
        max_length=16, choices=StatusChoices.choices, default=StatusChoices.pending
    )

    author = models.ForeignKey(
        Author,
        models.PROTECT,
        db_column="user",
        related_name="teasers",
        related_query_name="teaser",
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Teaser: {self.__str__()}"

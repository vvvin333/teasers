from django.db import models

from users.models import Author


class TeaserPrice(models.Model):
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.price)

    def __repr__(self) -> str:
        return f"TeaserPrice: {self.__str__()}"


class Account(models.Model):
    current_balance = models.FloatField(default=0)
    teaser_price = models.ForeignKey(
        TeaserPrice,
        models.PROTECT,
        related_name="accounts",
        related_query_name="account",
    )
    author = models.OneToOneField(
        Author,
        models.PROTECT,
        db_column="user",
        related_name="account",
    )

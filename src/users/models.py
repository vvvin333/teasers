from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64, default=None)
    last_name = models.CharField(max_length=64, default=None)

    user = models.OneToOneField(
        User,
        models.PROTECT,
        db_column="user_uid",
        related_name="author",
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"Author: {self.__str__()}"

    class Meta:
        app_label = "users"
        db_table = "author"


class AdminProfile(models.Model):
    first_name = models.CharField(max_length=64, default=None)
    last_name = models.CharField(max_length=64, default=None)

    user = models.OneToOneField(
        User,
        models.PROTECT,
        db_column="user_uid",
        related_name="admin_profile",
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"AdminProfile: {self.__str__()}"

    class Meta:
        app_label = "users"
        db_table = "admin_profile"

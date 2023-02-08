from django.db import models


class GroupChoices(models.TextChoices):
    authors = "authors"
    admins = "admins"

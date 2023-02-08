from django.db import models


class StatusChoices(models.TextChoices):
    pending = "pending"
    paid = "paid"
    denied = "denied"

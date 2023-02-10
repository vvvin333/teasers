from django.db.models import QuerySet

from accounts.models import Account
from teasers.choices import StatusChoices
from teasers.models import Teaser


def pay_for_teasers(accounts_with_teasers: QuerySet[Account]) -> QuerySet[Teaser]:
    teasers_qs = Teaser.objects.none()
    for account in accounts_with_teasers:
        teasers = account.author.teasers.all()
        teasers_qs |= teasers
        for _ in teasers:
            account.current_balance += account.teaser_price.price
    Account.objects.bulk_update(accounts_with_teasers, ("current_balance",))
    teasers_qs.update(status=StatusChoices.paid)
    return teasers_qs

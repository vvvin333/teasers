from django.db.models import Prefetch
from django.http import HttpRequest
from ninja import Router

from accounts.models import Account
from api.teasers import schemas
from api.teasers.shortcuts import pay_for_teasers
from teasers.choices import StatusChoices
from teasers.models import Teaser

router = Router(tags=["teasers"])


@router.get(
    "/",
    response=list[schemas.Teaser],
)
def get_teasers(
    _: HttpRequest,
) -> list[Teaser]:
    return Teaser.objects.select_related("author__account").all()


@router.patch(
    "/paid",
    response=list[schemas.Teaser],
)
def set_paid_teasers(
    _: HttpRequest,
    payload: schemas.IdList,
) -> list[Teaser]:
    teaser_ids: list[str] = payload.ids
    accounts = Account.objects.filter(
        author__teaser__pk__in=teaser_ids,
        author__teaser__status=StatusChoices.pending,
    ).select_related(
        "teaser_price"
    ).prefetch_related(
        Prefetch(
            "author__teasers",
            queryset=Teaser.objects.filter(
                pk__in=teaser_ids,
                status=StatusChoices.pending,
            )
        )
    ).distinct()
    return pay_for_teasers(accounts)


@router.patch(
    "/denied",
    response=list[schemas.Teaser],
)
def set_denied_teasers(
    _: HttpRequest,
    payload: schemas.IdList,
) -> list[Teaser]:
    teaser_ids: list[str] = payload.ids
    teasers = Teaser.objects.filter(
        pk__in=teaser_ids,
        status=StatusChoices.pending,
    )
    teasers.update(status=StatusChoices.denied)
    return teasers

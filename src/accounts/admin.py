from django.contrib import admin

from accounts.models import Account, TeaserPrice
from users.choices import GroupChoices


@admin.register(TeaserPrice)
class TeaserPriceAdmin(admin.ModelAdmin):
    list_display = ("price", )

    def get_readonly_fields(self, request, obj=None) -> tuple:
        fields = super().get_readonly_fields(request, obj)
        if obj is not None:
            if (
                    GroupChoices.authors in request.user.groups.all().values_list("name", flat=True)
            ):
                fields += ("price",)

        return fields

    def has_add_permission(self, request) -> bool:
        has_permission = super().has_add_permission(request)
        if (
            GroupChoices.authors in request.user.groups.all().values_list("name", flat=True)
        ):
            has_permission = False
        return has_permission


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("author", "current_balance", "teaser_price")
    list_filter = ("author",)

    def get_readonly_fields(self, request, obj=None) -> tuple:
        fields = super().get_readonly_fields(request, obj)
        if obj is not None:
            if (
                    GroupChoices.authors in request.user.groups.all().values_list("name", flat=True)
            ):
                fields += ("current_balance", "teaser_price", "author")
            if (
                    GroupChoices.admins in request.user.groups.all().values_list("name", flat=True)
            ):
                fields += ("current_balance", "author")

        return fields

    def has_add_permission(self, request) -> bool:
        has_permission = super().has_add_permission(request)
        if (
            GroupChoices.authors in request.user.groups.all().values_list("name", flat=True)
        ):
            has_permission = False
        return has_permission

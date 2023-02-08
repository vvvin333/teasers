from django.contrib import admin

from teasers.forms import TeaserForm
from teasers.models import Teaser
from users.choices import GroupChoices


@admin.register(Teaser)
class TeaserAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "status", "author")
    search_fields = ("title",)
    list_filter = ("status", "category", "author")
    form = TeaserForm

    def get_form(self, request, *args, **kwargs):
        form = super().get_form(request, *args, **kwargs)
        form.request_user = request.user
        return form

    def get_readonly_fields(self, request, obj=None) -> tuple:
        fields = super().get_readonly_fields(request, obj)
        if (
            obj is not None
            and GroupChoices.admins in request.user.groups.all().values_list("name", flat=True)
        ):
            fields += ("title", "description", "category", "author",)

        if (
            GroupChoices.authors in request.user.groups.all().values_list("name", flat=True)
        ):
            fields += ("status",)

        return fields

    def has_add_permission(self, request) -> bool:
        has_permission = super().has_add_permission(request)
        if (
            GroupChoices.admins in request.user.groups.all().values_list("name", flat=True)
        ):
            has_permission = False
        return has_permission

from django.contrib import admin

from users.models import Author, AdminProfile


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user")
    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user")
    search_fields = (
        "first_name",
        "last_name",
    )

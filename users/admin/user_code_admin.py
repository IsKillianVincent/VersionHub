from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_code import UserCode

@admin.register(UserCode)
class UserCodeAdmin(ImportExportModelAdmin):
    list_display = ("id", "email", "code", "is_used", "created_at", "expires_at")
    search_fields = ("email", "code")
    list_filter = ("is_used", "created_at", "expires_at")
    ordering = ("-created_at",)
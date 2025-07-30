from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models import UserSettings

@admin.register(UserSettings)
class UserSettingsAdmin(ImportExportModelAdmin):
    list_display = ("user", "language", "timezone", "session_duration")
    search_fields = ("user__email",)
    list_filter = ("language", "timezone")
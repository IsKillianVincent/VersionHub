from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models import UserSetting

@admin.register(UserSetting)
class UserSettingAdmin(ImportExportModelAdmin):
    list_display = ("id", "user", "language", "timezone", "session_duration")
    search_fields = ("user__email",)
    list_filter = ("language", "timezone")
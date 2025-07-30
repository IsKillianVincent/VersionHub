from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_log import UserLog

@admin.register(UserLog)
class UserLogAdmin(ImportExportModelAdmin):
    list_display = ("user", "action", "ip", "timestamp")
    search_fields = ("user__email", "ip", "action")
    list_filter = ("action",)
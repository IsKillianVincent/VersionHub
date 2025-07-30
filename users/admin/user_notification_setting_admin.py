from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_notification_setting import UserNotificationSetting

@admin.register(UserNotificationSetting)
class UserNotificationSettingAdmin(ImportExportModelAdmin):
    list_display = ("user", "allow_email", "allow_push")
    search_fields = ("user__email",)
    list_filter = ("allow_email", "allow_push")
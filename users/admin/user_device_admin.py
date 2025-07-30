from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_device import UserDevice

@admin.register(UserDevice)
class UserDeviceAdmin(ImportExportModelAdmin):
    list_display = ("user", "device_name", "device_type", "last_seen")
    search_fields = ("user__email", "device_name", "device_type")
    list_filter = ("device_type",)
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models import User
from users.models import UserSettings

class UserSettingsInline(admin.StackedInline):
    model = UserSettings
    can_delete = False

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("id", "email", "user_name", "full_name", "is_active", "is_staff", "date_joined")
    search_fields = ("email", "user_name", "full_name")
    list_filter = ("is_active", "is_staff")
    inlines = [UserSettingsInline]
    ordering = ("-date_joined",)
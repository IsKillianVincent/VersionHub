from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_profile import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ("user", "phone")
    search_fields = ("user__email", "phone")
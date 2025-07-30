from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.user_agreement import UserAgreement

@admin.register(UserAgreement)
class UserAgreementAdmin(ImportExportModelAdmin):
    list_display = ("user", "version", "accepted_at")
    search_fields = ("user__email", "version")
    list_filter = ("version",)
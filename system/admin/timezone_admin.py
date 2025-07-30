from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from system.models import Timezone

@admin.register(Timezone)
class TimezoneAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "offset", "code")
    search_fields = ("name", "offset" , "code")
    ordering = ("offset",)
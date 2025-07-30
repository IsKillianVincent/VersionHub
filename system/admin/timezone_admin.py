from django.contrib import admin
from import_export.admin import ExportMixin
from system.models import Timezone

@admin.register(Timezone)
class TimezoneAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("id", "name", "offset")
    search_fields = ("name", "offset")
    ordering = ("offset",)

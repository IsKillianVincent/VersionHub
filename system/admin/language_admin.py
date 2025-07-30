from django.contrib import admin
from import_export.admin import ExportMixin
from system.models import Language

@admin.register(Language)
class LanguageAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")
    ordering = ("code",)

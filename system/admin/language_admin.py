from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from system.models import Language

@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")
    ordering = ("code",)
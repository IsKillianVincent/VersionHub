from django.db import models
from system.managers.language_manager import LanguageManager
import uuid

class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    objects = LanguageManager()

    class Meta:
        ordering = ["code"]
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return f"{self.name} ({self.code})"
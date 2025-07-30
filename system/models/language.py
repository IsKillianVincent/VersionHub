from django.db import models
from system.managers.language_manager import LanguageManager

class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    objects = LanguageManager()

    def __str__(self):
        return f"{self.name} ({self.code})"
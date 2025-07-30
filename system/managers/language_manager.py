from django.db import models
from system.querysets.language_queryset import LanguageQuerySet

class LanguageManager(models.Manager):
    def get_queryset(self):
        return LanguageQuerySet(self.model, using=self._db)

    def ordered(self):
        return self.get_queryset().ordered()
from django.db import models
from system.querysets.timezone_queryset import TimezoneQuerySet

class TimezoneManager(models.Manager):
    def get_queryset(self):
        return TimezoneQuerySet(self.model, using=self._db)

    def ordered(self):
        return self.get_queryset().ordered()
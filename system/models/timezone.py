import uuid
from django.db import models
from system.managers.timezone_manager import TimezoneManager

class Timezone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    offset = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    objects = TimezoneManager()

    class Meta:
        ordering = ["offset"]
        verbose_name = "Timezone"
        verbose_name_plural = "Timezones"

    def __str__(self):
        return f"{self.name} (UTC{self.offset})" if self.offset else self.name
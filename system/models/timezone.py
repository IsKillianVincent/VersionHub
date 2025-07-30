from django.db import models
from system.managers.timezone_manager import TimezoneManager

class Timezone(models.Model):
    name = models.CharField(max_length=100)
    offset = models.CharField(max_length=10, blank=True, null=True)

    objects = TimezoneManager()

    def __str__(self):
        return self.name

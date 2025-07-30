from django.db import models
from users.querysets.user_device_queryset import UserDeviceQuerySet

class UserDeviceManager(models.Manager):
    def get_queryset(self):
        return UserDeviceQuerySet(self.model, using=self._db)

    def recent(self):
        return self.get_queryset().recent()
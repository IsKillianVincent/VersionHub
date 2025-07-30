from django.db import models
from users.querysets.user_log_queryset import UserLogQuerySet

class UserLogManager(models.Manager):
    def get_queryset(self):
        return UserLogQuerySet(self.model, using=self._db)

    def recent(self):
        return self.get_queryset().recent()
from django.db import models
from users.querysets.user_profile_queryset import UserProfileQuerySet

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return UserProfileQuerySet(self.model, using=self._db)

    def with_phone(self):
        return self.get_queryset().with_phone()
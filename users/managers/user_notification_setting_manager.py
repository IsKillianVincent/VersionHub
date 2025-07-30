from django.db import models
from users.querysets.user_notification_setting_queryset import UserNotificationSettingQuerySet

class UserNotificationSettingManager(models.Manager):
    def get_queryset(self):
        return UserNotificationSettingQuerySet(self.model, using=self._db)
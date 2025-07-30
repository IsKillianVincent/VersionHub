from django.db import models
from users.models import User
from users.managers.user_notification_setting_manager import UserNotificationSettingManager

class UserNotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_settings")
    allow_email = models.BooleanField(default=True)
    allow_push = models.BooleanField(default=False)

    objects = UserNotificationSettingManager()

    class Meta:
        verbose_name = "Notification Setting"
        verbose_name_plural = "Notification Settings"

    def __str__(self):
        return f"Notif Settings for {self.user.email}"
from django.db import models

class UserNotificationSettingQuerySet(models.QuerySet):
    def enabled_email(self):
        return self.filter(allow_email=True)

    def enabled_push(self):
        return self.filter(allow_push=True)
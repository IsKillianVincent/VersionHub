from django.db import models

class UserDeviceQuerySet(models.QuerySet):
    def recent(self):
        return self.order_by('-last_seen')
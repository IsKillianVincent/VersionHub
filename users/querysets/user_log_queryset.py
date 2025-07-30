from django.db import models

class UserLogQuerySet(models.QuerySet):
    def recent(self):
        return self.order_by('-timestamp')
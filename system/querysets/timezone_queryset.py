from django.db import models

class TimezoneQuerySet(models.QuerySet):
    def ordered(self):
        return self.order_by('offset')
from django.db import models

class UserProfileQuerySet(models.QuerySet):
    def with_phone(self):
        return self.exclude(phone__exact='')
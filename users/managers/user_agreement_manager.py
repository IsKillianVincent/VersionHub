from django.db import models

class UserAgreementManager(models.Manager):
    def latest_for_user(self, user):
        return self.get_queryset().latest_for_user(user)
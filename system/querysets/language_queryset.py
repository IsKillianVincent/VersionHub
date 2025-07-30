from django.db import models

class LanguageQuerySet(models.QuerySet):
    def ordered(self):
        return self.order_by('code')
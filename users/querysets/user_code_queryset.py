from django.utils import timezone
from django.db.models import QuerySet

class UserCodeQuerySet(QuerySet):
    def valid(self):
        return self.filter(is_used=False, expires_at__gt=timezone.now())

    def expired(self):
        return self.filter(expires_at__lte=timezone.now())
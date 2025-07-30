from django.db import models
from django.utils import timezone
from users.querysets.user_code_queryset import UserCodeQuerySet
from users.managers.user_code_manager import UserCodeManager
import uuid

class UserCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    objects = UserCodeManager.from_queryset(UserCodeQuerySet)()

    def is_valid(self):
        return not self.is_used and timezone.now() < self.expires_at

    def __str__(self):
        return f"Code for {self.email}"
import uuid
from django.db import models
from django.utils import timezone
from users.models import User
from users.querysets.user_agreement_queryset import UserAgreementQuerySet
from users.managers.user_agreement_manager import UserAgreementManager

class UserAgreement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agreements")
    version = models.CharField(max_length=20)
    accepted_at = models.DateTimeField(default=timezone.now)

    objects = UserAgreementManager.from_queryset(UserAgreementQuerySet)()

    class Meta:
        unique_together = ("user", "version")
        ordering = ['-accepted_at']

    def __str__(self):
        return f"{self.user.email} accepted v{self.version}"
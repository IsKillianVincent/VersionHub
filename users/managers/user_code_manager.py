import random
from datetime import timedelta
from django.utils import timezone
from django.db import models

class UserCodeManager(models.Manager):
    def create_code(self, email):
        code = ''.join(random.choices('0123456789', k=6))
        now = timezone.now()
        return self.create(
            email=email,
            code=code,
            created_at=now,
            expires_at=now + timedelta(minutes=10)
        )

    def verify_code(self, email, code):
        try:
            code_obj = self.get_queryset().valid().get(email=email, code=code)
            code_obj.is_used = True
            code_obj.save()
            return True
        except self.model.DoesNotExist:
            return False
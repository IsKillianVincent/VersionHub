from django.contrib.auth.models import BaseUserManager
from users.querysets.user_queryset import UserQuerySet

class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def staff(self):
        return self.get_queryset().staff()

    def with_settings(self):
        return self.get_queryset().with_settings()

    def search(self, query):
        return self.get_queryset().search(query)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
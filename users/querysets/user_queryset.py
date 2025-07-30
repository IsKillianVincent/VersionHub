from django.db import models

class UserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def staff(self):
        return self.filter(is_staff=True)

    def with_settings(self):
        return self.select_related("settings")

    def search(self, query):
        return self.filter(
            models.Q(email__icontains=query) |
            models.Q(user_name__icontains=query) |
            models.Q(full_name__icontains=query)
        )
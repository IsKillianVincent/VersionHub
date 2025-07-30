from django.db import models
from users.models import User
import uuid
from users.managers.user_profile_manager import UserProfileManager

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    objects = UserProfileManager()

    def __str__(self):
        return f"Profile of {self.user.email}"
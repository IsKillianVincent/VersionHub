from django.db import models
from system.models import Language, Timezone
from users.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.SET_NULL)
    timezone = models.ForeignKey(Timezone, null=True, blank=True, on_delete=models.SET_NULL)
    session_duration = models.PositiveIntegerField(default=604800)
    date_format = models.CharField(max_length=20, default='YYYY-MM-DD')
    time_format = models.CharField(max_length=20, default='HH:mm')
    display_mode = models.CharField(max_length=20, default='light')
    extra_preferences = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Settings for {self.user.email}"
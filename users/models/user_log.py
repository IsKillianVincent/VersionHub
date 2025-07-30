from django.db import models
from users.models import User
from users.managers.user_log_manager import UserLogManager

class UserLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserLogManager()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "User Log"
        verbose_name_plural = "User Logs"

    def __str__(self):
        return f"{self.user.email} - {self.action} @ {self.timestamp}"
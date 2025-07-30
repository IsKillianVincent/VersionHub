from django.db import models
from users.models import User
from users.managers.user_device_manager import UserDeviceManager
import uuid

class UserDevice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="devices")
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    last_seen = models.DateTimeField(auto_now=True)

    objects = UserDeviceManager()

    class Meta:
        ordering = ['-last_seen']
        verbose_name = "User Device"
        verbose_name_plural = "User Devices"

    def __str__(self):
        return f"{self.device_name} ({self.device_type}) for {self.user.email}"
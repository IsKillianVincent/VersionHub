from rest_framework import serializers
from users.models.user_device import UserDevice

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['id', 'user', 'device_name', 'device_type', 'last_login_ip', 'last_seen']
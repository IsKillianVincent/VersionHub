from rest_framework import serializers
from users.models.user_log import UserLog

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ['id', 'user', 'action', 'ip', 'timestamp']
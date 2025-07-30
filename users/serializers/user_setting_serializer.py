from rest_framework import serializers
from users.models import UserSetting

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = [
            'id', 'user', 'language', 'timezone',
            'session_duration', 'date_format',
            'time_format', 'display_mode', 'extra_preferences'
        ]
        read_only_fields = ['id', 'user']
from rest_framework import serializers
from users.models import UserSettings

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            'id', 'user', 'language', 'timezone',
            'session_duration', 'date_format',
            'time_format', 'display_mode', 'extra_preferences'
        ]
        read_only_fields = ['id', 'user']
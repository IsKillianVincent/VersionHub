from rest_framework import serializers
from users.models.user_notification_setting import UserNotificationSetting

class UserNotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationSetting
        fields = ['id', 'user', 'allow_email', 'allow_push']
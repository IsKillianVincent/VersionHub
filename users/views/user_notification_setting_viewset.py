from rest_framework import viewsets
from users.models.user_notification_setting import UserNotificationSetting
from users.serializers.user_notification_setting_serializer import UserNotificationSettingSerializer

class UserNotificationSettingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserNotificationSetting.objects.select_related("user").all()
    serializer_class = UserNotificationSettingSerializer
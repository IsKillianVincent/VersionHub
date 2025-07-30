from rest_framework import viewsets
from users.models import UserSetting
from users.serializers import UserSettingSerializer

class UserSettingViewSet(viewsets.ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
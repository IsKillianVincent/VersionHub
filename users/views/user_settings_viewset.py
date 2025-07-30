from rest_framework import viewsets
from users.models import UserSettings
from users.serializers import UserSettingsSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
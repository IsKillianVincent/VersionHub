from rest_framework import viewsets
from users.models.user_device import UserDevice
from users.serializers.user_device_serializer import UserDeviceSerializer

class UserDeviceViewSet(viewsets.ModelViewSet):
    queryset = UserDevice.objects.select_related("user").recent()
    serializer_class = UserDeviceSerializer
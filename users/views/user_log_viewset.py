from rest_framework import viewsets
from users.models.user_log import UserLog
from users.serializers.user_log_serializer import UserLogSerializer

class UserLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserLog.objects.select_related("user").recent()
    serializer_class = UserLogSerializer
from rest_framework import viewsets
from users.models.user_code import UserCode
from users.serializers.user_code_serializer import UserCodeSerializer

class UserCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserCode.objects.all()
    serializer_class = UserCodeSerializer
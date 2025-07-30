from rest_framework import viewsets
from users.models.user_profile import UserProfile
from users.serializers.user_profile_serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related("user").all()
    serializer_class = UserProfileSerializer
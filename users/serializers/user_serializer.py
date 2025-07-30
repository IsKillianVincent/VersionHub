from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'user_name', 'full_name', 'is_active', 'is_staff', 'date_joined']
        read_only_fields = ['id', 'date_joined', 'is_staff']
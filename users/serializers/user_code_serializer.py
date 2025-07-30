from rest_framework import serializers
from users.models.user_code import UserCode

class UserCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCode
        fields = ['id', 'email', 'code', 'created_at', 'expires_at', 'is_used']
        read_only_fields = ['created_at', 'expires_at', 'is_used']
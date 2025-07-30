from rest_framework import serializers
from users.models.user_agreement import UserAgreement

class UserAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAgreement
        fields = ['id', 'user', 'version', 'accepted_at']
        read_only_fields = ['accepted_at']
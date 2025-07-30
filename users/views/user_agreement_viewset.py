from rest_framework import viewsets
from users.models.user_agreement import UserAgreement
from users.serializers.user_agreement_serializer import UserAgreementSerializer

class UserAgreementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserAgreement.objects.all()
    serializer_class = UserAgreementSerializer
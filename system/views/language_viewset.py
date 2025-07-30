from rest_framework import viewsets
from system.models import Language
from system.serializers import LanguageSerializer

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.ordered()
    serializer_class = LanguageSerializer
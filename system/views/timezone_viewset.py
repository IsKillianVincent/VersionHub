from rest_framework import viewsets
from system.models import Timezone
from system.serializers import TimezoneSerializer

class TimezoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Timezone.objects.ordered()
    serializer_class = TimezoneSerializer
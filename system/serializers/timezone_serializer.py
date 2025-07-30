from rest_framework import serializers
from system.models import Timezone

class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['id', 'name', 'offset', 'code']
from rest_framework import serializers

from .models import Reading, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name')


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'sensor', 'read_at', 'reading')

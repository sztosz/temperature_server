from rest_framework import viewsets
from .models import Reading, Sensor
from .serializers import ReadingSerializer, SensorSerializer
from .pagination import ResultsSetPagination


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        queryset = Reading.objects.all()
        sensor = self.kwargs.get('sensor', None)
        if sensor:
            queryset = queryset.filter(sensor=sensor)
        return queryset

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorView(ListCreateAPIView):  # отображение всех датчиков, создание одного датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorInfoView(RetrieveAPIView):  # вывод данных по одному датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdateView(RetrieveUpdateAPIView):  # обновление данных по 1 датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):  # запись измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

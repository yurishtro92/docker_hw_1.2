from django.contrib import admin
from django.urls import path
from measurement.views import SensorView, MeasurementView, SensorInfoView, SensorUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>', SensorInfoView.as_view()),
    path('sensors/update/<pk>', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]

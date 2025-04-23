from django.urls import path
from .views import SensorDataView, HistorialUsuarioView

urlpatterns = [
    path('api/sensor_data/', SensorDataView.as_view()),
    path('api/historial/<int:usuario_id>/', HistorialUsuarioView.as_view()),
]

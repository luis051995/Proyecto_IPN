from django.urls import path
from .views import RegisterUserView, SensorDataView, HistorialUsuarioView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('sensor_data/', SensorDataView.as_view(), name='sensor_data'),
    path('historial/<int:usuario_id>/', HistorialUsuarioView.as_view(), name='historial_usuario'),
]

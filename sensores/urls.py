from django.urls import path
from .views import RegisterUserView, SensorDataView, HistorialUsuarioView, get_historial, LoginView, RegistroMedicoView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('sensor_data/', SensorDataView.as_view(), name='sensor_data'),
    path('historial/<int:usuario_id>/', HistorialUsuarioView.as_view(), name='historial_usuario'),
    path('get_historial/<int:usuario_id>/', get_historial, name='get_historial'),
    path('login/', LoginView.as_view(), name='login'),
    path('registro/', RegistroMedicoView.as_view(), name='registro_medico'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

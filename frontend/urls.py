from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.registro, name='register_user'),
    path('historial/<int:usuario_id>/', views.historial_usuario, name='historial'),
]

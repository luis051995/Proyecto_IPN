from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Usuario, Historial
from .ml.predict import predecir_diabetes

class RegisterUserView(APIView):
    """
    Registra un nuevo usuario con 'usuario' y 'contrasena'.
    """
    def post(self, request):
        nombre = request.data.get('usuario')
        contrasena = request.data.get('contrasena')

        if not nombre or not contrasena:
            return Response(
                {"error": "Los campos 'usuario' y 'contrasena' son obligatorios"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Usuario.objects.filter(nombre=nombre).exists():
            return Response(
                {"error": "El usuario ya existe"},
                status=status.HTTP_400_BAD_REQUEST
            )

        u = Usuario.objects.create(nombre=nombre, contrasena=contrasena)
        return Response(
            {"mensaje": "Usuario registrado con éxito", "usuario_id": u.id},
            status=status.HTTP_201_CREATED
        )


class SensorDataView(APIView):
    """
    Recibe:
      - acetona: número
      - usuario: nombre
      - contrasena: contraseña
    Sólo guarda datos si las credenciales existen en Usuario.
    """
    def post(self, request):
        # 1) Comprueba campos obligatorios
        faltantes = [f for f in ('acetona','usuario','contrasena') if request.data.get(f) is None]
        if faltantes:
            return Response(
                {"error": f"Faltan campos: {', '.join(faltantes)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2) Convierte acetona
        try:
            acetona = float(request.data['acetona'])
        except (ValueError, TypeError):
            return Response(
                {"error": "El campo 'acetona' debe ser un número"},
                status=status.HTTP_400_BAD_REQUEST
            )

        nombre = request.data['usuario']
        pwd    = request.data['contrasena']

        # 3) Valida usuario
        try:
            usuario = get_object_or_404(Usuario, nombre=nombre, contrasena=pwd)
        except:
            return Response(
                {"error": "Usuario o contraseña inválidos"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 4) Predicción
        try:
            resultado = predecir_diabetes(acetona)
        except Exception as e:
            return Response(
                {"error": f"Error en predicción: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # 5) Guardar historial
        Historial.objects.create(usuario=usuario, acetona=acetona, resultado=resultado)

        # 6) Retornar diagnóstico
        return Response(
            {"mensaje": "Datos recibidos", "resultado": resultado},
            status=status.HTTP_201_CREATED
        )


class HistorialUsuarioView(APIView):
    """
    GET /api/historial/<usuario_id>/
    Devuelve lista de registros con acetona, resultado y fecha.
    """
    def get(self, request, usuario_id):
        registros = Historial.objects.filter(usuario_id=usuario_id).order_by('-fecha')
        data = [
            {"acetona": r.acetona, "resultado": r.resultado, "fecha": r.fecha}
            for r in registros
        ]
        return Response(data, status=status.HTTP_200_OK)

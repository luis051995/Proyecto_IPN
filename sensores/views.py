from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Historial
from django.shortcuts import get_object_or_404
from .ml.predict import predecir_diabetes

class SensorDataView(APIView):
    def post(self, request):
        try:
            acetona = float(request.data.get('acetona'))
            nombre_usuario = request.data.get('usuario')
            contrasena = request.data.get('contrasena')

            usuario = get_object_or_404(Usuario, nombre=nombre_usuario, contrasena=contrasena)
            resultado = predecir_diabetes(acetona)

            Historial.objects.create(
                usuario=usuario,
                acetona=acetona,
                resultado=resultado
            )

            return Response({
                "mensaje": "Datos recibidos",
                "resultado": resultado
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class HistorialUsuarioView(APIView):
    def get(self, request, usuario_id):
        historiales = Historial.objects.filter(usuario_id=usuario_id).order_by('-fecha')
        data = [
            {
                "acetona": h.acetona,
                "resultado": h.resultado,
                "fecha": h.fecha
            } for h in historiales
        ]
        return Response(data)

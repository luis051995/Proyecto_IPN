from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acetona = models.FloatField()
    resultado = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

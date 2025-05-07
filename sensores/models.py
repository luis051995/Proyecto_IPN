from django.db import models
from django.contrib.auth.models import AbstractUser



class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    peso = models.FloatField(help_text="Peso en kilogramos", default=70.0)  # <-- nuevo
    altura = models.FloatField(help_text="Altura en metros", default=1.70)  # <-- nuevo
    antecedentes = models.TextField(blank=True, help_text="Antecedentes médicos (opcional)")



class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acetona = models.FloatField()
    resultado = models.CharField(max_length=20)  # 'Diabético' o 'No diabético'
    fecha = models.DateTimeField(auto_now_add=True)
    
class Medico(AbstractUser):
    is_medico = models.BooleanField(default=True)


    

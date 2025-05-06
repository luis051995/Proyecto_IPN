from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, default=18)
    sexo = models.CharField(blank=True, max_length=10)  # Ejemplo: 'Masculino', 'Femenino', etc.
    peso = models.FloatField(blank=True, help_text="Peso en kilogramos",default=65)
    altura = models.FloatField(blank=True, help_text="Altura en metros",default=1.7)
    antecedentes = models.TextField(blank=True, help_text="Antecedentes médicos (opcional)")

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    RESULTADO_CHOICES = [
        ('Diabético', 'Diabético'),
        ('No diabético', 'No diabético'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acetona = models.FloatField()
    resultado = models.CharField(max_length=20)  # 'Diabético' o 'No diabético'
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.usuario.nombre} - {self.fecha}"
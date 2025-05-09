from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, contrasena=None, **extra_fields):
        if not nombre:
            raise ValueError('El nombre de usuario es obligatorio')
        
        user = self.model(
            nombre=nombre,
            **extra_fields
        )
        user.set_password(contrasena)
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser):
    SEXO_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=128,default='')
    edad = models.IntegerField(null=True, default=18)
    sexo = models.CharField(blank=True, max_length=10)  # Ejemplo: 'Masculino', 'Femenino', etc.
    peso = models.FloatField(blank=True, help_text="Peso en kilogramos",default=65)
    altura = models.FloatField(blank=True, help_text="Altura en metros",default=1.7)
    antecedentes = models.TextField(blank=True, help_text="Antecedentes médicos (opcional)")

# Campos requeridos para el modelo de usuario personalizado
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'nombre'

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

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
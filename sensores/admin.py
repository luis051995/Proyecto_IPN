from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Historial, Medico

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'sexo', 'peso', 'altura')
    search_fields = ('nombre', 'sexo', 'antecedentes')
    list_filter = ('sexo',)

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acetona', 'resultado', 'fecha')
    list_filter = ('resultado', 'fecha')
    search_fields = ('usuario__nombre',)

@admin.register(Medico)
class MedicoAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_medico', 'is_staff')
    list_filter = ('is_medico', 'is_staff')
    search_fields = ('username', 'email')



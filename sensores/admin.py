from django.contrib import admin
from .models import Usuario, Historial

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



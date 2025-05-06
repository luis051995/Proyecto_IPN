from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from sensores.models import Usuario, Historial
import plotly.express as px
from plotly.offline import plot
import pandas as pd
from django.utils.timezone import localtime

def registro(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def historial_usuario(request, usuario_id):
    # Verificar que el usuario existe
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    # Obtener historial ordenado por fecha
    historial = Historial.objects.filter(usuario=usuario).order_by('fecha')
    
    # Crear lista de diccionarios con los datos
    datos = []
    for h in historial:
        datos.append({
            'Fecha': localtime(h.fecha).strftime('%Y-%m-%d %H:%M'),  # Formatear fecha
            'Acetona': float(h.acetona),
            'Resultado': h.resultado
        })
    
    # Verificar si hay datos
    if not datos:
        return render(request, 'historial.html', {
            'mensaje': 'No hay datos de historial disponibles',
            'usuario_id': usuario_id
        })
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    try:
        # Gráfica de línea para acetona
        fig_line = px.line(
            data_frame=df,
            x='Fecha',
            y='Acetona',
            title=f'Historial de Acetona - {usuario.nombre}',
            labels={'Acetona': 'Nivel de Acetona', 'Fecha': 'Fecha de Medición'}
        )
        plot_div_line = plot(fig_line, output_type='div', include_plotlyjs=False)
        
        # Gráfica de barras para resultados
        fig_bar = px.bar(
            data_frame=df,
            x='Fecha',
            y='Acetona',
            color='Resultado',
            title='Resultados por Fecha',
            color_discrete_map={'Diabético': 'red', 'No diabético': 'green'}
        )
        plot_div_bar = plot(fig_bar, output_type='div', include_plotlyjs=False)
        
    except Exception as e:
        return render(request, 'historial.html', {
            'error': f'Error al generar gráficas: {str(e)}',
            'usuario_id': usuario_id
        })
    
    return render(request, 'historial.html', {
        'plot_div_line': plot_div_line,
        'plot_div_bar': plot_div_bar,
        'usuario_id': usuario_id,
        'usuario_nombre': usuario.nombre
    })
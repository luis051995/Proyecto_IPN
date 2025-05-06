# sensores/management/commands/import_diabetes_data.py
import csv
import codecs
from django.core.management.base import BaseCommand
from sensores.models import Usuario, Historial
from django.utils import timezone

class Command(BaseCommand):
    help = 'Importa datos de diabetes desde un CSV'

    def handle(self, *args, **options):
        csv_path = 'dataset/diabetes_database.csv'#'sample.csv'  # Ruta a tu archivo CSV

        with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
              # Leer el CSV considerando que la primera fila es el encabezado
            reader = csv.DictReader(csv_file, skipinitialspace=True)
            
            # Verificar que las columnas requeridas existan
            required_columns = ['Edad', 'Sexo', 'Peso', 'Altura', 'Antecedentes', 'Acetona', 'Salida']
            if not all(col in reader.fieldnames for col in required_columns):
                missing = set(required_columns) - set(reader.fieldnames)
                raise ValueError(f"Columnas faltantes en el CSV: {missing}. Columnas encontradas: {reader.fieldnames}")
            
            for row_num, row in enumerate(reader, start=2):  # start=2 porque la fila 1 es el encabezado
                try:
                    # Limpiar espacios en los valores
                    cleaned_row = {k: v.strip() for k, v in row.items()}
                    
                    # Crear o actualizar usuario
                    usuario, created = Usuario.objects.get_or_create(
                        nombre=f"user_{cleaned_row['Edad']}_{cleaned_row['Sexo']}_{cleaned_row['Peso']}",
                        defaults={
                            'edad': int(cleaned_row['Edad']),
                            'sexo': cleaned_row['Sexo'],
                            'peso': float(cleaned_row['Peso']),
                            'altura': float(cleaned_row['Altura']),
                            'antecedentes': cleaned_row['Antecedentes'],
                            'contrasena': 'defaultpassword'
                        }
                    )

                
                    # Crear registro histórico
                    Historial.objects.create(
                        usuario=usuario,
                        acetona=float(cleaned_row['Acetona']),
                        resultado='Diabético' if cleaned_row['Salida'] == '1' else 'No diabético',
                        fecha=timezone.now()
                    )
                    
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f"Error en fila {row_num} ({row}): {str(e)}"
                    ))
                    continue

        self.stdout.write(self.style.SUCCESS('Datos importados exitosamente'))

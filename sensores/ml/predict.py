import joblib
import numpy as np
import os

modelo_path = os.path.join(os.path.dirname(__file__), 'modelo_entrenado.pkl')
modelo = joblib.load(modelo_path)

# Recibe lista de características [Edad, Sexo (0/1), Peso, Altura, Antecedentes (0/1), Acetona]
def predecir_diabetes(entrada_lista):
    entrada = np.array([entrada_lista])
    pred = modelo.predict(entrada)[0]
    return "Diabético" if pred == 1 else "No diabético"

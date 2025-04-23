import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import VotingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import joblib

# Cargar CSV
df = pd.read_csv("dataset/diabetes_database.csv")

# Codificar variables categóricas
label_sexo = LabelEncoder()
label_antecedentes = LabelEncoder()

df['Sexo'] = label_sexo.fit_transform(df['Sexo'])  # Hombre = 1, Mujer = 0
df['Antecedentes'] = label_antecedentes.fit_transform(df['Antecedentes'])  # Yes = 1, No = 0

# Separar características y etiquetas
X = df.drop("Salida", axis=1)  # Salida = etiqueta (0 = No diabético, 1 = Diabético)
y = df["Salida"]

# División de entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Modelos
svm = SVC(probability=True)
mlp = MLPClassifier(hidden_layer_sizes=(6, 6), max_iter=1000)

model = VotingClassifier(estimators=[
    ('svm', svm),
    ('mlp', mlp)
], voting='soft')

# Entrenar
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, 'sensores/ml/modelo_entrenado.pkl')

print("✅ Modelo entrenado y guardado correctamente.")

import joblib
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Cargar modelos
svm_model = joblib.load('svm_model.pkl')
bp_model = load_model('bp_model.h5')
scaler = joblib.load('scaler.pkl')

def predict_diabetes(acetona):
    x = np.array([[acetona]])  # puedes agregar más features si tienes
    x_scaled = scaler.transform(x)
    svm_pred = svm_model.predict(x_scaled)
    combined_input = np.column_stack((x_scaled, svm_pred))
    y_pred = bp_model.predict(combined_input)[0][0]
    return 'Diabetes' if y_pred > 0.5 else 'No Diabetes'

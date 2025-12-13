import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_model(X_train, y_train, model_type='linear'):
    """
    Entrena un modelo especificado.
    Opciones: 'linear', 'random_forest'
    """
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'random_forest':
        # n_estimators=100 es un buen estándar, random_state para reproducibilidad
        model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    else:
        raise ValueError("Modelo no soportado. Usa 'linear' o 'random_forest'")
    
    print(f"Entrenando modelo: {model_type}...")
    model.fit(X_train, y_train)
    return model
    

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
    

def evaluate_model(model, X_test, y_test, model_name="Modelo"):
    """
    Realiza predicciones y calcula métricas de error.
    """
    # Predicción
    y_pred = model.predict(X_test)
    
    # Métricas
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print(f"--- Resultados para {model_name} ---")
    print(f"MAE (Error Medio Absoluto): {mae:.4f}")
    print(f"RMSE (Error Cuadrático Medio): {rmse:.4f}")
    print(f"R2 Score (Coeficiente de Determinación): {r2:.4f}")
    print("-" * 30)
    
    return y_pred, {
        'mae': mae, 
        'rmse': rmse, 
        'r2': r2
    }

def plot_predictions(y_test, y_pred, title="Real vs Predicho"):
    """
    Grafica una porción de las predicciones para visualización.
    """
    plt.figure(figsize=(12, 6))
    # Graficamos solo los primeros 100 o 200 puntos para ver detalle
    limit = 150
    plt.plot(y_test.values[:limit], label='Real (Test)', color='blue', alpha=0.7)
    plt.plot(y_pred[:limit], label='Predicción', color='red', alpha=0.7, linestyle='--')
    plt.title(title)
    plt.legend()
    plt.xlabel('Días (Muestra)')
    plt.ylabel('Consumo de Energía (Escalado)')
    plt.grid(True)
    plt.show()

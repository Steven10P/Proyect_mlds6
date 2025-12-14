import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(y_true, y_pred):
    """
    Calcula las métricas técnicas del modelo.
    Retorna un diccionario.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    return {
        'mae': mae, 
        'rmse': rmse, 
        'r2': r2
    }

def print_metrics(metrics_dict, model_name="Modelo"):
    """
    Imprime las métricas con formato limpio.
    """
    print(f"\n📊 --- Resultados para {model_name} ---")
    print(f"   MAE  (Error Absoluto Medio): {metrics_dict['mae']:.4f}")
    print(f"   RMSE (Raíz Error Cuadrático): {metrics_dict['rmse']:.4f}")
    print(f"   R2   (Coeficiente Determinación): {metrics_dict['r2']:.4f}")
    print("-" * 40)

def plot_real_vs_predicted(y_true, y_pred, limit=150, title="Real vs Predicho"):
    """
    Grafica una serie de tiempo comparativa (Zoom a los primeros N puntos).
    """
    plt.figure(figsize=(14, 6))
    
    # Asegurar que y_true sea array para slicing seguro
    if isinstance(y_true, (pd.Series, pd.DataFrame)):
        y_true = y_true.values.flatten()
        
    # Graficar límite
    plt.plot(y_true[:limit], label='Real (Test)', color='navy', alpha=0.8, linewidth=2)
    plt.plot(y_pred[:limit], label='Predicción', color='crimson', alpha=0.8, linestyle='--', linewidth=2)
    
    plt.title(title, fontsize=16)
    plt.legend()
    plt.xlabel('Muestra (Días/Registros)')
    plt.ylabel('Valor Target')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_residuals(y_true, y_pred):
    """
    Grafica la distribución de los errores (Residuales).
    Vital para ver si el modelo tiene sesgos (bias).
    """
    if isinstance(y_true, (pd.Series, pd.DataFrame)):
        y_true = y_true.values.flatten()
        
    residuals = y_true - y_pred
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: Scatter de Residuales vs Predicción
    sns.scatterplot(x=y_pred, y=residuals, ax=axes[0], alpha=0.5)
    axes[0].axhline(0, color='red', linestyle='--')
    axes[0].set_title('Residuales vs Predicción (Homocedasticidad)')
    axes[0].set_xlabel('Predicción')
    axes[0].set_ylabel('Residual (Real - Predicho)')
    
    # Gráfico 2: Histograma de errores
    sns.histplot(residuals, kde=True, ax=axes[1], color='purple')
    axes[1].set_title('Distribución de Errores (Normalidad)')
    axes[1].set_xlabel('Error')
    
    plt.tight_layout()
    plt.show()
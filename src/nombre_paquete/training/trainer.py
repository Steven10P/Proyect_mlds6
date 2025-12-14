import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor 
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def get_hyperparameter_grid(model_type):
    """
    Define los espacios de búsqueda para la optimización.
    """
    if model_type == 'random_forest':
        return {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10]
        }
    elif model_type == 'xgboost':
        return {
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.05, 0.1],
            'max_depth': [3, 5, 7],
            'subsample': [0.7, 0.9, 1.0],
            'colsample_bytree': [0.7, 0.9, 1.0]
        }
    return {}

def train_model(X_train, y_train, model_type='linear', tune_hyperparams=False):
    """
    Entrena un modelo. Si tune_hyperparams=True, realiza búsqueda aleatoria.
    """
    print(f" Entrenando modelo: {model_type} (Tuning: {tune_hyperparams})")
    
    # 1. Selección del Modelo Base
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'random_forest':
        model = RandomForestRegressor(random_state=42, n_jobs=-1)
    elif model_type == 'xgboost':
        model = XGBRegressor(random_state=42, n_jobs=-1)
    else:
        raise ValueError(f"Modelo '{model_type}' no soportado.")

    # 2. Búsqueda de Hiperparámetros (Solo para modelos complejos)
    if tune_hyperparams and model_type != 'linear':
        print(f" Iniciando RandomizedSearchCV para {model_type}...")
        param_grid = get_hyperparameter_grid(model_type)
        
        search = RandomizedSearchCV(
            estimator=model,
            param_distributions=param_grid,
            n_iter=10,      # Número de combinaciones a probar (bajo por velocidad)
            cv=3,           # Validación cruzada de 3 pliegues
            scoring='neg_mean_squared_error',
            verbose=1,
            random_state=42,
            n_jobs=-1
        )
        search.fit(X_train, y_train)
        print(f" Mejores params: {search.best_params_}")
        return search.best_estimator_
    
    # 3. Entrenamiento directo
    else:
        model.fit(X_train, y_train)
        return model

def evaluate_model(model, X_test, y_test):
    """
    Calcula métricas y retorna predicciones + diccionario de métricas.
    """
    predictions = model.predict(X_test)
    
    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "rmse": np.sqrt(mean_squared_error(y_test, predictions)),
        "r2": r2_score(y_test, predictions)
    }
    
    return metrics, predictions



def get_feature_importance(model, feature_names, model_type='linear'):
    """
    Extrae la importancia de las variables dependiendo del modelo.
    Retorna un DataFrame ordenado.
    """
    import pandas as pd
    import numpy as np
    
    importance_df = pd.DataFrame()
    importance_df['feature'] = feature_names
    
    try:
        # A. Para Regresión Lineal (Coeficientes)
        if model_type == 'linear':
            # Tomamos el valor absoluto para ver la magnitud del impacto
            importance_df['importance'] = model.coef_
            # Columna extra para saber si suma o resta
            importance_df['direction'] = np.where(model.coef_ > 0, 'Positivo', 'Negativo')
            importance_df['abs_importance'] = np.abs(model.coef_)
            
            # Ordenar por valor absoluto
            importance_df = importance_df.sort_values(by='abs_importance', ascending=False)
            
        # B. Para Árboles (Random Forest / XGBoost)
        elif model_type in ['random_forest', 'xgboost']:
            importance_df['importance'] = model.feature_importances_
            importance_df['abs_importance'] = model.feature_importances_ # En árboles siempre es positivo
            
            # Ordenar
            importance_df = importance_df.sort_values(by='importance', ascending=False)
            
        return importance_df

    except Exception as e:
        print(f" No se pudo extraer importancia para {model_type}: {e}")
        return None
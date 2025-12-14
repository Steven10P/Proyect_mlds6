import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Realiza la limpieza, ingeniería de características y encoding.
    """
    print(" Iniciando limpieza y feature engineering...")
    
    # 1. Copia de seguridad
    df_proc = df.copy()

    # 2. Manejo de Fechas y Ordenamiento
    if 'date' in df_proc.columns:
        if df_proc['date'].dtype == 'object':
            df_proc['date'] = pd.to_datetime(df_proc['date'])
        
        # Ordenar cronológicamente (VITAL para series de tiempo)
        df_proc = df_proc.sort_values(by=['country', 'date'])
    else:
        print("⚠️ Advertencia: No se encontró columna 'date'.")

    # 3. Limpieza (Rolling Mean para Urban Population)
    # Suaviza saltos irrealistas en la data
    if 'urban_population' in df_proc.columns and 'country' in df_proc.columns:
        df_proc['urban_population'] = df_proc.groupby('country')['urban_population']\
                                             .transform(lambda x: x.rolling(window=30, min_periods=1).mean())

    # 4. Ingeniería de Características (Feature Engineering)
    # Extraer componentes cíclicos
    df_proc['month'] = df_proc['date'].dt.month
    df_proc['day_of_week'] = df_proc['date'].dt.dayofweek
    df_proc['quarter'] = df_proc['date'].dt.quarter
    
    # 5. Codificación de Variables Categóricas (Encoding)
    # dtype=int asegura que sean 0 y 1 en lugar de True/False (mejor para Spark)
    print("Dummy encoding de la columna 'country'...")
    df_proc = pd.get_dummies(df_proc, columns=['country'], drop_first=True, dtype=int)

    # 6. Establecer índice
    df_proc = df_proc.set_index('date')
    
    print(f"✅ Preprocesamiento completado. Shape final: {df_proc.shape}")
    return df_proc

def split_and_scale(df, cutoff_date='2024-01-01'):
    """
    Divide en train/test cronológicamente y escala las variables numéricas.
    Retorna: train_scaled, test_scaled, scaler_object
    """
    print(f" Dividiendo datos con fecha de corte: {cutoff_date}")
    
    # 1. División Train / Test
    train = df[df.index < cutoff_date].copy()
    test = df[df.index >= cutoff_date].copy()
    
    if len(test) == 0:
        print(" CUIDADO: El set de Test está vacío. Revisa la fecha de corte.")

    # 2. Configurar el Scaler
    scaler = StandardScaler()

    # Identificar columnas a escalar (excluyendo las one-hot encoded)
    # Excluimos las que tienen "country_" y también las de fecha (month, day, etc si no quieres escalarlas)
    cols_to_scale = [c for c in train.columns if 'country_' not in c and c not in ['month', 'day_of_week', 'quarter']]
    
    print(f" Escalando {len(cols_to_scale)} variables numéricas...")

    # 3. Escalado
    # Ajustar (fit) SOLO con train para evitar Data Leakage
    train_scaled = train.copy()
    test_scaled = test.copy()

    if cols_to_scale:
        train_scaled[cols_to_scale] = scaler.fit_transform(train[cols_to_scale])
        test_scaled[cols_to_scale] = scaler.transform(test[cols_to_scale])
    
    return train_scaled, test_scaled, scaler
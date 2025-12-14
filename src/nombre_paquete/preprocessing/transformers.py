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
        print(" Advertencia: No se encontró columna 'date'.")

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
    
    print(f" Preprocesamiento completado. Shape final: {df_proc.shape}")
    return df_proc
# En transformers.py

def split_and_scale(df, target_col='energy_consumption', cutoff_date='2024-01-01'):
    """
    Divide en train/test y escala SOLO las variables predictoras (X),
    dejando el target (y) en sus unidades originales.
    """
    print(f" Dividiendo datos. Target: {target_col}")
    
    # 1. División Train / Test
    train = df[df.index < cutoff_date].copy()
    test = df[df.index >= cutoff_date].copy()

    # 2. Configurar el Scaler
    scaler = StandardScaler()

    # IDENTIFICAR COLUMNAS A ESCALAR (X)
    # Excluímos:
    # - El target (¡IMPORTANTE!)
    # - Las categóricas encoded (country_...)
    # - Las de fecha (month, day...) si no quieres escalarlas
    cols_to_exclude = [target_col, 'month', 'day_of_week', 'quarter']
    
    # Seleccionamos solo las columnas que NO están en la lista de exclusión y NO empiezan con 'country_'
    cols_to_scale = [c for c in train.columns 
                     if c not in cols_to_exclude 
                     and not c.startswith('country_')]

    print(f" Escalando {len(cols_to_scale)} features (Input)...")
    print(f"  Variables a escalar: {cols_to_scale}")

    # 3. Escalado (SOLO A LAS FEATURES)
    # Ajustar (fit) solo con train
    scaler.fit(train[cols_to_scale])

    # Transformar train y test
    train[cols_to_scale] = scaler.transform(train[cols_to_scale])
    test[cols_to_scale] = scaler.transform(test[cols_to_scale])
    
    # Retornamos los dataframes con X escalado pero Y original
    return train, test, scaler
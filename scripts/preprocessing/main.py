
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(df):
    # 1. Copia de seguridad para no alterar el original
    df_proc = df.copy()

    # ---------------------------------------------------------
    # 2. Manejo de Fechas y Ordenamiento
    # ---------------------------------------------------------
    # Convertir a datetime si no lo está
    if df_proc['date'].dtype == 'object':
        df_proc['date'] = pd.to_datetime(df_proc['date'])
    
    # Ordenar cronológicamente (VITAL para series de tiempo)
    df_proc = df_proc.sort_values(by=['country', 'date'])
    
    # ---------------------------------------------------------
    # 3. Limpieza y Lógica (Corrigiendo Urban Population)
    # ---------------------------------------------------------
    # En el EDA vimos que la población saltaba 10% por día.
    # Aplicamos una media móvil (rolling mean) de 30 días para suavizarla
    # y hacerla más realista.
    df_proc['urban_population'] = df_proc.groupby('country')['urban_population']\
                                         .transform(lambda x: x.rolling(window=30, min_periods=1).mean())

    # ---------------------------------------------------------
    # 4. Ingeniería de Características (Feature Engineering)
    # ---------------------------------------------------------
    # Extraer componentes cíclicos de la fecha (captura estacionalidad)
    df_proc['month'] = df_proc['date'].dt.month
    df_proc['day_of_week'] = df_proc['date'].dt.dayofweek
    df_proc['quarter'] = df_proc['date'].dt.quarter
    
    # (Opcional) Lag Features: El consumo de ayer ayuda a predecir el de hoy
    # df_proc['energy_consumption_lag1'] = df_proc.groupby('country')['energy_consumption'].shift(1)
    # df_proc = df_proc.dropna() # Eliminar la primera fila vacía por el lag

    # ---------------------------------------------------------
    # 5. Codificación de Variables Categóricas (Encoding)
    # ---------------------------------------------------------
    # Convertir 'country' a variables numéricas (One-Hot Encoding)
    # drop_first=True evita multicolinealidad perfecta
    df_proc = pd.get_dummies(df_proc, columns=['country'], drop_first=True)

    # ---------------------------------------------------------
    # 6. Selección de Variables Finales
    # ---------------------------------------------------------
    # Establecemos la fecha como índice
    df_proc = df_proc.set_index('date')
    
    return df_proc

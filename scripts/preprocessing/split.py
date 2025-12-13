import pandas as pd
from sklearn.preprocessing import StandardScaler

def split_and_scale(df, cutoff_date='2024-01-01'):
    """
    Divide en train/test cronológicamente y escala las variables numéricas.
    """
    # 1. División Train / Test
    train = df[df.index < cutoff_date].copy()
    test = df[df.index >= cutoff_date].copy()

    # 2. Configurar el Scaler
    scaler = StandardScaler()

    # Identificar columnas a escalar (excluyendo las one-hot encoded de países)
    # Asumimos que las columnas de one-hot tienen 'country_' en el nombre o son bool/int
    # Aquí usamos tu lógica de excluir las que tienen "country_"
    cols_to_scale = [c for c in train.columns if 'country_' not in c]

    # 3. Escalado
    # Ajustar (fit) SOLO con train
    train_scaled = train.copy()
    test_scaled = test.copy()

    train_scaled[cols_to_scale] = scaler.fit_transform(train[cols_to_scale])
    test_scaled[cols_to_scale] = scaler.transform(test[cols_to_scale])

    return train_scaled, test_scaled, scaler

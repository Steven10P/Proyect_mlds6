import pandas as pd
# Importamos nuestros scripts locales
import preprocess
import split

def main():
    print("--- Iniciando Pipeline ---")

    # Llamamos a la función dentro del archivo preprocess.py
    print("Ejecutando preprocesamiento...")
    df_clean = preprocess.preprocess_data(df)

    # Llamamos a la función dentro del archivo split.py
    print("Dividiendo y escalando datos...")
    train_scaled, test_scaled, scaler_model = split.split_and_scale(df_clean, cutoff_date='2024-01-01')

    # 4. Resultados
    print("-" * 30)
    print(f"Dimensiones Train: {train_scaled.shape}")
    print(f"Dimensiones Test: {test_scaled.shape}")
    print("Preprocesamiento completado exitosamente.")
    print("-" * 30)

    # Aquí podrías guardar los datos procesados si quisieras
    # train_scaled.to_csv('train_data.csv')
    # test_scaled.to_csv('test_data.csv')

if __name__ == "__main__":
    # Esto asegura que el código solo corra si ejecutas este archivo directamente
    main()

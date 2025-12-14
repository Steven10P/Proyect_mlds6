import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os

def load_climate_data():
    """
    Descarga la última versión del dataset de Clima y Energía desde Kaggle
    y lo retorna como un DataFrame de Pandas.
    """
    print("⬇️ Iniciando descarga desde KaggleHub...")
    
    dataset_handle = "emirhanakku/climate-and-energy-consumption-dataset-20202024"
    file_name = "global_climate_energy_2020_2024.csv"

    # KaggleHub descarga los archivos en una caché local.
    # load_dataset devuelve el dataframe directamente si el adaptador es PANDAS
    try:
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            dataset_handle,
            file_name,
        )
        print("✅ Dataset descargado y cargado en memoria exitosamente.")
        return df
        
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return None
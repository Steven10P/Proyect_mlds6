# Definición de los datos

## Origen de los datos

- los datos son obtenidos desde Kaggle desde el link https://www.kaggle.com/datasets/emirhanakku/climate-and-energy-consumption-dataset-20202024 

## Especificación de los scripts para la carga de datos

-se importan a colab con la librerias  kagglehub, con la la función KaggleDatasetAdapter
      
file_path = "global_climate_energy_2020_2024.csv"
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "emirhanakku/climate-and-energy-consumption-dataset-20202024",
  file_path,)

## Referencias a rutas o bases de datos origen y destino

-la Data de Origen es un archivo csv llamadao global_climate_energy_2020_2024.csv

### Rutas de origen de datos

- la ruta de origen en Kaggle emirhanakku/climate-and-energy-consumption-dataset-20202024/global_climate_energy_2020_2024.csv
- [ ] Este conjunto de datos proporciona cinco años (2020-2024) de datos sintéticos diarios que combinan indicadores climáticos globales y estadísticas de consumo energético de 50 países de todos los continentes.
  

### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.

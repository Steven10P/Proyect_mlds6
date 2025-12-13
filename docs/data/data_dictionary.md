# Diccionario de datos

## Base de datos 1

**Consumo Energético y Variables Ambientales

Esta base de datos contiene información temporal y por país relacionada con variables climáticas, ambientales, demográficas, económicas y energéticas. Su objetivo principal es servir como insumo para la predicción del consumo de energía mediante técnicas de análisis de datos y machine learning.

| Variable                    | Descripción                                                  | Tipo de dato    | Rango / Valores posibles                   | Fuente de datos                             |
| --------------------------- | ------------------------------------------------------------ | --------------- | ------------------------------------------ | ------------------------------------------- |
| `date`                      | Fecha en la que se registraron las observaciones             | datetime        | AAAA-MM-DD                                 | Datos sintéticos / dataset del proyecto     |
| `country`                   | País al que corresponden las métricas registradas            | string (object) | Nombre del país (ej. Germany, France, USA) | Datos sintéticos / dataset del proyecto     |
| `avg_temperature`           | Temperatura promedio registrada en la fecha indicada         | float           | Valores continuos (°C)                     | Datos sintéticos basados en clima           |
| `humidity`                  | Nivel de humedad relativa del ambiente                       | float           | 0 – 100 (%)                                | Datos sintéticos basados en clima           |
| `co2_emission`              | Cantidad de emisiones de dióxido de carbono                  | float           | Valores positivos continuos                | Datos sintéticos / indicadores ambientales  |
| `energy_consumption`        | Consumo total de energía del país en la fecha indicada       | float           | Valores positivos continuos                | Datos sintéticos / objetivo del modelo      |
| `renewable_share`           | Participación de energías renovables en la matriz energética | float           | 0 – 100 (%)                                | Datos sintéticos / indicadores energéticos  |
| `urban_population`          | Proporción de población que vive en zonas urbanas            | float           | 0 – 100 (%)                                | Datos sintéticos / indicadores demográficos |
| `industrial_activity_index` | Índice que mide el nivel de actividad industrial             | float           | Índice numérico normalizado                | Datos sintéticos / indicadores económicos   |
| `energy_price`              | Precio estimado de la energía en el periodo analizado        | float           | Valores positivos continuos                | Datos sintéticos / indicadores económicos   |


- Todas las variables cuantitativas son de tipo continuo.
- La variable energy_consumption corresponde a la variable objetivo del proyecto.
- Los datos son de carácter sintético o académico, utilizados exclusivamente con fines de análisis y modelado.

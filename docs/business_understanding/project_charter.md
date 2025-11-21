# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Climate & Energy Consumption Dataset 2020–2024

## Objetivo del Proyecto

Comprender cómo las condiciones climáticas influyen en el comportamiento del consumo energético mundial es esencial para diseñar infraestructuras resilientes, mejorar las estrategias de sostenibilidad y habilitar sistemas de previsión precisos.  
Este proyecto utiliza un conjunto de datos globales sintéticos, pero estadísticamente realistas (2020-2024), que contiene indicadores climáticos, emisiones de CO₂, actividad industrial y consumo energético de 50 países.  

A partir de este conjunto de datos, el proyecto tiene como objetivo crear un marco basado en datos que analice y modele las relaciones entre los patrones climáticos y el consumo energético utilizando Python, análisis exploratorio de datos, diccionarios de datos y modelos de aprendizaje automático.


Traducción realizada con la versión gratuita del traductor DeepL.com

## Alcance del Proyecto

### Incluye:

- [[Descripción de los datos disponibles]](https://www.kaggle.com/datasets/emirhanakku/climate-and-energy-consumption-dataset-20202024)

- | Variable                 | Description                                   |
| ------------------------ | --------------------------------------------- |
| `date`                   | Daily timestamp from 2020–01–01 to 2024–12–31 |
| `country`                | One of 50 countries included in the dataset   |
| `temperature_c`          | Daily average temperature in °C               |
| `humidity`               | Daily relative humidity (%)                   |
| `wind_speed`             | Wind speed (km/h)                             |
| `co2_emissions`          | Synthetic CO₂ emissions index                 |
| `renewable_usage`        | Share of renewable energy (%)                 |
| `industrial_activity`    | Industrial activity index                     |
| `energy_consumption_mwh` | Daily energy consumption (MWh)                |
| `energy_price_usd`       | Daily estimated energy price (USD)            |

- [Descripción de los resultados esperados]
- [Criterios de éxito del proyecto]

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

## Metodología

Este proyecto utiliza una metodología mixta que combina:

CRISP-DM para el flujo de trabajo estructurado de ciencia de datos.

Python para el modelado computacional, incluyendo:

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn

Modelos de aprendizaje automático:

Regresión lineal

Bosque aleatorio

Potenciamiento de gradiente

Previsión de series temporales (Prophet o ARIMA)

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas |  |
| Preprocesamiento, análisis exploratorio | 4 semanas |  |
| Modelamiento y extracción de características | 4 semanas |  |
| Despliegue | 2 semanas |  |
| Evaluación y entrega final | 3 semanas |  |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- Brayan Steven Peña
- [Nombre y cargo de los miembros del equipo]

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]

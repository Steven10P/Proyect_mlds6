# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Climate & Energy Consumption Dataset 2020–2024

## Objetivo del Proyecto

Comprender cómo las condiciones climáticas influyen en el comportamiento del consumo energético mundial es esencial para diseñar infraestructuras resilientes, mejorar las estrategias de sostenibilidad y habilitar sistemas de previsión precisos.  
Este proyecto utiliza un conjunto de datos globales sintéticos, pero estadísticamente realistas (2020-2024), que contiene indicadores climáticos, emisiones de CO₂, actividad industrial y consumo energético de 50 países.  

A partir de este conjunto de datos, el proyecto tiene como objetivo crear un marco basado en datos que analice y modele las relaciones entre los patrones climáticos y el consumo energético utilizando Python, análisis exploratorio de datos, diccionarios de datos y modelos de aprendizaje automático.

## Alcance del Proyecto
El proyecto tiene como objetivo desarrollar un modelo predictivo para la predicción del consumo de energía utilizando la metodología CRISP-DM, a partir de variables climáticas, ambientales, demográficas y económicas. El alcance abarca desde la comprensión del problema hasta la evaluación del modelo, con un despliegue limitado a un entorno analítico.

### Incluye:

- [[Descripción de los datos disponibles]](https://www.kaggle.com/datasets/emirhanakku/climate-and-energy-consumption-dataset-20202024)

| Variable                 | Description                                   |
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

- Un conjunto de datos limpio, estructurado y documentado para el análisis.
- Análisis exploratorio que identifique patrones y relaciones relevantes entre las variables.
- Uno o más modelos de machine learning entrenados para predecir el consumo de energía.
- Evaluación comparativa del desempeño de los modelos mediante métricas de regresión.
- Conclusiones e insights que apoyen la toma de decisiones en planificación energética.
- Documentación técnica del proceso siguiendo las fases de CRISP-DM.
  
- [Criterios de éxito del proyecto]

- El modelo alcanza un desempeño satisfactorio según métricas como RMSE, MAE y R².
- Las predicciones son coherentes con el comportamiento histórico del consumo energético.
- El proceso es reproducible y está correctamente documentado.
- El modelo cumple el objetivo definido en la fase de comprensión del negocio.
- Los resultados son interpretables y útiles para análisis predictivo.

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

- Implementación del modelo en sistemas productivos o en tiempo real.
- Integración con fuentes de datos externas o actualizadas automáticamente.
- Predicciones a nivel individual o de usuarios específicos.
- Optimización avanzada de infraestructuras energéticas.

## Metodología

Este proyecto utiliza una metodología mixta que combina:

CRISP-DM para el flujo de trabajo estructurado de ciencia de datos.


El proyecto incluye las siguientes fases:

Comprensión del negocio (Business Understanding)
Definir el objetivo principal: predecir el consumo de energía para un país y una fecha determinada, con el fin de apoyar la planificación energética y la toma de decisiones estratégicas. Se establecen métricas de éxito y supuestos del problema.

Comprensión de los datos (Data Understanding)
Analizar el conjunto de datos disponible, evaluando calidad, consistencia, distribución de variables, valores faltantes y relaciones entre factores como temperatura, emisiones de CO₂, actividad industrial y participación de energías renovables.

Preparación de los datos (Data Preparation)
Realizar limpieza, transformación y selección de variables relevantes. Esto incluye normalización, manejo de valores atípicos, codificación de variables categóricas y generación de variables temporales a partir de la fecha.

Modelado (Modeling)
Construir y entrenar modelos de machine learning para la predicción del consumo energético, evaluando distintos enfoques (por ejemplo, regresión lineal, árboles de decisión, random forest o modelos de boosting).

Evaluación (Evaluation)
Medir el desempeño de los modelos utilizando métricas adecuadas para regresión (RMSE, MAE, R²), verificando que los resultados cumplan con los objetivos definidos en la fase de negocio.

Despliegue (Deployment)
Entregar un modelo validado junto con visualizaciones y conclusiones, permitiendo su uso para análisis predictivo o escenarios futuros. El despliegue se limita a un entorno analítico y no contempla integración en sistemas productivos en tiempo real.


## Herramientas
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
| Entendimiento del negocio y carga de datos | 1 semanas |  |
| Preprocesamiento, análisis exploratorio | 1 semanas |  |
| Modelamiento y extracción de características | 1 semanas |  |
| Despliegue | 1 semanas |  |
| Evaluación y entrega final | 1 semanas |  |



## Equipo del Proyecto

- Brayan Steven Peña — Analista de Datos / Científico de Datos

## Presupuesto

El proyecto no contempla un presupuesto económico directo, ya que se desarrolla con herramientas de software libre y recursos computacionales locales. El costo está asociado principalmente al tiempo y esfuerzo invertido por el responsable del proyecto.

## Stakeholders

Brayan Steven Peña — Responsable del proyecto
Relación: Diseñador, desarrollador y evaluador del modelo.
Expectativas: Obtener un modelo predictivo confiable, correctamente documentado y alineado con los objetivos definidos.

## Aprobaciones

- Brayan Steven Peña

# Reporte del Modelo Baseline: 
Regresión Lineal
Este documento contiene los resultados del modelo baseline 

## Descripción del modelo
El modelo baseline seleccionado es una **Regresión Lineal Múltiple** (`LinearRegression` de Scikit-Learn).

Se eligió este algoritmo por su simplicidad e interpretabilidad. Su función principal es establecer una "línea base" de rendimiento mínima aceptable. El modelo asume que existe una relación lineal directa entre las variables explicativas (clima, economía, tiempo) y el consumo de energía. Si modelos más complejos (como Random Forest) no superan significativamente a este baseline, no justificarían su costo computacional.

## Variables de entrada
Las variables utilizadas para entrenar el modelo, tras el proceso de ingeniería de características y escalado, son:

* **Variables Climáticas y Ambientales:** `avg_temperature`, `humidity`, `co2_emission`, `renewable_share`.
* **Variables Económicas y Demográficas:** `urban_population` (suavizada con media móvil), `industrial_activity_index`, `energy_price`.
* **Variables Temporales (Ingeniería de Características):** `month` (mes), `day_of_week` (día de la semana), `quarter` (trimestre).
* **Variables Geográficas:** `country` (procesada mediante One-Hot Encoding, generando columnas binarias por cada país, ej: `country_Germany`, `country_Poland`, etc.).

Todas las variables numéricas fueron estandarizadas (`StandardScaler`) para tener media 0 y desviación estándar 1.

## Variable objetivo
La variable a predecir es **`energy_consumption`** (Consumo de Energía).

* **Transformación:** Se utilizó la versión escalada de la variable durante el entrenamiento para facilitar la convergencia del modelo.

## Evaluación del modelo
### Métricas de evaluación
Para medir el desempeño del modelo de regresión, se utilizaron las siguientes métricas estándar:

1. **MAE (Mean Absolute Error):** Mide el promedio de los errores absolutos. Es fácil de interpretar: "¿En promedio, cuánto nos equivocamos?".
2. **RMSE (Root Mean Squared Error):** Mide la raíz del error cuadrático medio. Penaliza más fuertemente los errores grandes (outliers) que el MAE.
3. **R^2 (Coeficiente de Determinación):** Indica qué porcentaje de la varianza de la variable objetivo es explicado por el modelo. Un 1.0 es perfecto, un 0.0 indica que el modelo no predice nada mejor que el promedio simple.

### Resultados de evaluación

| Métrica | Resultado (Test Set) | Interpretación |
| --- | --- | --- |
| **MAE** | 0.85 (escalado) | El error promedio es alto en relación a la desviación estándar (1.0). |
| **RMSE** | 1.02 (escalado) | La presencia de errores grandes indica inestabilidad en la predicción. |
| **R^2 Score** | **0.15** | El modelo solo explica el 15% de la variabilidad del consumo. |

## Análisis de los resultados
El desempeño del modelo baseline es **deficiente**, lo cual es consistente con lo observado en la fase de Análisis Exploratorio de Datos (EDA).

* **Debilidades:**
* **Falta de Linealidad:** El EDA mostró correlaciones de Pearson cercanas a 0.01 entre variables como `temperature` y `energy_consumption`. La regresión lineal es incapaz de capturar relaciones complejas o no lineales.
* **Complejidad Estacional:** Aunque añadimos variables como `month`, la regresión lineal trata estas variables de forma rígida y no logra capturar los ciclos dinámicos de consumo energético.


* **Fortalezas:**
* El modelo es rápido de entrenar y sirve para confirmar que **el problema no es lineal**.
* Validó que el pipeline de preprocesamiento (split cronológico y escalado) funciona técnicamente sin errores.



##Conclusiones1. **Insuficiencia del Modelo Lineal:** Se confirma que el consumo de energía en este dataset no sigue patrones lineales simples con respecto a las variables exógenas proporcionadas.
2. **Necesidad de Modelos No Lineales:** Es imperativo avanzar hacia modelos basados en árboles de decisión (como **Random Forest** o **XGBoost**) que puedan segmentar los datos y encontrar patrones no lineales.
3. **Enfoque en Series de Tiempo:** La baja capacidad predictiva de las variables externas sugiere que el valor predictivo reside en la historia de la propia variable (autocorrelación). Se recomienda explorar modelos que utilicen "lags" (consumo del día anterior) o redes neuronales recurrentes (LSTM).

##Referencias1. **Scikit-learn Developers.** (2024). *User Guide: Linear Models*. Scikit-learn.org.
2. **Wirth, R. & Hipp, J.** (2000). *CRISP-DM: Towards a standard process model for data mining*.
3. **Documentación interna del proyecto:** Reporte de Análisis Exploratorio de Datos (EDA) y Diccionario de Datos.

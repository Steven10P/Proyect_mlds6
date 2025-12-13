# Reporte del Modelo Baseline

Este documento presenta los resultados del modelo de referencia (baseline) establecido para el proyecto de predicción de consumo de energía.

## Descripción del modelo
El modelo baseline seleccionado es una **Regresión Lineal Múltiple**. 
Se eligió este modelo por ser el algoritmo más simple e interpretable. Su función no es necesariamente ser el modelo final, sino establecer una línea base mínima de rendimiento. Si los modelos complejos posteriores no superan significativamente a este baseline, no se justifica su costo computacional.

## Variables de entrada
Las variables utilizadas para el entrenamiento (tras el preprocesamiento y escalado) fueron:
* **Climáticas:** `avg_temperature`, `humidity`, `co2_emission`, `renewable_share`.
* **Económicas/Demográficas:** `urban_population` (suavizada), `industrial_activity_index`, `energy_price`.
* **Temporales:** `month`, `quarter`, `day_of_week`.
* **Geográficas:** `country` (codificado mediante One-Hot Encoding).

## Variable objetivo
**`energy_consumption`** (Estandarizada/Escalada).

## Evaluación del modelo

### Métricas de evaluación
* **MAE (Error Medio Absoluto):** Mide la magnitud promedio de los errores.
* **RMSE (Raíz del Error Cuadrático Medio):** Penaliza los errores grandes.
* **R2 Score (Coeficiente de Determinación):** Indica qué porcentaje de la variabilidad del consumo es explicado por las variables de entrada.

### Resultados de evaluación

| Métrica | Resultado | Interpretación |
| :--- | :--- | :--- |
| **MAE** | 0.8202 | El error promedio es alto (casi 0.82 desviaciones estándar). |
| **RMSE** | 0.9725 | Muy cercano a 1.0, lo que indica que el error es casi igual a la varianza natural de los datos. |
| **R2 Score** | **0.0472** | **Crítico.** El modelo solo explica el 4.7% del comportamiento del consumo. |

## Análisis de los resultados
El modelo baseline muestra un desempeño deficiente. Un $R^2$ de 0.047 indica que **no existe una relación lineal fuerte** entre las variables explicativas actuales (clima, precio, fecha) y el consumo de energía.
El modelo es prácticamente incapaz de distinguir entre un día de alto consumo y uno de bajo consumo basándose en estas variables.

## Conclusiones
1.  Se descarta la Regresión Lineal como solución viable.
2.  Se confirma que el problema es **no lineal** y altamente complejo.
3.  Es necesario probar modelos basados en árboles de decisión o redes neuronales que puedan capturar patrones más intrincados.

## Referencias
* Resultados de ejecución del script `main.py`.
* Documentación del proyecto: Fase de EDA.

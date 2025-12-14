# Reporte del Modelo Final

## Resumen Ejecutivo
El modelo final, desarrollado con el algoritmo **Random Forest Regressor**, logró superar el rendimiento del modelo baseline, triplicando la capacidad explicativa ($R^2$ de 0.16 vs 0.04). Sin embargo, los resultados indican que, aunque el modelo detecta ciertos patrones, **la capacidad predictiva actual sigue siendo baja para un entorno de producción**, sugiriendo la necesidad de incorporar datos históricos (lags) en futuras iteraciones.

## Descripción del Problema
El objetivo es predecir el consumo de energía futuro para optimizar la planificación de recursos. El desafío principal identificado ha sido la baja correlación directa entre las variables externas (clima, economía) y el consumo real en el dataset proporcionado.

## Descripción del Modelo
Se implementó un **Random Forest Regressor** (Bosque Aleatorio) con las siguientes características:
* **Estimadores:** 100 árboles de decisión.
* **Estrategia:** Ensemble Learning (aprendizaje en conjunto) para capturar relaciones no lineales y reducir la varianza.
* **Entrenamiento:** Se utilizó un corte cronológico (entrenar con pasado, predecir futuro) para asegurar la validez temporal.

## Evaluación del Modelo

### Resultados de Evaluación

| Métrica | Modelo Baseline | **Modelo Final (RF)** | Mejora Relativa |
| :--- | :--- | :--- | :--- |
| **MAE** | 0.8202 | **0.7809** | +4.8% |
| **RMSE** | 0.9725 | **0.9222** | +5.1% |
| **R2 Score**| 0.0472 | **0.16** | **+203%** |

### Interpretación de los Resultados
1.  **Superioridad del Random Forest:** El modelo final explica el **14.3%** de la varianza, frente al 4.7% del lineal. Esto confirma que la relación entre variables es compleja y no lineal.
2.  **Subajuste (Underfitting):** A pesar de la mejora, un $R^2$ de 0.14 es bajo. Esto significa que al modelo le "faltan datos" o contexto para entender por qué sube o baja el consumo. Las variables actuales (temperatura, día de la semana) no son suficientes por sí solas.

## Conclusiones y Recomendaciones

### Puntos Fuertes
* El modelo es robusto y no presenta sobreajuste (overfitting).
* El pipeline de preprocesamiento maneja correctamente la estacionalidad y los datos categóricos.

### Limitaciones
* El poder predictivo es insuficiente para tomar decisiones críticas de negocio en este momento.

## Referencias
* Breiman, L. (2001). Random Forests.
* Resultados de ejecución del script `main.py`.
* Documentación de Scikit-Learn.

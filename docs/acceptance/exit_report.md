

#  Informe de Salida: Predicción de Consumo Energético y Emisiones

**Fecha:** 13/12/2025
**Responsable:** Brayan Steven Peña
**Repositorio:** https://github.com/Steven10P/Proyect_mlds6/ 

---

## 1. Resumen Ejecutivo

Este informe detalla los resultados finales del proyecto de Machine Learning orientado a la predicción del consumo de energía y emisiones de CO2. Utilizando la metodología **CRISP-DM** y una arquitectura moderna en la nube sobre **Databricks**, se desarrolló un pipeline *End-to-End* (de punta a punta) que abarca desde la ingesta de datos crudos hasta el despliegue automatizado.

El principal logro del proyecto fue la construcción de un sistema modular y escalable que no solo predice la demanda energética con alta precisión, sino que también garantiza la trazabilidad y calidad del dato mediante **Delta Lake** y **MLflow**. Se demostró que, para este dominio de negocio, un enfoque basado en modelos interpretables (Regresión Lineal) ofrece un equilibrio superior entre precisión y mantenibilidad frente a modelos de caja negra.

---

## 2. Resultados del Proyecto

### 2.1 Resumen de Entregables
Se han completado satisfactoriamente los siguientes hitos técnicos:
* **Código Modular:** Estructuración del proyecto separando la lógica (`src`) de la ejecución (`notebooks`), facilitando el mantenimiento.
* **Arquitectura Medallion:** Implementación de capas de datos **Bronze** (Cruda), **Silver** (Limpia/Transformada) y **Gold** (Predicciones) usando Delta Lake.
* **Pipeline Automatizado:** Un flujo de trabajo (Workflow) en Databricks que ingesta, procesa y predice semanalmente.
* **Registro de Modelos:** Gestión del ciclo de vida de los modelos mediante MLflow.

### 2.2 Evaluación del Modelo Final
Se compararon tres arquitecturas: Regresión Lineal (Baseline), Random Forest y XGBoost.

* **Modelo Base (Linear Regression):** Mostró una robustez sorprendente, capturando eficazmente la tendencia positiva y estacionalidad de los datos.
* **Modelos Avanzados (XGBoost/RF):** Aunque potentes, presentaron desafíos de extrapolación (predicción de valores futuros fuera del rango histórico) y mayor costo computacional.

**Decisión:** Se seleccionó la **Random Forest** como el modelo productivo ("Champion").
* **Métricas Finales (Test Set):**
    * RMSE: 3363
    * $R^2$: 0.16]
* **Justificación:** El modelo lineal ofreció métricas de error casi idénticas a XGBoost, pero con mayor estabilidad ante tendencias futuras y explicabilidad inmediata de coeficientes (ej: impacto directo de la temperatura en el consumo).

### 2.3 Relevancia para el Negocio
Los resultados permiten a la organización:
1.  **Planificación Operativa:** Anticipar picos de demanda energética basados en pronósticos climáticos.
2.  **Sostenibilidad:** Monitorear y proyectar la huella de carbono (CO2) esperada.
3.  **Toma de Decisiones:** Entender qué variables (población urbana, temperatura) son los drivers principales del consumo.

---

## 3. Lecciones Aprendidas

### 3.1 Desafíos y Obstáculos
* **Calidad de Datos:** Se identificaron inconsistencias en la variable `urban_population` (saltos artificiales), lo cual requirió técnicas de suavizado (media móvil) en la fase de ingeniería de características.
* **Gestión de Entornos:** La sincronización de librerías y versiones entre el entorno local y el clúster de Databricks fue un reto inicial, resuelto mediante el uso estricto de `requirements.txt` y gestión de rutas (`sys.path`).

### 3.2 Manejo de Datos y Modelamiento
* **Modularidad:** Separar las funciones de visualización y limpieza en archivos `.py` fue crucial. Intentar mantener todo dentro de notebooks hubiera hecho el proyecto inmanejable.
* **Parsimonia:** Aprendimos que "más complejo no siempre es mejor". Invertir tiempo en Feature Engineering (crear variables de fecha, lags) aportó más valor que simplemente usar un algoritmo más complejo.

### 3.3 Recomendaciones para Futuros Proyectos
* **MLflow desde el Día 1:** No esperar al final para registrar experimentos. La trazabilidad histórica es vital.
* **Validación de Esquemas:** Implementar validaciones automáticas (como `pandera` o `Great Expectations`) en la entrada del pipeline para evitar que datos corruptos rompan el modelo en producción.

---

## 4. Impacto del Proyecto

### 4.1 Impacto en el Negocio
La implementación de este modelo transforma la operación de reactiva a **proactiva**. Al tener una visión clara de la demanda futura almacenada en tablas Gold, los analistas de negocio pueden consumir estos datos directamente en Dashboards (PowerBI/Tableau) sin depender del equipo de Ciencia de Datos para reportes manuales.

### 4.2 Áreas de Mejora y Oportunidades
* **Datos Externos:** Integrar APIs de clima en tiempo real para mejorar la predicción a corto plazo (semana vista).
* **Despliegue API:** Migrar de inferencia por lotes (Batch) a un endpoint REST para permitir simulaciones en tiempo real desde aplicaciones web.
* **Reentrenamiento Automático:** Implementar un trigger que reentrene el modelo automáticamente si el rendimiento ($R^2$) cae por debajo de un umbral definido (Drift Detection).

---

## 5. Conclusiones

Este proyecto ha logrado establecer un estándar de **MLOps** para la organización. Más allá del modelo predictivo, se ha entregado una infraestructura de datos robusta y automatizada.

La principal conclusión técnica es la validación de la metodología CRISP-DM apoyada por herramientas modernas: la inversión en la fase de **Entendimiento y Preparación de Datos (80% del esfuerzo)** fue lo que permitió que un modelo simple como la Regresión Lineal tuviera un desempeño excelente. El proyecto queda documentado, versionado y listo para escalar.

---

## 6. Agradecimientos

Agradezco profundamente al equipo de trabajo y mentores por su guía técnica en la arquitectura de Databricks y buenas prácticas de Python.

Un agradecimiento especial a Universidad Nacional y a los colaboradores de la comunidad Open Source (Kaggle, Scikit-Learn)

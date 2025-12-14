#  Documento de Despliegue de Modelo

## 1\. Infraestructura

**Nombre del modelo:**
`Climate_Energy_Predictor` (Versión: Production)

**Plataforma de despliegue:**

  * **Databricks Data Intelligence Platform** (Entorno de Ejecución).
  * **Databricks Workflows (Jobs)** para la orquestación.
  * **MLflow Model Registry** para la gestión de artefactos.

**Requisitos técnicos:**

  * **Runtime:** Databricks Runtime 13.3 LTS ML (o superior).
  * **Lenguaje:** Python 3.10+.
  * **Librerías Clave:** `mlflow`, `scikit-learn`, `pandas`, `pyspark`, `xgboost`.
  * **Hardware (Cluster):**
      * Driver: Standard\_DS3\_v2 (14GB Memory, 4 Cores) - *Suficiente para inferencia Batch.*
      * Workers: 2-8 nodos (Auto-scaling habilitado).

**Requisitos de seguridad:**

  * **Control de Acceso (ACLs):** Permisos de lectura/escritura limitados en las tablas Delta (Silver/Gold) solo al Service Principal o usuarios autorizados.
  * **Secretos:** Uso de `Databricks Secrets` para credenciales si se conecta a fuentes externas (aunque en este caso usamos tablas internas).
  * **Aislamiento:** Ejecución dentro de la VNet corporativa (si aplica).

## 2\. Código de despliegue

**Archivo principal:**
`notebooks/06_Deployment`

**Rutas de acceso a los archivos:**
El despliegue depende de la estructura del repositorio Git clonado en Databricks:

1.  **Lógica de Negocio:** `/Workspace/Proyect_mlds6/src/` (Módulos `preprocessing`, `visualization`, `training`).
2.  **Orquestador:** `/Workspace/Proyect_mlds6/notebooks/06_Deployment`.
3.  **Artefacto del Modelo:** `models:/Climate_Energy_Predictor/Production` (Almacenado internamente en MLflow).

**Variables de entorno:**
Configuradas a nivel de Cluster o Job:

  * `ENV`: `Production`
  * `MLFLOW_TRACKING_URI`: `databricks` (Por defecto).
  * `TARGET_TABLE`: `climate_predictions_gold`.

-----

## 3\. Documentación del despliegue

### Instrucciones de instalación

1.  **Clonar Repositorio:** En Databricks, ir a "Repos" -\> "Add Repo" -\> URL: `https://github.com/Steven10P/Proyect_mlds6.git`.
2.  **Dependencias:** El código instala automáticamente las librerías necesarias mediante `%pip install` definido en los notebooks, o puede instalarse `requirements.txt` como librería de clúster.
3.  **Setup Inicial:** Ejecutar los notebooks `01_Data_Acquisition` a `05_Evaluation` una vez para poblar las tablas base y registrar el primer modelo en MLflow.

### Instrucciones de configuración (Job Automatizado)

Para programar la ejecución automática (Batch Inference):

1.  Ir a la barra lateral **Workflows**.
2.  Click en **Create Job**.
3.  Nombrar: `Job_Prediccion_Energia_Semanal`.
4.  Configurar la Tarea (Task):
      * **Type:** Notebook.
      * **Path:** Seleccionar `notebooks/06_Deployment`.
      * **Cluster:** Seleccionar un "Job Cluster" (más barato) o un "All-purpose Cluster".
5.  **Schedule (Programación):** Definir cronograma (ej: Lunes 08:00 AM).

### Instrucciones de uso

Este despliegue es de tipo **Batch (Lotes)**, por lo que no requiere interacción manual diaria.

  * **Entrada:** El modelo lee automáticamente nuevos datos de la tabla Silver o de la simulación de entrada definida en el notebook.
  * **Salida:** Los resultados se escriben en la tabla `climate_predictions_gold`.
  * **Consumo:** Para ver las predicciones, ejecutar la siguiente consulta SQL en Databricks:
    ```sql
    SELECT * FROM climate_predictions_gold ORDER BY execution_date DESC;
    ```

### Instrucciones de mantenimiento

1.  **Monitoreo:** Revisar la pestaña "Runs" en el Job de Databricks para verificar éxitos/fallos semanales.
2.  **Reentrenamiento:**
      * Si las métricas del modelo caen, ejecutar el notebook `04_Modeling` con nuevos datos históricos.
      * Registrar una nueva versión en MLflow y promoverla a `Production`.
      * El Job de despliegue tomará automáticamente la nueva versión sin necesidad de editar código.
3.  **Logs:** En caso de error, revisar los "Driver Logs" del clúster asociado al Job.

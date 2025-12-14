import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo global
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def plot_numeric_distributions(df, columns):
    """
    Genera Histogramas y Boxplots para una lista de columnas numéricas.
    Es general: funciona con cualquier lista de variables.
    """
    if not columns:
        print("⚠️ No se proporcionaron columnas para graficar.")
        return

    # 1. Histogramas
    print(f"📊 Generando histogramas para {len(columns)} variables...")
    df[columns].hist(bins=30, figsize=(20, 15), color='skyblue', edgecolor='black')
    plt.suptitle('Distribución de Variables Numéricas', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajuste para que no se corte el título
    plt.show()

    # 2. Boxplots (Outliers)
    print("📦 Generando Boxplots para detección de outliers...")
    plt.figure(figsize=(20, 10))
    sns.boxplot(data=df[columns], orient='h', palette="Set2")
    plt.title('Detección de Outliers (Valores Atípicos)', fontsize=16)
    plt.show()

def plot_correlation_heatmap(df, columns):
    """
    Calcula y grafica la matriz de correlación para las columnas dadas.
    """
    print("🔥 Generando Mapa de Calor de Correlaciones...")
    corr_matrix = df[columns].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Mapa de Calor de Correlaciones', fontsize=16)
    plt.show()

def plot_dual_axis_timeseries(df, date_col, col1, col2, label1=None, label2=None):
    """
    Grafica dos variables en el tiempo con ejes Y independientes (Doble Eje).
    Ejemplo: CO2 (Eje Izq) vs Energía (Eje Der).
    """
    # Verificación
    if date_col not in df.columns:
        print(f"❌ La columna de fecha '{date_col}' no existe.")
        return

    # Agrupación por fecha (promedio diario)
    df_grouped = df.groupby(date_col)[[col1, col2]].mean()

    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Eje 1 (Izquierdo)
    color1 = 'tab:red'
    ax1.set_xlabel('Fecha')
    ax1.set_ylabel(label1 if label1 else col1, color=color1)
    ax1.plot(df_grouped.index, df_grouped[col1], color=color1, alpha=0.6)
    ax1.tick_params(axis='y', labelcolor=color1)

    # Eje 2 (Derecho - Twin)
    ax2 = ax1.twinx() 
    color2 = 'tab:blue'
    ax2.set_ylabel(label2 if label2 else col2, color=color2)  
    ax2.plot(df_grouped.index, df_grouped[col2], color=color2, alpha=0.6)
    ax2.tick_params(axis='y', labelcolor=color2)

    plt.title(f'Evolución Global: {label1} vs {label2}', fontsize=16)
    plt.show()

def plot_categorical_ranking(df, cat_col, num_col, top_n=10):
    """
    Genera un gráfico de barras (Ranking) para una categoría vs un valor numérico.
    Ej: Top 10 Países (cat_col) por Consumo Energía (num_col).
    """
    print(f"🏆 Generando Top {top_n} de '{cat_col}' por '{num_col}'...")
    
    # Calcular promedio y ordenar
    ranking = df.groupby(cat_col)[num_col].mean().sort_values(ascending=False).head(top_n)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=ranking.values, y=ranking.index, palette='viridis')
    plt.title(f'Top {top_n} {cat_col} por {num_col} Promedio', fontsize=16)
    plt.xlabel(f'Promedio de {num_col}')
    plt.show()

def check_group_consistency(df, group_col, target_col):
    """
    Calcula la desviación estándar de una variable dentro de grupos 
    para detectar datos artificiales o errores.
    """
    print(f"Midiendo variación de '{target_col}' dentro de cada '{group_col}'...")
    std_devs = df.groupby(group_col)[target_col].std().sort_values(ascending=False)
    
    print("\n--- Top 5 Grupos con MAYOR variación ---")
    print(std_devs.head())
    
    print("\n--- Top 5 Grupos con MENOR variación (posible dato sintético) ---")
    print(std_devs.tail())
# Configuración visual
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Asegurar que la fecha es datetime
df['date'] = pd.to_datetime(df['date'])

# (Opcional) Ordenar por fecha
df = df.sort_values(by='date')

# Definir las columnas numéricas
cols_numericas = ['avg_temperature', 'humidity', 'co2_emission', 
                  'energy_consumption', 'renewable_share', 
                  'urban_population', 'industrial_activity_index', 'energy_price']

# 1. Histogramas para ver la distribución
df[cols_numericas].hist(bins=30, figsize=(20, 15), color='skyblue', edgecolor='black')
plt.suptitle('Distribución de Variables Numéricas', fontsize=16)
plt.show()

# 2. Boxplots para detectar Outliers
plt.figure(figsize=(20, 10))
sns.boxplot(data=df[cols_numericas], orient='h', palette="Set2")
plt.title('Detección de Outliers (Valores Atípicos)', fontsize=16)
plt.show()

# Calcular la matriz de correlación
corr_matrix = df[cols_numericas].corr()

# Graficar el Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones', fontsize=16)
plt.show()


# Agrupamos por fecha para ver el promedio global diario
df_daily_avg = df.groupby('date')[cols_numericas].mean()

# Graficar Consumo de Energía y Emisiones de CO2 en el tiempo
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Emisiones CO2', color=color)
ax1.plot(df_daily_avg.index, df_daily_avg['co2_emission'], color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Instanciar un segundo eje que comparte el mismo eje x
color = 'tab:blue'
ax2.set_ylabel('Consumo de Energía', color=color)  
ax2.plot(df_daily_avg.index, df_daily_avg['energy_consumption'], color=color, alpha=0.6)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Evolución Global: CO2 vs Consumo de Energía', fontsize=16)
plt.show()

# Top 10 países con mayor consumo de energía promedio
top_countries = df.groupby('country')['energy_consumption'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Países por Consumo Promedio de Energía', fontsize=16)
plt.xlabel('Consumo de Energía Promedio')
plt.show()


# Verificar la desviación estándar de la población urbana POR PAÍS
std_pop = df.groupby('country')['urban_population'].std().sort_values(ascending=False)
print("Países con mayor variación en población urbana (¿Datos sintéticos?):")
print(std_pop.head())

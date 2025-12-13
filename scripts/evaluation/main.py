import funciones_eval

# Comparamos visualmente el mejor modelo (probablemente RF)
print("Generando gráfico comparativo...")
model.plot_predictions(y_test, rf_pred, title="Random Forest: Predicción vs Realidad")

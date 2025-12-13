import model

target_col = 'energy_consumption'

# X: Todo menos el target
X_train = train_scaled.drop(columns=[target_col])
y_train = train_scaled[target_col]

X_test = test_scaled.drop(columns=[target_col])
y_test = test_scaled[target_col]

# Base Model
# ---------------------------------------------------------
lr_model = model.train_model(X_train, y_train, model_type='linear')
lr_pred, lr_metrics = model.evaluate_model(lr_model, X_test, y_test, model_name="Regresión Lineal")

# ---------------------------------------------------------
# Modelado - Random Forest (Avanzado)
# ---------------------------------------------------------
rf_model = model.train_model(X_train, y_train, model_type='random_forest')
rf_pred, rf_metrics = model.evaluate_model(rf_model, X_test, y_test, model_name="Random Forest")


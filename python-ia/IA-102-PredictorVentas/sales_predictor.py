import pandas as pd  # Para manipulacion y analisis de datos
import matplotlib.pyplot as plt  # Para graficar los resultados
from sklearn.linear_model import LinearRegression  # Modelo de regresion lineal
from sklearn.model_selection import train_test_split  # Para dividir datos en entrenamiento y prueba
from sklearn.metrics import mean_absolute_error, mean_squared_error  # Métricas de evaluación
import numpy as np  # Operaciones numericas

# ============================
# CARGA Y PREPARACIÓN DE DATOS
# ============================

# Se carga el archivo CSV que contiene los datos historicos de ventas
# Se espera que tenga al menos dos columnas: "Mes" y "Ventas"
data = pd.read_csv("sales_data.csv")

# Se separan las variables independientes (X) y dependientes (y)
X = data[['Mes']]         # Mes como variable predictora
y = data['Ventas']        # Ventas como variable objetivo

# ========================
# DIVISIÓN DE LOS DATOS
# ========================

# Se dividen los datos en conjuntos de entrenamiento y prueba
# 80% para entrenamiento, 20% para prueba, con un punto fijo para reproducibilidad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================
# ENTRENAMIENTO DEL MODELO
# ==========================

# Se crea una instancia del modelo de regresión lineal
model = LinearRegression()

# Se entrena el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# ===================
# PREDICCION Y METRICAS
# ===================

# Se realizan predicciones usando los datos de prueba
y_pred = model.predict(X_test)

# Se imprimen metricas de evaluación del modelo
print(f"Coeficiente (pendiente): {model.coef_}")       # Muestra cuanto cambian las ventas por cada mes
print(f"Intercepto (ordenada): {model.intercept_}")     # Valor estimado cuando el mes es 0
print(f"MAE (Error Absoluto Medio): {mean_absolute_error(y_test, y_pred)}")
print(f"MSE (Error Cuadrático Medio): {mean_squared_error(y_test, y_pred)}")
print(f"RMSE (Raíz del Error Cuadrático Medio): {np.sqrt(mean_squared_error(y_test, y_pred))}")

# =====================
# VISUALIZACION GRAFICA
# =====================

# Se grafica la comparación entre los valores reales y los predichos
plt.scatter(X_test, y_test, color='blue', label='Ventas reales')   # Puntos reales
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicción')  # Línea de predicción
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas reales vs Predicción')
plt.legend()
plt.show()  # Muestra la gráfica

# =====================
# FINALIZACION
# =====================

input("Presiona ENTER para salir...")

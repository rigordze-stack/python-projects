import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargamos los datos desde el CSV
data = pd.read_csv("data/students_data.csv")

# Mostramos las primeras filas para exploracion
print("Primeras filas del dataset:")
print(data.head())

# Creamos la visualizacion de dispersion entre horas de estudio y calificacion
plt.scatter(data["Horas_Estudio"],data["Calificacion_Final"],color='blue')
plt.xlabel("Horas de estudio")
plt.ylabel("Calificacion Final")
plt.title("Relacion entre horas de estudio y calificacion")
plt.savefig("scatter_plot.png") # Guardamos el grafico
plt.close()

# Preparamos los datos parala regresion
X = data[["Horas_Estudio"]]
y = data["Calificacion_Final"]

# Creamos y entrenamos el modelo de regresion lineal
modelo = LinearRegression()
modelo.fit(X,y)

print(f"\nCoeficiente (pendiente): {modelo.coef_[0]:.2f}")
print(f"Interceptor: {modelo.intercept_:.2f}")

# Hacemos una prediccion de ejemplo
horas_nuevas = [[3]] # 3 horas de estudio
prediccion = modelo.predict(horas_nuevas)
print(f"\nPrediccion para 3 horas de estudio: {prediccion[0]:.2f}")


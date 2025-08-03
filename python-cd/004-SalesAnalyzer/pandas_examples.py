import pandas as pd

# Crear DataFrame desde diccionario
data = {
    "Categoria": ["Electrónica", "Electrónica", "Ropa", "Ropa", "Alimentos"],
    "Ventas": [1000, 1500, 700, 800, 1200],
    "Unidades": [5, 7, 3, 4, 6]
}
df = pd.DataFrame(data)
print(df)

# Filtrar ventas mayores a 800
df_filtrado = df[df["Ventas"] > 800]
print(df_filtrado)

# Agrupar y sumar ventas por categoría
ventas_por_categoria = df.groupby("Categoria")["Ventas"].sum()
print(ventas_por_categoria)

# Promedio de unidades por categoría
promedio_unidades = df.groupby("Categoria")["Unidades"].mean()
print(promedio_unidades)

# Merge ejemplo
df1 = pd.DataFrame({
    "Producto": ["A", "B", "C"],
    "Precio": [10, 20, 30]
})

df2 = pd.DataFrame({
    "Producto": ["A", "B", "D"],
    "Stock": [100, 150, 200]
})

df_merge = pd.merge(df1, df2, on="Producto", how="inner")
print(df_merge)

# Exportar a Excel
df.to_excel("reporte.xlsx", index=False)

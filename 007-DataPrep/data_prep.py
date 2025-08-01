# data_prep.py

import pandas as pd
from dataprep import fill_nulls, normalize_column

# 1. Cargar los datos
df = pd.read_csv("data/my_data.csv")

# 2. Aplicar limpieza de nulos
df_clean = fill_nulls(df, strategy="median")

# 3. Normalizar columna de ventas
df_norm = normalize_column(df_clean, "ventas")

# 4. Mostrar resultados
print(df_norm.head())

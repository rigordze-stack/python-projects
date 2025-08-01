# DataPrep - Utilidades para limpieza y transformación de datos

DataPrep es un paquete de funciones reutilizables desarrollado para preparar conjuntos de datos antes de usarlos en análisis, reportes o tableros de inteligencia de negocios (BI). Contiene funciones clave para limpieza, detección de outliers, normalización y transformaciones estructurales. Cada función está documentada línea por línea para facilitar su comprensión y reutilización.

## Requisitos

- Python 3.7 o superior  
- Librerías necesarias: pandas, numpy

## Ejemplo de uso: 
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


---

## Autor
<p align="center">
Rigoberto Rodríguez 
</p>
<p align="center">
Full Stack .NET Developer 
</p>

<p align="center">
  <a href="https://dotnet.microsoft.com/" target="_blank">
    <img alt=".NET" src="https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=.net&logoColor=white" />
  </a>
  <a href="https://dotnet.microsoft.com/apps/aspnet" target="_blank">
    <img alt="ASP.NET Core" src="https://img.shields.io/badge/ASP.NET_Core-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" />
  </a>
  <a href="https://getbootstrap.com/" target="_blank">
    <img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
  </a>
  <a href="https://learn.microsoft.com/en-us/dotnet/desktop/wpf/" target="_blank">
    <img alt="WPF" src="https://img.shields.io/badge/WPF-512BD4?style=for-the-badge&logo=windows&logoColor=white" />
  </a>
  <a href="https://learn.microsoft.com/en-us/dotnet/csharp/" target="_blank">
    <img alt="C#" src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white" />
  </a>
  <a href="https://docs.microsoft.com/en-us/office/vba/api/overview/excel" target="_blank">
    <img alt="VBA" src="https://img.shields.io/badge/VBA-1E77B0?style=for-the-badge&logo=microsoft-excel&logoColor=white" />
  </a>
  <a href="https://www.python.org/" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  </a>
  <a href="https://www.microsoft.com/en-us/sql-server" target="_blank">
    <img alt="SQL Server" src="https://img.shields.io/badge/SQL_Server-D92F2F?style=for-the-badge&logo=microsoft-sql-server&logoColor=white" />
  </a>
  <a href="https://www.postgresql.org/" target="_blank">
    <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  </a>
  <a href="https://azure.microsoft.com/services/devops/" target="_blank">
    <img alt="Azure DevOps" src="https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azure-devops&logoColor=white" />
  </a>
  <a href="https://github.com/" target="_blank">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

## 📬 Contacto

- 📧 **rigordze@gmail.com**
- 🌐 [LinkedIn](https://www.linkedin.com/in/rigoberto-rodriguez-dev/)
- 💻 [GitHub](https://github.com/rigordze-stack/rigordze-stack)

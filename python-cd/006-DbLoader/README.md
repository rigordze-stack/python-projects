# DbLoader - Carga de datos a PostgreSQL desde Python

## Descripción

DbLoader es un script en Python diseñado para cargar datos desde un archivo CSV o Excel a una tabla PostgreSQL.  
El proceso incluye conexión segura a la base de datos, inserción masiva de filas (bulk insert) y validación del número de registros insertados para asegurar que la carga se realizó correctamente.

## Requisitos

- Python 3.7 o superior  
- PostgreSQL  
- Librerías de Python:
  - `psycopg2-binary` para la conexión a PostgreSQL  
  - `pandas` para la lectura y manipulación de datos  
  - `python-dotenv` para cargar variables de entorno  
- Archivo `.env` en la raíz del proyecto, guardado en codificación **UTF-8 sin BOM**, con la siguiente información:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=nombre_de_la_BD
DB_USER=postgres
DB_PASSWORD=tu_contraseña

## Uso

1. **Crear la tabla**  
 Ejecuta el script SQL `schema.sql` en tu cliente de PostgreSQL para crear la tabla `sales_data` si aún no existe.

2. **Configurar el entorno**   
 - Abre `.env`, reemplaza los valores de ejemplo con los de tu conexión real y guarda el archivo como UTF-8 sin BOM.

3. **Preparar los datos**  
 - Coloca tu archivo `data_to_load.csv` dentro de la carpeta `data/`.  
 - Asegúrate de que las columnas coincidan con el esquema: `categoria`, `producto`, `ventas`, `unidades`.

4. **Instalar dependencias**  
 En la terminal de tu proyecto, ejecuta:

 py -m pip install psycopg2-binary pandas python-dotenv

 5. **Ejecuta la carga con**
 py db_loader.py



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

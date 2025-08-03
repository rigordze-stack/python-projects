from pathlib import Path    # Para manejo de rutas
import os   # Carga os para leer variables de entorno
from dotenv import load_dotenv  # Carga el contenido de un archivo env a variables de entorno
import psycopg2 # Cliente PostgreSQL para Python
import pandas as pd # manejo de datos tabulares, tuplas

# cargamos las variables definidas en .env
load_dotenv()

# Obtenemos valores de conexion desde el entorno
DB_HOST     = os.getenv("DB_HOST", "localhost")
DB_PORT     = os.getenv("DB_PORT", 5432)
DB_NAME     = os.getenv("DB_NAME", "pythondb")
DB_USER     = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin1123$")

def connect_db():
    """
    Establece la conexion con PostgreSQL usando psycopg2
    """
    try:
        # Intentamos conectar con los parametros recibidos
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        # Imprime el error y retorna none si falla
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def insert_data_bulk(conn, df,table_name):
    """
    Insertamos todas las filas de un dataFrame en la tabla espcificada
    """
    
    # Creamos cursos para ejecutar la inserccion
    cursor = conn.cursor()
    # Convertimos cada fila del dataFrame en una tupla
    tuples = [tuple(x) for x in df.to_numpy()]
    # Preparamos la lista de columnas
    cols = ','.join(list(df.columns))
    
    # Armamos la consulta con placeholder %s para execute_values
    query =f"INSERT INTO {table_name} ({cols}) VALUES %s"
    try:
        # Importamos la funcion especializada para bulk insert
        from psycopg2.extras import execute_values
        execute_values(cursor, query, tuples)
        # Confirmamos los cambios en la base de datos
        conn.commit()
        print(f"{cursor.rowcount} filas insertadas.")
    except Exception as e:
        # En caso de error, revertimos la transaccion
        conn.rollback()
        print(f"Error en inserccion: {e}")
    finally:
        # Cerramos el cursor para liberar recursos
        cursor.close()
        
def validate_rows(conn, table_name):
    """
    Cuenta e imprime cuantas filas tiene la tabla destino
    """
    
    cursor = conn.cursor()
    try:
        # Ejecutamos un COUNT(*) para validar insercciones
        cursor.excute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Total filas en {table_name}: {count}")
    except Exception as e:
        print(f"Error al validar filas: {e}")
    finally:
        cursor.close()
        
def main():
    # Ruta al archivo CSV o Excel con datos
    input_file = Path("data/data_to_load.csv")
    # Nombre de la tabla destino en postgreSQL
    table_name = "sales_data"
    
    # Leemos los datos a un dataFrame de pandas
    df = pd.read_csv(input_file)
    
    # Abrimos la conexion
    conn = connect_db()
    if conn is None:
        return
    
    # Insertamos los datos en bloque
    insert_data_bulk(conn, df, table_name)
    # Validamos el numero de filas insertadas
    validate_rows(conn, table_name)
    
    # Cerramos la conexion
    conn.close()
    
if __name__ == "__main__":
    main()
    


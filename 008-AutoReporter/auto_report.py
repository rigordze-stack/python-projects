import pandas as pd
from datetime import datetime
import schedule
import time
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Configuramos las rutas principales
TEMPLATE_DIR = Path("templates") # Carpeta con la platilla HTML
OUTPUT_DIR = Path("out") # Carpeta donde se guardaran los reportes
DATA_FILE = Path("data/sales.csv") # Archivo de datos de ejemplo

# Creamos la carpeta de salida si no existe
OUTPUT_DIR.mkdir(parents=True,exist_ok=True)

def generate_kpis(df):
    """
    Calcula KPIs básicos (totales, primedio, top categoria)
    df: dataFrame con datos de ventas
    return: Diccionario con métricas
    """
    total_ventas = df["Ventas"].sum() # Suma total de ventas
    # Promedio de ventas
    promedio_ventas = df["Ventas"].mean()
    # Categoria con mayores ventas
    top_categoria = (
        df.groupby("Categoria")["Ventas"]
        .sum()
        .sort_values(ascending=False)
        .idxmax()
    )
    return {
        "total_ventas":total_ventas,
        "promedio_ventas":promedio_ventas,
        "top_categoria":top_categoria
    }
def render_html_report(kpis, template_name="report.html"):
        """
        Genera el reporte en formato HTML usando la plantilla Jinja2
        Kpis: Diccionario con las metricas calculadas
        template_name: Nombre de la plantilla en la carpeta templates
        """
        # Cargamos el entorno jinja2
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(template_name)
        
        # Fecha actual para el reporte
        fecha = datetime.now().strftime("%Y-%m-%d")
        
        # Renderizamos la plantilla con las metricas
        html_content = template.render(
            fecha=fecha,
            total_ventas=kpis["total_ventas"],
            promedio_ventas=kpis["promedio_ventas"],
            top_categoria=kpis["top_categoria"]
        )
        
        # Guardamos el archivo HTML
        output_file = OUTPUT_DIR / f"report_{fecha}.html"
        with open(output_file,"w",encoding="utf-8") as f:
            f.write(html_content)
        print(f"Reporte generado: {output_file}")
def job():
    """
    Tarea programada: carga datos, calcula KPIs y genera el reporte
    """
    print("Ejecuta tarea de generacion de reporte...")
    df = pd.read_csv(DATA_FILE) # Leemos los datos de ventas
    kpis = generate_kpis(df) # Calculamos las metricas
    render_html_report(kpis) # Generamos el reporte HTML
    
# Programamos la tarea para ejecutarse todos los días a las 12:00
schedule.every().day.at("12:20").do(job)

# Bucle infinito para que schedule se mantenga ejecutando
if __name__ == "__main__":
    print("Iniciando AutoReporter- Esperando ejecucion...")
    while True:
        schedule.run_pending()
        time.sleep(60) # Espera 60 segundos antes de volver a comprobar

    
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

def create_visual_kpis(input_path,output_dir):
    """
    Genera graficos KPIs a partir de datos de ventas
    
    Parametros
    input_path (str o Path): archivo csv con datos
    output_dir (str o Path): carpeta donde se guardaran los graficos
    """
    
    df = pd.read_csv(input_path) # Lee el archivo csv con pandas y lo guardamos en un Dataframe
    output_dir = Path(output_dir) # Convertimos la ruta de salida a un objeto path para facilidad de uso
    output_dir.mkdir(exist_ok=True, parents=True) # Creamos la carpeta de salida si no existe (incluye padres)
    
    # Creamos una figura para el grafico de barras con tamaño de 8x5 pulgadas
    plt.figure(figsize=(8,5))
    # Agrupamos las ventas por categoria y sumamos los valores
    ventas_por_categoria = df.groupby("Categoria")["Ventas"].sum().reset_index()
    # Dibujamos el grafico de barras con categorias y ventas totales
    plt.bar(ventas_por_categoria["Categoria"],ventas_por_categoria["Ventas"])
    # Ponemos titulo al grafico
    plt.title("Ventas Totales por Categoria")
    # Guardamos el grafico en la carpeta de salida como png
    plt.savefig(output_dir / "bar_chart.png")
    # Cerramos la figura para liberar memoria
    plt.close()
    
    # Iniciamos nueva figura para grafico de lineas
    plt.figure(figsize=(8,5))
    # Creamos grafico de lineas con seaborn, mostrando unidades por categoria
    sns.lineplot(data=df,x="Categoria", y="Unidades", markers="o")
    # Titulo del grafico
    plt.title("Unidades vendidas por categoria")
    # Guardamos grafico de lineas como PNG
    plt.savefig(output_dir / "line_plot.png")
    # Cerramos figura
    plt.close()
    
    # Nueva figura pra boxplot
    plt.figure(figsize=(8,5))
    # Creamos boxplot para distribucion de ventas por categoria
    sns.boxplot(x="Categoria", y="Ventas",data=df)
    # Titulo del boxplot
    plt.title("Distribucion de ventas por categoria")
    # Guardamos como png
    plt.savefig(output_dir / "boxplot.png")
    # Cerramos figura
    plt.close()
    
    # Nueva figura para histogramas
    plt.figure(figsize=(8,5))
    # Creamos histograma de las ventas con 5 intervalos
    plt.hist(df["Ventas"],bins=5)
    # Titulo del histograma
    plt.title("Histograma de Ventas")
    # Guardamos histograma como PNG
    plt.savefig(output_dir / "histogram.png")
    # Cerramos figura
    plt.close()
    
if __name__ == "__main__":
    # Definimos ruta al archivo CSV con datos de ventas
    input_file = Path("data/sales.csv")
    # Definimos carpeta donde se guardaran los graficos
    output_folder = Path("figures")
    
    # Ejecutamos la funcion principal que crea los graficos kpi
    create_visual_kpis(input_file,output_folder)
    
    
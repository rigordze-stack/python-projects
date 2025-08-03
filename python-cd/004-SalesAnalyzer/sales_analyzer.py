import pandas as pd
from pathlib import Path

def analyze_sales(input_path, output_path, top_n=3):
    """
    Analiza venta por categoria y genera un resumen y top categorias
    
    Parametros:
    input_path (str o Path): Ruta al archivo CSV con datos de ventas
    output_path (str_Path): Ruta donde se guarda el archivo excel de resumen
    top_n (int): Numero de categorias top a mostrar
    
    Genera:
    Archivo excel con hojas Resumen y Top Categorias
    """
    
    df = pd.read_csv(input_path)
    
    resumen = pd.DataFrame()
    resumen["Ventas Totales"] = df.groupby("Categoria")["Ventas"].sum()
    resumen["Promedio Ventas"] = df.groupby("Categoria")["Ventas"].mean()
    
    top_categorias = resumen.sort_values(by="Ventas Totales",ascending=False).head(top_n)
    
    with pd.ExcelWriter(output_path) as writer:
        resumen.to_excel(writer, sheet_name="Resumen")
        top_categorias.to_excel(writer,sheet_name="Top Categorias")
        
if __name__ == "__main__":
    input_file = Path("data/sales.csv")
    output_file = Path("reports/sales_summary.xlsx")
    analyze_sales(input_file,output_file)
    

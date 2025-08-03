import pandas as pd
from pathlib import Path

def main():
    # Definimos la ruta del archivo original
    input_file = Path("data/sales_raw.csv")
    output_file = Path("exports/final_dataset.csv")
    
    # Leemos los datos originales
    df = pd.read_csv(input_file)
    
    # -- Limpieza basica --
    # Eliminamos filas con datos incompletos
    df.dropna(inplace=True)
    
    # Aseguramos que los tipos de datos sean correctos
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["PrecioUnitario"] = pd.to_numeric(df["PrecioUnitario"])
    df["Cantidad"] = pd.to_numeric(df["Cantidad"])
    
    # --- Agregamos columnas utiles ---
    df["TotalVenta"] = df["Cantidad"] * df["PrecioUnitario"]
    
    # --- Guardamos el archivo en limpio --
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"Dataset exportado correctamente a {output_file}")
    
if __name__ == "__main__":
    main()
    

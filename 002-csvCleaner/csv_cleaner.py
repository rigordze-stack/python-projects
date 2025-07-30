import csv
from pathlib import Path

def clean_csv(input_path, output_path):
    seen = set()
    cleaned_rows = []
    
    with open(input_path, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        cleaned_rows.append(header)
        
        for row in reader:
            # limpiar cada celda trim y minusculas
            cleaned_row = [cell.strip().lower() for cell in row]
            
            # convertir fila a tupla para set
            row_tuple = tuple(cleaned_row)
            
            if row_tuple not in seen:
                seen.add(row_tuple)
                cleaned_rows.append(cleaned_row)
                
    with open(output_path, 'w',newline='',encoding='utf-8') as outfile:
        write = csv.writer(outfile)
        write.writerows(cleaned_rows)
        
if __name__ == "__main__":
    input_file = Path("data/raw.csv")
    output_file = Path("data/clean.csv")
    
    clean_csv(input_file,output_file)
            
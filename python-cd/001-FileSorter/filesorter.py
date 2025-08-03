import os
import shutil

def ensure_unique_path(dest_path: str)-> str:
    """Si existe un archivo con el mismo nombre, agrega 1, 2, ... antes de la extension"""
    if not os.path.exists(dest_path):
        return dest_path
    
    base, ext = os.path.splitext(dest_path)
    counter = 1
    while True:
        candidate = f"{base} ({counter}){ext}"
        if not os.path.exists(candidate):
            return candidate
        counter += 1

def sort_files_by_extension(folder_path: str):
    if not os.path.isdir(folder_path):
        print("Ruta no valida")
        return
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file_name)
        if not os.path.isfile(file_path):
            continue # ignora subcarpetas

        # Detecta extension o marca no extension
        if '.' in file_name and not file_name.startswith('.'):
            ext = file_name.rsplit('.',1)[-1].lower()
        else:
            ext = 'sin_extension'

        target_dir = os.path.join(folder_path,f"{ext}_files")
        os.makedirs(target_dir,exist_ok=True)

        dest = os.path.join(target_dir, file_name)
        dest = ensure_unique_path(dest) # evita sobrescribir

        shutil.move(file_path, dest)

    print("Archivos organizados correctamente")

if __name__ == "__main__":
    # cambiar ruta a una de prueba
    sort_files_by_extension(r"C:\Users\RRodriguez\Downloads")

        


    
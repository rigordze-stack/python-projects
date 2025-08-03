import os
import shutil

TYPE_MAP = {
"Imágenes": {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"},
    "Documentos": {"pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "csv"},
    "Audio": {"mp3", "wav", "aac", "flac", "ogg", "m4a"},
    "Video": {"mp4", "mkv", "avi", "mov", "wmv"},
    "Comprimidos": {"zip", "rar", "7z", "tar", "gz"},
    "Código": {"py", "js", "ts", "html", "css", "json", "xml", "yml", "yaml", "cs", "java", "cpp", "c", "sql"}
}

def get_categoria(ext: str)->str:
    if not ext:
        return "Sin_extension"
    for category,extensions in TYPE_MAP.items():
        if ext in extensions:
            return category
        return "Otros"

def ensure_unique_path(dest_path: str) -> str:
    if not os.path.exists(dest_path):
        return dest_path
    base, ext = os.path.splitext(dest_path)
    i = 1
    while True:
        candidate = f"{base} ({i}){ext}"
        if not os.path.exists(candidate):
            return candidate
        i += 1

def sort_files_by_tipe(folder_path: str):
    if not os.path.isdir(folder_path):
        print("Ruta no valida")
        return
    
    for name in os.listdir(folder_path):
        src = os.path.join(folder_path, name)
        if not os.path.isfile(src):
            continue

        # extension sin el punto
        ext = ""
        if '.' in name and not name.startswith('.'):
            ext = name.rsplit('.',1)[-1].lower()

        category = get_categoria(ext)
        target_dir = os.path.join(folder_path, category)
        os.makedirs(target_dir, exist_ok=True)

        dest = os.path.join(target_dir, name)
        dest = ensure_unique_path(dest)
        shutil.move(src, dest)

    print("Archivos organizados por tipo correctamente.")

if __name__ == "__main__":
    # Ruta de prueba
    sort_files_by_tipe(r"C:\Users\RRodriguez\Downloads")
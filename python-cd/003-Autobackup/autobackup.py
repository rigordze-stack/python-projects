import os
import shutil
import logging
from pathlib import Path

# Configuración del módulo logging para registrar eventos y errores en un archivo de log.
logging.basicConfig(
    filename='logs/backup.log',              # Archivo donde se guardarán los logs
    level=logging.INFO,                      # Nivel de registro (INFO y superior)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de cada línea en el log
)

def incremental_backup(src, dst):
    """
    Realiza un respaldo incremental de la carpeta src a la carpeta dst.
    Solo copia archivos nuevos o modificados desde la última copia.
    
    Parámetros:
    src (str o Path): Ruta de la carpeta origen a respaldar.
    dst (str o Path): Ruta de la carpeta destino donde se almacenará el respaldo.
    """
    src = Path(src)
    dst = Path(dst)
    
    # Crear carpeta destino si no existe
    if not dst.exists():
        dst.mkdir(parents=True)
        logging.info(f'Carpeta de destino creada: {dst}')
    
    # Recorrer todas las subcarpetas y archivos de la carpeta origen
    for root, dirs, files in os.walk(src):
        rel_path = Path(root).relative_to(src)   # Ruta relativa para mantener estructura
        dest_dir = dst / rel_path                 # Ruta destino correspondiente
        
        # Crear carpeta destino si no existe
        if not dest_dir.exists():
            dest_dir.mkdir(parents=True)
            logging.info(f'Carpeta creada: {dest_dir}')
        
        # Iterar por cada archivo en la carpeta actual
        for file in files:
            src_file = Path(root) / file
            dst_file = dest_dir / file
            
            # Copiar archivo si no existe o si fue modificado (fecha de modificación más reciente)
            if not dst_file.exists() or src_file.stat().st_mtime > dst_file.stat().st_mtime:
                shutil.copy2(src_file, dst_file)  # copy2 copia metadata también
                logging.info(f'Archivo copiado: {src_file} a {dst_file}')

if __name__ == "__main__":
    # Rutas de ejemplo, pueden modificarse según entorno
    origen = 'data/origen'
    destino = 'data/backup'
    
    logging.info('Inicio del respaldo incremental')
    incremental_backup(origen, destino)
    logging.info('Respaldo finalizado')

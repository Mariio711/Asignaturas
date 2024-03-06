import os
import shutil

def mover_archivos_a_directorio_actual():
    directorio_actual = os.getcwd()
    for raiz, dirs, archivos in os.walk(directorio_actual):
        for archivo in archivos:
            ruta_archivo = os.path.join(raiz, archivo)
            if raiz != directorio_actual:  # Evitar mover archivos que ya están en el directorio actual
                shutil.move(ruta_archivo, directorio_actual)

mover_archivos_a_directorio_actual()
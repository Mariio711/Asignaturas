"""15. Realice un script en Python que mueva al directorio actual, todos los
archivos contenidos en subdirectorios del mismo. Tenga en cuenta que un
directorio puede contener a su vez otros directorios y que la longitud en
la jerarquía del árbol no está definida y por tanto, el script debe funcionar
para todos los casos"""

import shutil, os

# Lista para almacenar las rutas de los archivos a mover
archivos_a_mover = []

# Primero, recopilamos todas las rutas de los archivos
for raiz, dirs, archivos in os.walk('.', topdown=False):
    for nombre in archivos:
        ruta_origen = os.path.join(raiz, nombre)
        archivos_a_mover.append(ruta_origen)

# Luego, movemos los archivos al directorio actual
for ruta_origen in archivos_a_mover:
    nombre_archivo = os.path.basename(ruta_origen)
    ruta_destino = os.path.join('.', nombre_archivo)
    # Verificar si el archivo ya existe en el destino para evitar sobrescrituras
    if not os.path.exists(ruta_destino):
        shutil.move(ruta_origen, '.')
    else:
        print(f"El archivo {nombre_archivo} ya existe en el destino. No se movió.")
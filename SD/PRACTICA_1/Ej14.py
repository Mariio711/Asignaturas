"""14.Implemente un script en Python, utilizando el módulo os, que liste todos
los ficheros del directorio actual junto a su tamaño en bytes. Por último, el
script mostrará la suma total del tamaño de los ficheros del directorio. Se
deben incluir, además, los ficheros existentes en subdirectorios."""

import os

totalbytes = 0

for raiz, dirs, archivos in os.walk('.'): # os.walk: Para cada directorio en el árbol enraizado en el directorio top (incluido top), produce una tupla de 3 tuplas (dirpath, dirnames, filenames).
    for nombre in archivos:
        ruta = os.path.join(raiz, nombre)
        tamaño = os.path.getsize(ruta)
        print(f"{ruta}: {tamaño} bytes")
        totalbytes += tamaño
print(f"Total: {totalbytes} bytes")


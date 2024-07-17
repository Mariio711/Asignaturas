"""16. Realizar un script en Python que imprima por pantalla el directorio de
trabajo actual, junto a la lista de ficheros existentes en dicho directorio.
Posteriormente, el mismo script permitirá al usuario renombrar un
fichero. Para ello solicitará al usuario el nombre del fichero que quiere
renombrar y el nuevo nombre que quiere darle. Se deben gestionar
correctamente las posibles excepciones que puedan darse en la ejecución
del script."""

import os

def mostrar_archivos_cwd():
    print(os.listdir(os.getcwd()))

def mod_filename_cwd(archivo, newname):

    if not isinstance(archivo, str) or not os.path.isfile(archivo):
        raise ValueError("El archivo proporcionado no es una cadena o no esiste")
    
    if not isinstance(newname, str):
        raise ValueError("El nuevo nombre no es una cadena")
    
    os.rename(archivo, newname)


mostrar_archivos_cwd()
archivo = str(input("Nombre del archivo a renombrar: "))
newname = str(input("Nuevo nombre: "))

mod_filename_cwd(archivo, newname)
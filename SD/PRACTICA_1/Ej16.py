import os

# Imprimir el directorio actual
print("Directorio actual:", os.getcwd())

# Imprimir la lista de archivos
print("Archivos:")
for archivo in sorted(os.listdir('.')):
    print(archivo)


# Pedir al usuario el nombre del archivo a renombrar y el nuevo nombre
archivo_a_renombrar = input("Introduce el nombre del archivo a renombrar: ")
nuevo_nombre = input("Introduce el nuevo nombre: ")

# Intentar renombrar el archivo
try:
    os.rename(archivo_a_renombrar, nuevo_nombre)
    print("Archivo renombrado con éxito.")
except FileNotFoundError:
    print("El archivo no existe.")
except Exception as e:
    print("Error al renombrar el archivo:", str(e))
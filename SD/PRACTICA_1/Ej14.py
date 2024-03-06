import os



contenido = os.listdir('.')
bytes_archivos = [os.path.getsize(archivo) for archivo in contenido if os.path.isfile(archivo)]
contenido_con_bytes = zip(contenido, bytes_archivos)

for archivo, tamano in contenido_con_bytes:
    print(f'Archivo: {archivo}, Tamaño: {tamano} bytes')
"""implementacion de socket UDP servidor"""

import socket, os

# Verifica si un archivo ya existe en el sistema
def archivo_existe(nombre_archivo):
    return os.path.isfile(nombre_archivo)

# Recibe un archivo a través de una conexión de socket y lo guarda
def recibir_archivo(s, nombre_archivo):
    # Primero, lee el tamaño del archivo
    tamanio_archivo = s.recvfrom(1024)[0].decode("utf-8")
    tamanio_archivo = int(tamanio_archivo)  # Asegúrate de convertirlo a entero

    recibido = 0
    with open(nombre_archivo, "wb") as f:
        while recibido < tamanio_archivo:
            datos = s.recvfrom(1024)[0]
            if not datos:
                break  # Esto no debería ocurrir si el cliente envía los datos correctamente
            f.write(datos)
            recibido += len(datos)  # Actualiza el contador de bytes recibidos

# Configura y ejecuta el servidor para recibir archivos
def iniciar_servidor(dir, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((dir, puerto))
    print(f"Servidor asignado en {dir} : {puerto} ...")

    whiling = True

    while whiling:
        nombre_archivo, addr = s.recvfrom(1024)
        print(f"mensaje recibido de {addr}")
        print(f"El cliente desea enviar: {nombre_archivo}")

        if archivo_existe(nombre_archivo):
            s.sendto(b"EXISTE", addr)
            respuesta = s.recvfrom(1024)[0].decode("utf-8")

            if respuesta != 's':
                print(f"El cliente ({addr}) ha cancelado la transferencia de {nombre_archivo}")
                s.close()  # Cierra la conexión si el cliente decide no sobrescribir el archivo
                whiling = False
            else:
                s.sendto(b"OK", addr)  # Indica al cliente que puede enviar el archivo
                recibir_archivo(s, nombre_archivo)  # Recibe y guarda el archivo
                print(f"Archivo {nombre_archivo} recibido")
                s.sendto(b"Recibido", addr)  # Confirma la recepción del archivo
                s.close()  # Cierra la conexión
                whiling = False
        else:
            s.sendto(b"OK", addr)  # Indica al cliente que puede enviar el archivo
            recibir_archivo(s, nombre_archivo)  # Recibe y guarda el archivo
            print(f"Archivo {nombre_archivo} recibido")
            s.sendto(b"Recibido", addr)  # Confirma la recepción del archivo
            s.close()  # Cierra la conexión
            whiling = False

if __name__ == "__main__":
    iniciar_servidor("localhost", 1026)
"""implementacion de socket TCP servidor"""

import socket, os

# Verifica si un archivo ya existe en el sistema
def archivo_existe(nombre_archivo):
    return os.path.isfile(nombre_archivo)

# Recibe un archivo a través de una conexión de socket y lo guarda
def recibir_archivo(conn, nombre_archivo):
    # Primero, lee el tamaño del archivo
    tamanio_archivo = conn.recv(1024).decode()
    tamanio_archivo = int(tamanio_archivo)  # Asegúrate de convertirlo a entero

    recibido = 0
    with open(nombre_archivo, "wb") as f:
        while recibido < tamanio_archivo:
            datos = conn.recv(1024)
            if not datos:
                break  # Esto no debería ocurrir si el cliente envía los datos correctamente
            f.write(datos)
            recibido += len(datos)  # Actualiza el contador de bytes recibidos

# Configura y ejecuta el servidor para recibir archivos
def iniciar_servidor(dir, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((dir, puerto))
    s.listen(1)
    print(f"Esperando conexión en {dir}:{puerto} ...")

    while True:
        conn, addr = s.accept()
        print(f"Conexion establecida con{addr}")

        nombre_archivo = conn.recv(1024).decode("utf-8")
        print(f"El cliente desea enviar: {nombre_archivo}")

        if archivo_existe(nombre_archivo):
            conn.send(b"EXISTE")
            respuesta = conn.recv(1024).decode("utf-8")

            if respuesta != 's':
                conn.close()  # Cierra la conexión si el cliente decide no sobrescribir el archivo
                continue
            else:
                conn.send(b"OK")  # Indica al cliente que puede enviar el archivo

                recibir_archivo(conn, nombre_archivo)  # Recibe y guarda el archivo
                print(f"Archivo {nombre_archivo} recibido")
                conn.send(b"Recibido")  # Confirma la recepción del archivo
                conn.close()  # Cierra la conexión

if __name__ == "__main__":
    iniciar_servidor("localhost", 1026)






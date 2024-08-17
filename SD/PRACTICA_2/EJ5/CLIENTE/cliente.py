"""implementacion de socket TCP cliente"""

import socket, os

def inicio_socket(servidor, puerto):
    
    #cambiar directorio de trabajo
    os.chdir("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ5\CLIENTE")


    #creamos el socket con SOCK_STREAM puesto que es TCP y conectamos con el servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((servidor, puerto))
    return s

#recibe un archivo jpg por socket
def recibir_jpg(conn, nombre_archivo):
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
    print(f"Archivo {nombre_archivo} recibido")
    conn.send(b"Recibido")  # Confirma la recepción del archivo
    conn.close()  # Cierra la conexión

def inicio(dir, port):
    #iniciamos la conexion con el servidor
    cliente = inicio_socket(dir, port)

    #recibimos mensaje del servidor que nos pedira el nombre del archivo jpg que queremos descargar
    mensaje = cliente.recv(1024).decode("utf-8")
    respuesta = str(input(f"Servidor: {mensaje}"))
    cliente.send(respuesta.encode("utf-8"))

    recibir_jpg(cliente, respuesta)


if __name__ == "__main__":
    inicio("localhost", 1026)
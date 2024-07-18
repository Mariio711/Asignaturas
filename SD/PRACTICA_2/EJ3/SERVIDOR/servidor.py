"""implementacion de socket TCP servidor recibir archivo y enviarlo invertido"""

import socket, os

def invertir_txt(nombre_archivo):
    with open("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ3\SERVIDOR" + os.sep + nombre_archivo, "r") as f:
        txt = f.read()
        txt = txt[::-1]
    with open("invertido.txt", "w") as f:
        f.write(txt)

#envia un archivo
def enviar_txt(s, ruta_archivo, nombre_archivo):
    
    # Primero, envía el tamaño del archivo
    tamanio_archivo = os.path.getsize(ruta_archivo)
    s.send(str(tamanio_archivo).encode("utf-8"))

    notificacion = s.recv(1024).decode("utf-8")
    if notificacion == "Recibido":

        with open(ruta_archivo, "rb") as fichero:
                datos = fichero.read(1024)
                while datos:
                    s.send(datos)
                    datos = fichero.read(1024)
        print("Fichero enviado con exito")
        notificacion = s.recv(1024).decode("utf-8")
        if notificacion == "Recibido":
            print("El servidor ha recibido el archivo. Eliminando archivo")
            os.remove("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ3\SERVIDOR" + os.sep + nombre_archivo)
    else:
        print("No se ha recibido tamaño de archivo ... \nCerrando conexión")
        s.close()
        exit

# Recibe un archivo a través de una conexión de socket y lo guarda
def recibir_archivo(conn, nombre_archivo):
    # Primero, lee el tamaño del archivo
    tamanio_archivo = conn.recv(1024).decode("utf-8")
    tamanio_archivo = int(tamanio_archivo)  # Asegúrate de convertirlo a entero

    conn.send(b"Recibido")

    recibido = 0
    with open("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ3\SERVIDOR" + os.sep + nombre_archivo, "wb") as f:
        while recibido < tamanio_archivo:
            datos = conn.recv(1024)
            if not datos:
                break  # Esto no debería ocurrir si el cliente envía los datos correctamente
            f.write(datos)
            recibido += len(datos)  # Actualiza el contador de bytes recibidos
    conn.send(b"Recibido")  # Confirma la recepción del archivo
    return tamanio_archivo
    
#inicia el socket
def inicio_socket(dir, puerto):
    #creamos el socket con SOCK_STREAM puesto que es TCP y conectamos con el servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((dir, puerto))
    s.listen(1)
    print(f"Esperando conexión en {dir}:{puerto} ...")
    conn, addr = s.accept()
    print(f"Conexion establecida con{addr}")
    return conn, s

def principal(dir, puerto):

    #iniciamos socket y conectamos con el cliente
    cliente, servidor = inicio_socket(dir, puerto)

    #recibimos la solicitud de envio de fichero
    nombre_fichero = cliente.recv(1024).decode("utf-8")

    #recibimos el fichero
    tamanio_archivo = recibir_archivo(cliente, nombre_fichero)

    #invertimos el contenido
    invertir_txt(nombre_fichero)

    #enviamos el fichero invertido
    enviar_txt(cliente, os.getcwd()+"/invertido.txt", nombre_fichero)

    #cerramos conexiones
    cliente.close()
    servidor.close()

if __name__ == "__main__":
    principal("localhost", 1026)
"""implementacion de socket TCP servidor"""

import socket, os

def inicio_socket(dir, puerto):
    
    #cambiar directorio de trabajo
    os.chdir("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ5\SERVIDOR")


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((dir, puerto))
    s.listen(1)
    print(f"Esperando conexión en {dir}:{puerto} ...")

    conn, addr = s.accept()
    print(f"Conexion establecida con{addr}")

    return s, conn

# Verifica si un archivo ya existe en el sistema
def archivo_existe(nombre_archivo):
    return os.path.isfile(nombre_archivo)

#envia un archivo jpg si existe
def enviar_jpg(nombre, conn, s):

    #comprobamos si el archivo existe
    if not archivo_existe(nombre):

        conn.send(b"La imagen no existe cerando conexion")
        conn.close()
        s.close()
    else:
        ruta_archivo = os.getcwd() + os.sep + nombre

        # Primero, envía el tamaño del archivo
        tamanio_archivo = os.path.getsize(ruta_archivo)
        conn.send(str(tamanio_archivo).encode("utf-8"))
        
        with open(ruta_archivo, "rb") as fichero:
            datos = fichero.read(1024)
            while datos:
                conn.send(datos)
                datos = fichero.read(1024)

        print("Fichero enviado con exito")
        notificacion = conn.recv(1024).decode("utf-8")

        if notificacion == "Recibido":
            print("El cliente ha recibido el archivo. cerrando conexion")
        else:
            print("El cliente no ha recibido el archivo. cerrando conexion, intentelo de nuevo mas tarde")

        conn.close()
        s.close()

def inicio (dir, port):

    #iniciamos servidor en direccion y puerto
    servidor, cliente = inicio_socket(dir, port)

    #pedimos al cliente el nombre del archivo jpg que desea
    cliente.send(b"Escriba el nombre de la imagen que quiere descargar (con extension .jpg)\n")

    nombre = cliente.recv(1024).decode("utf-8")

    #enviamos la imagen
    enviar_jpg(nombre, cliente, servidor)

if __name__ == "__main__":
    inicio("localhost", 1026)

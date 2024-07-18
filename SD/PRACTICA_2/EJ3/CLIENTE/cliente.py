"""implementacion de socket TCP cliente enviar archivo y recibirlo invertido"""

import socket, os

#envia un archivo
def enviar_txt(s, ruta_archivo):
    
    # Primero, envía el tamaño del archivo
    tamanio_archivo = os.path.getsize(ruta_archivo)
    s.send(str(tamanio_archivo).encode("utf-8"))
    
            
    with open(ruta_archivo, "rb") as fichero:
            datos = fichero.read(1024)
            while datos:
                s.send(datos)
                datos = fichero.read(1024)
    print("Fichero enviado con exito")
    notificacion = s.recv(1024).decode("utf-8")
    if notificacion == "Recibido":
        print("El servidor ha recibido el archivo. Eliminando archivo")
        os.remove(ruta_archivo)

# Recibe un archivo a través de una conexión de socket y lo guarda
def recibir_archivo(conn, nombre_archivo):
    # Primero, lee el tamaño del archivo
    tamanio_archivo = conn.recv(1024).decode("utf-8")
    tamanio_archivo = int(tamanio_archivo)  # Asegúrate de convertirlo a entero

    recibido = 0
    with open(nombre_archivo, "wb") as f:
        while recibido < tamanio_archivo:
            datos = conn.recv(1024)
            if not datos:
                break  # Esto no debería ocurrir si el cliente envía los datos correctamente
            f.write(datos)
            recibido += len(datos)  # Actualiza el contador de bytes recibidos
    conn.send(b"Recibido")  # Confirma la recepción del archivo
    return tamanio_archivo
    
#inicia el socket
def inicio_socket(servidor, puerto):
    #creamos el socket con SOCK_STREAM puesto que es TCP y conectamos con el servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((servidor, puerto))
    return s

def principal(servidor, puerto, ruta_archivo):

    #iniciamos el socket y conectamos con el servidor
    s = inicio_socket(servidor, puerto)

    #se solicita enviar un fichero al servidor especificando el nombre
    nombre_fichero = ruta_archivo.split('/')[-1]
    s.send(nombre_fichero.encode("utf-8"))

    #enviamos el txt
    enviar_txt(s, ruta_archivo)

    #recibimos el txt invertido
    tamanio_archivo = recibir_archivo(s, "invertido.txt")

    with open("invertido.txt", "r") as f:
        linea = f.read(1024)
        print(linea)
    print(f"El tamaño del archivo es: {tamanio_archivo} bytes")
    
    #cerramos conexion
    s.close()

if __name__ == "__main__":
    principal("localhost", 1026, "C:/REPOS-GIT/Asignaturas/SD/PRACTICA_2/EJ3/CLIENTE/archivo.txt")
    


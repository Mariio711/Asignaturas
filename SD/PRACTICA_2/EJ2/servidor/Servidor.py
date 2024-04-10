#Servidor TCP
import socket
import os

def archivo_existe(nombre_archivo):
    return os.path.isfile(nombre_archivo)

def recibir_archivo(conn, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        while True:
            datos = conn.recv(1024)
            if not datos:
                # El cliente ha cerrado la conexión, por lo que salimos del bucle
                break
            archivo.write(datos)

def iniciar_servidor(direccion, puerto):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direccion, puerto))
    servidor.listen(1)
    print(f"Servidor escuchando en {direccion}:{puerto}")

    while True:
        conn, addr = servidor.accept()
        print(f"Conexión establecida desde {addr}")

        nombre_archivo = conn.recv(1024).decode('utf-8')
        print(f"Cliente desea enviar: {nombre_archivo}")
        
        if archivo_existe(nombre_archivo):
            conn.send(b"EXISTE")
            respuesta = conn.recv(1024).decode('utf-8')
            if respuesta != "SI":
                conn.close()
                continue
        else:
            conn.send(b"NO_EXISTE")

        recibir_archivo(conn, nombre_archivo)
        print(f"Archivo {nombre_archivo} recibido.")
        conn.send(b"Recibido")
        conn.close()

if __name__ == "__main__":
    iniciar_servidor("localhost", 65432)
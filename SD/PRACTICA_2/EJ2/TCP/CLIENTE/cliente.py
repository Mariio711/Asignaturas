"""implementacion de socket TCP cliente"""

import socket, os

def enviar_archivos(servidor, puerto, ruta_archivo):
    #creamos el socket con SOCK_STREAM puesto que es TCP y conectamos con el servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((servidor, puerto))

    #se solicita enviar un fichero al servidor especificando el nombre
    nombre_fichero = ruta_archivo.split('/')[-1]
    s.send(nombre_fichero.encode("utf-8"))

    #luego recibimos la respuesta del servidor, si es afirmativa enviamos el fichero y si el fichero existe 
    #el servidor nos poreguntara si queremos sobreescribirlo
    respuesta = s.recv(1024).decode("utf-8")

    if respuesta != "EXISTE":
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
        s.close()
    else:
        print("El fichero ya existe, ¿desea sobreescribirlo? (s/n): ")
        accion = input()
        s.send(accion.encode("utf-8"))

        if accion != 's':
            print("Trasnferencia cancelada")
            s.close()
            return
        
        respuesta = s.recv(1024).decode("utf-8")
        if respuesta == "OK":
            
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
            s.close()
        else:
            print("Fichero no enviado")
            s.close()

if __name__ == "__main__":
    enviar_archivos('localhost', 1026, 'C:/REPOS-GIT/Asignaturas/SD/PRACTICA_2/EJ2/TCP/CLIENTE/fichero.pdf')
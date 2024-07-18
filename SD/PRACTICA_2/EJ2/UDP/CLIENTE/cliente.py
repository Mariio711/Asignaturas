"""implementacion de socket UDP cliente"""

import socket, os

def enviar_archivo(HOST, PORT, ruta_archivo):

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #se solicita enviar un fichero al servidor especificando el nombre
    nombre_fichero = ruta_archivo.split('/')[-1]
    cliente.sendto(str.encode(nombre_fichero), (HOST, PORT))

    #luego recibimos la respuesta del servidor, si es afirmativa enviamos el fichero y si el fichero existe 
    #el servidor nos poreguntara si queremos sobreescribirlo
    respuesta = cliente.recvfrom(1024)[0].decode("utf-8")

    print(respuesta)

    if respuesta != "EXISTE":

        # Primero, envía el tamaño del archivo
        tamanio_archivo = os.path.getsize(ruta_archivo)
        cliente.sendto(str.encode(str(tamanio_archivo)), (HOST, PORT))

        with open(ruta_archivo, "rb") as fichero:
            datos = fichero.read(1024)
            while datos:
                cliente.sendto(datos, (HOST, PORT))
                datos = fichero.read(1024)
        print("Fichero enviado con exito")
        notificacion = cliente.recvfrom(1024)[0].decode("utf-8")
        if notificacion == "Recibido":
            print("El servidor ha recibido el archivo. Eliminando archivo")
            os.remove(ruta_archivo)
        cliente.close()
    else:
            print("El fichero ya existe, ¿desea sobreescribirlo? (s/n): ")
            accion = input()
            cliente.sendto(accion.encode("utf-8"), (HOST, PORT))

            if accion != 's':
                print("Trasnferencia cancelada")
                cliente.close()
                return
            
            respuesta = cliente.recvfrom(1024)[0].decode("utf-8")
            if respuesta == "OK":
                
                # Primero, envía el tamaño del archivo
                tamanio_archivo = os.path.getsize(ruta_archivo)
                cliente.sendto(str.encode(str(tamanio_archivo)), (HOST, PORT))

                with open(ruta_archivo, "rb") as fichero:
                    datos = fichero.read(1024)
                    while datos:
                        cliente.sendto(datos, (HOST, PORT))
                        datos = fichero.read(1024)
                print("Fichero enviado con exito")
                notificacion = cliente.recvfrom(1024)[0].decode("utf-8")
                if notificacion == "Recibido":
                    print("El servidor ha recibido el archivo. Eliminando archivo")
                    os.remove(ruta_archivo)
                cliente.close()
            else:
                print("Fichero no enviado")
                cliente.close()

if __name__ == "__main__":
    enviar_archivo('localhost', 1026, 'C:/REPOS-GIT/Asignaturas/SD/PRACTICA_2/EJ2/UDP/CLIENTE/fichero.pdf')

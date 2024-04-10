#Cliente TCP
import socket
import os

def enviar_archivo(servidor, puerto, ruta_archivo):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((servidor, puerto))
    
    nombre_archivo = ruta_archivo.split('/')[-1]
    cliente.send(nombre_archivo.encode('utf-8'))

    respuesta = cliente.recv(1024).decode('utf-8')
    if respuesta == "EXISTE":
        accion = input(f"El archivo {nombre_archivo} ya existe en el servidor. ¿Desea sobrescribirlo? (SI/NO): ")
        cliente.send(accion.encode('utf-8'))
        if accion != "SI":
            print("Transferencia cancelada.")
            cliente.close()
            return
        
    with open(ruta_archivo, 'rb') as archivo:
        datos = archivo.read(1024)
        while datos:
            cliente.send(datos)
            datos = archivo.read(1024)

    print("Archivo enviado.")
    notificacion = cliente.recv(1024).decode('utf-8')
    if notificacion == "Recibido":
        print("Servidor ha recibido el archivo. Eliminando archivo local...")
        os.remove(ruta_archivo)
    cliente.close()

if __name__ == "__main__":
    enviar_archivo('localhost', 65432, 'SD\PRACTICA_2\EJ2\hola.pdf')
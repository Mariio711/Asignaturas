"""implementacion de socket UDP cliente conversacion con servidor"""

import socket

def conversacion(cliente, addr, mensaje):
    
    respuesta = str(input(f"Servidor: {mensaje}"))

    cliente.sendto(respuesta.encode("utf-8"), addr)

    while respuesta != "cerrar":

        mensaje = cliente.recvfrom(1024)[0].decode("utf-8")

        print("para terminar la conversacion escribe 'cerrar'")
        respuesta = str(input(f"Servidor: {mensaje}"))

        cliente.sendto(respuesta.encode("utf-8"), addr)
        mensaje = cliente.recvfrom(1024)[0].decode("utf-8")
        print(f"Servidor: {mensaje}")
        
    cliente.close()



def inicio(dir, port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cliente.sendto("Hola servidor".encode("utf-8"), (dir, port))

    mensaje , addr = cliente.recvfrom(1024)
    
    conversacion(cliente, addr, mensaje.decode("utf-8"))
    
if __name__ == "__main__":
    inicio("localhost", 1026)
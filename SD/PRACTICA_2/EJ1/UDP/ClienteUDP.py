"""implementacion de socket UDP cliente"""

import socket


#establecemos la direccion y puerto del SERVIDOR
HOST = 'localhost'
PORT = 1025

#creamos el socket con SOCK_DGRAM puesto que es UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#enviamos directamente un mensaje al servidor sin conexiones ni vainas (UDP) con sendto()
s.sendto("Hola servidor, soy el cliente".encode("utf-8"), (HOST, PORT))

#cerramos el socket
s.close()
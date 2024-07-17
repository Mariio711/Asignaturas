"""implementacion de socket UDP servidor"""

import socket


#establecemos la direccion y puerto del servidor
HOST = 'localhost'
PORT = 1025

#creamos el socket con SOCK_DGRAM puesto que es UDP y le asignamos una direccion y un puerto (la del servidor)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

#luego nos mantenemos a la espera a que entre algun mensaje por ese puerto (de cualquier cliente)
print("Nos mantenemos a la espera . . .")#el print se hace antes por que el recv UDP es bloqueante y no seguira la ejecucion hasta que reciba un mensaje
mensaje, addr = s.recvfrom(1024) # ->1024 es el numero de bytes que vamos a recibir

#luego vamos a mostrar por la terminal el mensaje recibido y la IP y puerto del cliente
print("recibido: ["+mensaje.decode("utf-8")+"] del cliente")
print("IP cliente: "+str(addr[0]))
print("Puerto cliente: "+str(addr[1]))

#por ultimo cerramos el socket del servidor
s.close()

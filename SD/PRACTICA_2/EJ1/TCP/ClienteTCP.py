"""implementacion de socket TCP cliente"""

import socket


#establecemos la direccion y puerto del sevidor
HOST = 'localhost'
PORT = 1024

#creamos el socket con SOCK_STREAM puesto que es TCP y conectamos con el servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#ahora vamos a mandar un mensaje al servidor de corma codificada con encofe utf-8
s.send("Hola,servidor".encode("utf-8"))
#luego vamos a recibir un mensaje del servidor y lo vamos a mostrar por la terminal
mensaje = s.recv(1024) # ->1024 es el numero de bytes que vamos a recibir como maximo
print("recibido: ["+mensaje.decode("utf-8")+"] del servidor")

#por ultimo cerramos la conexion con close()
s.close()
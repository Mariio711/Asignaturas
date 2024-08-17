"""implementacion de socket TCP servidor"""

import socket


#establecemos la direccion y puerto del cliente
HOST = 'localhost'
PORT = 1024

#creamos el socket con SOCK_STREAM puesto que es TCP y le asignamos una direccion y un puerto (la del servidor)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

#luego nos mantenemos escuchando en ese puerto a que un cliente se conecte
s.listen(1) # -> 1 por que esperamos la conexion de un solo cliente, esto cambiara segun el numero de clientes
print("Nos mantenemos a la espera . . .")

#cuando la conexion se ha ejecutado actualizamos dos variables con el socket del cliente y la direccion con accept()
s_cliente, addr = s.accept()

#luego vamos a recibir un mensaje del cliente y lo vamos a mostrar por la terminal
mensaje = s_cliente.recv(1024) # ->1024 es el numero de bytes que vamos a recibir como maximo
print("recibido: ["+mensaje.decode("utf-8")+"] del cliente con la direccion: "+ str(addr))

#ahora vamos a mandar un mensaje al cliente
s_cliente.send("Hola cliente, soy el servidor".encode("utf-8"))

#por ultimo cerramos la conexion con close() en el cliente y luego en el servidor
s_cliente.close()
s.close()
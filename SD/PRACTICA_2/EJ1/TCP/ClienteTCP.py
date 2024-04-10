import socket


# Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: IPv4, SOCK_STREAM: TCP

# Conectamos el socket
s.connect(('localhost', 1234))

# Enviamos un mensaje
s.send(b'Hola, soy un cliente')

# Recibimos la respuesta
respuesta = s.recv(1024)
print(respuesta.decode('utf-8'))

# Cerramos la conexión
s.close()

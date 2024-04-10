import socket

HOST = 'localhost'
PORT = 1234

# Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: IPv4, SOCK_STREAM: TCP

# Enlazamos el socket
s.bind((HOST, PORT))

# Ponemos el socket en modo escucha
s.listen(1)

# Aceptamos la conexión
conn, addr = s.accept()
print('Conectado por', addr)

# Recibimos el mensaje
mensaje = conn.recv(1024)
print(mensaje.decode('utf-8'))

# Enviamos una respuesta
conn.send(b'Hola, soy el servidor')

# Cerramos la conexión
conn.close()
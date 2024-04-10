import socket

HOST = 'localhost'
PORT = 1234

# Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP

# Enlazamos el socket
s.bind((HOST, PORT))

# Recibimos el mensaje
mensaje, addr = s.recvfrom(1024)
print(mensaje.decode('utf-8'))
print('Conectado por', addr)
print('Puerto:', PORT)

# Enviamos una respuesta
s.sendto(b'Hola, soy el servidor', addr)

# no cerramos la conexión porque UDP no tiene conexión peroi si cerramos el socket
s.close()
import socket

HOST = 'localhost'
PORT = 1234

# Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP

#enivamos directamente el mensaje
s.sendto(b'Hola, soy un cliente', (HOST, PORT))

# Recibimos la respuesta
respuesta, addr = s.recvfrom(1024)
print(respuesta.decode('utf-8'))
print('Conectado por', addr)
print('Puerto:', PORT)

#no cerraos la conexión porque UDP no tiene conexión pero si cerramos el socket
s.close()

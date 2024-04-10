#cliente UDP

import socket
import os
import shutil

HOST = 'localhost'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente iniciado.")

while True:
    comando = input("Ingrese un comando: ")
    s.sendto(comando.encode(), (HOST, PORT))
    if comando == "exit":
        break
    data, addr = s.recvfrom(1024)
    print(data.decode())
s.close()
print("Cliente finalizado.")
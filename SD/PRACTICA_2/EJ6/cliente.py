"""implementacion de socket TCP cliente"""

import socket, os

def inicio_socket():
    
    #cambiar directorio de trabajo
    os.chdir("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ6")


    #creamos el socket con SOCK_DGRAM puesto que es UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def enviar_comando(cliente, addr):
    
    comando = str(input())

    while comando != 'exit':
        cliente.sendto(comando.encode("utf-8"), addr)
        mensaje, addr = cliente.recvfrom(1024)
        if comando == 'ls':
            lista = mensaje.decode("utf-8")
            lista = lista.split()
            print(lista)
        else:
            print(mensaje.decode("utf-8"))

        comando = str(input())

def inicio(dir, port):
    addr = dir, port

    cliente = inicio_socket()

    enviar_comando(cliente, addr)

    cliente.sendto("exit".encode("utf-8"), addr)
    cliente.close()

if __name__ == "__main__":
    inicio("localhost", 1026)
import socket
import os
import shutil

HOST = 'localhost'
PORT = 1024

def ls():
    return os.listdir()

def cd(directorio):
    try:
        os.chdir(directorio)
        return True
    except:
        return False

def mv(origen, destino):
    try:
        shutil.move(origen, destino)
        return True
    except:
        return False

def rm(archivo):
    try:
        os.remove(archivo)
        return True
    except:
        return False

def writedata(archivo, data):
    try:
        with open(archivo, 'w') as f:
            f.write(data)
        return True
    except:
        return False
    
def seleccionar_comando(comando):
    if comando == "ls":
        return ls()
    elif comando[:2] == "cd":
        return cd(comando[3:])
    elif comando[:2] == "mv":
        origen, destino = comando[3:].split(' ')
        return mv(origen, destino)
    elif comando[:2] == "rm":
        return rm(comando[3:])
    elif comando[:2] == "wr":
        archivo, data = comando[3:].split(' ')
        return writedata(archivo, data)
    else:
        return "Comando no reconocido."

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((HOST, PORT))
        print("Servidor iniciado.")
        while True:
            print("Esperando conexión...")
            datos, direccion = servidor.recvfrom(1024)
            comando = datos.decode()
            respuesta = seleccionar_comando(comando)
            servidor.sendto(str(respuesta).encode(), direccion)
    
if __name__ == "__main__":
    main()
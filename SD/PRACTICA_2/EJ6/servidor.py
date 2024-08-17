"""implementacion de socket TCP servidor"""

import socket, os, shutil

def inicio_socket(dir, puerto):
    
    #cambiar directorio de trabajo
    os.chdir("C:\REPOS-GIT\Asignaturas\SD\PRACTICA_2\EJ6")


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((dir, puerto))

    return s

def ls():
    return os.listdir(os.getcwd())

def rm(nombre_archivo):

    ruta = os.getcwd() + os.sep + nombre_archivo

    os.remove(ruta)

    if os.path.isfile(ruta):
        return False
    else:
        return True

def write(nombre_archivo, texto):
    with open(nombre_archivo, 'w') as f:
        f.write(texto)

    with open(nombre_archivo, 'r') as f:
        if texto == f.read(2048):
            return True
        else:
            return False
    
def exit(s):
    s.close()

def cd(nombre_dir):

    ruta = os.getcwd() + os.sep + nombre_dir

    if os.path.isdir(ruta):
        os.chdir(ruta)
        return True
    else:
        return False
    
def mv(nombre_archivo, destino):

    ruta_origen = os.getcwd() + os.sep + nombre_archivo

    if os.path.isdir(destino):
        ruta_destino = destino + os.sep + nombre_archivo
    else:
        ruta_destino = destino
    
    shutil.move(ruta_origen, ruta_destino)

    if os.path.isfile(ruta_destino):
        return True
    else:
        return False
    
def inicio(dir, port):

    #iniciamos socket
    servidor = inicio_socket(dir, port)

    whiling = True

    while whiling:
        mensaje, addr= servidor.recvfrom(1024)
        lista = mensaje.split()
        comando = lista[0].decode("utf-8")
        if len(lista) == 2:
            argumento1 = lista[1].decode("utf-8")
        elif len(lista) == 3:
            argumento1 = lista[1].decode("utf-8")
            argumento2 = lista[2].decode("utf-8")
        elif len(lista) > 3:
            argumento1 = lista[1].decode("utf-8")
            argumentos_adicionales = []
            for i in range(2, len(lista)):
                argumentos_adicionales.append(lista[i].decode("utf-8"))
            argumento2 = ' '.join(argumentos_adicionales)


        if comando == 'ls':
            lista = ls()
            cadena = ' '.join(lista)  # Convierte la lista en una cadena, separada por espacios
            bytes_cadena = cadena.encode('utf-8')  # Codifica la cadena en bytes usando UTF-8

            servidor.sendto(bytes_cadena, addr)

        elif comando == 'rm':
            flag = rm(argumento1)
            if flag:
                servidor.sendto(f"Se ha eliminado el archivo {argumento1} correctamente\n".encode("utf-8"), addr)
            else:
                servidor.sendto(f"No se ha podido eliminar el archivo {argumento1} correctamente\n".encode("utf-8"), addr)
        
        elif comando == 'write':
            flag = write(argumento1, argumento2)
            if flag:
                servidor.sendto(f"Se ha creado el archivo {argumento1} y escrito {argumento2} correctamente\n".encode("utf-8"), addr)
            else:
                servidor.sendto(f"No se ha podido crear el archivo {argumento1} correctamente\n".encode("utf-8"), addr)

        elif comando == 'exit':
            exit(servidor)
            whiling = False

        elif comando == 'cd':
            flag = cd(argumento1)
            if flag:
                servidor.sendto(f"Se ha movido a {argumento1} correctamente\n".encode("utf-8"), addr)
            else:
                servidor.sendto(f"No se ha podido mover a {argumento1} correctamente\n".encode("utf-8"), addr)
        
        elif comando == 'mv':
            flag = mv(argumento1, argumento2)
            if flag:
                servidor.sendto(f"Se ha movido el archivo {argumento1} a {argumento2} correctamente\n".encode("utf-8"), addr)
            else:
                servidor.sendto(f"No se ha podido mover el archivo {argumento1} a {argumento2} correctamente\n".encode("utf-8"), addr)
        
        else:
            servidor.sendto("No se reconoce el comando, para salir del servidor escriba 'exit'\n".encode("utf-8"), addr)


if __name__ == "__main__":
    inicio("localhost", 1026)
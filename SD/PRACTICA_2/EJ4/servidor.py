"""implementacion de socket UDP servidor conversacion con cliente"""

import socket

def conversacion(s, addr, mensaje):
    
    nombre = mensaje.decode("utf-8")

    while mensaje != "cerrar":
        s.sendto(f"{nombre}, ¿En que puedo ayudarte?\n".encode("utf-8"), addr)

        mensaje = s.recvfrom(1024)[0].decode("utf-8")

        print(f"cliente: {mensaje}")

        s.sendto("Debe ponerse en contacto con el servicio de atencion de dudas cuya direccion es duda@panpan.com\n".encode("utf-8"), addr)

    s.close()


def inicio(dir, port):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((dir, port))
    print(f"Servidor asignado en {dir} : {port} ...")

    mensaje, addr = servidor.recvfrom(1024)

    servidor.sendto("¡Bienvenido! Cual es su nombre para que pueda dirijirme a usted?\n".encode("utf-8"), addr)
    
    mensaje, addr = servidor.recvfrom(1024)

    conversacion(servidor, addr, mensaje)
    
if __name__ == "__main__":
    inicio("localhost", 1026)
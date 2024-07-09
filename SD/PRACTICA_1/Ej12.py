"""12.Implemente una función copiar(origen,destino) que copie el contenido
del fichero origen, en el fichero destino (usando open())."""

def copiar(origen, destino):
    with open(origen, 'r') as f1:
        contenido = f1.read()

    with open(destino, 'w') as f2:
        f2.write(contenido)

copiar("archivo_origen", "archivo_destino")
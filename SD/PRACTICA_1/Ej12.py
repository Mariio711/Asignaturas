def copy_file(origen, destino):
    with open(origen, 'r') as file_origen:
        contenido = file_origen.read()
        
    with open(destino, 'w') as file_destino:
        file_destino.write(contenido)
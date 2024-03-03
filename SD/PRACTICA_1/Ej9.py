import os

def get_file_info(filename):
    if type(filename) is not str or filename is None:
        raise TypeError("Error: el parametro no es una cadena o es nulo")

    info = []

    #comprobar el numero de bytes de un fichero
    num_bytes = os.path.getsize(filename)
    info.append(num_bytes)

    #almacenar las palabras que terminan por 's'
    with open(filename, 'r') as file:
        texto = file.read()
        palabras = texto.split()
        palabras_acabadas_en_s = [palabra for palabra in palabras if palabra.endswith('s')]
        info.append(palabras_acabadas_en_s)
    
    return info

    
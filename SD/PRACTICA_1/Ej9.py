"""9. Implemente la función get_file_info(filename) para que devuelva una
tupla con el tamaño en bytes del fichero, cuyo nombre se indica como
parámetro filename, en la primera posición, y una lista con las palabras
acabadas con el carácter 's' que contenga el fichero, en segunda posición.
Por ejemplo, la invocación get_file_info('mifichero.txt'), suponiendoque 'mifichero.txt' contiene el texto 
" La casa está pintada en muchos colores", devolverá la tupla (39, ['muchos','colores']). Si el
parámetro filename no es una cadena o es nulo (None) o si el fichero
indicado no existe, se deberá generar la excepción correspondiente."""

from genericpath import getsize
import shutil, os

def get_file_info(filename):
    if not isinstance(filename, str) or filename is None:
        raise ValueError("El nombre del fichero no es una cadena o es nulo")
    else:
        if not os.path.isfile(filename):
            raise OSError("FileNotFound")
        else:

            with open(filename) as f:
                contenido = f.readlines()

            palabras_con_s = [palabra for linea in contenido for palabra in linea.split() if palabra.endswith('s')]
            res = (getsize(filename), palabras_con_s)
    
    return res

print(get_file_info("archivo.txt"))
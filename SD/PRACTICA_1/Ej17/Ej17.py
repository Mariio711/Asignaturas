"""17. Realizar un script en Python que combine todos los ficheros de texto
(.txt) existentes en el directorio de trabajo actual en un único fichero de
texto, llamado “union.txt”. Tanto los ficheros con una extensión distinta,
como los que se encuentren en subdirectorios, deberán ignorarse."""

import os

def uniontxt():
    txt = []

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith('.txt'):
                txt.append(os.path.join(dirpath, filename))

    with open('union.txt', 'w') as outfile:
        for filetxt in txt:
            with open(filetxt) as f:
                outfile.write(f.read())


uniontxt()
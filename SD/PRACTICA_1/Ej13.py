"""13.Imprima por pantalla el listado de directorios de inicio de los usuarios
que hay en el sistema (p. ej., /home/root , /home/osboxes, . . . ). Pista: hay
un fichero con esta información. También existe una función muy
interesante en Python llamada split, que convierte de string a lista."""

import os

lista = os.listdir("C:/users/Mario")
print(lista)
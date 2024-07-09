"""6. Implemente la función list_del(mylist, e) para que elimine la primera
ocurrencia del elemento e de la lista mylist y devuelva la lista resultante.
Por ejemplo, la invocación list_del([5, 2, 4], 2) deberá devolver como
resultado [5, 4]. Si el elemento es nulo (‘None’) o la lista mylist está
vacía, se deberá generar la o las excepciones correspondientes."""

def list_del(mylist, e):

    i = 0

    if e is None:
        raise ValueError("El elemento es nulo")
    else:
        mylist.remove(e)

    return mylist

lista = list_del([2, 5, 8, 3, 5], 5)
print(lista)

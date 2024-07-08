"""5. Implemente la función list_add(mylist, e) para que añada el elemento e
a la lista mylist y devuelva la lista resultante. Por ejemplo, la invocación
de list_add([5, 2], 4) deberá devolver como resultado [5, 2, 4]. Si el
elemento es nulo (‘None’), se deberá generar la excepción
correspondiente."""



def list_add(mylist, e):
    if e == None:
        raise ValueError("el elemento a añadir es nulo")
    else:
        mylist.append(e) #para insertar un elemento al final de una lista usamos append
    return mylist

mylist = [1,2]
lista = list_add(mylist, 4)

for l in lista:
    print(l)

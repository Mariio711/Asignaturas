"""10.Implemente una función en Python que realice la intersección de dos
listas. Tenga en cuenta que no puede haber elementos repetidos."""

def interseccion_listas(lista1, lista2):
    lista1 = set(lista1)
    lista2 = set(lista2)
    res = lista1.intersection(lista2)
    return res

print(interseccion_listas([1,3,5,7,10],[1,2,3,4,5,6,7,8,9,10]))
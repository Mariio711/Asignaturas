"""11.Implemente una función en Python que realice la unión de dos listas.
Tenga en cuenta que no puede haber elementos repetidos."""

def union_listas(lista1, lista2):
    res = set(lista1 + lista2)
    return res

print(union_listas([1,3,5,7,10],[1,2,3,4,5,6,7,8,9,10]))
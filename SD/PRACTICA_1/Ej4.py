def accum(x, y, z):
    if not all(type(i) is int for i in [x, y, z]):
        # si no es un entero lanza TypeError exception
        raise TypeError("Solo se permiten enteros")
    
    return sum(i for i in [x, y, z] if i % 2 == 0)
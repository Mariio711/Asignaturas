def dict_add(mydict: dict, t):
    if type(t) is None:
        raise TypeError("Error: la tupla a añadir es nula")
    if not isinstance(t, tuple):
        raise TypeError("Error: el segundo argumento debe ser una tupla")
    
    #hay que desempaquetar la tupla t en dos parametros para añadirlos al diccionario
    clave, valor = t
    mydict[clave] = valor

    return mydict
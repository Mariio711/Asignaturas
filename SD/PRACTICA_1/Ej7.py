"""7. Implemente la función dict_add(mydict, t) para que añada la tupla
(clave, valor) t pasada por parámetro al diccionario mydict. Por ejemplo,
la invocación dict_add({1: 'manzana'}, (2,'fresa')) deberá devolver
como resultado {1: 'manzana', 2: 'fresa'}. Si el elemento t es nulo
(None) o no es una tupla de dos elementos, se deberá generar la o las
excepciones correspondientes."""

def dict_add(mydict, t):
    if not isinstance(t, tuple) or t is None:
        raise ValueError("El elemento no es una tupla o es nulo")
    else:
        mydict[t[0]] = t[1]
    return mydict

dict1 = {1: "manzana", 2: "pera"}
tupla = (3, "fresa")

dict2 = dict_add(dict1, tupla)
print(dict2.items())
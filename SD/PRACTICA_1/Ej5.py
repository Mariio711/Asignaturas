def list_add(mylist: list, e):
    if type(e) is None:
        raise TypeError("El elemento es nulo")
    return mylist.append(e)
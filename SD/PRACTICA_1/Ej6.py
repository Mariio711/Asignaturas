def list_del(mylist: list, e):
    if len(mylist) == 0:
        raise RuntimeError("Error: lista vacia.")
    
    if type(e) is None:
        TypeError("Error: el elemento a borrar es nulo")

    return mylist.remove(e)
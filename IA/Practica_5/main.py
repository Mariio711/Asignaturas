from busquedaAlum import *

def main():
    print("Seleccione el método de búsqueda:")
    print("1. Búsqueda en Anchura")
    print("2. Búsqueda en Profundidad")
    print("3. Búsqueda en Profundidad Limitada")
    print("4. Búsqueda en Profundidad Limitada Iterativa")
    
    opcion = int(input("Ingrese el número de la opción deseada: ").strip())
    nodo_inicial = nodoInicial()

    if opcion == 1:
        objetivo = busquedaAnchura()
    elif opcion == 2:
        objetivo = busquedaProfundidad()
    elif opcion == 3:
        limite = int(input("Ingrese el límite de profundidad: "))
        objetivo = busquedaProfundidadLimitada(nodo_inicial, limite)
    elif opcion == 4:
        limite_max = int(input("Ingrese el límite máximo de profundidad: "))
        objetivo = busquedaProfundidadLimitadaIterativa(nodo_inicial, limite_max)
    else:
        print("Opción no reconocida")
        return

    if objetivo:
        print("Se ha alcanzado una solución")
    else:
        print("No se ha alcanzado ninguna solución")

if __name__ == "__main__":
    main()
from __future__ import annotations
from NPuzle_Alum import *
from collections import deque

@dataclass
class Nodo:
    estado: tEstado
    operador: str
    costeCamino: int
    profundidad: int
    padre: Nodo


def nodoInicial() -> Nodo:
    return Nodo(estadoInicial(), None, 0, 0, None)


def dispCamino(nodo: Nodo) -> None:
    lista = []
    aux = nodo
    while aux.padre != None:
        lista.append((aux.estado.tablero, aux.operador))
        aux = aux.padre
    for i in lista[::-1]: # Se utiliza ::-1 para recorrer la lista en sentido inverso, desde la raíz hasta el nodo objetivo.
        print("Operador: ", operadores[i[1]], "\n", i[0])
        print()


def dispSolucion(nodo: Nodo) -> None:
    dispCamino(nodo)
    print("Profundidad: ", nodo.profundidad)
    print("Coste: ", nodo.costeCamino)


def expandir(nodo: Nodo) -> list:
    nodos = []

    coste = 0
    profundidad = 0
    op = 2
    for op in operadores:  
        if esValido(op, nodo.estado):
            nuevo = aplicaOperador(op, nodo.estado)
            nodos.append(Nodo(nuevo, op, nodo.costeCamino + 1, nodo.profundidad + 1, nodo))

    return nodos

def busquedaAnchura():
    nodo_inicial = nodoInicial()
    if testObjetivo(nodo_inicial.estado):
        dispSolucion(nodo_inicial)
        return True

    frontera = deque([nodo_inicial])
    cerrados = set()

    while frontera:
        nodo = frontera.popleft()
        cerrados.add(nodo.estado)

        for sucesor in expandir(nodo):
            if sucesor.estado not in cerrados and sucesor not in frontera:
                if testObjetivo(sucesor.estado):
                    dispSolucion(sucesor)
                    return True
                frontera.append(sucesor)

    return False

def busquedaProfundidad():
    nodo_inicial = nodoInicial()
    if testObjetivo(nodo_inicial.estado):
        dispSolucion(nodo_inicial)
        return True

    frontera = [nodo_inicial]
    cerrados = set()

    while frontera:
        nodo = frontera.pop()
        cerrados.add(nodo.estado)

        for sucesor in expandir(nodo):
            if sucesor.estado not in cerrados and sucesor not in frontera:
                if testObjetivo(sucesor.estado):
                    dispSolucion(sucesor)
                    return True
                frontera.append(sucesor)

    return False

def busquedaProfundidadLimitada(nodo: Nodo, limite: int) -> bool:
    if testObjetivo(nodo.estado):
        dispSolucion(nodo)
        return True
    elif nodo.profundidad == limite:
        return False
    else:
        for sucesor in expandir(nodo):
            if busquedaProfundidadLimitada(sucesor, limite):
                return True
        return False

def busquedaProfundidadLimitadaIterativa(raiz: Nodo, limite_max: int) -> bool:
    for limite in range(limite_max + 1):
        if busquedaProfundidadLimitada(raiz, limite):
            return True
    print("No se ha encontrado solución dentro del límite máximo")
    return False


from tictactoeAlum import *


def PSEUDOminimax(nodo):
    mejorJugada = -1
    puntos = -2
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            util = utilidad(intento)
            if util > puntos:
                puntos = util
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo


def jugadaAdversario(nodo):
    valida = False
    jugada = None
    while not valida:
        fila = int(input("Fila: "))
        col = int(input("Col: "))
        jugada = Jugada(fila, col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def minimax(nodo):
    jugador = 1
    mejorJugada = jugadas[0]
    max_valor = -10000

    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, jugador)
            max_actual = valorMin(intento)
            if max_actual > max_valor:
                max_valor = max_actual
                mejorJugada = jugada

    nodo = aplicaJugada(nodo, mejorJugada, jugador)
    return nodo


def valorMin(nodo):
    valor_min = float('inf')
    jugador = -1

    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        valor_min = float('inf')
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_min = min(valor_min, valorMax(aplicaJugada(nodo, jugada, jugador)))
    
    return valor_min


def valorMax(nodo):
    valor_max = -float('inf')
    jugador = 1

    if terminal(nodo):
        valor_max = utilidad(nodo)
    else:
        valor_max = -float('inf')
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_max = max(valor_max, valorMin(aplicaJugada(nodo, jugada, jugador)))
    
    return valor_max

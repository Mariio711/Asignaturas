from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import numpy as np

visual = {1: "❌", -1: "⭕", 0.0: " "}


@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    N: int

    def __init__(self, tablero):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.vacias = len(np.where(tablero == 0)[0])

    def __str__(self):
        string = f"{' ----+----+----'}\n|"
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if i == 2 and j == 2:
                string += f"\n ----+----+----\n"
            else:
                string += f"\n ----+----+----\n|"
        return f"{string}"


@dataclass
class Jugada:
    x: int
    y: int

    def __str__(self):
        return f"\nFila: ({self.x}, Col: {self.y})"


######
# Se crean todas las posibles jugadas para el for de rango (for jugada in jugadas)
jugadas = []
for i in range(0, 3):
    for j in range(0, 3):
        jugadas.append(Jugada(i, j))
######

""" Funciones complementarias
    * crearNodo
    * nodoInicial
    * opuesto
"""


def crearNodo(tablero):
    return Nodo(tablero)


def nodoInicial():
    tablero_inicial = np.zeros((3, 3))
    return Nodo(tablero_inicial)


def opuesto(jugador):
    return jugador * -1


""" Funciones Búsqueda MiniMax
    * aplicaJugada
    * esValida
    * terminal
    * utilidad
"""


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo_nodo = deepcopy(actual)

    if jugador == -1:
        nuevo_nodo.tablero[jugada.x, jugada.y] = -1
    if jugador == 1:
        nuevo_nodo.tablero[jugada.x, jugada.y] = 1

    return nuevo_nodo


def esValida(actual: Nodo, jugada: Jugada) -> bool:
    """Comprueba si dada una Jugada, es posible aplicarla o no.

    Args:
        actual (Nodo)
        jugada (Jugada)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        bool: Devuelve True en caso de que pueda realizarse la Jugada, False en caso contrario
    """
    raise NotImplementedError


def terminal(actual: Nodo) -> bool:
    """Comprueba si el juego se ha acabado, ya sea porque alguno de los jugadores ha ganado o bien
    porque no sea posible realizar ningún movimiento más.

    Args:
        actual (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        bool: Devuelve True en caso de Terminal, False en caso contrario
    """

    ###                                 Importante:
    #   Si considera más sencillo trabajar con una representación en vector en lugar de matriz puede
    #   hacer uso de la función reshape o la función flatten que contiene la biblioteca numpy. 
    #   Puede comprobar un ejemplo si ejecuta este código mediante python tictactoeAlum.py
    ###
    raise NotImplementedError


def utilidad(nodo: Nodo) -> int:
    """La función de utilidad, también llamada objetivo, asigna un valor numérico al nodo recibido como parámetro.
    Por ejemplo, en un juego de 'Suma cero', se puede establecer que devuelve -100, 0, 100 en función de qué jugador
    gana o bien si hay un empate.

    Args:
        nodo (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        int: Valor de utilidad
    """
    raise NotImplementedError


if __name__ == "__main__":
    M = np.array([
        [1,2],
        [3,4]
    ])
    print(M)
    M_vector = M.reshape(4)
    print(M_vector)
    M_vector = M.flatten()
    print(M_vector)
    M_de_nuevo = M_vector.reshape(2,2)
    print(M_de_nuevo)
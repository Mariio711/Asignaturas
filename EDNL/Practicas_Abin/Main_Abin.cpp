#include <iostream>

#include "Ej_P1.cpp"
#include "Ej_P2.cpp"
#include "abin.h" // Asegúrate de que este archivo exista y contenga la definición de Abin
#include "abin_E-S.h"


// Aquí irían las funciones evaluarExpresion_Rec y evaluarExpresion

int main() {
    // Crear un árbol de expresiones
    Abin<Elemento> A;
    A.insertarRaiz(Elemento(0, '+'));
    Abin<Elemento>::nodo n = A.raiz();
    A.insertarHijoIzqdo(n, Elemento(2)); // 2
    A.insertarHijoDrcho(n, Elemento(3)); // 3

    // Evaluar la expresión
    double resultado = evaluarExpresion(A);
    std::cout << "El resultado es: " << resultado << std::endl; // Debería imprimir 5

    system("pause");
    return 0;
}
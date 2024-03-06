#include <iostream>
#include <fstream>
#include <queue>

#include "abin.h"
#include "abin_E-S.h"

using namespace std;

typedef char tElto;

//Ejercicio 1 -- Dos arboles son similares cuando tienen identica estructura de ramificacion, es decir ambos son vacios,
//               o tienen subarboles similares. Implementa un programa que determine si dos arboles binarios son similares
template <typename tElto>
bool AbinSimilares(const Abin<tElto>& A, const Abin<tElto>& B){
    return AbinSimilaresRec(A, B, A.raiz(), B.raiz());
}

bool AbinSimilaresRec(const Abin<tElto>& A,const Abin<tElto>& B, const Abin<tElto>::nodo nA, const Abin<tElto>::nodo nB){
    if(nA == Abin<tElto>::NODO_NULO || nB == Abin<tElto>::NODO_NULO){
        return nA == Abin<tElto>::NODO_NULO && nB == Abin<tElto>::NODO_NULO;
    }

    return AbinSimilaresRec(A, B, A.hijoDrcho(nA), B.hijoDrcho(nB)) && AbinSimilaresRec(A, B, A.hijoIzqdo(nA), B.hijoIzqdo(nB));
}

//Ejercicio 2 -- Para un arbol binasrio B podemos construir el arbol binario reflejado B^R cambuando los subarboles
//               izquierdo y derecho de cada nodo. implementa un programa que devuelva el arbol binario reflejado de uno dado


void AbinRefRec(const Abin<tElto>& A, Abin<tElto>& ARef, const Abin<tElto>::nodo nA, const Abin<tElto>::nodo nB){

    if(A.hijoIzqdo(nA) != Abin<tElto>::NODO_NULO){
        ARef.insertarHijoDrcho(nB,nA->hizq->elto);
        return AbinRefRec(A, ARef, A.hijoIzqdo(nA), ARef.hijoDrcho(nB));
    }

    if(A.hijoDrcho(nA) != Abin<tElto>::NODO_NULO){
        ARef.insertarHijoIzqdo(nB,nA->hder->elto);
        return AbinRefRec(A, ARef, A.hijoDrcho(nA), ARef.hijoIzqdo(nB));
    }
}

Abin<tElto> AbinRef(const Abin<tElto>& A){
    Abin<tElto> ARef;
    if (!A.arbolVacio()) {
        ARef.insertarRaiz(A.elemento(A.raiz()));
        AbinRefRec(A, ARef, A.raiz(), ARef.raiz());
    }
    return ARef;
}

/*El TAD árbol binario (abin) puede albergar expresiones matemáticas mediante un árbol de expresión.
 Dentro del árbol binario los nodos hojas contendrán los operandos,
 y el resto de los nodos los operadores. a) Define el tipo de los elementos del árbol 
 para que los nodos puedan almacenar operadores y operandos.*/
 
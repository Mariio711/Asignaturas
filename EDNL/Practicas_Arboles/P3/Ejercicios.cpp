#include <iostream>
#include <fstream>
#include "agenlis.h"
#include "agen_E-S.h"

using namespace std;
typedef char tElto;

//. Implementa un subprograma que dado un árbol general nos calcule su grado. 
int gradoAgen_Rec(const Agen<tElto>& A, Agen<tElto>::nodo n){
    int grado = 0;
    Agen<tElto>::nodo hijo = A.hijoIzqdo(n);

    // Contar los hijos del nodo actual
    while (hijo != Agen<tElto>::NODO_NULO) {
        ++grado;
        hijo = A.hermDrcho(hijo);
    }

    // Comprobar los hijos del nodo actual para ver si tienen más hijos
    hijo = A.hijoIzqdo(n);
    int max_grado_hijos = 0;
    while (hijo != Agen<tElto>::NODO_NULO) {
        max_grado_hijos = max(max_grado_hijos, gradoAgen_Rec(A, hijo));
        hijo = A.hermDrcho(hijo);
    }

    return max(grado, max_grado_hijos);
}

int gradoAgen(const Agen<tElto> A){
    if (A.arbolVacio()){
        return 0;
    }else{
        return gradoAgen_Rec(A, A.raiz());
    }

}

//pofundidad de un nodo dado
int profundidadAgen (const Agen<tElto> A, const Agen<tElto>::nodo n){
    if (n == A.raiz()){
        return 0;
    }else{
        return 1 + profundidadAgen(A, A.padre(n));
    }
}

//se define desequilibrio de un arbol general como la maxima diferencia
//entre las alturas de los subarboles mas bajo y mas alto de cada nivel
int altura(const Agen<tElto>& A, Agen<tElto>::nodo n) {
    if (n == Agen<tElto>::NODO_NULO) {
        return 0;
    } else {
        int altura_max = 0;
        Agen<tElto>::nodo hijo = A.hijoIzqdo(n);
        while (hijo != Agen<tElto>::NODO_NULO) {
            altura_max = max(altura_max, altura(A, hijo));
            hijo = A.hermDrcho(hijo);
        }
        return altura_max + 1;
    }
}

int desequilibrioAgen_Rec(const Agen<tElto>& A, Agen<tElto>::nodo n) {
    if (n == Agen<tElto>::NODO_NULO) {
        return 0;
    } else {
        int altura_max = 0;
        int altura_min = 20000;
        int desequilibrio = 0;
        Agen<tElto>::nodo hijo = A.hijoIzqdo(n);
        while (hijo != Agen<tElto>::NODO_NULO) {
            int altura_hijo = altura(A, hijo);
            altura_max = max(altura_max, altura_hijo);
            altura_min = min(altura_min, altura_hijo);
            desequilibrio = max(desequilibrio, desequilibrioAgen_Rec(A, hijo));
            hijo = A.hermDrcho(hijo);
        }
        return max(desequilibrio, altura_max - altura_min);
    }
}

int desequilibrioAgen (const Agen<tElto> A){
    if (A.arbolVacio()){
        return 0;
    }else{
        return desequilibrioAgen_Rec(A, A.raiz());
    }
}

//dado un arbol general y un entrero implementa un programa que realice la poda de A a apertir de x.  se asume que no hay elementos repetidos en A
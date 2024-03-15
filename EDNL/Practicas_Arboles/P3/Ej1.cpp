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
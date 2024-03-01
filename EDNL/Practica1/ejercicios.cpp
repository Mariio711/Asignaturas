#include <iostream>
#include <fstream>
#include <queue>

#include "abin.h"
#include "abin_E-S.h"

using namespace std;

typedef char tElto;
const tElto fin = '#';


//Ejercicio 1 - Calcular el numero de nodos de un arbol binario. 
//el recorrido del arbol es en profundidad

template <typename tElto>
int numeronodos(const Abin<tElto>& A){//funcion llamadora a la recursiva 
    return numeronodos_Rec(A, A.raiz());
}

template <typename tElto>
int numeronodos_Rec(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    if (n == Abin<tElto>::NODO_NULO) {
        return 0;
    } else {
        return 1 + numeronodos_Rec(A, A.hijoIzqdo(n)) + numeronodos_Rec(A, A.hijoDrcho(n));
    }
}


//Ejercicio 2 - altura de un arbol binario

//funcion llamadora
template <typename tElto>
int altura (const Abin<tElto>& A){
    return altura_Rec(A, A.raiz());
}


template <typename tElto>
int altura_Rec(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    if (n == Abin<tElto>::NODO_NULO) {
        return -1;      //se pone -1 por que si un nodo es nulo no existe 
    } else {
        int hizq = 1 + altura_Rec(A, A.hijoIzqdo(n));
        int hder = 1 + altura_Rec(A, A.hijoDrcho(n));
        return (hizq > hder) ? hizq : hder;
    }
}

//Ejercicio 3 - dado un arbol binario y un nodo del mismo, determine la profundidad de un nodo
template <typename tElto>
int profundidad(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    // if (n == A.padre(n)){
        //return 0;                 de esta forma la profundidad es 0 por que el nodo que he pasado es el padre o la raíz.
    //}
    if (n == Abin<tElto>::NODO_NULO) {
        return -1;                 // de esta forma el nodo es nulo como la precondicion dice que el arbol no pude ser -
                                   // - vacio continuara hacia delant y si luego no tiene padre se restara 1-1 que seria 0 igual que la anterior 
    } else {                       
        return 1 + profundidad(A, A.padre(n));
    }
}

//Ejercicio 6 - nivel de desequilibrio de un arbol binario
//mirar el propio desequilibrio del nodo hay que tener en cuenta todo.
template <typename tElto>
int desequilibrio (const Abin<tElto>& A){

    int niveld=0, niveli=0;

    if (A.hijoDrcho(0) != Abin<tElto>::NODO_NULO)
    niveld = 1 + A.altura(A.hijoDrcho(0));

    if (A.hijoIzqdo(0) != Abin<tElto>::NODO_NULO)
    niveli = 1 + A.altura(A.hijoIzqdo(0));

    return (niveld > niveli)? niveld : niveli;
}

//ejercicio 7 - arbol pseudocompleto
template <typename tElto>
bool pseudocompletocola (const Abin<tElto>& A){
        if (A.arbolVacioB()) {
        return true;
    }

    std::queue<typename Abin<tElto>::nodo> cola;
    cola.push(A.raiz());

    bool bandera = false; // Se activa cuando encontramos un nodo que no tiene dos hijos

    while (!cola.empty()) {
        typename Abin<tElto>::nodo nodoActual = cola.front();
        cola.pop();

        if (A.hijoIzqdo(nodoActual) != Abin<tElto>::NODO_NULO) {
            if (bandera) { // Si encontramos un nodo con hijo después de un nodo sin dos hijos
                return false;
            }
            cola.push(A.hijoIzqdo(nodoActual));
        } else {
            bandera = true; // Este nodo no tiene hijo izquierdo
        }

        if (A.hijoDrcho(nodoActual) != Abin<tElto>::NODO_NULO) {
            if (bandera) { // Si encontramos un nodo con hijo después de un nodo sin dos hijos
                return false;
            }
            cola.push(A.hijoDrcho(nodoActual));
        } else {
            bandera = true; // Este nodo no tiene hijo derecho
        }
    }

    return bandera;
}

template <typename tElto>
bool pseudocompletonocola(const Abin<tElto>& A, typename Abin<tElto>::nodo n = Abin<tElto>::NODO_NULO) {
    if (n == Abin<tElto>::NODO_NULO) {
        return true;
    }

    if ((A.hijoIzqdo(n) != Abin<tElto>::NODO_NULO && A.hijoDrcho(n) == Abin<tElto>::NODO_NULO) ||
        (A.hijoIzqdo(n) == Abin<tElto>::NODO_NULO && A.hijoDrcho(n) != Abin<tElto>::NODO_NULO)) {
        return false;
    }

    return pseudocompletonocola(A, A.hijoIzqdo(n)) && pseudocompletonocola(A, A.hijoDrcho(n));
}

int main(){
    Abin<tElto> A, B;
    ifstream fe("abin.dat"); // Abrir fichero de entrada.
    rellenarAbin(fe, A); // Desde fichero.
    fe.close();
    cout << "\n*** Mostrar árbol binario B ***\n";
    imprimirAbin(A); // En std::cout

    cout << "numero de nodos(A)= " << numeronodos(A) << endl; //numero de nodos

    cout << "altura(A)= " << altura(A) << endl; //altura del arbol

    cout << "profundidad de un nodo dado" << profundidad(A, A.hijoIzqdo(A.raiz())) << endl; //profundidad de un nodo
    system("pause");
}


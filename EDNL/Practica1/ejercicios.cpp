#include <iostream>
#include <fstream>
#include <conio.h>
#include "abin.h"
#include "abin_E-S.h"

using namespace std;

typedef char tElto;
const tElto fin = '#';


//Ejercicio 1 - Calcular el numero de nodos de un arbol binario. 
//el recorrido del arbol es en profundidad
template <typename tElto>
int numeronodos(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    if (n == Abin<tElto>::NODO_NULO) {
        return 0;
    } else {
        return 1 + numeronodos(A, A.hijoIzqdo(n)) + numeronodos(A, A.hijoDrcho(n));
    }
}


//Ejercicio 2 - altura de un arbol binario
template <typename tElto>
int altura(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    if (n == Abin<tElto>::NODO_NULO) {
        return 0;
    } else {
        int hizq = 1 + altura(A, A.hijoIzqdo(n));
        int hder = 1 + altura(A, A.hijoDrcho(n));
        return (hizq > hder) ? hizq : hder;
    }
}

//Ejercicio 3 - dadop un arbol binario y un nodo del mismo, determine la profundidad de un nodo
template <typename tElto>
int profundidad(const Abin<tElto>& A, typename Abin<tElto>::nodo n){
    if (n == Abin<tElto>::NODO_NULO) {
        return 0;
    } else {
        return 1 + profundidad(A, A.padre(n));
    }
}

//Ejercicio 6 - nivel de desequilibrio de un arbol binario
template <typename tElto>
int desequilibrio (const Abin<tElto>& A){
    int niveld=0, niveli=0;
    if (A.hijoDrcho(0) != Abin<tElto>::NODO_NULO)
    niveld = 1 + A.altura(A.hijoDrcho(0));
    if (A.hijoIzqdo(0) != Abin<tElto>::NODO_NULO)
    niveli = 1 + A.altura(A.hijoIzqdo(0));
    return max(niveld, niveli);
}

//ejercicio 7 - arbol pseudo completo
template <typename tElto>
bool pseudocompleto (const Abin<tElto>& A){
    int n=0 ;
    if(A.arbolVacio() != Abin<tElto>::NODO_NULO){
        n = A.raiz();
        while(A.hijoDrcho(n) != Abin<tElto>::NODO_NULO || A.hijoIzqdo(n) != Abin<tElto>::NODO_NULO){

            //no se
        }
    }
    else
    return false;
}


int main(){
    Abin<tElto> A, B;
    ifstream fe("abin.dat"); // Abrir fichero de entrada.
    rellenarAbin(fe, A); // Desde fichero.
    fe.close();
    cout << "\n*** Mostrar árbol binario B ***\n";
    imprimirAbin(A); // En std::cout

    cout << "numero de nodos(A)= " << numeronodos(A, A.raiz()) << endl; //numero de nodos

    cout << "altura(A)= " << altura(A, A.raiz()) << endl; //altura del arbol

    cout << "profundidad de un nodo dado" << profundidad(A, A.hijoIzqdo(A.raiz())) << endl; //profundidad de un nodo
    getch();
}


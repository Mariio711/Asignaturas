#include <iostream>
#include <fstream>
#include "agenlis.h"
#include "agen_E-S.h"
#include "Ejercicios.cpp"

using namespace std;
typedef char tElto;
const tElto fin = '*'; // fin de lectura

int main (){
    Agen<tElto> A(16), B(16);
    cout << "*** Lectura del árbol A ***\n";
    rellenarAgen(A, fin); // Desde std::cin
    ofstream fs("agen.dat"); // Abrir fichero de salida.
    imprimirAgen(fs, A, fin); // En fichero.
    fs.close();
    cout << "\n*** Árbol A guardado en fichero agen.dat ***\n";
    cout << "\n*** Lectura de árbol B de agen.dat ***\n";
    ifstream fe("agen.dat"); // Abrir fichero de entrada.
    rellenarAgen(fe, B); // Desde fichero.
    fe.close();
    cout << "\n*** Mostrar árbol B ***\n";
    imprimirAgen(B); // En std::cout

    cout << "El grado del arbol es : " << gradoAgen(A) << endl;
    cout << "El deesequilibrio del arbol es : " << desequilibrioAgen(A) << endl;


    
    system("pause");
    return 0;
}
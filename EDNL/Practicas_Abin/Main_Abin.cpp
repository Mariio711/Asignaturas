#include <iostream>
#include <fstream>
#include <queue>

#include "Ej_P1.cpp"
#include "Ej_P2.cpp"



int main (){
    Abin<tElto> A, B;
    cout << "*** Lectura del árbol binario A ***\n";
    rellenarAbin(A, fin); // Desde std::cin
    ofstream fs("abin.dat"); // Abrir fichero de salida.
    imprimirAbin(fs, A, fin); // En fichero.
    fs.close();
    cout << "\n*** Árbol A guardado en fichero abin.dat ***\n";
    cout << "\n*** Lectura de árbol binario B de abin.dat ***\n";
    rellenarAbin(B, fin);
    cout << "\n*** Mostrar árbol binario B ***\n";
    imprimirAbin(B); // En std::cout
    

    if (AbinSimilares(A,B)){
        puts("SI son similares");
    }else
        puts("NO son similares");

    imprimirAbin(AbinRef(A));
    system("pause");
    return 0;
} 


/*5. Diseñe una función recursiva que devuelva la suma de todos los elementos i-ésimo de un vector A de n enteros que cumplan la siguiente propiedad:
1 ≤ i ≤ n/2 pte entera por exceso : A[i] = 2 · A[n − i + 1] 2
Implemente dicha función en C.*/

#include <stdio.h>

//cabecera: int suma(int *v, int n, int i)
//precondicion: n > 0, v es un vector de n enteros
//postcondicion: devuelve la suma de los elementos i-esimo de un vector A de n enteros que cumplan la propiedad A[i] = 2 · A[n − i + 1]

int sumarec(int *v, int n, int i, int suma){
    if(i < n/2){
        if(v[i] == 2 * v[n - i - 1]){
            suma += v[i];
        }
        return sumarec(v, n, i + 1, suma);
    }
    return suma;
}

//cabecera: int Llamada_suma(v, n);
//precondicion: n > 0, v es un vector de n enteros
//postcondicion: devuelve la suma de los elementos i-esimo de un vector A de n enteros que cumplan la propiedad A[i] = 2 · A[n − i + 1]

int Llamada_suma(int *v, int n){
    return sumarec(v, n, 0, 0);
}

//prueba, resultado esperado 20 + 16 = 36

int main(){
    int v[] = {20, 2, 16, 4, 5, 6, 7, 8, 9, 10}; 
    printf("La suma de los elementos i-esimo de un vector A de n enteros que cumplan la propiedad A[i] = 2 · A[n - i + 1] es: %d\n", Llamada_suma(v, 10));
    return 0;
}

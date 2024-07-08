/*1. Dado un vector A de n enteros, diseñe una función recursiva que determine si existen en el vector dos elementos cuyo producto sea el valor x.
Implemente dicha función en C.*/

#include <stdio.h>
#include <stdlib.h>

int llamada_producto(int *A, int n, int x);
int producto(int *A, int n, int x, int i, int j);

//cabecera: int llamada_producto(int *A, int n, int x)
//precondicion: A es un vector de n enteros, x es un entero
//postcondicion: devuelve 1 si existen dos elementos en A cuyo producto sea x, 0 en caso contrario
int llamada_producto(int *A, int n, int x){
    return producto(A, n, x, 0, 1);
}

//cabecera: int producto(int *A, int n, int x, int i, int j)
//precondicion: A es un vector de n enteros, x es un entero
//postcondicion: devuelve 1 si existen dos elementos en A cuyo producto sea x, 0 en caso contrario
int producto(int *A, int n, int x, int i, int j){
    if (i == n){
        return 0;
    }
    if (j == n){
        return producto(A, n, x, i+1, i+2);
    }
    if (A[i] * A[j] == x){
        return 1;
    }
    return producto(A, n, x, i, j+1);
}

//prueba

int main(){
    int A[] = {1, 2, 3, 4, 5};
    int n = 5;
    int x = 1;
    printf("%d\n", llamada_producto(A, n, x));
    return 0;
}
/* En la selección de personal de una empresa, a igualdad de puntuación en el baremo,
 deciden tener en cuenta los valores de algunos de los elementos por los que han sido evaluados los candidatos,
  utilizando para el desempate un criterio de decisión minimax, o también denominado pesimista, sobre esos valores.
 Dicho criterio consiste en seleccionar al candidato que tenga la nota más alta de entre las más bajas de cada uno de ellos.*/
 
#include <stdio.h>
#include <stdlib.h>

//cabecera: void minimax(int A[], int n, int i, int j, int min, int max)
//precondicion: n > 0, i = 0, j = 0, min = A[0], max = A[0]
//postcondicion: selecciona al candidato que tenga la nota más alta de entre las más bajas de cada uno de ellos

void minimax(int A[], int n, int i, int j, int min, int max){
    if (i == n){
        printf("El candidato seleccionado es el que tiene la nota mas alta de entre las mas bajas de cada uno de ellos\n");
        return;
    }
    if (j == n){
        printf("El candidato seleccionado es el que tiene la nota mas alta de entre las mas bajas de cada uno de ellos\n");
        return;
    }
    if (A[j] < min){
        min = A[j];
    }
    if (A[j] > max){
        max = A[j];
    }
    minimax(A, n, i + 1, j + 1, min, max);
}

//cabecera: void Llamada_minimax(int A[], int n)
//precondicion: n > 0
//postcondicion: selecciona al candidato que tenga la nota más alta de entre las más bajas de cada uno de ellos

void Llamada_minimax(int A[], int n){
    minimax(A, n, 0, 0, A[0], A[0]);
}

//prueba
int main(){
    int A[] = {1, 2, 3, 4, 5};
    Llamada_minimax(A, 5);
    return 0;
}
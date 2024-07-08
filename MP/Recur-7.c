/*Dado un vector A[1..n] de n enteros estrictamente positivos y ordenados crecientemente, siendo
n ≥ 1, diseñe una función recursiva que calcule el número de parejas (j, k) que cumplan:
1 ≤ j, k ≤ n : sumatorio desde α=1 hasta j de A[α] = A[k] */

#include <stdio.h>

//cabecera: int sumatorio(int A[], int n, int j, int k, int sum)
//precondicion: n > 0, j = 1, k = 1, sum = 0
//postcondicion: devuelve el numero de parejas (j, k) que cumplan: 1 ≤ j, k ≤ n : sumatorio desde α=1 hasta j de A[α] = A[k]

int sumatorio(int A[], int n, int j, int k, int sum) {
    if (j > n) {
        return sum;
    }
    if (A[j] == A[k]) {
        return sumatorio(A, n, j + 1, k, sum + 1);
    }
    if (A[j] < A[k]) {
        return sumatorio(A, n, j + 1, k, sum);
    }
    if (A[j] > A[k]) {
        return sumatorio(A, n, j, k + 1, sum);
    }
}

//cabecera: void Llamada_sumatorio(int A[], int n)
//precondicion: n > 0
//postcondicion: imprime el numero de parejas (j, k) que cumplan: 1 ≤ j, k ≤ n : sumatorio desde α=1 hasta j de A[α] = A[k]

void Llamada_sumatorio(int A[], int n){
    printf("%d\n", sumatorio(A, n, 1, 1, 0));
}

//prueba, resultado esperado 3 para A = {1, 2, 2, 3, 4}
int main(){
    int A[] = {1, 2, 2, 3, 4};
    Llamada_sumatorio(A, 5);
    return 0;
}
/*Desarrolle un procedimiento recursivo que, recibiendo como parámetro un número entero positivo n, genere la matriz que contenga todas las posibles descomposiciones del número como suma de dos cubos. Cada fila de la matriz deberá contener a una pareja. Por ejemplo, para el número 1729, la matriz será:
(1 12)
(9 10)
Nota.- No se pueden repetir parejas. En el ejemplo anterior se considera que la pareja 1,12 es igual a la pareja 12,1. Ídem con la pareja 9,10.
Implemente dicho procedimiento en C.
*/

#include <stdio.h>

//cabecera: int potencia(int base, int exponente)
//precondicion: exponente >= 0
//postcondicion: devuelve la base elevada al exponente

int potencia(int base, int exponente) {
    if (exponente == 0) {
        return 1;
    }
    return base * potencia(base, exponente - 1);
}

//cabecera: void descomposicion(int n, int i, int j)
//precondicion: n > 0, i = 0, j = 0
//postcondicion: genera la matriz que contenga todas las posibles descomposiciones del número como suma de dos cubos

void descomposicion(int n, int i, int j) {
    if (i > j) {
        return;
    }
    if (potencia(i, 3) + potencia(j, 3) == n) {
        printf("(%d %d)\n", i, j);
        descomposicion(n, i + 1, j - 1);
    } else if (potencia(i, 3) + potencia(j, 3) < n) {
        descomposicion(n, i, j - 1);
    } else {
        descomposicion(n, i + 1, j);
    }
}

//cabecera: void Llamada_descomposicion(int n)
//precondicion: n > 0
//postcondicion: genera la matriz que contenga todas las posibles descomposiciones del número como suma de dos cubos

void Llamada_descomposicion(int n){
    descomposicion(n, 0, n);
}

//prueba, resultado esperado (1 12) (9 10) para n = 1729
int main(){
    Llamada_descomposicion(1729);
    return 0;
}
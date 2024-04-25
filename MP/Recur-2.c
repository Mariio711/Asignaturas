/*2. Diseñe una función recursiva que devuelva el máximo común divisor de dos números n y m, utilizando el algoritmo de Euclides.
Implemente dicha función en C.
*/

#include <stdio.h>
#include <stdlib.h>

int mcd(int n, int m);

//cabecera: int mcd(int n, int m)
//precondicion: n y m son enteros positivos
//postcondicion: devuelve el maximo comun divisor de n y m usando el algoritmo de auclides

int mcd(int n, int m){
    if (m == 0){
        return n;
    }
    return mcd(m, n % m);
}

//prueba

int main(){
    int n = 12;
    int m = 18;
    int a = 120;
    int b = 34;

    printf("El mcd de %d y %d = %d\n", a, b, mcd(a, b));
    printf("El mcd de %d y %d = %d\n", n, m, mcd(n, m));

}
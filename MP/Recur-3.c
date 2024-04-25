/*3. Diseñe una función recursiva que devuelva el producto de dos números mediante la multiplicación rusa.
Implemente dicha función en C.*/

#include <stdio.h>
#include <stdlib.h>

int multiplicacion_rusa(int n, int m);

//cabecera: int multiplicacion_rusa(int n, int m)
//precondicion: n y m son ensteros
//postcondicion: devuelve el producto de n y m usando el algoritmo de la multiplicacion rusa
int multiplicacion_rusa(int n, int m){
    if (n == 1){
        return m;
    }
    if (n % 2 == 0){
        return multiplicacion_rusa(n/2, m*2);
    }
    return m + multiplicacion_rusa(n-1, m); //se va acumulando cuando n es impar (se resta 1 para que)
}

//prueba

int main(){
    int n = 12;
    int m = 18;
    int a = 120;
    int b = 34;

    printf("El producto de %d y %d = %d\n", a, b, multiplicacion_rusa(a, b));
    printf("El producto de %d y %d = %d\n", n, m, multiplicacion_rusa(n, m));

}
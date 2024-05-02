/*6. Diseñe un procedimiento recursivo que, dado un número natural n, encuentre dos números
s naturales k y s tal que n = sumatorio desde i=1 hasta s de i^k.
Implemente dicho procedimiento en C.*/

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

//cabecera: void encuentra(int n, int k, int s, int i, int sum)
//precondicion: n > 0, k > 0, s > 0,  i = 1
//postcondicion: encuentra dos numeros naturales k y s tal que n = sumatorio desde i=1 hasta s de i^k.
void encuentra(int n, int k, int s) {
    int sum = 0;
    for (int i = 1; i <= s; i++) {
        sum += potencia(i, k);
    }
    if (sum == n) {
        printf("k = %d, s = %d\n", k, s);
        return;
    }
    if (sum < n) {
        encuentra(n, k, s + 1);
    } else {
        encuentra(n, k + 1, 1);
    }
}

//cabecera: void Llamada_sumatorio(int n)
//precondicion: n > 0, k > 0, s > 0,  i = 1
//postcondicion: encuentra dos numeros naturales k y s tal que n = sumatorio desde i=1 hasta s de i^k

void Llamada_sumatorio(int n){
    encuentra(n, 1, 1);
}


//prueba, resultado esperado k = 3, s = 4 para n = 100
int main(){
    Llamada_sumatorio(100);
    return 0;
}
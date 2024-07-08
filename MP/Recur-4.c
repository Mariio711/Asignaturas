/*4. Diseñe una función recursiva que devuelva xy, siendo y > 0. Implemente dicha función en C.*/

#include <stdio.h>

//cabecera: int Elevadorecur(int x, int y, int aux);
//preciondicion: x es un entero e y es un entero positivo
//postcondicion: devuelve x^y
int Elevadorecur(int x, int y, int aux){
    if (y == 1){
        return x;
    }else{
        return Elevadorecur(x*aux, y-1, aux);
    }
}


//cabecera: int Llamada_Elevadorecur(int x, int y);
//preciondicion: x es un entero e y es un entero positivo
//postcondicion: devuelve x^y
int Llamada_Elevadorecur(int x, int y){
    return Elevadorecur(x, y, x);
}


//prueba

int main() {
    int base = 2;
    int exponente = 4;
    int resultado = Llamada_Elevadorecur(base, exponente);
    printf("El resultado de %d elevado a %d es %d\n", base, exponente, resultado);
    return 0;
}

#include <polinom.h>


//Cabezera: polinomio operator +(const polinomio& pol1, const polinomio& pol2)
//Precondición: Recibe dos polinomios en el orden el cual se quiere sumar pol1 es el sumando y pol2 el sumado
//Postcondición: Devuelve la suma pol1 + pol2
polinomio operator +(const polinomio& pol1, const polinomio& pol2){
    int gradopol1, gradopol2, gradoRes;

    //Almacenamos el grado de los polinomios
    gradopol1 = pol1.grado();
    gradopol2 = pol2.grado();

    //Genereamos el polinomio resultado con el grado del mas grande
    if(gradopol1 >= gradopol2){
        gradoRes = gradopol1;
    }else{
        gradoRes = gradopol2;
    }
    polinomio PolRes(gradoRes);

    //Sumamos uno a uno los elementos, y lo asignamos al polinomio resultado
    for(int n = 0; n <= gradoRes; n++){
        PolRes.coeficiente(n, (pol1.coeficiente(n) + pol2.coeficiente(n)));
    }
}

//Cabezera: polinomio operator -(const polinomio& pol1, const polinomio& pol2)
//Precondición: Recibe dos polinomios en el orden el cual se quiere restar pol1 es el restando y pol2 el restado
//Postcondición: Devuelve la resta pol1 - pol2
polinomio operator -(const polinomio& pol1, const polinomio& pol2){
    int gradopol1, gradopol2, gradoRes;

    //Almacenamos el grado de los polinomios
    gradopol1 = pol1.grado();
    gradopol2 = pol2.grado();

    //Genereamos el polinomio resultado con el grado del mas grande
    if(gradopol1 >= gradopol2){
        gradoRes = gradopol1;
    }else{
        gradoRes = gradopol2;
    }
    polinomio PolRes(gradoRes);

    //Restamos uno a uno los elementos, y lo asignamos al polinomio resultado
    for(int n = 0; n <= gradoRes; n++){
        PolRes.coeficiente(n, (pol1.coeficiente(n) - pol2.coeficiente(n)));
    }
}

//Cabezera: polinomio operator *(const polinomio& pol1, const polinomio& pol2)
//Precondición: Recibe dos polinomios
//Postcondición: Devuelve el producto pol1 x pol2
polinomio operator *(const polinomio& pol1, const polinomio& pol2){
        int gradopol1, gradopol2;

    //Almacenamos el grado de los polinomios
    gradopol1 = pol1.grado();
    gradopol2 = pol2.grado();

    //Genereamos el polinomio resultado
    polinomio PolRes(gradopol1 + gradopol2);
    int aux[gradopol1 + gradopol2];

    //multiplicamos uno a uno los elementos, y lo asignamos al auxiliar, teniendo en cuenta que los grados stambien se multiplican
    for(int n = 0; n <= gradopol1; n++){
        for (int i = 0; i <= gradopol2; i++)
        aux[n + i] += pol1.coeficiente(n) * pol2.
    };
}
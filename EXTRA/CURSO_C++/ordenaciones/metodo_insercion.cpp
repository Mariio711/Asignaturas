/**
 * Este programa ordena un arreglo de números utilizando el método de inserción.
 * El usuario debe ingresar el número de elementos y luego los números a ordenar.
 * Luego de ordenar el arreglo, se muestra el resultado en orden ascendente y descendente.
 */
#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    int numeros[100], n, aux;
    cout << "Digite el numero de elementos: ";
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << "Digite un numero: ";
        cin >> numeros[i];
    }

    // Metodo de insercion
    for (int i = 0; i < n; i++)
    {
        int j = i;
        aux = numeros[i];
        while (j > 0 && aux < numeros[j - 1])
        {
            numeros[j] = numeros[j - 1];
            j--;
        }
        numeros[j] = aux;
    }

    cout << "\nOrden ascendente: ";
    for (int i = 0; i < n; i++)
    {
        cout << numeros[i] << " ";
    }

    cout << "\nOrden descendente: ";
    for (int i = n - 1; i >= 0; i--)
    {
        cout << numeros[i] << " ";
    }

    getch();
    return 0;
}
#include <iostream>
#include <stdio.h>

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

    // Metodo burbuja
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (numeros[j] > numeros[j + 1])
            {
                aux = numeros[j];
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = aux;
            }
        }
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

    cin.get();
    return 0;
}
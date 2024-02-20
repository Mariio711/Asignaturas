#include <iostream> // for std::cout, std::cin
  // for getch

using namespace std; // for std::cout, std::cin

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

    // Metodo de seleccion
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (numeros[j] < numeros[min])
            {
                min = j;
            }
        }
        aux = numeros[i];
        numeros[i] = numeros[min];
        numeros[min] = aux;
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
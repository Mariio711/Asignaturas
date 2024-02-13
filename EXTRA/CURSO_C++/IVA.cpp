#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    float precio, iva, total;
    cout << "Introduce el precio del producto: ";
    cin >> precio;
    iva = precio * 0.21;
    total = precio + iva;
    cout << "El precio del producto es: " << precio << endl;
    cout << "El IVA es: " << iva << endl;
    cout << "El precio total es: " << total << endl;
    system ("pause");
    return 0;
}
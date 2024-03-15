#ifndef ABIN_E_S_H
#define ABIN_E_S_H

#include <cassert>
#include <iostream>
#include <fstream>

using std::istream;
using std::ostream;
using std::cin;
using std::cout;
using std::endl;

template <typename T>
void rellenarAbin(Abin<T>& A, const T& fin)
// Pre: A está vacío.
// Post: Rellena el árbol A con la estructura y elementos
//       leídos en preorden de la entrada estándar, usando
//       fin como elemento especial para introducir nodos nulos.
{
   T e;

   assert(A.arbolVacio());
   cout << "Raíz (Fin = " << fin << "): "; cin >> e;
   if (e != fin) {
      A.insertarRaiz(e);
      rellenarDescendientes(A.raiz(), A, fin);
   }
}

template <typename T>
void rellenarDescendientes(typename Abin<T>::nodo n, Abin<T>& A, const T& fin)
// Pre: n es un nodo hoja de A.
// Post: Lee de la entrada estándar y en preorden los descendientes de n,
//       usando fin para introducir nodos nulos.
{
   T ehi, ehd;

   assert(A.hijoIzqdo(n) == Abin<T>::NODO_NULO &&
          A.hijoDrcho(n) == Abin<T>::NODO_NULO);
   cout << "Hijo izqdo. de " << A.elemento(n) <<
                " (Fin = " << fin << "): ";
   cin >> ehi;
   if (ehi != fin) {
      A.insertarHijoIzqdo(n, ehi);
      rellenarDescendientes(A.hijoIzqdo(n), A, fin);
   }
   cout << "Hijo drcho. de " << A.elemento(n) <<
                " (Fin = " << fin << "): ";
   cin >> ehd;
   if (ehd != fin) {
      A.insertarHijoDrcho(n, ehd);
      rellenarDescendientes(A.hijoDrcho(n), A, fin);
   }
}

template <typename T>
void rellenarAbin(istream& is, Abin<T>& A)
// Pre: A está vacío.
// Post: Extrae los nodos de A del flujo de entrada is,
//       que contendrá el elemento especial que denota
//       un nodo nulo seguido de los elementos en preorden,
//       incluyendo los correspondientes a nodos nulos.
{
   T e, fin;

   assert(A.arbolVacio());
   if (is >> fin && is >> e && e != fin) {
      A.insertarRaiz(e);
      rellenarDescendientes(is, A.raiz(), A, fin);
   }
}

template <typename T>
void rellenarDescendientes(istream& is, typename Abin<T>::nodo n, Abin<T>& A, const T& fin)
// Pre: n es un nodo hoja de A.
// Post: Lee del flujo de entrada is y en preorden los descendientes de n,
//       usando fin para los nodos nulos.
{
   T ehi, ehd;

   assert(A.hijoIzqdo(n) == Abin<T>::NODO_NULO &&
          A.hijoDrcho(n) == Abin<T>::NODO_NULO);
   if (is >> ehi && ehi != fin) {
      A.insertarHijoIzqdo(n, ehi);
      rellenarDescendientes(is, A.hijoIzqdo(n), A, fin);
   }
   if (is >> ehd && ehd != fin) {
      A.insertarHijoDrcho(n, ehd);
      rellenarDescendientes(is, A.hijoDrcho(n), A, fin);
   }
}

template <typename T>
void imprimirAbin (const Abin<T>& A)
// Post: Muestra los nodos de A en la salida estándar.
{
   if (!A.arbolVacio())
   {
      cout << "Raíz del árbol: "
                << A.elemento(A.raiz()) << endl;
      imprimirDescendientes(A.raiz(), A);
   }
   else
      cout << "Árbol vacío\n";
}

template <typename T>
void imprimirDescendientes (typename Abin<T>::nodo n, const Abin<T>& A)
// Post: Muestra los descendientes de n en la salida estándar.
{
   if (A.hijoIzqdo(n) != Abin<T>::NODO_NULO)
   {
      cout << "Hijo izqdo de " << A.elemento(n) << ": "
                << A.elemento(A.hijoIzqdo(n)) << endl;
      imprimirDescendientes(A.hijoIzqdo(n), A);
   }
   if (A.hijoDrcho(n) != Abin<T>::NODO_NULO)
   {
      cout << "Hijo derecho de " << A.elemento(n) << ": "
                << A.elemento(A.hijoDrcho(n)) << endl;
      imprimirDescendientes(A.hijoDrcho(n), A);
   }
}

template <typename T>
void imprimirAbin (ostream& os, const Abin<T>& A, const T& fin)
// Post: Inserta en el flujo de salida os los nodos de A en preorden,
//       precedidos del elemento especial usado para denotar un nodo nulo.
{
   if (!A.arbolVacio())
   {
      os << fin << endl
         << A.elemento(A.raiz()) << ' ';
      imprimirDescendientes(os, A.raiz(), A, fin);
      os << endl;
   }
}

template <typename T>
void imprimirDescendientes (ostream& os, typename Abin<T>::nodo n, const Abin<T>& A, const T& fin)
// Post: Inserta en el flujo de salida os y en preorden
//       los descendientes de n, usando fin como nodo nulo.
{
   if (A.hijoIzqdo(n) != Abin<T>::NODO_NULO)
   {
      os << A.elemento(A.hijoIzqdo(n)) << ' ';
      imprimirDescendientes(os, A.hijoIzqdo(n), A, fin);
   }
   else
      os << fin << ' ';
   if (A.hijoDrcho(n) != Abin<T>::NODO_NULO)
   {
      os << A.elemento(A.hijoDrcho(n)) << ' ';
      imprimirDescendientes(os, A.hijoDrcho(n), A, fin);
   }
   else
      os << fin << ' ';
}


class Elemento {
public:
   double operando;
   char operador;

   Elemento(double operando = 0, char operador = 0)
      : operando(operando), operador(operador) {}
};

// Sobrecarga del operador de inserción <<
std::ostream& operator<<(std::ostream& os, const Elemento& e) {
   if (e.operador != 0) {
      os << "Operador: " << e.operador;
   } else {
      os << "Operando: " << e.operando;
   }
   return os;
}

// Sobrecarga del operador de extracción >>
std::istream& operator>>(std::istream& is, Elemento& e) {
   // Aquí necesitarías definir cómo se lee un Elemento de la entrada
   // Por ejemplo, podrías leer primero un operador y, si es un caracter válido,
   // asignarlo al campo operador de e. Si no es un caracter válido, podrías
   // tratar de leerlo como un operando.
   // Este es solo un ejemplo y necesitarías adaptarlo a tus necesidades.
   char c;
   if (is >> c && (c == '+' || c == '-' || c == '*' || c == '/')) {
      e.operador = c;
      e.operando = 0;
   } else {
      is.unget();
      if (is >> e.operando) {
         e.operador = 0;
      } else {
         // Maneja el error como prefieras
      }
   }
   return is;
}

// Sobrecarga del operador de desigualdad !=
bool operator!=(const Elemento& e1, const Elemento& e2) {
   return e1.operando != e2.operando || e1.operador != e2.operador;
}
#endif  //ABIN_E_S_H

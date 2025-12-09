#ifndef ABIN_H_
#define ABIN_H_

#include <cassert>
#include <cstddef> //size_t
#include <utility> //swap

template <typename T>
class Abin
{
    struct celda; // declaración adelantada privada
public:
    typedef celda *nodo;
    static const nodo NODO_NULO;

    Abin();
    void insertarRaiz(const T &e);
    void insertarHijoIzqdo(nodo n, const T &e);
    void insertarHijoDrcho(nodo n, const T &e);
    void eliminarHijoIzqdo(nodo n);
    void eliminarHijoDrcho(nodo n);
    void eliminarRaiz();
    bool vacio() const;
    size_t tama() const;
    const T &elemento(nodo n) const; // Lec. en abin const
    T &elemento(nodo n);             // Lec./Esc. en abin no-const
    nodo raiz() const;
    nodo padre(nodo n) const;
    nodo hijoIzqdo(nodo n) const;
    nodo hijoDrcho(nodo n) const;
    Abin(const Abin &A);            // Ctor de copia
    Abin &operator=(const Abin &A); // Asig. de arboles
    ~Abin();

private:
    struct celda
    {
        T elto;
        nodo padre, hizq, hder;
    };
    nodo r;          // raiz del arbol
    size_t numNodos; // tamaño del arbol
    nodo copiar(nodo n);
    void destruir(nodo &n);
}; // class Abin

// definicion del nodo nulo
template <typename T>
const typename Abin<T>::nodo Abin<T>::NODO_NULO = {nullptr};

// ctor por defecto
template <typename T>
inline Abin<T>::Abin() : r{NODO_NULO}, numNodos{0} {}

// insercion de la raiz
template <typename T>
inline void Abin<T>::insertarRaiz(const T &e)
{
    asser(vacio());
    r = new celda{e};
    numNodos = 1
}

// inserción hijo izquierdo
template <typename T>
inline void Abin<T>::insertarHijoIzqdo(nodo n, const T &e)
{
    assert(n != NODO_NULO);
    assert(n->hizq == NODO_NULO);
    n->hizq = new celda{e, n};
    ++numNodos;
}

// inserción hijo derecho
template <typename T>
inline void Abin<T>::insertarHijoDrcho(nodo n, const T &e)
{
    assert(n != NODO_NULO);
    assert(n->hder == NODO_NULO);
    n->hder = new celda{e, n};
    ++numNodos;
}

// eliminación hijo izquierdo
template <typename T>
inline void Abin<T>::eliminarHijoIzqdo(nodo n)
{
    assert(n != NODO_NULO);
    assert(n->hizq != NODO_NULO);                                     // existe hijo izquierdo
    assert(n->hizq->hizq == NODO_NULO && n->hizq->hder == NODO_NULO); // y es hoja
    delete n->hizq;
    n->hizq = NODO_NULO;
    --numNodos;
}

// eliminación hijo derecho
template <typename T>
inline void Abin<T>::eliminarHijoIzqdo(nodo n)
{
    assert(n != NODO_NULO);
    assert(n->hder != NODO_NULO);                                     // existe hijo izquierdo
    assert(n->hder->hizq == NODO_NULO && n->hder->hder == NODO_NULO); // y es hoja
    delete n->hder;
    n->hder = NODO_NULO;
    --numNodos;
}

// eliminacion de la raiz
template <typename T>
inline void Abin<T>::eliminarRaiz()
{
    assert(numNodos == 1);
    delete r;
    r = NODO_NULO;
    numNodos = 0;
}

// comprobacion si el arbol esta vacio
template <typename T>
inline bool Abin<T>::vacio() const
{
    return numNodos == 0;
}

// devuelve el tamaño del atbol
template <typename T>
inline size_t Abin<T>::tama() const
{
    return numNodos;
}

// devuelve el elemento del nodo const
template <typename T>
inline const T &Abin<T>::elemento(nodo n) const
{
    assert(n != NODO_NULO);
    return n->elto;
}

// devuelve el elemento del nodo no-const
template <typename T>
inline T &Abin<T>::elemento(nodo n)
{
    assert(n != NODO_NULO);
    return n->elto;
}

// devuelve la raiz del arbol
template <typename T>
inline typename Abin<T>::nodo Abin<T>::raiz() const
{
    return r;
}

// devuelve el padre del nodo
template <typename T>
inline
    typename Abin<T>::nodo
    Abin<T>::padre(nodo n) const
{
    assert(n != NODO_NULO);
    return n->padre;
}

// devuelve el hijo izquierdo del nodo
template <typename T>
inline
    typename Abin<T>::nodo
    Abin<T>::hijoIzqdo(nodo n) const
{
    assert(n != NODO_NULO);
    return n->hizq;
}

// devuelve el hijo derecho del nodo
template <typename T>
inline
    typename Abin<T>::nodo
    Abin<T>::hijoDrcho(nodo n) const
{
    assert(n != NODO_NULO);
    return n->hder;
}

// constructor de copia
template <typename T>
inline Abin<T>::Abin(const Abin &A) : Abin{}
{
    r = copiar(A.r); // Copiar raíz y descendientes.
    numNodos = A.numNodos;
}

// operador de asignación
template <typename T>
inline Abin<T> &Abin<T>::operator=(const Abin &A)
{
    Abin B{A};
    std::swap(r, B.r);
    std::swap(numNodos, B.numNodos);
    return *this;
}

// eliminar arbol completo
template <typename T>
inline Abin<T>::~Abin()
{
    destruir(r); // Vaciar el árbol.
}

/*--------------------------------------------------------*/
/* Métodos privados */
/*--------------------------------------------------------*/

// Destruye un nodo y todos sus descendientes
template <typename T>
void Abin<T>::destruir(nodo &n)
{
    if (n != NODO_NULO)
    {
        destruir(n->hizq);
        destruir(n->hder);
        delete n;
        n = NODO_NULO;
    }
}

// Devuelve una copia de un nodo y todos sus descendientes
template <typename T>
typename Abin<T>::nodo Abin<T>::copiar(nodo n)
{
    nodo m = NODO_NULO;
    if (n != NODO_NULO)
    {
        Abin A;                      // Contiene los nodos copiados.
                                     // Si la copia no se completa, A es destruido.
        A.r = new celda{n->elto};    // Copiar n en raíz.
        A.r->hizq = copiar(n->hizq); // Copiar subárbol izqdo.
        if (A.r->hizq != NODO_NULO)
            A.r->hizq->padre = A.r;
        A.r->hder = copiar(n->hder); // Copiar subárbol drcho.
        if (A.r->hder != NODO_NULO)
            A.r->hder->padre = A.r;
        m = A.r;
        A.r = NODO_NULO; // Evita destruir la copia.
    }
    return m;
}

#endif
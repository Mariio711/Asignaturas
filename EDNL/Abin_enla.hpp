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

//inserción hijo derecho
template <typename T>
inline void Abin<T>::insertarHijoDrcho(nodo n, const T& e)
{
    assert(n != NODO_NULO);
    assert(n->hder == NODO_NULO);
    n->hder = new celda{e, n};
    ++numNodos;
}

// eliminación hijo izquierdo

#endif
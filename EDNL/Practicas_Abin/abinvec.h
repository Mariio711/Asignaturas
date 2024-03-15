#include <vector>
#include <cmath>
#include <cassert>
#include <cstddef>

template <typename T>
class Abin {
public:
    typedef int nodo; // Índice del vector
    static const nodo NODO_NULO;
    explicit Abin(size_t H = 0); // Árbol vacío
    void insertarRaiz(const T& e);
    void insertarHijoIzqdo(nodo n, const T& e);
    nodo padre(nodo n) const;

private:
    struct celda {
        T elto;
        nodo padre;
        celda(const T& e, nodo p = NODO_NULO) : elto(e), padre(p) {}
    };
    std::vector<celda> nodos; // Vector de nodos
    size_t alturaMax; // Altura máxima del árbol
    int altura(nodo n) const; // Calcula la altura de un nodo
};

template <typename T>
const typename Abin<T>::nodo Abin<T>::NODO_NULO(-1);

template <typename T>
Abin<T>::Abin(size_t H) : nodos(1), alturaMax(H) {}

template <typename T>
void Abin<T>::insertarRaiz(const T& e) {
    assert(nodos[0].elto == T()); // Árbol vacío
    nodos[0].elto = e;
}

template <typename T>
void Abin<T>::insertarHijoIzqdo(nodo n, const T& e) {
    assert(n >= 0 && n < nodos.size());
    assert(nodos[n].elto != T()); // Nodo existente
    int h = altura(n);
    nodo pos = n - std::pow(2, h - 1);
    if (pos >= nodos.size()) {
        nodos.resize(pos + 1);
    }
    nodos[pos] = celda(e, n);
}

template <typename T>
typename Abin<T>::nodo Abin<T>::padre(nodo n) const {
    assert(n >= 0 && n < nodos.size());
    return nodos[n].padre;
}

template <typename T>
int Abin<T>::altura(nodo n) const {
    assert(n >= 0 && n < nodos.size());
    int p = 0; // Profundidad del nodo
    for (nodo m = n; m != NODO_NULO; m = padre(m)) {
        ++p;
    }
    return alturaMax - p;
}
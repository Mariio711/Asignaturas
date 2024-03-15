#ifndef LISTAENL_H_INCLUDED
#define LISTAENL_H_INCLUDED
#include<cassert>
#include<iostream>
//#include"celdasgen.h"

using namespace std;

template <typename T> class Lista {
struct nodo; // Declaración adelantada privada
public:
    typedef nodo* posicion; // Posición de un elemento
    Lista(); // Constructor, requiere ctor. T()
    Lista(const Lista<T>& Lis); // Ctor. de copia, requiere ctor. T()
    Lista<T>& operator =(const Lista<T>& Lis); // Asig. de listas
    void insertar(const T& x, posicion p);
    void eliminar(posicion p);
    void destruir(Lista<T> &, const T&);
    const T& elemento(posicion p) const;// Lec. elto. en Lista const
    T& elemento(posicion p); // Lec/Esc elto. en Lista no=const
    posicion siguiente(posicion p) const;
    posicion anterior(posicion p) const;
    posicion primera() const;
    posicion fin() const; // Posición después del último
    void show();
    void ImprimeInverso();
    ~Lista(); // Destructor
private:
    struct nodo {
        T elto;
        nodo* sig;
        nodo(const T& e, nodo* p = nullptr): elto(e), sig(p) {}
    };
    nodo* L; // Lista enlazada de nodos

    void copiar(const Lista<T>& Lis);
};


// Método privado
template <typename T>
void Lista<T>::copiar(const Lista<T> &Lis)
{
    L = new nodo(T()); // Crear el nodo cabecera
    nodo* q = L;
    for (nodo* r = Lis.L->sig; r; r = r->sig) {
        q->sig = new nodo(r->elto);
        q = q->sig;
    }
}

template <typename T>
inline Lista<T>::Lista() : L(new nodo(T())) // Crear cabecera
{}

template <typename T>
inline Lista<T>::Lista(const Lista<T>& Lis)
{
    copiar(Lis);
}

template <typename T>
Lista<T>& Lista<T>::operator =(const Lista<T>& Lis)
{
    if (this != &Lis) { // Evitar autoasignación
        this->~Lista(); // Vaciar la lista actual
        copiar(Lis);
    }
    return *this;
}

template <typename T>
inline void Lista<T>::insertar(const T& x, posicion p)
{
    p->sig = new nodo(x, p->sig);
    // El nuevo nodo con x queda en la posición p
}

template <typename T>
inline void Lista<T>::eliminar(posicion p)
{
    assert(p->sig); // p no es fin
    nodo* q = p->sig;
    p->sig = q->sig;
    delete q;
    // El nodo siguiente queda en la posición p
}

template <typename T>
inline const T& Lista<T>::elemento(posicion p) const
{
    assert(p->sig); // p no es fin
    return p->sig->elto;
}

template <typename T>
inline T& Lista<T>::elemento(posicion p)
{
    assert(p->sig); // p no es fin
    return p->sig->elto;
}

template <typename T> inline
typename Lista<T>::posicion Lista<T>::siguiente(posicion p) const
{
    assert(p->sig); // p no es n
    return p->sig;
}

template <typename T>
typename Lista<T>::posicion Lista<T>::anterior(posicion p) const
{
    assert(p != L); // p no es la primera posición
    nodo* q;
    for (q = L; q->sig != p; q = q->sig);
    return q;
}

template <typename T>
inline typename Lista<T>::posicion Lista<T>::primera() const
{ return L; }

template <typename T>
typename Lista<T>::posicion Lista<T>::fin() const
{
    nodo* p;
    for (p = L; p->sig; p = p->sig);
    return p;
}

// Destructor: destruye el nodo cabecera y vacía la lista
template <typename T> Lista<T>::~Lista()
{
    nodo* q;
    while (L) {
        q = L->sig;
        delete L;
        L = q;
    }
}

template <typename T>
void Lista<T>::destruir(Lista& l, const T& x){
    assert(L->sig);
    nodo *q=L;
    nodo *p;
    while(q->sig){
        if(q->sig->elto==x){
            p=q->sig;
            q->sig=p->sig;
            delete p;
        }else{
            q=q->sig;
        }
    }
}

template <typename T>
void Lista<T>::show(){
    nodo *p=L;
    while(p->sig){
        cout<<p->sig->elto<<endl;
        p=p->sig;
    }
}

/*template <typename T>
void Lista<T>::ImprimeInverso(){
    Pila<int> P;
    nodo *p=L;
    while(p->sig){
        P.push(p->sig->elto);
        p=p->sig;
    }
    while(!P.vacia()){
        cout<<P.tope()<<endl;
        P.pop();
    }
}*/

#endif // LISTAENL_H_INCLUDED

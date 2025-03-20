#include "cadena.hpp"
#include <stdexcept>

//constructor predeterminado
Cadena::Cadena(int n, char a):tam_(n), s_(new char[n + 1]){
    std::memset(s_, a, n);
    s_[n] = '\0';
};

//constructor de conversión
Cadena::Cadena(const char* cadena) : tam_(std::strlen(cadena)), s_(new char[tam_ + 1]) {
    std::strcpy(s_, cadena);
}

//constructor de copia
Cadena::Cadena(const Cadena& otra): Cadena(otra.s_){}       //delegamos la copia en la conversion

//operador de asignacion
Cadena& Cadena::operator=(const Cadena& otra) {
    if (this != &otra) {
        delete[] s_; // Liberar la memoria existente
        tam_ = otra.tam_;
        s_ = new char[tam_ + 1];
        std::strcpy(s_, otra.s_);
    }
    return *this;
}

//destructor
Cadena::~Cadena(){
    delete[] s_;
}

//operadores de comparacion
bool operator==(const Cadena& a, const Cadena& b){
    return std::strcmp(a.s_, b.s_) == 0;
}

bool operator<(const Cadena& a, const Cadena& b) {
    return std::strcmp(a.s_, b.s_) < 0;
}

bool operator>(const Cadena& a, const Cadena& b) {
    return std::strcmp(a.s_, b.s_) > 0;
}

bool operator<=(const Cadena& a, const Cadena& b) {
    return std::strcmp(a.s_, b.s_) <= 0;
}

bool operator>=(const Cadena& a, const Cadena& b) {
    return std::strcmp(a.s_, b.s_) >= 0;
}

bool operator!=(const Cadena& a, const Cadena& b) {
    return std::strcmp(a.s_, b.s_) != 0;
}

//operaodres de indice
//no const
char& Cadena::operator[](size_t i){
    return s_[i];
}

//const
const char& Cadena::operator[](size_t i) const{
    return s_[i];
}

/*-----------------METODOS------------------*/
//funcion que devuleve el caracter del indice comprobando si este esta o no fuera de rango
//no const
char& Cadena::at(size_t i){
    if (i >= length()){
        throw std::out_of_range("Indice fuera de rango");
    }
    return s_[i];
}

//const
const char& Cadena::at(size_t i) const {
    if (i >= length()) {
        throw std::out_of_range("Índice fuera de rango");
    }
    return s_[i];
}

//funcion que devuelve una cadena formada por los caracteres desde el indice i hasta los caracteres tam.
Cadena Cadena::substr(unsigned int i, unsigned int tam) const{
    if (i >= length() || (length() - i) < tam){
        throw std::out_of_range("Indice fuera de rango o tamaño de la cadena supera los caracteres desde el indice");
    }
    char* subs = new char[tam + 1];
    std::strncpy(subs, s_ +i, tam);
    subs[tam] = '\0';
    Cadena res(subs);
    delete[] subs;
    return res;
}


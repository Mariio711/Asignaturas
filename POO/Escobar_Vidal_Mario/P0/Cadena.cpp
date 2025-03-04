#include "Cadena.hpp"

//constructor

Cadena::Cadena(int n, char a):longitud_{n}{
    if (n == 0){
        cadena_ = new char[1];
        cadena_[0] = '\0';
    }else{
        cadena_ = new char[n +1];
        std::memset(cadena_, a, n);
        cadena_[n] = '\0';
    }
};
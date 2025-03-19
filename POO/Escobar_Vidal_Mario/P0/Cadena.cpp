#include "cadena.hpp"

//constructor predeterminado
Cadena::Cadena(int n, char a):tam_(n), cadena_(new char[n + 1]){
    std::memset(cadena_, a, n);
    cadena_[n] = '\0';
};
#ifndef CADENA_H_
#define CADENA_H_

#include <cstring>

class Cadena{
    public:
        //constructor
        Cadena(int n = 0, char a = '\0');

        //metodos observadores

        size_t lenght() const {return strlen(cadena_);}; //devuelve la longitud de la cadena c
    private:
        char vacia[1]{'\0'};
        size_t tam_;
        char* cadena_{}†;

};

#endif 
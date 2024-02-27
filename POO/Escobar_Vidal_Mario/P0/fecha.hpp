#ifndef Fecha_H
#define Fecha_H

#include <iostream>
#include <string>
#include <ctime>
#include <cassert>

class Fecha {
public:

    static const int AnnoMaximo = 2037;
    static const int AnnoMinimo = 1902;
    Fecha(int d=0, int m=0, int a=0);
    Fecha(char* f);
    void verificacion(int d, int m, int a);
    Fecha operator ++();
    Fecha operator --();
    Fecha operator -(int a);
    Fecha operator +(int a);

    class Invalida{
        public:
        
            Invalida(const char* razon) : razon_{razon} {}
            const char* por_que() const {return razon_;}
        private:

            const char* razon_;
    };
private:

    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
};

#endif //Fecha_H
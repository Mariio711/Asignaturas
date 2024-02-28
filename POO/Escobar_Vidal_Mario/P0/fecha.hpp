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

    //operadores aritmeticos
    Fecha& operator +=(int n);
    Fecha& operator -=(int n);
    Fecha& operator +(int n);
    Fecha& operator -(int n);
    Fecha& operator ++();
    Fecha& operator ++(int);
    Fecha& operator --();
    Fecha& operator --(int);

    //operadores logicos
    bool operator ==(const Fecha& otra) const;
    bool operator <(const Fecha& otra) const;
    bool operator !=(const Fecha& otra) const;
    bool operator >(const Fecha& otra) const;
    bool operator <=(const Fecha& otra) const;
    bool operator >=(const Fecha& otra) const;

    //metodos observadores
    const int dia() const;
    const int mes() const;
    const int anno() const;


    class Invalida{
        public:
        
            Invalida(const char* razon) : razon_{razon} {}
            const char* por_que() const {return razon_;}
        private:

            const char* razon_;
    };
private:
    void verificacion();
    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
};

#endif //Fecha_H
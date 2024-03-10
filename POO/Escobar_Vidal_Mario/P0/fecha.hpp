#ifndef Fecha_H
#define Fecha_H

#include <iostream>
#include <cstring>
#include <ctime>
#include <cassert>

class Fecha {
public:

    //parametros
    static const int AnnoMaximo = 2037;
    static const int AnnoMinimo = 1902;
    mutable char crep[36]{};

    //constructores
    Fecha(int d = 0, int m = 0, int a = 0);
    Fecha(char* f);

    //operadores aritmeticos
    Fecha& operator +=(int n);
    Fecha& operator -=(int n);
    Fecha operator +(int n);
    Fecha operator -(int n);
    Fecha& operator ++();
    Fecha operator ++(int);
    Fecha& operator --();
    Fecha operator --(int);

    //operadores logicos
    bool operator ==(const Fecha& otra) const;
    bool operator <(const Fecha& otra) const;
    bool operator !=(const Fecha& otra) const;
    bool operator >(const Fecha& otra) const;
    bool operator <=(const Fecha& otra) const;
    bool operator >=(const Fecha& otra) const;

    //metodos observadores
    int dia() const;
    int mes() const;
    int anno() const;

    //operadores de conversion
    operator const char*() const;


    class Invalida{
        public:
        
            Invalida(const char* razon) : razon_{razon} {}
            const char* por_que() const {return razon_;}
        private:

            const char* razon_;
    };
private:
    void verificarDia(int);
    void verificarMes(int);
    void verificarAnno(int);
    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
    const char* dias[7] {"domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"};
    const char* meses[12] {"enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"};
    mutable bool actual {false};
};

#endif //Fecha_H

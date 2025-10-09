#ifndef FECHA_H_
#define FECHA_H_

#include <iostream>
#include <stdexcept>
#include <ctime>

class Fecha
{
public:
    // constantes año max y año min
    static const int AnnoMinimo = 1902, AnnoMaximo = 2037;

    // Constructores
    explicit Fecha(int d = 0, int m = 0, int a = 0); // con tres parámetros
    Fecha(const char *f);                            // de una cadena de texto formato DD/MM/AAA

    // Metodos observadores
    int dia() const { return dia_; };
    int mes() const { return mes_; };
    int anno() const { return anno_; };

    // sobrecarga de operadores de comparación
    friend bool operator==(const Fecha &a, const Fecha &b);
    friend bool operator<(const Fecha &a, const Fecha &b);
    friend bool operator>(const Fecha &a, const Fecha &b);
    friend bool operator<=(const Fecha &a, const Fecha &b);
    friend bool operator>=(const Fecha &a, const Fecha &b);
    friend bool operator!=(const Fecha &a, const Fecha &b);

    // sobrecarga de operadores aritmeticos
    Fecha &operator+=(int n);
    Fecha &operator-=(int n);
    Fecha operator+(int n) const;
    Fecha operator-(int n) const;

    // sobrecraga operadores de incremento
    Fecha operator++(int); // sufijo
    Fecha &operator++();   // prefijo
    Fecha operator--(int); // sufijo
    Fecha &operator--();   // prefijo

    // conversión a const char*
    operator const char *() const;

    // sobrecraga de operador de extraccion
    friend std::ostream &operator>>(std::ostream &os, const Fecha &f);

    // clase Fecha::invalida
    class Invalida
    {
    public:
        Invalida(const char *error) : error_(error) {}
        const char *por_que() const { return error_; }

    private:
        const char *error_;
    };

private:
    int dia_, mes_, anno_;
    mutable char crep[40]{};
    bool valida() const;
    mutable bool actual = false;
};

#endif
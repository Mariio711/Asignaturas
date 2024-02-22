#ifndef FECHA_H
#define FECHA_H
#include <iostream>
#include <cstring>
#include <ctime>
#include <cassert>
class Fecha {
public:

    Fecha();
    Fecha(int d);
    Fecha(int d, int m);
    Fecha(int d, int m, int a);
    Fecha(const Fecha& f);
    Fecha(char* f);
private:
    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
};

//constructor por defecto
inline Fecha::Fecha() : dia_{tiempo_descompuesto->tm_mday}, mes_{tiempo_descompuesto->tm_mon+1}, anno_{tiempo_descompuesto->tm_year+1900} {}
//contructor con 1 solo parametro, el dia
inline Fecha::Fecha(int d) : dia_{d}, mes_{tiempo_descompuesto->tm_mon+1}, anno_{tiempo_descompuesto->tm_year+1900} {}
//constructor con dos pparametros el dia y el mes en se orden
inline Fecha::Fecha(int d, int m) : dia_{d}, mes_{m}, anno_{tiempo_descompuesto->tm_year+1900} {}
//contructor con tres parametros el dia el mes y el año en ese orden
inline Fecha::Fecha(int d, int m, int a) : dia_{d}, mes_{m}, anno_{a} {}
//constructor a partir de otra Fecha
inline Fecha::Fecha(const Fecha& f) : dia_{f.dia_}, mes_{f.mes_}, anno_{f.anno_} {}
//constructor a partir de una cadena de caracteres de bajo nivel del tipo "dd/mm/aaaa"
inline Fecha::Fecha(char* f)  : dia_{std::stoi(strtok(f, "/"))}, mes_{std::stoi(strtok(NULL, "/"))}, anno_{std::stoi(strtok(NULL, "/"))} {}





#endif //FECHA_H
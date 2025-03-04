#include <ctime>
#include "Fecha.hpp"

//Constructor 
Fecha::Fecha(int d, int m, int a): dia_{d}, mes_{m}, anno_{a} {
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
    int dia = tiempo_descompuesto->tm_mday;
    int mes = tiempo_descompuesto->tm_mon + 1; // tm_mon: 0 (ene)..11 (dic)
    int anno = tiempo_descompuesto->tm_year + 1900; // tm_year: a~nos desde 1900 
    
    if (d == 0){dia_ = dia;};
    if (m == 0){mes_ = mes;};
    if (a == 0){anno_ = anno;};
 
    //valida(); // funcion que comprueba que la fecha es correcta
}
#include "Fecha.hpp"
#include <ctime>
#include <cstring>
#include <stdexcept>
#include <string>
#include <sstream>

const int dias_mes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

void Fecha::obtener_fecha_actual(int &dia, int &mes, int &anno){
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
    dia = tiempo_descompuesto->tm_mday;
    mes = tiempo_descompuesto->tm_mon + 1; // tm_mon: 0 (ene)..11 (dic)
    anno = tiempo_descompuesto->tm_year + 1900; // tm_year: a~nos desde 1900 
}

//Funcion que valida si una fecha es valida
bool Fecha::valida() const{
    if(mes_ < 1 || mes_ > 12){return false;};
    int dias_en_mes = dias_mes[mes_-1];

    //comprobamos si es año bisiesto
    if (mes_ == 2 && ((anno_ % 4 == 0 && anno_ % 100 != 0) || (anno_ % 400 == 0))) {
        dias_en_mes = 29;
    }

    return dia_ >= 1 && dia_ <= dias_en_mes;
}

//Constructor por defecto
Fecha::Fecha(int d, int m, int a): dia_{d}, mes_{m}, anno_{a} {
    int dia, mes, anno;
    obtener_fecha_actual(dia, mes, anno);
    
    if (d == 0){dia_ = dia;};
    if (m == 0){mes_ = mes;};
    if (a == 0){anno_ = anno;};
 
    if (!valida()) {
        throw std::invalid_argument("Fecha inválida");
    }
}

// Constructor que toma un char*
Fecha::Fecha(const char* f) {
    int d, m, a;
    

    if (!valida()) {
        throw std::invalid_argument("Fecha inválida");
    }
}
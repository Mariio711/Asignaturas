#include "fecha.hpp"

//constructor por defecto
//contructor con tres parametros el dia el mes y el año en ese orden
Fecha::Fecha(int d, int m, int a){

    //excepcion si el dia, el mes o el año son invalidos
    try{
        verificacion(d, m, a);
    }
    catch(const Fecha::Invalida& e)
    {
        std::cerr << "Error: " << e.por_que() << std::endl;
    }

    //constuccion de la Fecha
    dia_ = (d == 0) ? tiempo_descompuesto->tm_mday : d;
    mes_ = (m == 0) ? tiempo_descompuesto->tm_mon+1 : m;
    anno_ = (a == 0) ? tiempo_descompuesto->tm_year+1900 : a;
}

//constructor con un parametro de tipo char*
Fecha::Fecha(char* f){
    int dia, mes, anno;

    if(sscanf(f, "%d/%d/%d", &dia, &mes, &anno) != 3){
        throw Invalida("Formato incorrecto");
    }
    //excepcion si el dia, el mes o el año son invalidos
    try{

        verificacion(dia, mes, anno);

    }catch(const Fecha::Invalida& e)
    {
        std::cerr << "Error: " << e.por_que() << std::endl;
    }
    //constuccion de la Fecha
    dia_ = dia;
    mes_ = mes;
    anno_ = anno;
}

//funcion que verifica si el dia, el mes o el año son invalidos
int Fecha::verificacion(int d, int m, int a){
    if(a < AnnoMinimo || a > AnnoMaximo){
        throw Invalida("Año invalido");
    }
    if(m < 1 || m > 12){
        throw Invalida("Mes invalido");
    }
    if(d < 1 || d > 31){
        throw Invalida("Dia invalido");
    }
    if(d > 30 && (m == 4 || m == 6 || m == 9 || m == 11)){
        throw Invalida("Dia invalido");
    }
    if(m == 2 && d > 29){
        throw Invalida("Dia invalido");
    }
    if(m == 2 && d == 29 && !(a%4 == 0 && (a%100 != 0 || a%400 == 0))){
        throw Invalida("Dia invalido");
    }
    return 0;
}
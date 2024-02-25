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
    Fecha();
    Fecha(int d);
    Fecha(int d, int m);
    Fecha(int d, int m, int a);
    Fecha(const Fecha& f);
    Fecha(char* f);
    class Invalida : public std::exception {
        public:
            Invalida(const char* razon) : razon_{razon} {}
            const char* por_que() const {return razon_;}
        private:
            const char* razon_;
            static void verificarDia(int d);
            static void verificarMes(int m);
            static void verificarAnno(int a);
    };
private:
    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
};

//verificaciones de la clase Fecha::Invalida para el dia, mes y año
//verificacion del dia
inline void Fecha::Invalida::verificarDia(int d) {
    if (d < 0 || d > 31) {
        throw Fecha::Invalida("Dia invalido");
    }
}
//verificacion del mes
inline void Fecha::Invalida::verificarMes(int m) {
    if (m < 0 || m > 12) {
        throw Fecha::Invalida("Mes invalido");
    }
}
//verificacion del año
inline void Fecha::Invalida::verificarAnno(int a) {
    if (a < Fecha::AnnoMinimo || a > Fecha::AnnoMaximo) {
        throw Fecha::Invalida("Anno invalido");
    }
}


//constructor por defecto
inline Fecha::Fecha() : dia_{tiempo_descompuesto->tm_mday}, mes_{tiempo_descompuesto->tm_mon+1}, anno_{tiempo_descompuesto->tm_year+1900} {}

//contructor con 1 solo parametro, el dia
inline Fecha::Fecha(int d){
    //excepcion si el dia es invalido
    try
    {
        Fecha::Invalida::verificarDia(d);
    }
    catch(const Fecha::Invalida& e)
    {
        std::cerr << "Error: " << e.por_que() << std::endl;
    }
    //constuccion de la Fecha
    dia_ = (d == 0) ? tiempo_descompuesto->tm_mday : d;
    mes_ = tiempo_descompuesto->tm_mon+1;
    anno_ = tiempo_descompuesto->tm_year+1900;
}

//constructor con dos parametros el dia y el mes en se orden
inline Fecha::Fecha(int d, int m){
    //excepcion si el dia o el mes son invalidos
    try{
        Fecha::Invalida::verificarDia(d);
        Fecha::Invalida::verificarMes(m);
    }
    catch(const Fecha::Invalida& e)
    {
        std::cerr << "Error: " << e.por_que() << std::endl;
    }
    //constuccion de la Fecha
    dia_ = (d == 0) ? tiempo_descompuesto->tm_mday : d;
    mes_ = (m == 0) ? tiempo_descompuesto->tm_mon+1 : m;
    anno_ = tiempo_descompuesto->tm_year+1900;
}

//contructor con tres parametros el dia el mes y el año en ese orden
inline Fecha::Fecha(int d, int m, int a){

    //excepcion si el dia, el mes o el año son invalidos
    try{
        Fecha::Invalida::verificarDia(d);
        Fecha::Invalida::verificarMes(m);
        Fecha::Invalida::verificarAnno(a);
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

//constructor a partir de otra Fecha
inline Fecha::Fecha(const Fecha& f){
    //excepcion si el dia, el mes o el año son invalidos
    try{
        Fecha::Invalida::verificarDia(f.dia_);
        Fecha::Invalida::verificarMes(f.mes_);
        Fecha::Invalida::verificarAnno(f.anno_);
    }
    catch(const Fecha::Invalida& e)
    {
        std::cerr << "Error: " << e.por_que() << std::endl;
    }
    //constuccion de la Fecha
    dia_ = (f.dia_ == 0) ? tiempo_descompuesto->tm_mday : f.dia_;
    mes_ = (f.mes_ == 0) ? tiempo_descompuesto->tm_mon+1 : f.mes_;
    anno_ = (f.anno_ == 0) ? tiempo_descompuesto->tm_year+1900 : f.anno_;
}

//constructor a partir de una cadena de caracteres de bajo nivel del tipo "dd/mm/aaaa",
//ceros a la izquierda se aceptan y se descartan, si hay mas caracteres no numericos despues de la Fecha se ignoran
inline Fecha::Fecha(char* f) {
    char* token = std::strtok(f, "/"), tokenaux = token;
    int dia, mes, anno;
    //excepcion si el dia, el mes o el año son invalidos con token auxiliar para saber cual es el valor invalido
    try{
        dia = std::stoi(token);
        token = std::strtok(nullptr, "/");
        mes = std::stoi(token);
        token = std::strtok(nullptr, "/");
        anno = std::stoi(token);
    }
    catch(const std::invalid_argument& e)
    {
        throw Fecha::Invalida("Argumento inválido en la fecha");
    }
    catch(const std::out_of_range& e)
    {
        throw Fecha::Invalida("Valor fuera de rango en la fecha");
    }

    Fecha::Invalida::verificarDia(dia);
    Fecha::Invalida::verificarMes(mes);
    Fecha::Invalida::verificarAnno(anno);

    //constuccion de la Fecha
    dia_ = (dia == 0) ? tiempo_descompuesto->tm_mday : dia;
    mes_ = (mes == 0) ? tiempo_descompuesto->tm_mon+1 : mes;
    anno_ = (anno == 0) ? tiempo_descompuesto->tm_year+1900 : anno;
}





#endif //Fecha_H
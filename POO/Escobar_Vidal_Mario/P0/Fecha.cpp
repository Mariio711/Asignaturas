#include "fecha.hpp"



const int dias_mes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

//función para obtener fecha actual.
void obtener_fecha_actual(int &dia, int &mes, int &anno){
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
    dia = tiempo_descompuesto->tm_mday;
    mes = tiempo_descompuesto->tm_mon + 1; // tm_mon: 0 (ene)..11 (dic)
    anno = tiempo_descompuesto->tm_year + 1900; // tm_year: a~nos desde 1900 
}

//función para determinar dia, mes o año actual si alguno fuese 0.
void f_actual(int &d, int &m, int &a){
    int dia, mes, anno;
    obtener_fecha_actual(dia, mes, anno);

    if (d == 0) d = dia;
    if (m == 0) m = mes;
    if (a == 0) a = anno;
}

//Funcion que valida si una fecha es válida
bool Fecha::valida() const{
    if(mes_ < 1 || mes_ > 12){return false; };
    int dias_en_mes = dias_mes[mes_-1];

    //comprobamos si es año bisiesto
    if (mes_ == 2 && ((anno_ % 4 == 0 && anno_ % 100 != 0) || (anno_ % 400 == 0))) {
        dias_en_mes = 29;
    }

    //comprobamos si el año esta comprendido entre AnnoMinimo y AnnoMaximo
    if (anno_ > Fecha::AnnoMaximo || anno_ < Fecha::AnnoMininmo){return false; };

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

// Constructor que toma un char* (conversión)
Fecha::Fecha(const char* f) {
    int d, m, a;
    if (sscanf(f, "%d/%d/%d", &d, &m, &a) != 3) {
        throw std::invalid_argument("Formato de fecha inválido");
    }

    f_actual(d, m ,a);
    dia_ = d;
    mes_ = m;
    anno_ = a;

    if (!valida()) {
        throw std::invalid_argument("Fecha inválida");
    }
}

//operadores de comparación
bool operator==(const Fecha& a, const Fecha& b){
    return b.dia_ == a.dia_ && b.mes_ == a.mes_ && b.anno_ == a.anno_ ;
}

bool operator<(const Fecha& a, const Fecha& b){
    return (a.anno_ < b.anno_) || (a.anno_ == b.anno_ && a.mes_ < b.mes_) || (a.anno_ == b.anno_ && a.mes_ == b.mes_ && a.dia_ < b.dia_);
}

bool operator>(const Fecha& a, const Fecha& b){
    return b < a;
}

bool operator<=(const Fecha& a, const Fecha& b){
    return !(b < a);
}

bool operator>=(const Fecha& a, const Fecha& b){
    return !(a < b);
}

bool operator!=(const Fecha& a, const Fecha& b){
    return !(b == a);
}


//sobrecarga de operadores aritméticos
Fecha& Fecha::operator+=(int n){

    std::tm* tiempo_descompuesto = std::localtime(nullptr);
    tiempo_descompuesto->tm_mday = dia_;
    tiempo_descompuesto->tm_mon = mes_ - 1;
    tiempo_descompuesto->tm_year = anno_ - 1990;
    tiempo_descompuesto->tm_mday += n;
    std::mktime(tiempo_descompuesto);

    dia_ = tiempo_descompuesto->tm_mday;
    mes_ = tiempo_descompuesto->tm_mon + 1;
    anno_ = tiempo_descompuesto->tm_year + 1990;
    if (!valida()){
        throw std::overflow_error("Desbordamiento sobre AnnoMaximo o AnnoMinimo");
    }
    actual = true;
    return *this;
}

Fecha& Fecha::operator-=(int n){
    return *this += -n;
}

Fecha Fecha::operator+(int n){
    Fecha t(*this);
    t += n;
    return t;
}

Fecha Fecha::operator-(int n){
    Fecha t(*this);
    t += -n;
    return t;
}

//operadores de incremento
Fecha Fecha::operator++(int){     //sufijo f++
    Fecha t(*this);
    *this += 1;
    return t;
}

Fecha& Fecha::operator++(){         //prefijo ++f
    *this += 1;
    return *this;
}

Fecha Fecha::operator--(int){     //sufijo f--
    Fecha t(*this);
    *this += -1;
    return t;
}

Fecha& Fecha::operator--(){         //prefijo --f
    *this += -1;
    return *this;
}

//operadorde conversion a const char*
Fecha::operator const char*() const{

    if (actual){
        return crep;
    } else {
        struct tm fecha_tm = {};
        fecha_tm.tm_mday = dia_;
        fecha_tm.tm_mon = mes_ - 1; // tm_mon es 0-11
        fecha_tm.tm_year = anno_ - 1900; // tm_year es años desde 1900

        // Normaliza la fecha
        mktime(&fecha_tm);
    
        static const char* dias_semana[] = {"domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"};
        static const char* meses[] = {"enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"};

        snprintf(crep, sizeof(crep), "%s %02d de %s de %04d", dias_semana[fecha_tm.tm_wday], fecha_tm.tm_mday, meses[fecha_tm.tm_mon], fecha_tm.tm_year + 1900);
        return crep;
    }
    
}
#include "fecha.hpp"

using namespace std;

//funcion que verifica si el dia es invalido
void Fecha::verificarDia(int dia){
    if(dia < 1 || dia > 31){
        throw Invalida("Dia invalido");
    }
    if(dia > 30 && (mes_ == 4 || mes_ == 6 || mes_ == 9 || mes_ == 11)){
        throw Invalida("Dia invalido");
    }
    if(mes_ == 2 && dia > 29){
        throw Invalida("Dia invalido");
    }
    if(mes_ == 2 && dia == 29 && !(anno_%4 == 0 && (anno_%100 != 0 || anno_%400 == 0))){
        throw Invalida("Dia invalido");
    }
}

//funcion que verifica si el mes es invalido
void Fecha::verificarMes(int mes){
    if(mes < 1 || mes > 12){
        throw Invalida("Mes invalido");
    }
}

//funcion que verifica si el anno es invalido
void Fecha::verificarAnno(int anno){
    if(anno < AnnoMinimo || anno > AnnoMaximo){
        throw Invalida("Año invalido");
    }
}

//constructor por defecto
//contructor con tres parametros el dia el mes y el año en ese orden
Fecha::Fecha(int d, int m, int a){

    //constuccion de la Fecha
    dia_ = (d == 0) ? tiempo_descompuesto->tm_mday : d;
    mes_ = (m == 0) ? tiempo_descompuesto->tm_mon+1 : m;
    anno_ = (a == 0) ? tiempo_descompuesto->tm_year+1900 : a;

    //excepcion si el dia, el mes o el año son invalidos
    verificarDia(d);
    verificarMes(m);
    verificarAnno(a);
}

//constructor con un parametro de tipo char*
Fecha::Fecha(const char* f){
    int dia, mes, anno;

    if(sscanf(f, "%d/%d/%d", &dia, &mes, &anno) != 3){
        throw Invalida("Formato incorrecto");
    }

    //excepcion si el dia, el mes o el año son invalidos
    verificarDia(dia);
    verificarMes(mes);
    verificarAnno(anno);

    //constuccion de la Fecha
    dia_ = dia;
    mes_ = mes;
    anno_ = anno;
    
}


/*----------------------------operadores aritmeticos----------------------------------*/


//operador de suma con asignacion += f=f+n
Fecha& Fecha::operator+=(int n){
    //convertimos la fecha a un struct tm para usar mktime
    struct tm fecha_tm; //inicializamos a cero
    fecha_tm.tm_mday = dia_;
    fecha_tm.tm_mon = mes_ - 1;
    fecha_tm.tm_year = anno_ - 1900 ;

    //le sumamos los dias
    fecha_tm.tm_mday += n;

    //usamos mktime para convertir a fecha y controlamos las excepciones de mktime
    time_t tiempo = mktime(&fecha_tm);
    if (tiempo == -1) {
        throw std::runtime_error("mktime falló");
    }

    //convertimos el valor time a fecha de nuevo con localtime
    struct tm* fecha_tm_ptr = localtime(&tiempo);
    if (fecha_tm_ptr == nullptr) {
        throw std::runtime_error("localtime falló");
    }

    //verificaciones
    verificarDia(fecha_tm_ptr->tm_mday);
    verificarMes(fecha_tm_ptr->tm_mon + 1);
    verificarAnno(fecha_tm_ptr->tm_year + 1900);

    //re asignamos los valores de la fecha_tm_ptr (ya actualizada) a la fecha (this)
    dia_ = fecha_tm_ptr->tm_mday;
    mes_ = fecha_tm_ptr->tm_mon + 1 ;
    anno_ = fecha_tm_ptr->tm_year + 1900;

    actual = false; //la fecha se ha actualizado por lo que ponemos actual a falso
    return *this;
}

//operador de resta con asignacion -= f=f-n
Fecha& Fecha::operator-=(int n){
    return (*this) += -n;
}

//operador +
Fecha Fecha::operator +(int n) const{
    Fecha copia(*this); //creamos copia de la fecha
    copia += n; //usamos el operador += 
    return copia;
}

//operador -
Fecha Fecha::operator -(int n) const{
    Fecha copia(*this); //creamos copia de la fecha
    copia += -n; //usamos el operador += 
    return copia;
}

//operador ++
Fecha& Fecha::operator++(){
    return (*this) += 1;
}

//operador ++ a la derecha (incremento postfijo)
Fecha Fecha::operator++(int){
    Fecha copia(*this); //creamos copia de la fecha
    *this  += 1;
    return copia;
}

//operador --
Fecha& Fecha::operator--(){
    return (*this) += -1;
}

//operador -- a la derecha (incremento postfijo)
Fecha Fecha::operator--(int){
    Fecha copia(*this); //creamos copia de la fecha
    *this  += -1;
    return copia;
}

/*----------------------------operadores logicos----------------------------------*/

//operador de igualdad ==
bool Fecha::operator==(const Fecha& otra) const {
    return dia_ == otra.dia_ && mes_ == otra.mes_ && anno_ == otra.anno_;
}

//operador menor-que <
bool Fecha::operator<(const Fecha& otra) const {
    if (anno_ > otra.anno_)
        return false;
    else
        if(anno_ == otra.anno_ && mes_ > otra.mes_)
            return false;
        else
            if(anno_ == otra.anno_ && mes_ == otra.mes_ && dia_ >= otra.dia_)
                return false;
            else
                return true;
}

//operador !=
bool Fecha::operator!=(const Fecha& otra) const{
    return !(*this == otra);
} 


//operador >
bool Fecha::operator>(const Fecha& otra) const{
    return otra < *this;
} 


//operador <=
bool Fecha::operator<=(const Fecha& otra) const{
    return !(otra < *this);
} 


//operador >=
bool Fecha::operator>=(const Fecha& otra) const{
    return !(*this < otra);
} 

/*----------------------------metodos observadores----------------------------------*/

//muestra el dia de la fecha
int Fecha::dia() const{
    return this->dia_;
}

//muestra el mes de la fecha
int Fecha::mes() const{
    return this->mes_;
}

//muestra el año de la fecha
int Fecha::anno() const{
    return this->anno_;
}

/*sobrecarga del operador de conversion a const char*. */

Fecha::operator const char*() const {
    if(actual == true){
        return this->crep;
    }else{
        //convertimos la fecha a un struct tm para usar mktime
        struct tm fecha_tm; //inicializamos a cero
        fecha_tm.tm_mday = dia_;
        fecha_tm.tm_mon = mes_ - 1;
        fecha_tm.tm_year = anno_ - 1900 ;
    
        // Usamos mktime para obtener el tiempo en segundos desde la época Unix (1 de enero de 1970)
        // y luego lo convertimos a un struct tm local con localtime
        time_t tiempo = mktime(&fecha_tm);
        struct tm* tiempo_local = localtime(&tiempo);
        
        //convertimos el tiempo local a cadena de texto formateada con strftime (tiene muchas opciones mirar documentación)
        char fecha_str[36];
        strftime(fecha_str, 36, "%w %d %m %Y", tiempo_local);
    
        //ahora leemos la fecha_str formateada y almacenamos sus campos en variables temporales segun lo hayamos formateado
        //en este caso el formato es "%w %d %m %Y" que significa "dia_semana dia_mes mes año
        int dia_semana, dia, mes, anno;
        sscanf(fecha_str, "%d %d %d %d", &dia_semana, &dia, &mes, &anno);
    
        //luego formateamos la cadena de salida con el formato deseado, la almacenamos en el crep y la devolvemos 
        char mes_str[10];
        char dia_str[10];
        strcpy(dia_str, Fecha::dias[dia_semana]);
        strcpy(mes_str, Fecha::meses[mes - 1]);
        sprintf(crep, "%s %d de %s de %d", dia_str, dia, mes_str, anno);
    
        //actualizamos el valor del booleano de actualizacion a true
        actual = true;
        return crep;
    }



    
}
#include "fecha.hpp"


//funcion que verifica si el dia, el mes o el año son invalidos
void Fecha::verificacion(int d, int m, int a){
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
}

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

//sobrecarga del operador ++
Fecha Fecha::operator ++(){
    if(dia_ == 31 && mes_ == 12){
        dia_ = 1;
        mes_ = 1;
        anno_++;
    }else 
        if(dia_ == 31 && (mes_ == 1 || mes_ == 3 || mes_ == 5 || mes_ == 7 || mes_ == 8 || mes_ == 10)){
            dia_ = 1;
            mes_++;
        }else 
            if(dia_ == 30 && (mes_ == 4 || mes_ == 6 || mes_ == 9 || mes_ == 11)){
                dia_ = 1;
                mes_++;
            }else 
                if(mes_ == 2 && dia_ == 28 && !((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                    dia_ = 1;
                    mes_++;
                }else 
                    if(mes_ == 2 && dia_ == 29 && ((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                        dia_ = 1;
                        mes_++;
                    }else
                        dia_++;
                    
    return *this;
}

//sobrecarga del operador --
Fecha Fecha::operator --(){
    if(dia_ == 1 && mes_ == 1){
        dia_ = 31;
        mes_ = 12;
        anno_--;
    }else
        if(dia_ == 1 && (mes_ == 4 || mes_ == 6 || mes_ == 9 || mes_ == 11)){
            dia_ = 31;
            mes_--;
        }else
            if(dia_ == 1 && (mes_ == 1 || mes_ == 5 || mes_ == 7 || mes_ == 8 || mes_ == 10)){
                dia_ = 31;
                mes_--;
            }else
                if(dia_ == 1 && mes_ == 3 && !((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                    dia_ = 28;
                    mes_--;
                }else
                    if(dia_ == 1 && mes_ == 3 && ((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                        dia_ = 29;
                        mes_--;
                    }else
                        dia_--;
     return *this;               
}

//sobrecarga del operador -
Fecha Fecha::operator -(int a){
    for( a; a=0; a--){
        if(dia_ == 1 && mes_ == 1){
            dia_ = 31;
            mes_ = 12;
            anno_--;
        }else
            if(dia_ == 1 && (mes_ == 4 || mes_ == 6 || mes_ == 9 || mes_ == 11)){
                dia_ = 31;
                mes_--;
            }else
                if(dia_ == 1 && (mes_ == 1 || mes_ == 5 || mes_ == 7 || mes_ == 8 || mes_ == 10)){
                    dia_ = 31;
                    mes_--;
                }else
                    if(dia_ == 1 && mes_ == 3 && !((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                        dia_ = 28;
                        mes_--;
                    }else
                        if(dia_ == 1 && mes_ == 3 && ((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                            dia_ = 29;
                            mes_--;
                        }else
                            dia_--;
    }
}
//sobrecarga del operador +
Fecha Fecha::operator +(int a){
    int auxmes=0;
    for( auxmes; auxmes==a ; auxmes++){
        if(dia_ == 31 && mes_ == 12){
            dia_ = 1;
            mes_ = 1;
            anno_++;
        }else 
            if(dia_ == 31 && (mes_ == 1 || mes_ == 3 || mes_ == 5 || mes_ == 7 || mes_ == 8 || mes_ == 10)){
                dia_ = 1;
                mes_++;
            }else 
                if(dia_ == 30 && (mes_ == 4 || mes_ == 6 || mes_ == 9 || mes_ == 11)){
                    dia_ = 1;
                    mes_++;
                }else 
                    if(mes_ == 2 && dia_ == 28 && !((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                        dia_ = 1;
                        mes_++;
                    }else 
                        if(mes_ == 2 && dia_ == 29 && ((anno_%4 == 0 && anno_%100 != 0) || anno_%400 == 0)){
                            dia_ = 1;
                            mes_++;
                        }else
                            dia_++;
    }       
}
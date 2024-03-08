#include "cadena.hpp"
#include <string.h>
#include <new>

using namespace std;

char Cadena::vacio[1] = {'\0'}; // Inicialización del caracter terminador de la cadena

//constructor con dos parametros
Cadena::Cadena(int tam, char s){
    if(tam == 0){
        s_ = vacio;//cadena vacia si la longitud deseada es 0 (por defecto)
    }else{
        //asignamos memoria dinamica 
        s_ = new char[tam];

        //rellenamos la cadena con el carcacter de relleno
        for (int i = 0; i < tam; i++){
            s_[i] = s;
        }
        s_[tam] = *vacio; //nos aseguramos de que la cadena termine en caracter nulo
    }
}

//constructor a partir de una cadena de bajo nivel
Cadena::Cadena(const char* s){
    s_ = new char[strlen(s)+1]; //asignamos memoria dinamica del tamaño de la cadena dada mas un espacio para el caracter termiandor
    strcpy(s_, s); //copiamos la cadena de s en s_ 
    tam_ = strlen(s_); //asignamos el tamaño a la instancia de la cadena
}

//constructor de copia
Cadena::Cadena(const Cadena& otra){
    tam_ = otra.tam_;
    s_ = new char(tam_ + 1);
    strcpy(s_, otra.s_);
}

//sobrecarga de operador de asignacion (=) para una cadena
Cadena& Cadena::operator=(const Cadena& otra){
    if (this != &otra){ //evitar la auto asignaicon
        char* nueva_s = nullptr;

        //si no hay suficiente memoria no se realiza la asignacion
        try{
            nueva_s = new char[otra.tam_ + 1]; // asignamos memoria
        }catch(const std::bad_alloc&){
            return *this;
        }

        //si la asignacion de memoria fue exitosa
        strcpy(nueva_s, otra.s_);
        nueva_s[otra.tam_] = '\0';

        //liberamos la memoria antigua y actualizamos los miembros
        delete[] s_;
        s_ = nueva_s;
        tam_ = otra.tam_;
    }  
    return *this;
}


//sobrecarga de operador de asignacion (=) para una cadena de bajo nivel
Cadena& Cadena::operator=(const char* s){
    char* nueva_s = nullptr;

    //si no hay suficiente memoria no se realiza la asignacion
    try{
        nueva_s = new char[strlen(s) + 1]; // asignamos memoria
    }catch(const std::bad_alloc&){
        return *this;
    }

    //si la asignacion de memoria fue exitosa
    strcpy(nueva_s, s);
    nueva_s[strlen(s) + 1] = '\0';

    //liberamos la memoria antigua y actualizamos los miembros
    delete[] s_;
    s_ = nueva_s;
    tam_ = strlen(s) + 1;
    return *this;
}  

Cadena::operator const char *() const{
    return (tam_ > 0) ? s_ : vacio;
}



int Cadena::length()const{
    return tam_;
}

//sobrecarga del operador de suma con asignacion
Cadena& Cadena::operator+=(const Cadena& otra){  
    int nueva_longitud = tam_ + otra.tam_ + 1;
    char* nueva_s = nullptr;

    //si no hay suficiente memoria no se realiza la asignacion
    try{
        nueva_s = new char[nueva_longitud]; // asignamos memoria
    }catch(const std::bad_alloc&){
        return *this;
    }

    //si la asignacion de memoria fue exitosa
    strcpy(nueva_s, s_);
    strcat(nueva_s, otra.s_);

    //liberamos la memoria antigua y actualizamos los miembros
    delete[] s_;
    s_ = nueva_s;
    tam_ = strlen(strcat(s_, otra.s_)) + 1;
    return *this;
}

//sobrecarga del operador de suma
Cadena Cadena::operator+(const Cadena& otra){
    int nueva_longitud = tam_ + otra.tam_ + 1;
    char* nueva_s = nullptr;

    //si no hay suficiente memoria no se realiza la asignacion
    try{
        nueva_s = new char[nueva_longitud]; // asignamos memoria
    }catch(const std::bad_alloc&){
        throw; // Lanzamos la excepción hacia arriba
    }

    //si la asignacion de memoria fue exitosa
    strcpy(nueva_s, s_);
    strcat(nueva_s, otra.s_);

    // Creamos una nueva Cadena con la cadena concatenada
    Cadena nueva_cadena(nueva_longitud - 1);
    strcpy(nueva_cadena.s_, nueva_s);

    // Liberamos la memoria temporal
    delete[] nueva_s;

    return nueva_cadena;
}

//sobrecarga del operador de igualdad
bool Cadena::operator ==(const Cadena& otra) const{
    return strcmp(s_, otra.s_) == 0;
}

//sobrecarga del operador de igualdad (cadena primero)
bool operator ==(const char* str, const Cadena& cadena){
    return cadena == str;
}

//sobrecarga del operador distinto
bool Cadena::operator !=(const Cadena& otra) const{
    return strcmp(s_, otra.s_) != 0;
}

//sobrecarga del operador menor que
bool Cadena::operator <(const Cadena& otra) const{
    return strcmp(s_, otra.s_) < 0;
}

//sobrecarga del operador mayor que
bool Cadena::operator >(const Cadena& otra) const{
    return strcmp(s_, otra.s_) > 0;
}

//sobrecarga del operador menor igual
bool Cadena::operator <=(const Cadena& otra) const{
    return strcmp(s_, otra.s_) <= 0;
}

//sobrecarga del operador mayor igual
bool Cadena::operator >=(const Cadena& otra) const{
    return strcmp(s_, otra.s_) >= 0;
}

//sobrecarga del operador de indice
#include <stdexcept> // para std::out_of_range

char& Cadena::operator[](int unsigned indice) {
    if (indice >= tam_) {
        throw std::out_of_range("Índice fuera de rango");
    }
    return s_[indice];
}

const char& Cadena::operator[](int unsigned indice) const {
    if (indice >= tam_) {
        throw std::out_of_range("Índice fuera de rango");
    }
    return s_[indice];
}

// devuelve el caracter al que apunta la posicion del indice
char& Cadena::at(int unsigned indice){
    if (indice >= tam_) {
        throw std::out_of_range("Índice fuera de rango");
    }
    return s_[indice];
}

Cadena Cadena::substr(unsigned int indice, unsigned int tam){
    if (indice >= tam_ || tam > tam_ - indice) {
        throw std::out_of_range("Índice fuera de rango");
    }
    
    char* subcadena = new char[tam + 1];
    strncpy(subcadena, s_ + indice, tam);
    subcadena[tam] = '\0'; // Asegúrate de que la subcadena esté terminada en null

    Cadena resultado(subcadena);
    delete[] subcadena; // No olvides liberar la memoria que has asignado con new

    return resultado;
}

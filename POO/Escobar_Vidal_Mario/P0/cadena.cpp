#include "cadena.hpp"
#include <string.h>
#include <new>

using namespace std;

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

explicit Cadena::operator const char *() const{
    return (tam_ > 0) ? s_ : vacio;
}

int Cadena::length(){
    return tam_;
}

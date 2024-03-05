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
Cadena::Cadena(char* s){
    s_ = new char[strlen(s)+1]; //asignamos memoria dinamica del tamaño de la cadena dada mas un espacio para el caracter termiandor
    strcpy(s, s_); //copiamos la cadena de s en s_ 
    tam_ = strlen(s_); //asignamos el tamaño a la instancia de la cadena
}

//sobrecarga de operador de asignacion (=) para una cadena
Cadena& Cadena::operator=(const Cadena& otra){
    if (this != &otra){ //evitar la auto asignaicon
        char* nueva_s = nullptr;

        //si no hay suficiente memoria nos e realiza la asignacion
        try{
            nueva_s = new char[otra.tam_ + 1]; // asignamos memoria
        }catch(const std::bad_alloc&){
            return *this;
        }

        //si la asignacion de memoria fue exitosa
        delete[] s_;
        s_ = nueva_s;
        

    } 
        
}
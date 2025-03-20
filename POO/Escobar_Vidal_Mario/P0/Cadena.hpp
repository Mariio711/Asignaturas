#ifndef CADENA_H_
#define CADENA_H_

#include <cstring>

class Cadena{
    public:
        //constructores
        explicit Cadena(int n = 0, char a = '\0');  //predeterminado
        explicit Cadena(const char* cadena);        //de conversion
        Cadena(const Cadena& otra);                 //de copia

        //operador de aignación
        Cadena& operator=(const Cadena& otra);

        //destructor
        ~Cadena();

        //metodos observadores
        size_t length() const {return std::strlen(s_);}; //devuelve la longitud de la cadena c

        //operadores de comparación
        friend bool operator== (const Cadena& a, const Cadena& b);
        friend bool operator< (const Cadena& a, const Cadena& b);
        friend bool operator> (const Cadena& a, const Cadena& b);
        friend bool operator<= (const Cadena& a, const Cadena& b);
        friend bool operator>= (const Cadena& a, const Cadena& b);
        friend bool operator!= (const Cadena& a, const Cadena& b);

        //operador de indice
        char& operator[] (size_t i);
        const char& operator[] (size_t i) const;

        //metodos
        char& at(size_t i);
        const char& at(size_t i) const;
        Cadena substr(unsigned int i, unsigned int tam) const;
    private:
        char vacia[1]{'\0'};
        size_t tam_;
        char* s_;

};

#endif 
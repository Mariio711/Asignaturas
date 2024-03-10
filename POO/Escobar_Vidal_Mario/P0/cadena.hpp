#ifndef CADENA
#define CADENA
#include <cstddef>

class Cadena{
    public:

        //constructores
        Cadena(int tam = 0, char s = ' '); //con dos parametros, los demas se consctruiran a partir de este
        Cadena(const char* s); //a partir de una cadena de bajo nivel
        Cadena(const Cadena& otra); //constructor de copia

        //sobrecarga de operadores
        Cadena& operator=(const Cadena& otra); //sobrecarga del operador de asignacion para otra clase cadena
        Cadena& operator=(const char* s); //sobrecarga del operador de asignacion para cadena de bajo nivel
        Cadena& operator+=(const Cadena& otra);//sobrecarga del operador de suma con asignacion
        friend Cadena operator+(const Cadena& c1, const Cadena& c2);//sobrecarga del operador de suma

        //sobrecarga de operadores de conversion
        explicit operator const char*() const;

        //sobrecarga de operadores logicos
        friend bool operator==(const Cadena& c1, const Cadena& c2);
        friend bool operator==(const char* str, const Cadena& c);
        friend bool operator!=(const Cadena& c1, const Cadena& c2);
        friend bool operator<(const Cadena& c1, const Cadena& c2);
        friend bool operator>(const Cadena& c1, const Cadena& c2);
        friend bool operator<=(const Cadena& c1, const Cadena& c2);
        friend bool operator>=(const Cadena& c1, const Cadena& c2);

        //sobrecarga de operador de indice
        char& operator[](int unsigned indice); // devuelve el caracter al que apunta la posicion del indice
        const char& operator[](int unsigned indice) const; // devuelve el caracter al que apunta la posicion del indice
        char& at(int unsigned indice) const; // devuelve el caracter al que apunta la posicion del indice
        
        //metodos observadores
        size_t length() const; //devuelve el tamaño de la cadena

        const Cadena substr(int unsigned indice, int unsigned tam) const; //devuelve un substring de la cadena conla que se llama a partir del indice y el tamaño
        
    private:
        
        //atributos
        static char vacio[1]; //puntero al caracter terminador comunes a todos los objetos de la clase
        unsigned int tam_; // tamaño de la cadena
        char* s_; // puntero a una cadena de caracteres

};

bool operator ==(const char* str, const Cadena& cadena);
#endif 
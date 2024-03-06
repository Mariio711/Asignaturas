#ifndef CADENA
#define CADENA
class Cadena{
    public:

        //constructores
        Cadena(int tam = 0, char s = ' '); //con dos parametros, los demas se consctruiran a partir de este
        Cadena(const char* s); //a partir de una cadena de bajo nivel

        //sobrecarga de operadores
        Cadena& operator=(const Cadena& otra); //sobrecarga del operador de asignacion para otra clase cadena
        Cadena& operator=(const char* s); //sobrecarga del operador de asignacion para otra clase cadena
        
        //sobrecarga de operadores de conversion
        explicit operator const char*() const;

        //metodos observadores
        int length();
    private:
        
        //atributos
        static char vacio[1]; //puntero al caracter terminador comunes a todos los objetos de la clase
        size_t tam_; // tamaño de la cadena
        char* s_; // puntero a una cadena de caracteres

};

char Cadena::vacio[1] = {'\0'}; // Inicialización del caracter terminador de la cadena
#endif 
#ifndef FECHA_H_
#define FECHA_H_

class Fecha{
    public:
        //Metodos observadores
        int dia()const {return dia_;};
        int mes()const {return mes_;};
        int anno()const {return anno_;};

        //Constructores
        Fecha(int d = 0, int m = 0, int a = 0); //con tres parámetros


    private:
        int dia_;
        int mes_;
        int anno_;

};
 
#endif
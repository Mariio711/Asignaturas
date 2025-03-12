#ifndef FECHA_H_
#define FECHA_H_

class Fecha{
    public:
        //constantes año max y año min
        const int AnnoMininmo = 1902, AnnoMaximo = 2037;

        //Metodos observadores
        int dia()const {return dia_;};
        int mes()const {return mes_;};
        int anno()const {return anno_;};

        //Constructores
        Fecha(int d = 0, int m = 0, int a = 0); //con tres parámetros
        Fecha(const Fecha& f): dia_{f.dia_}, mes_{f.mes_}, anno_{f.anno_}{} // de copia
        Fecha(const char * f);


    private:
        int dia_, mes_, anno_;
        bool valida() const;
        void obtener_fecha_actual(int &dia, int &mes, int &anno);

};
 
#endif
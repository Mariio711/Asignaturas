#ifndef FECHA_H
#define FECHA_H
#include <ctime>
#include <cassert>
class Fecha {
    int dia_, mes_, anno_;
    std::time_t tiempo_calendario = std::time(nullptr);
    std::tm* tiempo_descompuesto = std::localtime(&tiempo_calendario);
public:

    Fecha() : dia_{tiempo_descompuesto->tm_mday}, mes_{tiempo_descompuesto->tm_mon+1}, anno_{tiempo_descompuesto->tm_year+1900};

    Fecha(int d, int m, int a) :
        dia_{d}, mes_{m}, anno_{a};
    
};



#endif //FECHA_H
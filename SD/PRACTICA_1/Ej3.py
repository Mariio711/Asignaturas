"""Haga un script en Python que cree una copia de un fichero cualquiera.
Puede implementar una función propia o utilizar una existente. A continuación,
utilice la librería/módulo necesario para comprobar que los ficheros anteriores son iguales."""

import shutil
import filecmp

shutil.copy('SD/PRACTICA_1/archivo_origen','SD/PRACTICA_1/archivo_destino')

print(filecmp.cmp('SD/PRACTICA_1/archivo_origen','SD/PRACTICA_1/archivo_destino')) 



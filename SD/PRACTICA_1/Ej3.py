"""3. Haga un script en Python que cree una copia de un fichero cualquiera.
Puede implementar una función propia o utilizar una existente. A
continuación, utilice la librería/módulo necesario para comprobar que los
ficheros anteriores son iguales.
"""

import shutil, filecmp

shutil.copy("archivo_destino", "archivo_origen")

a = filecmp.cmp("archivo_destino", "archivo_origen", shallow=False)

print(a)
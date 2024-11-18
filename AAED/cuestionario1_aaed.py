import random
import os


enunciado = {
    "1": "¿Cuál es la definición de la notación asintótica O?",
    "3": "¿Cuál es la jerarquía correcta de los órdenes asintóticos?",
    "5": "¿Qué implica la relación O(f) = O(g) ↔ Ω(f) = Ω(g)?",
    "7": "Si se elige una operación crítica, ¿cuál de las siguientes NO es una de sus características?",
    "9": "¿Por qué no existen algoritmos de búsqueda con coste O(log(n)) en cualquier vector?",
    "11": "¿Qué es la dualidad en el contexto de análisis de algoritmos?",
    "13": "¿Cuál es la característica principal de un algoritmo recursivo en comparación con su equivalente iterativo?",
    "15": "¿Cuál es el orden de complejidad correcto en la siguiente jerarquía: O(n^2), O(n), O(nlog(n)), O(log(n)), O(1)?",
    "17": "Según The Standish Group, ¿cuál de las siguientes es una causa endógena del fracaso del software?",
    "19": "¿Qué es una operación crítica dentro de un algoritmo?",
    "21": "Si un algoritmo pertenece al orden O(log(n)), ¿qué significa?",
    "23": "¿Qué implica el principio de invarianza en el análisis de algoritmos?",
    "25": "Según la notación O, ¿cuál de las siguientes expresiones es correcta para O(c * f(n)) donde c es una constante positiva?",
    "27": "¿Cuál de las siguientes NO es una característica de un análisis de eficiencia de algoritmos en unidades de tiempo?",
    "29": "¿Qué implica que una función pertenezca al orden Θ(f)?",
    "31": "¿Cuál de las siguientes afirmaciones sobre operaciones críticas es verdadera?",
    "33": "¿Qué tipo de orden asintótico induce el preorden?",
    "35": "¿Cuál de las siguientes afirmaciones sobre la jerarquía de complejidad es correcta?",
    "37": "¿Qué es una operación elemental en un algoritmo?",
    "39": "¿Cuál es el objetivo principal al identificar una operación crítica en un algoritmo?",
    "41": "¿Cuál de las siguientes complejidades indica la mejor eficiencia en un algoritmo de búsqueda?",
    "43": "¿Por qué la notación O se utiliza para analizar la eficiencia de algoritmos?",
    "45": "¿Qué diferencia hay entre O(n^2) y O(n) en términos de eficiencia para entradas grandes?",
    "47": "En el contexto de eficiencia de algoritmos, ¿qué representa la notación Ω(f)?",
    "49": "¿Cuál es el significado de la notación asintótica Θ(f)?",
    "51": "¿Qué representa la jerarquía de complejidad de algoritmos?",
    "53": "¿Qué implica que un algoritmo pertenezca al orden O(n^2)?",
    "55": "¿Cuál es una propiedad de la notación O en la comparación de funciones?",
    "57": "Si una función pertenece al orden Ω(f), ¿qué representa en términos de crecimiento?",
    "59": "¿Cuál es la complejidad típica de un algoritmo de búsqueda en un arreglo ordenado mediante búsqueda binaria?",
    "61": "¿Por qué las constantes multiplicativas no son importantes en la notación asintótica?",
    "63": "¿Cuál es el objetivo de la notación O en el análisis de algoritmos?",
    "65": "¿Qué se entiende por jerarquía de crecimiento en el análisis de algoritmos?",
    "67": "¿Cuál de las siguientes complejidades es mejor para grandes conjuntos de datos?",
    "69": "¿Qué significa decir que una función f(n) es acotada superiormente por otra función g(n)?",
    "71": "¿Qué es la notación O en el análisis de algoritmos?",
    "73": "Si un algoritmo pertenece a Θ(n), ¿qué significa?",
    "75": "¿Qué implica que una función sea acotada inferiormente por otra en Ω(g)?",
    "77": "¿Cuál es la relación entre Ω y Θ en términos de complejidad?",
    "79": "¿Cuál de las siguientes afirmaciones sobre el análisis asintótico es verdadera?",
    "81": "¿Qué significa que una operación tenga complejidad O(1)?",
    "83": "¿Cuál es el objetivo principal del análisis de eficiencia de algoritmos?",
    "85": "En el contexto de análisis de algoritmos, ¿qué es una operación elemental?",
    "87": "¿Qué diferencia hay entre complejidad promedio y complejidad en el peor caso?",
    "89": "¿Cuál es el impacto de las constantes en el análisis asintótico cuando n es grande?",
    "91": "¿Qué indica que un algoritmo tiene complejidad O(nlog(n))?",
    "93": "¿Qué significa que una función pertenece al orden O(1)?",
    "95": "¿Cuál es la ventaja de un algoritmo de orden O(log(n)) frente a uno de orden O(n)?",
    "97": "En términos de complejidad, ¿cuál es mejor para grandes entradas: O(n^2) o O(nlog(n))?",
    "99": "¿Qué representa el mejor caso de un algoritmo?",
    "101": "¿Cuál es el impacto de los términos de menor crecimiento en la notación asintótica?",
    "103": "¿Qué indica que un algoritmo de orden O(n^2) es menos eficiente que uno de orden O(n)?",
    "105": "¿Qué se entiende por cota superior en análisis de algoritmos?",
    "107": "¿Qué significa que una función sea Θ(n)?",
    "109": "¿Cuál es el papel de la notación Θ en la clasificación de algoritmos?",
    "111": "¿Por qué es importante el análisis de la complejidad en el peor caso?",
    "113": "¿Qué tipo de crecimiento describe O(2^n)?",
    "115": "¿Qué representa la notación Ω en análisis de algoritmos?",
    "117": "¿Qué significa que un algoritmo tenga complejidad Ω(n)?",
    "119": "¿Cómo se compara O(n) con O(n^3) en términos de eficiencia?",
    "121": "¿Cuál es la complejidad del algoritmo de búsqueda binaria en una lista ordenada?",
    "123": "¿Qué es una operación dominante en el análisis de algoritmos?",
    "125": "¿Qué representa el caso promedio en el análisis de un algoritmo?",
    "127": "¿Qué describe la cota inferior de un algoritmo?"
}

solucion = {
    "1": "Conjunto de funciones acotadas superiormente por múltiplos reales de f.",
    "3": "O(1) < O(Log(n)) < O(n) < O(nLog(n)) < O(n^2) < 2^n < n!.",
    "5": "Que f y g crecen a la misma velocidad.",
    "7": "No debe ser elemental.",
    "9": "Porque solo es posible en vectores ordenados.",
    "11": "Es la propiedad que permite pasar características de O a Ω y viceversa.",
    "13": "Un algoritmo recursivo generalmente tiene una mayor sobrecarga en el sistema.",
    "15": "O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n^2).",
    "17": "Soporte ejecutivo insuficiente.",
    "19": "Es una operación que se ejecuta tantas veces como cualquier otra en el algoritmo y es representativa.",
    "21": "El algoritmo es eficiente en conjuntos de datos grandes y se acota por encima por una función logarítmica.",
    "23": "Permite analizar la eficiencia del algoritmo sin fijarse en el programa específico.",
    "25": "O(c * f(n)) = O(f(n)).",
    "27": "La eficiencia se mide siempre en número de instrucciones ejecutadas.",
    "29": "Es un conjunto de funciones acotadas tanto superior como inferiormente por f.",
    "31": "Una operación crítica es elemental y representativa de la eficiencia del algoritmo.",
    "33": "Induce el orden O.",
    "35": "O(log(n)) es mejor que O(n) para entradas suficientemente grandes.",
    "37": "Es una operación que se ejecuta en tiempo constante.",
    "39": "Seleccionar una operación representativa que mida la eficiencia del algoritmo.",
    "41": "O(log(n)).",
    "43": "Permite comparar la eficiencia de diferentes algoritmos para valores grandes de entrada.",
    "45": "O(n) es más eficiente que O(n^2) para grandes conjuntos de datos.",
    "47": "Representa una cota inferior de la eficiencia del algoritmo.",
    "49": "Es una cota tanto superior como inferior para el crecimiento de una función.",
    "51": "Una clasificación de funciones en base a su tasa de crecimiento.",
    "53": "El algoritmo tiene un crecimiento cuadrático en función de la entrada.",
    "55": "Si f ∈ O(g), entonces el crecimiento de f está acotado superiormente por g.",
    "57": "Es una cota inferior que describe el mínimo crecimiento de la función.",
    "59": "O(log(n)).",
    "61": "Porque solo importan los términos de mayor crecimiento en conjuntos grandes.",
    "63": "Describir la eficiencia de un algoritmo para grandes valores de entrada.",
    "65": "Una clasificación de funciones que muestra cuál crece más rápido.",
    "67": "O(log(n)).",
    "69": "Que f(n) crece a un ritmo no mayor que g(n) para grandes valores de n.",
    "71": "Una notación que expresa una cota superior para el crecimiento de la función.",
    "73": "El algoritmo tiene un crecimiento lineal exacto en términos de n.",
    "75": "Que el crecimiento de la función es al menos tan grande como g para valores grandes de entrada.",
    "77": "Si f ∈ Θ(g), entonces f pertenece a Ω(g) y O(g).",
    "79": "Describe el comportamiento del algoritmo para grandes valores de entrada.",
    "81": "Que la operación tiene un tiempo de ejecución constante, independientemente del tamaño de la entrada.",
    "83": "Determinar cómo el tiempo de ejecución del algoritmo aumenta con el tamaño de la entrada.",
    "85": "Una operación que se ejecuta en un tiempo constante.",
    "87": "La complejidad promedio se refiere al tiempo de ejecución esperado, mientras que el peor caso considera el tiempo más alto posible.",
    "89": "Las constantes se vuelven menos significativas a medida que n crece.",
    "91": "El algoritmo tiene un crecimiento sub-lineal multiplicado por log(n).",
    "93": "La función tiene un tiempo de ejecución constante.",
    "95": "Es más eficiente para grandes entradas, ya que crece más lentamente.",
    "97": "O(nlog(n)) es mejor para grandes entradas.",
    "99": "Es el escenario en el cual el algoritmo ejecuta el menor número de pasos.",
    "101": "Se ignoran en la notación asintótica, ya que no afectan el crecimiento para n grandes.",
    "103": "El orden cuadrático crece más rápido que el lineal cuando n es grande.",
    "105": "Es una medida de crecimiento máximo de una función respecto a otra.",
    "107": "La función crece de forma lineal con respecto a n.",
    "109": "Clasifica funciones en términos de su crecimiento exacto.",
    "111": "Permite entender el comportamiento del algoritmo en el escenario más complejo.",
    "113": "Un crecimiento exponencial en términos de n.",
    "115": "Representa una cota inferior para el crecimiento de un algoritmo.",
    "117": "El algoritmo tiene un crecimiento mínimo lineal en términos de n.",
    "119": "O(n) es más eficiente que O(n^3) para grandes valores de n.",
    "121": "O(log(n)).",
    "123": "Es la operación que define la eficiencia del algoritmo.",
    "125": "El tiempo de ejecución esperado considerando una entrada típica.",
    "127": "El crecimiento mínimo que puede alcanzar el algoritmo."
}

opciones = {
    "1": "Conjunto de funciones acotadas inferiormente por múltiplos reales de f./Conjunto de funciones acotadas superiormente por múltiplos reales de f./Conjunto de funciones sin restricción de límites./Conjunto de funciones acotadas superior e inferiormente por f.",
    "3": "O(1) < O(n) < O(Log(n)) < O(n^2) < O(n!)/O(1) < O(Log(n)) < O(n) < O(nLog(n)) < O(n^2) < 2^n < n!/O(n) < O(1) < O(n^2) < O(Log(n))/O(1) < O(nLog(n)) < O(Log(n)) < O(n^2)",
    "5": "Que f crece más rápido que g./Que g es siempre mayor que f./Que no hay relación entre f y g./Que f y g crecen a la misma velocidad.",
    "7": "Debe ser representativa del algoritmo./Debe ejecutarse tantas veces como cualquier otra operación./No debe ser elemental./Debe ser una operación elemental.",
    "9": "Porque la complejidad mínima de búsqueda es O(n)./Porque solo se aplica en vectores desordenados./Porque solo es posible en vectores ordenados./Porque depende de la implementación del algoritmo.",
    "11": "Es la propiedad que permite pasar características de O a Ω y viceversa./Es la propiedad que asegura que f(n) y g(n) crecen al mismo ritmo./Es una operación de recursividad sobre una función./Es la propiedad que permite reducir el tiempo de ejecución en casos de grandes entradas.",
    "13": "Un algoritmo recursivo generalmente tiene una mayor sobrecarga en el sistema./Un algoritmo recursivo siempre es más rápido que su equivalente iterativo./Un algoritmo recursivo utiliza menos memoria que su equivalente iterativo./Ambos son iguales en términos de velocidad.",
    "15": "O(n) < O(1) < O(log(n)) < O(n^2)/O(log(n)) < O(nlog(n)) < O(1) < O(n)/O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n^2)/O(n^2) < O(log(n)) < O(1) < O(nlog(n)).",
    "17": "La falta de definición de requerimientos./Soporte ejecutivo insuficiente./La falta de recursos técnicos./Costos de implementación bajos.",
    "19": "Es una operación que se ejecuta tantas veces como cualquier otra en el algoritmo y es representativa./Es una operación elemental que ocurre solo una vez en el algoritmo./Es una operación que se ignora en el análisis asintótico./Es cualquier operación dentro del algoritmo.",
    "21": "El algoritmo es eficiente en conjuntos de datos grandes y se acota por encima por una función logarítmica./El algoritmo siempre tendrá una complejidad peor que O(n)./El algoritmo solo es eficiente para conjuntos de datos pequeños./La eficiencia no se ve afectada por el tamaño del conjunto de datos.",
    "23": "Permite analizar la eficiencia del algoritmo sin fijarse en el programa específico./Permite asegurar que el algoritmo será eficiente en cualquier entorno./Implica que siempre se utiliza la misma cantidad de memoria./Permite intercambiar algoritmos sin afectar el tiempo de ejecución.",
    "25": "O(c * f(n)) = O(c) si c > 0./O(c * f(n)) = O(n)./O(c * f(n)) = O(f(n))./O(c * f(n)) = O(1) para cualquier función f.",
    "27": "La eficiencia se mide siempre en número de instrucciones ejecutadas./El análisis de eficiencia se basa en notación asintótica./La eficiencia se mide en términos de crecimiento con respecto a la entrada./El tiempo de ejecución se analiza en función de entradas suficientemente grandes.",
    "29": "Es un conjunto de funciones acotadas superiormente por f./Es un conjunto de funciones acotadas tanto superior como inferiormente por f./Es una cota que solo se aplica para valores pequeños de entrada./Es una cota que se aplica a todas las funciones en tiempo constante.",
    "31": "Una operación crítica es elemental y representativa de la eficiencia del algoritmo./Una operación crítica se elige para reducir el tiempo de ejecución./Las operaciones críticas solo ocurren en la inicialización del algoritmo./Las operaciones críticas deben evitarse en análisis de eficiencia.",
    "33": "Induce el orden O./Induce el orden Ω./Induce el orden Θ./Induce el orden log(n).",
    "35": "O(log(n)) es mejor que O(n) para entradas suficientemente grandes./O(n) es mejor que O(1) para entradas pequeñas./O(n^2) es mejor que O(nlog(n)) para entradas grandes./O(1) es mejor que O(log(n)) para entradas grandes.",
    "37": "Es una operación que se ejecuta en tiempo constante./Es una operación que se ejecuta una vez al inicio./Es una operación que se ejecuta infinitamente en el algoritmo./Es cualquier operación que sea crítica.",
    "39": "Seleccionar una operación representativa que mida la eficiencia del algoritmo./Reducir el tiempo de ejecución del algoritmo./Mejorar la complejidad asintótica del algoritmo./Eliminar operaciones innecesarias del algoritmo.",
    "41": "O(n^2)./O(n)./O(log(n))./O(nlog(n)).",
    "43": "Permite comparar la eficiencia de diferentes algoritmos para valores grandes de entrada./Se aplica a funciones con resultados inmediatos./Mide la complejidad de algoritmos sin importar su tamaño de entrada./Es solo aplicable a algoritmos de orden constante.",
    "45": "O(n) es más eficiente que O(n^2) para grandes conjuntos de datos./O(n) tiene mayor complejidad que O(n^2)./O(n^2) es más eficiente para grandes conjuntos de datos./Ambos son iguales para grandes conjuntos de datos.",
    "47": "Representa una cota inferior de la eficiencia del algoritmo./Es una cota superior de la eficiencia del algoritmo./Es una notación que indica el tiempo constante./Es una función de complejidad lineal.",
    "49": "Es una cota tanto superior como inferior para el crecimiento de una función./Es solo una cota superior para la función./Es una notación para funciones constantes./Es una notación solo para algoritmos recursivos.",
    "51": "Una clasificación de funciones en base a su tasa de crecimiento./Una descripción de las operaciones de entrada./Un conjunto de funciones limitadas por una constante./Una descripción de las instrucciones en un algoritmo.",
    "53": "El algoritmo tiene un crecimiento cuadrático en función de la entrada./El algoritmo tiene un crecimiento logarítmico en función de la entrada./El algoritmo es independiente del tamaño de la entrada./El algoritmo tiene un crecimiento exponencial en función de la entrada.",
    "55": "Si f ∈ O(g), entonces el crecimiento de f está acotado superiormente por g./Si f ∈ O(g), entonces f y g crecen al mismo ritmo./Si f ∈ O(g), entonces g crece más rápido que f siempre./Si f ∈ O(g), entonces f es siempre mayor que g.",
    "57": "Es una cota inferior que describe el mínimo crecimiento de la función./Es una cota superior que representa el crecimiento máximo./Es una medida exacta del tiempo de ejecución./Es una función sin restricciones en términos de crecimiento.",
    "59": "O(n)./O(log(n))./O(n^2)./O(1).",
    "61": "Porque solo importan los términos de mayor crecimiento en conjuntos grandes./Porque se ignoran en los algoritmos de búsqueda./Porque se analizan únicamente términos de menor crecimiento./Porque no afectan la ejecución en tiempo constante.",
    "63": "Describir la eficiencia de un algoritmo para grandes valores de entrada./Describir la cantidad exacta de tiempo que tomará un algoritmo./Medir la eficiencia solo en términos de operaciones críticas./Comparar algoritmos independientemente del tamaño de la entrada.",
    "65": "Una clasificación de funciones que muestra cuál crece más rápido./Una clasificación en función de la memoria utilizada./Una comparación de algoritmos en función de su tamaño de entrada./Una medida del tiempo en función de los ciclos de procesador.",
    "67": "O(n^2)./O(n)./O(log(n))./O(nlog(n)).",
    "69": "Que f(n) crece a un ritmo no mayor que g(n) para grandes valores de n./Que g(n) es siempre mayor que f(n) para valores pequeños./Que f(n) y g(n) crecen a ritmos iguales siempre./Que f(n) y g(n) no tienen relación alguna.",
    "71": "Una notación que expresa una cota superior para el crecimiento de la función./Una notación que muestra la eficiencia exacta de un algoritmo./Una notación que calcula el tiempo de ejecución real./Una notación utilizada solo en algoritmos recursivos.",
    "73": "El algoritmo tiene un crecimiento lineal exacto en términos de n./El algoritmo tiene un crecimiento logarítmico exacto./El algoritmo tiene un crecimiento cuadrático exacto./El algoritmo tiene un crecimiento constante.",
    "75": "Que el crecimiento de la función es al menos tan grande como g para valores grandes de entrada./Que el crecimiento de la función es exactamente igual a g para cualquier valor./Que el crecimiento es limitado solo por la complejidad de entrada./Que siempre es constante.",
    "77": "Si f ∈ Θ(g), entonces f pertenece a Ω(g) y O(g)./Si f ∈ Θ(g), entonces f es menor que g siempre./Si f ∈ Θ(g), entonces f no tiene relación con g./Si f ∈ Θ(g), entonces f es superior a g.",
    "79": "Describe el comportamiento del algoritmo para grandes valores de entrada./Determina el tiempo exacto de ejecución del algoritmo./Se enfoca únicamente en el peor caso./Es útil solo para algoritmos de orden constante.",
    "81": "Que la operación tiene un tiempo de ejecución constante, independientemente del tamaño de la entrada./Que la operación tiene un tiempo de ejecución que crece con la entrada./Que depende de los valores en tiempo promedio./Que es siempre la operación crítica.",
    "83": "Determinar cómo el tiempo de ejecución del algoritmo aumenta con el tamaño de la entrada./Medir el tiempo exacto que tomará el algoritmo en cualquier caso./Comparar diferentes algoritmos independientemente de la entrada./Evaluar la eficiencia en el peor caso únicamente.",
    "85": "Una operación que se ejecuta en un tiempo constante./Una operación que solo ocurre una vez./Una operación que se ejecuta múltiples veces./Una operación que siempre es crítica.",
    "87": "La complejidad promedio se refiere al tiempo de ejecución esperado, mientras que el peor caso considera el tiempo más alto posible./La complejidad promedio y el peor caso siempre son iguales./La complejidad promedio solo se usa para entradas grandes./El peor caso y el promedio son irrelevantes para el análisis asintótico.",
    "89": "Las constantes se vuelven menos significativas a medida que n crece./Las constantes siempre determinan la eficiencia./Las constantes se vuelven más significativas con entradas grandes./Las constantes no se consideran en ningún caso.",
    "91": "El algoritmo tiene un crecimiento sub-lineal multiplicado por log(n)./El algoritmo tiene crecimiento lineal./El algoritmo tiene un crecimiento exponencial./El algoritmo crece en tiempo constante.",
    "93": "La función tiene un tiempo de ejecución constante./La función tiene un crecimiento lineal./La función es cuadrática en relación con n./La función es exponencial.",
    "95": "Es más eficiente para grandes entradas, ya que crece más lentamente./Es menos eficiente que un algoritmo de orden O(n)./Es igual en eficiencia para grandes entradas./Es más rápido en pequeñas entradas únicamente.",
    "97": "O(nlog(n)) es mejor para grandes entradas./O(n^2) es mejor para grandes entradas./Ambos son iguales en eficiencia./Ninguno de los dos es eficiente para grandes entradas.",
    "99": "Es el escenario en el cual el algoritmo ejecuta el menor número de pasos./Es el caso en el cual el algoritmo ejecuta el mayor número de pasos./Es el caso promedio de ejecución./Es cuando el algoritmo falla.",
    "101": "Se ignoran en la notación asintótica, ya que no afectan el crecimiento para n grandes./Son decisivos en el análisis./Se consideran en algoritmos recursivos./Son más importantes que los términos de mayor crecimiento.",
    "103": "El orden cuadrático crece más rápido que el lineal cuando n es grande./El orden lineal crece más rápido que el cuadrático./Ambos crecen igual para n grande./El cuadrático es siempre más eficiente.",
    "105": "Es una medida de crecimiento máximo de una función respecto a otra./Es una medida de crecimiento mínimo./Es una medida exacta de eficiencia./Es una medida independiente del tamaño de la entrada.",
    "107": "La función crece de forma lineal con respecto a n./La función crece exponencialmente./La función crece cuadráticamente./La función no depende de n.",
    "109": "Clasifica funciones en términos de su crecimiento exacto./Es una cota superior para el crecimiento./Es una cota inferior del crecimiento./Solo aplica para funciones cuadráticas.",
    "111": "Permite entender el comportamiento del algoritmo en el escenario más complejo./Determina la media de tiempo de ejecución./Es una medida del mejor caso./Se ignora en el análisis de eficiencia.",
    "113": "Un crecimiento exponencial en términos de n./Un crecimiento cuadrático./Un crecimiento lineal./Un crecimiento constante.",
    "115": "Representa una cota inferior para el crecimiento de un algoritmo./Representa una cota superior para el crecimiento./Representa el tiempo de ejecución promedio./Es la cota exacta del tiempo.",
    "117": "El algoritmo tiene un crecimiento mínimo lineal en términos de n./El algoritmo tiene crecimiento exponencial./El algoritmo no depende de n./El algoritmo tiene un crecimiento máximo.",
    "119": "O(n) es más eficiente que O(n^3) para grandes valores de n./O(n^3) es más eficiente que O(n) para grandes valores de n./Ambos son iguales en términos de eficiencia./Ambos crecen al mismo ritmo.",
    "121": "O(n)./O(log(n))./O(n^2)./O(1).",
    "123": "Es la operación que define la eficiencia del algoritmo./Es una operación que se ignora en el análisis./Es una operación irrelevante./Es la última operación en el algoritmo.",
    "125": "El tiempo de ejecución esperado considerando una entrada típica./El tiempo de ejecución en el peor escenario./El tiempo de ejecución más bajo posible./El tiempo de ejecución en tiempo constante.",
    "127": "El crecimiento mínimo que puede alcanzar el algoritmo./El crecimiento máximo posible./El crecimiento exacto./El crecimiento sub-lineal.",
}




def ratemwar():
    aux="1"
    while aux != "x":
        os.system('color F0')
        os.system('cls' if os.name == 'nt' else 'clear')
        clave_aleatoria = random.choice(list(enunciado.keys()))
        # clave_aleatoria = "35" # Para pruebas
        print("\n\n\t" + enunciado[clave_aleatoria] + "\n")
        i = 1
        opciones_mezcladas = random.sample(opciones[clave_aleatoria].split('/'), len(opciones[clave_aleatoria].split('/')))
        for opcion in opciones_mezcladas:
            print("\t\t"+ str(i) + ". " + opcion)
            i = i + 1

        while True:
            respuesta = input("\n\t\tSelecciona una respuesta (1-4)(x para salir):")
            if respuesta in ["1", "2", "3", "4","x"]:
                break
            else:
                print("\n\t\tPor favor, selecciona una opción válida entre 1 y 4.")
        if respuesta != "x":    
            aux=respuesta
            respuesta = opciones_mezcladas[int(aux) - 1]
            if respuesta == solucion[clave_aleatoria]:
                os.system('color F2')
                print("\n")
                print("\t  ____ ___  ____  ____  _____ ____ _____ ___ ")
                print("\t / ___/ _ \|  _ \|  _ \| ____/ ___|_   _/ _ \ ")
                print("\t| |  | | | | |_) | |_) |  _|| |     | || | | |")
                print("\t| |__| |_| |  _ <|  _ <| |__| |___  | || |_| |")
                print("\t \____\___/|_| \_\_| \_\_____\____| |_| \___/")
            else:
                os.system('color F4')
                print ("\t  ___ _   _  ____ ___  ____  ____  _____ ____ _____ ___  ")
                print ("\t |_ _| \ | |/ ___/ _ \|  _ \|  _ \| ____/ ___|_   _/ _ \ ")
                print ("\t  | ||  \| | |  | | | | |_) | |_) |  _|| |     | || | | |")
                print ("\t  | || |\  | |__| |_| |  _ <|  _ <| |__| |___  | || |_| |")
                print ("\t |___|_| \_|\____\___/|_| \_\_| \_\_____\____| |_| \___/\n")
                print("\tLa respuesta correcta es: " + solucion[clave_aleatoria])
        else:
            break
        print("\n\n\n\n")
        input("\n\t\tPulsa Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar pantalla al salir del bucle while principal del juego 
if __name__ == '__main__':
    ratemwar()
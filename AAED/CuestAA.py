import random
import os

# Preguntas, opciones y soluciones actualizadas
enunciado = {
    "1": "Es posible realizar búsquedas en una lista en orden logarítmico, pero exige que los elementos de la lista estén ordenados.",
    "2": "Independientemente del tamaño del problema, es siempre mejor un algoritmo de orden logarítmico que de orden lineal.",
    "3": "nlog(n) ∈ O(n²) y nlog(n) ∈ Ω(n²)",
    "4": "Las constantes multiplicativas de los órdenes carecen de importancia si el tamaño del problema es lo bastante grande.",
    "5": "No existen algoritmos de búsqueda en cualquier vector de coste O(log(n)).",
    "6": "No existen algoritmos de ordenación de vectores con coste inferior a O(n²).",
    "7": "No es posible realizar búsquedas en una lista en orden logarítmico, aunque los elementos de la lista estén ordenados.",
    "8": "Si los elementos de una lista están ordenados, podemos asegurar un coste lineal en la búsqueda, y en el tiempo en caso promedio será mejor que cuando no están ordenados.",
    "9": "La eficiencia de un programa puede ser mejor que la del algoritmo subyacente, si está especialmente bien implementado.",
    "10": "Un algoritmo recursivo es igual de rápido que su equivalente iterativo.",
    "11": "Dos algoritmos del mismo orden ejecutan el mismo número de operaciones elementales.",
    "12": "Un algoritmo con eficiencia en Ω(n) es mejor que otro cuya eficiencia esté en O(n²).",
    "13": "Los órdenes asintóticos son una herramienta para medir la eficiencia de los algoritmos en unidades de tiempo.",
    "14": "El principio de invarianza nos permite analizar la eficiencia de los algoritmos en lugar de la de los programas.",
    "15": "El tiempo promedio de ejecución de un programa coincide con la media de los tiempos en los casos mejor y peor.",
    "16": "Las constantes multiplicativas de los órdenes asintóticos carecen de importancia si el tamaño del problema es lo bastante pequeño.",
    "17": "En el caso de órdenes parecidos n² vs nlog(n), las constantes multiplicativas son decisivas si el tamaño del problema es lo bastante grande.",
    "18": "El número de veces que se realiza la operación crítica en el caso mejor es siempre inferior al caso promedio.",
    "19": "El número de veces que se realiza la operación crítica en el caso mejor no es siempre inferior al del caso promedio.",
    "20": "n³ ∈ O(2^n) y n³ no ∈ Ω(2^n)",
}

opciones = {
    "1": "Verdadero./Falso, las búsquedas en una lista son de O(n)./Falso, no es necesario que la lista esté ordenada para lograr O(log n)./Falso, el orden logarítmico solo aplica a operaciones de ordenación.",
    "2": "Falso, depende de las constantes, los órdenes son asintóticos./Verdadero, ya que log(n) siempre crece más lentamente que n./Falso, un algoritmo lineal puede ser más eficiente para problemas pequeños./Falso, la eficiencia de los algoritmos no depende del orden asintótico.",
    "3": "Falso./Verdadero, porque nlog(n) está contenido en O(n²)./Falso, pero nlog(n) pertenece solo a O(n)./Verdadero, siempre que nlog(n) crezca más rápido que n².",
    "4": "Verdadero./Falso, las constantes siempre son importantes./Verdadero, pero solo si n < 10./Falso, depende del contexto del algoritmo.",
    "5": "Verdadero./Falso, porque el orden logarítmico se puede lograr con vectores desordenados./Falso, siempre que se use búsqueda binaria./Verdadero, excepto si el vector tiene elementos únicos.",
    "6": "Falso, existen algoritmos de ordenación con coste O(nlog(n))./Verdadero, ningún algoritmo puede superar O(n²)./Falso, los algoritmos de ordenación siempre son O(n²)./Verdadero, pero depende del tamaño del vector.",
    "7": "Verdadero./Falso, siempre es posible si se usa búsqueda binaria./Falso, los algoritmos de búsqueda son siempre lineales./Falso, no importa el orden del vector.",
    "8": "Falso./Verdadero, el coste siempre será lineal en todos los casos./Verdadero, pero solo si la lista es pequeña./Falso, el caso promedio no mejora al ordenar la lista.",
    "9": "Falso./Verdadero, depende de la implementación del programa./Verdadero, si se optimizan todas las operaciones críticas./Falso, la eficiencia depende solo del algoritmo.",
    "10": "Falso./Verdadero, siempre tienen la misma velocidad./Verdadero, solo si las operaciones críticas coinciden./Falso, pero dependen de la implementación.",
    "11": "Falso./Verdadero, si están en el mismo orden asintótico./Falso, depende del caso promedio./Falso, las operaciones elementales no importan.",
    "12": "Falso./Verdadero, los algoritmos en Ω(n) siempre son mejores./Falso, pero los órdenes no son comparables./Verdadero, porque el coste lineal siempre será mejor.",
    "13": "Falso./Verdadero, solo en unidades grandes de tiempo./Falso, los órdenes se usan para comparar algoritmos./Falso, no se mide en unidades de tiempo.",
    "14": "Verdadero./Falso, el principio de invarianza solo aplica a datos específicos./Falso, no analiza ni algoritmos ni programas./Verdadero, pero solo en análisis asintóticos.",
    "15": "Falso./Verdadero, la media coincide con el tiempo promedio./Falso, estará entre ambos, pero no coincide con la media./Falso, solo se estudian los casos extremos.",
    "16": "Falso, cuando es pequeño es cuando es importante./Falso, las constantes nunca importan./Falso, siempre son irrelevantes para problemas pequeños./Verdadero, si n es muy pequeño.",
    "17": "Falso, son decisivas si es lo bastante pequeño./Verdadero, si el tamaño del problema es suficientemente grande./Falso, los órdenes siempre son comparables./Verdadero, pero solo en órdenes no lineales.",
    "18": "Falso, puede ser igual./Verdadero, siempre es menor./Falso, nunca puede ser igual al caso promedio./Falso, depende de la estructura iterativa.",
    "19": "Verdadero./Falso, siempre será igual./Falso, depende del tamaño del vector./Verdadero, excepto en algoritmos recursivos.",
    "20": "Verdadero, 2^n acota por arriba a n³ y no por abajo./Falso, porque 2^n no es comparable con n³./Falso, los algoritmos no se clasifican así./Verdadero, pero solo si n³ crece exponencialmente.",
   
}

solucion = {
    "1": "Verdadero.",
    "2": "Falso, depende de las constantes, los órdenes son asintóticos.",
    "3": "Falso.",
    "4": "Verdadero.",
    "5": "Verdadero.",
    "6": "Falso, existen algoritmos de ordenación con coste O(nlog(n)).",
    "7": "Verdadero.",
    "8": "Falso.",
    "9": "Falso.",
    "10": "Falso.",
    "11": "Falso.",
    "12": "Falso.",
    "13": "Falso.",
    "14": "Verdadero.",
    "15": "Falso, estará entre ambos, pero no coincide con la media.",
    "16": "Falso, cuando es pequeño es cuando es importante.",
    "17": "Falso, son decisivas si es lo bastante pequeño.",
    "18": "Falso, puede ser igual.",
    "19": "Verdadero.",
    "20": "Verdadero, 2^n acota por arriba a n³ y no por abajo.",
}

# Función principal del cuestionario
def ratemwar():
    aciertos = 0
    errores = 0
    preguntas_respondidas = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        clave_aleatoria = random.choice(list(enunciado.keys()))
        print("\n\n\t" + enunciado[clave_aleatoria] + "\n")
        i = 1
        opciones_mezcladas = random.sample(opciones[clave_aleatoria].split('/'), len(opciones[clave_aleatoria].split('/')))
        for opcion in opciones_mezcladas:
            print("\t\t" + str(i) + ". " + opcion)
            i += 1

        respuesta = input("\n\t\tSelecciona una respuesta (1-4)(x para salir): ")
        if respuesta == "x":
            break
        elif respuesta in ["1", "2", "3", "4"]:
            respuesta_usuario = opciones_mezcladas[int(respuesta) - 1]
            if respuesta_usuario == solucion[clave_aleatoria]:
                print("\n\t¡Correcto!")
                aciertos += 1
            else:
                print("\n\tIncorrecto.")
                print("\tLa respuesta correcta es: " + solucion[clave_aleatoria])
                errores += 1
            preguntas_respondidas += 1
        else:
            print("\n\tPor favor, selecciona una opción válida.")
        input("\n\tPresiona Enter para continuar...")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tRESULTADOS FINALES")
    print(f"\tPreguntas respondidas: {preguntas_respondidas}")
    print(f"\tAciertos: {aciertos}")
    print(f"\tErrores: {errores}")

if __name__ == '__main__':
    ratemwar()

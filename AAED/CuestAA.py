import random
import os

# Diccionario con los enunciados de las preguntas
enunciado = {
    "1": "¿Qué se busca al comparar algoritmos en términos de eficiencia?",
    "2": "¿Cómo afecta el tamaño de entrada a los recursos utilizados por un algoritmo?",
    "3": "¿Qué enfoque de análisis de algoritmos se basa en la programación real del algoritmo?",
    "4": "En un análisis híbrido de tiempo, ¿qué pasos incluye?",
    "5": "¿Qué es una operación elemental en el contexto del análisis de algoritmos?",
    "6": "¿Qué tipo de operación se ejecuta tantas veces como cualquier otra operación en un algoritmo?",
    "7": "En el análisis de tiempo, ¿qué es el caso peor?",
    "8": "¿Qué estudia el caso promedio en el análisis de algoritmos?",
    "9": "En una estructura condicional, ¿cómo se calcula el tiempo en el caso peor?",
    "10": "En una estructura iterativa, si el tiempo de la condición no varía, ¿cuál es la fórmula para el tiempo total?",
    "11": "En una estructura iterativa, si tanto el tiempo de la condición como el tiempo de la operación varían en cada vuelta, ¿cómo se calcula el tiempo total?",
    "12": "¿Qué es lo que se mide en el análisis empírico del tiempo de un algoritmo?",
    "13": "¿Cuál es la fórmula para el tiempo en una estructura condicional en el caso promedio?",
    "14": "En el análisis de un algoritmo para encontrar el mínimo de un vector, ¿cuál es la operación crítica?",
    "15": "¿Cuál es la notación asintótica para el tiempo de ejecución del algoritmo que busca el mínimo de un vector de tamaño n?",
    "16": "En una estructura iterativa, si el tiempo de la condición varía en cada vuelta, ¿cómo se calcula el tiempo total?",
    "17": "¿Qué significa que el tiempo de una operación sea Θ(1)?",
    "18": "En el análisis de algoritmos, ¿qué es el caso mejor?",
    "19": "¿Qué tipo de análisis se utiliza cuando se conoce el comportamiento teórico del algoritmo y se ajusta mediante mediciones reales?"
}

# Diccionario con las opciones de respuesta para cada pregunta
opciones = {
    "1": "a) Comparar el tamaño del código\nb) Comparar el tiempo y el espacio utilizados\nc) Comparar la cantidad de operaciones realizadas\nd) Comparar la complejidad de las estructuras de datos",
    "2": "a) A menor tamaño de entrada, más recursos se utilizan\nb) A mayor tamaño de entrada, más recursos se utilizan\nc) El tamaño de entrada no influye en el uso de recursos\nd) Los recursos se utilizan independientemente del tamaño de la entrada",
    "3": "a) Teórico\nb) Empírico\nc) Híbrido\nd) Analítico",
    "4": "a) Solo la medición de tiempos reales\nb) Solo la programación del algoritmo\nc) Medición de tiempos reales y ajuste del modelo teórico mediante regresión\nd) Ninguna de las anteriores",
    "5": "a) Una operación cuyo tiempo de ejecución es constante\nb) Una operación que depende de la entrada\nc) Una operación cuyo tiempo de ejecución varía con el tamaño de la entrada\nd) Una operación que no afecta el tiempo de ejecución",
    "6": "a) Operación crítica\nb) Operación elemental\nc) Operación optimizada\nd) Operación condicional",
    "7": "a) La entrada de tamaño n más costosa\nb) La entrada de tamaño n menos costosa\nc) La entrada más común\nd) La entrada promedio",
    "8": "a) El comportamiento de las entradas con tamaño n más costosas\nb) La diferencia significativa entre el peor y el mejor caso\nc) La entrada más común\nd) El comportamiento de las entradas menos costosas",
    "9": "a) Sumar el tiempo de las operaciones críticas\nb) Tomar el máximo entre los tiempos de las operaciones C1 y C2\nc) Tomar el mínimo entre los tiempos de las operaciones C1 y C2\nd) Restar los tiempos de las operaciones C1 y C2",
    "10": "a) t(n) = v(n)t_C(n)\nb) t(n) = (v(n)+1)t_B(n)+v(n)t_C(n)\nc) t(n) = ∑(i=1, v(n)) t_C(i,n)\nd) Ninguna de las anteriores",
    "11": "a) t(n) = v(n)t_B(n)+v(n)t_C(n)\nb) t(n) = ∑(i=1, v(n)+1) t_B(i,n)+∑(i=1, v(n)) t_C(i,n)\nc) t(n) = (v(n)+1)t_B(n)+∑(i=1, v(n)) t_C(i,n)\nd) Ninguna de las anteriores",
    "12": "a) La cantidad de operaciones realizadas\nb) Los tiempos reales de ejecución\nc) El modelo teórico del algoritmo\nd) Ninguna de las anteriores",
    "13": "a) t(n) = t_B(n) + ρ(B)t_{C_1}(n) + ρ(¬B)t_{C_2}(n)\nb) t(n) = t_B(n) + max[t_{C_1}(n), t_{C_2}(n)]\nc) t(n) = t_B(n) + t_{C_1}(n) + t_{C_2}(n)\d) Ninguna de las anteriores",
    "14": "a) Comparar los elementos del vector\nb) Iterar sobre los elementos del vector\nc) Asignar el valor mínimo\nd) Ninguna de las anteriores",
    "15": "a) t(n) = n²\nb) t(n) = n log n\nc) t(n) = n - 1\nd) t(n) = log n",
    "16": "a) t(n) = v(n)t_B(n) + ∑(i=1, v(n)) t_C(i,n)\nb) t(n) = (v(n) + 1)t_B(n) + v(n)t_C(n)\nc) t(n) = ∑(i=1, v(n)) t_C(i,n)\d) Ninguna de las anteriores",
    "17": "a) Que la operación tiene un tiempo de ejecución que varía linealmente con el tamaño de la entrada\nb) Que la operación tiene un tiempo de ejecución constante\nc) Que la operación depende del número de elementos en el vector\nd) Ninguna de las anteriores",
    "18": "a) La entrada con el menor tiempo de ejecución posible\nb) La entrada más común\nc) La entrada que tiene el menor costo de ejecución en términos de tiempo\nd) Ninguna de las anteriores",
    "19": "a) Análisis teórico\nb) Análisis empírico\nc) Análisis híbrido\nd) Análisis en tiempo real"
}

# Diccionario con las soluciones correctas para cada pregunta
solucion = {
    "1": "b) Comparar el tiempo y el espacio utilizados",
    "2": "b) A mayor tamaño de entrada, más recursos se utilizan",
    "3": "b) Empírico",
    "4": "c) Medición de tiempos reales y ajuste del modelo teórico mediante regresión",
    "5": "a) Una operación cuyo tiempo de ejecución es constante",
    "6": "a) Operación crítica",
    "7": "a) La entrada de tamaño n más costosa",
    "8": "b) La diferencia significativa entre el peor y el mejor caso",
    "9": "b) Tomar el máximo entre los tiempos de las operaciones C1 y C2",
    "10": "b) t(n) = (v(n)+1)t_B(n)+v(n)t_C(n)",
    "11": "b) t(n) = ∑(i=1, v(n)+1) t_B(i,n)+∑(i=1, v(n)) t_C(i,n)",
    "12": "b) Los tiempos reales de ejecución",
    "13": "a) t(n) = t_B(n) + ρ(B)t_{C_1}(n) + ρ(¬B)t_{C_2}(n)",
    "14": "a) Comparar los elementos del vector",
    "15": "c) t(n) = n - 1",
    "16": "a) t(n) = v(n)t_B(n) + ∑(i=1, v(n)) t_C(i,n)",
    "17": "b) Que la operación tiene un tiempo de ejecución constante",
    "18": "c) La entrada que tiene el menor costo de ejecución en términos de tiempo",
    "19": "c) Análisis híbrido"
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
        opciones_mezcladas = random.sample(opciones[clave_aleatoria].split('\n'), len(opciones[clave_aleatoria].split('\n')))
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

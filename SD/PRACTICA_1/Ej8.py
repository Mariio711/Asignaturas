"""8. Implemente la función prime(a, b) para que devuelva una lista con los
números primos en el intervalo cerrado [a, b]. Por ejemplo, la invocación
prime(2, 10) deberá devolver como resultado [2, 3, 5, 7]. Si los
parámetros a o b no son enteros o son nulos (None), se deberá generar la o
las excepciones correspondientes."""

def prime(a, b):

    flag = 0
    res = []

    if a is None or b is None or not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Alguno de los parametros no son enteros o son nulos")
    else:
        for i in range(a, b):
            for j in range(1, i+1):
                if i % j == 0 :
                    flag += 1
                
            if flag == 2  :
               res.append(i)
          
            flag = 0

    return res

lista = prime(2, 10)
print(lista)
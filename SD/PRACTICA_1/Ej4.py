"""4. Implemente la función accum(x, y, z) para que devuelva la suma de
aquellos parámetros que incluyan un número par. Por ejemplo, la
invocación accum(5, 4, 2) deberá devolver como resultado 6. Si alguno
de los tres argumentos x, y, o z no es un valor entero, se deberá generar
la excepción correspondiente.
"""
def accum(x, y, z):
    sum = 0
    for n in [x, y, z]:
        
        if not isinstance(n, int):
            raise ValueError("Todos los argumentos deben ser enteros")
    
        if n % 2 == 0 :
            sum = sum + n
        
    return sum

print ("Introduce 3 numeros pares")
x = int(input("\nx= ")) #importante el int() para que se interprete bien en la funcion
y = int(input("\ny= "))
z = int(input("\nz= "))

sum = accum(x, y, z)
print(sum)
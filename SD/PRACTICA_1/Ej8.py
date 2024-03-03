def prime(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:  # los números primos son mayores que 1
            for i in range(2, num):
                if (num % i) == 0:  # si el número es divisible por cualquier número entre 2 y sí mismo, no es primo
                    break
            else:
                primes.append(num)
    return primes
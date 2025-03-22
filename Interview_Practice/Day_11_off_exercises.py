# Día 11

# Ejercicio 51: Crea una función que verifique si un número es perfecto.
# Conceptos: Bucles, condicionales.
# Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios
# (es decir, los divisores que son menores que el propio número).
def perfect_num(n):
    aux = []
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 6:
        return "there is no perfect number smaller than 6"
    for i in range(1, n):
        if n % i == 0: # porque se usa el modulo?
            aux.append(i)
    aux_sum = sum(aux)
    if n == aux_sum:
        return f"The number {n} is a perfect number"
    return f"The number {n} is not a perfect number"
    
print(perfect_num(496))
    
# Ejercicio 52: Escribe un programa que encuentre el mínimo común múltiplo (MCM) de dos números.
# Conceptos: Matemáticas, funciones.
# MCM significa mínimo común múltiplo. El mínimo común múltiplo de dos números es el número más pequeño que es multiplo de ambos.
def MCM(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("I only accept numbers")
    result_1, result_2 = set(), set()
    for i in range(1, 10):
        aux_1, aux_2 = a * i, b * i
        result_1.add(aux_1)
        result_2.add(aux_2)
    new = result_2.intersection(result_1)
    return F"The MCM of {a} and {b} is {min(new)}"
print(MCM(8, 6))

import math
def MCM(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("I only accept numbers")
    return f"The MCM of {a} and {b} is {abs(a * b) // math.gcd(a, b)}" # que hace el abs y math.gcd?

print(MCM(8, 6))


# Ejercicio 53: Crea una función que genere la serie de Fibonacci hasta n.
# Conceptos: Recursividad, bucles.
def fibonacci(n):
    a = 0
    b = 1
    fibo = [a]
    for i in range(n):
        a, b = b, a + b
        fibo.append(b)
    return fibo
print(fibonacci(10))

# Ejercicio 54: Escribe un programa que cuente las letras en un texto.
# Conceptos: Manipulación de strings, bucles.
def letters_in_words(texto):
    if not isinstance(texto, str):
        raise TypeError("I only accept words")
    count = 0
    aux = "1234567890"
    for i in texto.replace(" ", ""): # isalpha: 
        if i in aux:
            continue
        count += 1
    return f"The amount of letters in the text is: {count}"

print(letters_in_words("eric hernandez Edwards 10 octubre"))

# Ejercicio 55: Crea una función que reciba un número y devuelva su representación en binario.
# Conceptos: Funciones, matemáticas.
# La representación binaria de un número entero positivo es una cadena de unos y ceros que representa el número en base 2.
#   0     0    0   0    0  0   0  0   0 0 0 0
#  2048 1024 512 256   128 64 32 16   8 4 2 1
#    0   0    0   0     0   1  1  0   0 1 0 0 = 100
def Binary(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 1:
        raise ValueError("The number must be greater than 0")
    covert = bin(n)
    return covert[2::]
print(Binary(100))
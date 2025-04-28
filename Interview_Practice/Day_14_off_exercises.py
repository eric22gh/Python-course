# Día 14

# Ejercicio 66: Escribe un programa que imprima los números primos del 1 al 100.
# Conceptos: Bucles, condicionales.
def prime_nums():
    for i in range(2, 101):
        prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i, end=" ")      
prime_nums()

# Ejercicio 67: Crea una función que reciba una lista y devuelva la lista ordenada.
# Conceptos: Listas, funciones.
def order_list(aux):
    if not isinstance(aux, list):
        raise TypeError("I only accept list")
    elif len(aux) == 0:
        return "the list is empty"
    return sorted(aux)
import random
print(order_list([random.randint(1, 1000) for i in range(10)]))

# Ejercicio 68: Escribe un programa que encuentre la suma de los números impares del 1 al 100.
# Conceptos: Bucles, condicionales.
def odd_numbers():
    aux = 0
    for i in range(1, 101):
        if i % 2 != 0:
            aux += i
    return aux
print(odd_numbers())

# Ejercicio 69: Crea una función que reciba un número y devuelva su raíz cuadrada.
# Conceptos: Funciones, matemáticas.
def square_root(n):
    import math
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return "I don't accept 0"
    result = math.sqrt(n)
    return f"The square root from {n} is {result:.0f}"
print(square_root(9))

# Ejercicio 70: Escribe un programa que imprima una tabla de multiplicar en formato de tabla.
# Conceptos: Bucles, impresión.
def multiply_numbers(n):
    if not isinstance(n, int):
        raise TypeError("ERROR: is not a number")
    for i, a in enumerate(range(1, 13), start=1):
        print(f"{i}- {n} x {a} = {n*a}")
multiply_numbers(7)
# Día 5

# Ejercicio 21: Escribe un programa que encuentre el índice de un elemento en una lista.
# Conceptos: Listas, bucles.
def find_index(elements, item):
    if not isinstance(elements, list):
        raise TypeError("We need a list of elements")
    if item in elements:
        index = elements.index(item)
        return f"The element {item} its located in the index {index} of the list"
    return "Element Not found"

print(find_index(["eric", 22, 21, "helen"], "hola"))

# Ejercicio 22: Crea una función que convierta una cadena a mayúsculas.
# Conceptos: Manipulación de strings, funciones.
def UPPER_string(value):
    if not isinstance(value, str):
        raise TypeError("Only string is accepted")
    return value.upper()
print(UPPER_string("helen"))

# Ejercicio 23: Escribe un programa que imprima los números pares del 1 al 50.
# Conceptos: Bucles, condicionales.
def Even_numbers():
    for num in range(1, 51):
        if num % 2 == 0:
            print(num)
Even_numbers()

# Ejercicio 24: Crea una lista de números y encuentra la suma de todos los números.
# Conceptos: Listas, funciones integradas.
def sum_list():
    import random
    new_list = [random.randint(1, 100) for num in range(8)]
    total = sum(new_list)
    return f"the sum of the list is: {total}"
print(sum_list())

# Ejercicio 25: Escribe un programa que determine si un número es primo.
# Conceptos: Condicionales, bucles.
def Prime_numbers(num):
    if not isinstance(num, int):
        raise ValueError("we only accept numbers")
    if num < 2:
        return f"The number {num} is not a prime number."
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"The number {num} is not a prime number"
    return f"The number {num} is a prime number"

print(Prime_numbers(87))
# Un número primo es un número natural mayor que 1 que solo tiene dos divisores positivos: 1 y sí mismo. En otras palabras, 
# un número primo no puede ser dividido exactamente por ningún otro número aparte de 1 y el propio número.
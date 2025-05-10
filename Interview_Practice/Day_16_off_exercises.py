# Día 16

# Ejercicio 76: Escribe un programa que cuente los caracteres en una cadena.
# Conceptos: Manipulación de strings, bucles.
def count(string):
    if not string:
        return 0
    elif not isinstance(string, str):
        raise TypeError("I need a word")
    return len(string.replace(" ",""))

print(count("eric "))

# Ejercicio 77: Crea una función que reciba dos listas y devuelva la unión.
# Conceptos: Listas, funciones.
def union(list1, list2):
    if not list1 and not list2:
        return "there are not data in lists"
    elif not isinstance(list1, list) or not isinstance(list2, list):
        return "i only accept list"
    return list1 + list2
data = [8, 5, 2,]
data1 = [89, 22, 10]
data2 = ["eric", "helen"]
data3 = ["calvin", "edwards"]
print(union(data3, data2))
print(union(data, data1))

# Ejercicio 78: Escribe un programa que encuentre el promedio de una lista de números.
# Conceptos: Listas, funciones.
def average_of_list(numbers):
    if not numbers:
        return 0
    if not isinstance(numbers, list) or not all(isinstance(i, (int, float)) for i in numbers):
        raise TypeError("I only accept with numbers")
    return sum(numbers)/len(numbers)

import random
data = [random.randint(1, 100) for i in range(8)]
print(average_of_list(data))

# Ejercicio 79: Crea una función que reciba un número y devuelva su factorial.
# Conceptos: Funciones, recursividad. 
def factorial(num):
    if not (isinstance(num, (int,float)) or num < 0):
        raise TypeError("I only accept non-negative numbers")
    elif num == 1 or num == 0:
        return 1
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result
print(factorial(5))

# Ejercicio 80: Escribe un programa que imprima los números del 1 al 100 y los múltiplos de 5.
# Conceptos: Bucles, condicionales.

def Hundred_numbers_mutiply():
    multiply = []
    for i in range(1, 101):
        print(i, end=" ")
        if i % 5 == 0:
            multiply.append(i)
    return multiply

print(Hundred_numbers_mutiply())

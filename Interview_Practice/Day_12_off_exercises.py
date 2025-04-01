# Día 12

# Ejercicio 56: Escribe un programa que determine si dos cadenas son anagramas.
# Conceptos: Manipulación de strings, condicionales.
# un anagrama es cuando 2 palabras tienen las misma letras pero diferente orden.
def Anagram(word_1, word_2):
    if not isinstance(word_1, str) or not isinstance(word_2, str):
        raise TypeError("I only accept string")
    aux_1 = sorted(word_1.replace(" ", "").lower())
    aux_2 = sorted(word_2.replace(" ", "").lower())
    if aux_1 == aux_2:
        return f"The words {aux_1} and {aux_2} are anagrams"
    return f"The words {aux_1} and {aux_2} are not anagrams"
    
print(Anagram("roma", "amor"))

# Ejercicio 57: Crea una función que encuentre el índice de un elemento en una lista.
# Conceptos: Listas, bucles.
def Index_IN_list(elements, element):
    if not isinstance(elements, list):
        raise TypeError("I need a list")
    elif element not in elements:
        return "I did not find the element in the list"
    result = elements.index(element)
    return f"the index in the list from {element} is: {result}"
print(Index_IN_list(["eric", "Helen", "edwards", 8], "Helen"))

# Ejercicio 58: Escribe un programa que encuentre el número de palabras en una frase.
# Conceptos: Manipulación de strings, funciones.
def count_pharses(aux):
    if not isinstance(aux, str):
        raise TypeError("I only accept strings")
    count = len(aux.split())
    return f"The amount of words in the phrase is. {count}"
print(count_pharses(" eric hernandez edwards  Alexander"))

# Ejercicio 59: Crea un programa que imprima la tabla de multiplicar de un número.
# Conceptos: Bucles, impresión.
def Multiply(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 1:
        return "I need a number iqual or higher than 1"
    for i in range(1, 13):
        m = n * i
        print(f"{n} x {i}: {m}")
Multiply(5)

# Ejercicio 60: Escribe un programa que genere una lista de números aleatorios y encuentre su promedio.
# Conceptos: Listas, funciones.
def average_of_list(numbers):
    if not isinstance(numbers, list):
        raise TypeError("I only accept list")
    elif not numbers:
        return "the list is empty"
    if all(isinstance(i, (int, float)) for i in numbers):
        average = sum(numbers) / len(numbers)
        return f"The average of the list is: {average:.2f}"
    return "All the elements of the list must be numbers"

import random
list_numbers = [random.randint(1, 500) for i in range(8)]
print(average_of_list(list_numbers))
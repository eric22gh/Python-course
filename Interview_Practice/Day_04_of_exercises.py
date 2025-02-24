# Día 4
# Ejercicio 16: Crea un programa que cuente las consonantes en una cadena.
# Conceptos: Manipulación de strings, bucles.
def find_consonants(word):
    if not isinstance(word, str):
        raise TypeError
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0
    for aux in word.lower():
        if aux in consonants.lower():
            count += 1
    return f"You count {count} consonants in the word: {word}"
print(find_consonants("1.2"))

# Ejercicio 17: Escribe una función que devuelva el mayor de tres números.
# Conceptos: Funciones, condicionales.
import random
def tree_numbers(num):
    if not isinstance(num, list) or len(num) != 3:
        raise ValueError("We need a list with 3 numbers")
    return max(num)
number = [random.randint(1, 100) for n in range(3)]
print(tree_numbers(number))

# Ejercicio 18: Crea un programa que imprima los números del 1 al 100, pero reemplace múltiplos de 3 por "Fizz" y múltiplos de 5 por "Buzz".
# Conceptos: Bucles, condicionales.
for n, i in enumerate(range(1, 101), start=1):
    if n % 3 == 0:
        print(f"{i}- Fizz")
    elif n % 5 == 0:
        print(f"{i}- Buzz")
    else:
        print(f"{i}- {n}")

# Ejercicio 19: Escribe un programa que imprima los elementos de una lista en orden inverso.
# Conceptos: Listas, bucles.
def invert_list(list_elements):
    if not isinstance(list_elements, list):
        raise TypeError("The element is not a list")
    elif not list_elements:
        return "the list is empty"
    else:
        return list_elements[::-1]
    
print(invert_list(["eric", 8, 20, "helen"]))

# Ejercicio 20: Crea una función que reciba una lista y devuelva su suma.
# Conceptos: Funciones, listas.
def sum_of_list(list_of_number):
    if not isinstance(list_of_number, list):
        raise TypeError
    elif not list_of_number:
        return "the list is empty"
    else:
        aux = 0
        for n in list_of_number:
            # por si hay algun elemento en la lista que no sea un numero
            if isinstance(n, (int, float)):
                aux += n
        return f"the sum from the list is: {aux}"
print(sum_of_list([56, "eric", 22, "helen", 2.5]))
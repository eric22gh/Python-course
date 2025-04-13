# Día 13

# Ejercicio 61: Crea una función que verifique si una cadena es un palíndromo.
# Conceptos: Manipulación de strings, funciones. 
# UN  palindormo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios y signos de puntuación.
def Palindrome(aux):
    import string
    if not isinstance(aux, str):
        raise TypeError("I only accept strins")
    var = aux.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    if var == var[::-1]:
        return f"The word {aux} is a palindrome"
    return f"The word {aux} is not a palindrome"
    
print(Palindrome("amo la paloma"))

# Ejercicio 62: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz".
# Conceptos: Bucles, condicionales.
def Hundred_FIZZ_BUZZ():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

Hundred_FIZZ_BUZZ()

# Ejercicio 63: Crea una función que encuentre el número de veces que aparece un elemento en una lista.
# Conceptos: Listas, bucles.
def Count_elements(aux, list_elements):
    count = 0
    for i in list_elements:
        if aux == i:
            count += 1
    return f"I count {count} times the element {aux} in the list"

data = ["eric", 88, "helen", 21, "edwards", "eric"]
print(Count_elements("eric", data))

# Ejercicio 64: Escribe un programa que calcule la suma de los números en una lista.
# Conceptos: Listas, funciones.
def Sum_list(list):
    return sum(list)

import random
data = [random.randint(5, 100) for i in range(10)]
print(Sum_list(data))

# Ejercicio 65: Crea una función que reciba dos cadenas y devuelva True si son iguales, False en caso contrario.
# Conceptos: Manipulación de strings, funciones.
def Verify_strings(string_1, string_2):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
        raise TypeError("Both inputs must be strings")
    return string_1 == string_2
print(Verify_strings("amo", "amor"))
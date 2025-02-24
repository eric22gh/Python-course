# Día 3

# Ejercicio 11: Escribe un programa que calcule el factorial de un número.
# Conceptos: Bucles, recursividad.
# El factorial de un número es la multiplicacion de todos los números enteros positivos desde 1 hasta ese número dado.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(11))

def for_factorial(n):
    if n == 0:
        return 1
    else:
        while n > 0:
            return n * for_factorial(n - 1)

print(for_factorial(11))

# Ejercicio 12: Crea una función que verifique si una palabra es un palíndromo. Conceptos: Manipulación de strings, funciones. 
# Un palíndromo es una palabra, número, frase u otra secuencia de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda
def palindrome(word):
    if not isinstance(word, str):
        return "introduce a string please"
    else:
        word_1 = word[::-1].lower().replace(" ","")
        word_2 = word.lower().replace(" ","")
        if word_1 == word_2:
            return f"the word:{word_2} is a palindrome"
        return f"the word:{word_2} is not a palindrome"
        
print(palindrome("amo la paloma"))       

# Ejercicio 13: Escribe un programa que imprima la tabla de multiplicar de un número.
# Conceptos: Bucles, impresión.
def multiply(n):
    if n == 0:
        return "It doesnt have sense multiply cero"
    for number in range(1, 13):
        print(f"{n} x {number} = {n * number}")
multiply(8)


# Ejercicio 14: Crea un programa que genere una lista de números aleatorios.
# Conceptos: Módulo random, listas.
def list_of_ramdon_numbers():
    import random
    numbers = [random.randint(1, 100) for n in range(10)]
    return numbers

print(list_of_ramdon_numbers())

# Ejercicio 15: Escribe un programa que encuentre la longitud de una cadena.
# Conceptos: Manipulación de strings, funciones integradas.
def length_string(word):
    if not isinstance(word, str):
        return "introduce a string please"
    clean = word.replace(" ","")
    return F"The length of the string is: {len(clean)}"
print(length_string("Hernan dez"))
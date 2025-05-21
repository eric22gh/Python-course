# Día 17
# Ejercicio 81: Crea una función que encuentre el máximo y mínimo en una lista.
# Conceptos: Listas, funciones.
def max_min_of_list(list1):
    if not isinstance(list1, list) or not all(isinstance(i, int) for i in list1):
        raise TypeError("I only accept a list of numbers")
    elif len(list1) == 0:
        return "the list is empty"
    for i in range(0, len(list1)):
        for j in range(0, len(list1) -i -1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
    return list1[-1], list1[0]
data = [8, 1, 89, 100, 23, 10]
print(max_min_of_list(data))
##################
# def max_min_of_list(list1):
#     if not isinstance(list1, list) or not all(isinstance(i, int) for i in list1):
#         raise TypeError("I only accept a list of numbers")
#     elif len(list1) == 0:
#         return "the list is empty"
#     max_val = max_val = list1[0]
#     min_val = list1[0]
#     for num in list1:
#         if num > max_val:
#             max_val = num
#         if num < min_val:
#             min_val = num
#     return max_val, min_val


# Ejercicio 82: Escribe un programa que imprima los números del 1 al 50 y solo los múltiplos de 3.
# Conceptos: Bucles, condicionales.
def fifty_multiply():
    for i in range(1, 51):
        if i % 3 == 0:
            print(i, end= " ")
fifty_multiply()

# Ejercicio 83: Crea una función que reciba una cadena y devuelva la cantidad de letras.
# Conceptos: Manipulación de strings, funciones.
def count_letters(words):
    if not isinstance(words, str):
        raise TypeError("I only accept words")
    elif words is None:
        return 0
    import re
    aux = re.sub(r"[\s\W\d]", "", words)
    return f"I count: {len(aux)} letters"
print(count_letters("eric 8hern"))

# Ejercicio 84: Escribe un programa que encuentre el número de caracteres en una cadena.
# Conceptos: Manipulación de strings, funciones.
def count_letters(words):
    if not isinstance(words, str):
        raise TypeError("I only accept words")
    elif words is None:
        return 0
    return f"I count: {len(words)} letters"
print(count_letters("eric 8hern"))

# Ejercicio 85: Crea una función que reciba dos números y devuelva su máximo común divisor (MCD).
# Conceptos: Matemáticas, funciones.
# el mcd de 2 numeros es el mayor numero en el cual se dividen estos numeros sin dejar residuos.
# se soluciona facilmente con el algoritmo de euclides
def MCD(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("I only accept numbers")
    elif a < 0 or b < 0:
        raise ValueError("I dont accept negative numbers")
    while b:
        a, b = b, a % b
    return a
print(MCD(22, 32))

# Día 18
# Ejercicio 86: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz".
# Conceptos: Bucles, condicionales.
def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
FizzBuzz()

# Ejercicio 87: Crea una función que encuentre el número de veces que aparece un elemento en una lista.
# Conceptos: Listas, funciones. 
def count_element(list_2, aux):
    if not isinstance(list_2, list):
        raise TypeError("I only accept list") 
    count = 0
    for i in range(len(list_2)):
        if list_2[i] == aux:
            count += 1
    return f"I count {count} times the element {aux} in the list"

data_words = ["eric", "helen", "eric", "azul", "rojo"]
print(count_element(data_words, "eric"))

# Ejercicio 88: Escribe un programa que imprima la serie de Fibonacci hasta n.
# Conceptos: Recursividad, bucles.
def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("I only accept numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b, fibo = 0, 1, []
    for i in range(n):
        a, b = b, b + a
        fibo.append(b)
    return fibo
print(fibonacci(10))

# Ejercicio 89: Crea una función que reciba una lista y devuelva la lista sin duplicados.
# Conceptos: Listas, funciones.
def list_duplicade(values):
    if not isinstance(values, list):
        raise TypeError("I need a list")
    elif not values:
        return "the list is empty"
    aux = list(set(values))
    return aux

print(list_duplicade([2, 89,20, 20, 56]))

# Ejercicio 90: Escribe un programa que determine si un número es primo.
# Conceptos: Condicionales, bucles.
def prime(n):
    if not isinstance(n, int):
        raise ValueError("I only accept numbers")
    elif n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime(18))

# Día 19
# Ejercicio 91: Crea una función que verifique si una cadena contiene solo caracteres alfabéticos.
# Conceptos: Manipulación de strings, funciones.
def verify_alphabetics(string):
    if not isinstance(string, str):
        raise TypeError("I only accept words")
    from string import ascii_letters as aph
    for aux in string:
        if aux not in aph:
            return "Not verified Correctly"
            break
    return "Successfully verified"

print(verify_alphabetics("eric8"))

# Ejercicio 92: Escribe un programa que imprima el primer carácter y el último de una cadena.
# Conceptos: Manipulación de strings, índices.
def string_characters(word):
    if not isinstance(word, str):
        raise TypeError("I only accept words")
    return word[0], word[-1]

data_w = "eric"
print(string_characters(data_w))

# Ejercicio 93: Crea una función que reciba una lista y devuelva la lista con los elementos en orden inverso.
# Conceptos: Listas, funciones.
def invert_list(aux):
    if not isinstance(aux, list):
        raise TypeError("I only accept list")
    return aux[::-1]
data_N = [8, 10, 56, 23, 10]
print(invert_list(data_N))

# Ejercicio 94: Escribe un programa que cuente cuántas veces aparece un carácter en una cadena.
# Conceptos: Manipulación de strings, bucles.
def count_strings(string):
    if not isinstance(string, str):
        raise TypeError("I need a string")
    aux = {}
    for i in string:
        if i in aux:
            aux[i] += 1
        else:
            aux[i] = 1
    return aux
print(count_strings("muercielago"))

# Ejercicio 95: Crea una función que reciba un número y devuelva su representación en hexadecimal.
# Conceptos: Funciones, matemáticas.
def convert_hexadecimal(number):
    if not isinstance(number, int):
        raise TypeError("I only accept numbers")
    elif number == 0:
        return "0x0"
    return hex(number)
print(convert_hexadecimal(-11))

# Día 20
# Ejercicio 96: Escribe un programa que imprima la tabla de multiplicar de un número hasta 10.
# Conceptos: Bucles, impresión.
def multiply(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return "It does not have sense multiply 0"
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
multiply(10)

# Ejercicio 97: Crea una función que encuentre la suma de los elementos en una lista de listas.
# Conceptos: Listas, bucles anidados.
def sum_elements(elements):
    if not isinstance(elements, list) and not all(isinstance(n, int) for n in elements):
        raise TypeError("I need a list with only numbers")
    elif not elements:
        return "the list is empty"
    elif len(elements) == 1:
        return elements[0]
    count = 0
    for i in range(0, len(elements)):
        count += elements[i]
    return count
from random import randint as rd
data_new = [rd(1, 100) for i in range(8)]
print(sum_elements(data_new))

# def sum_elements(elements):
#     if not isinstance(elements, list):
#         raise TypeError("I need a list")
#     count = 0
#     for sublist in elements:
#         if isinstance(sublist, list):
#             count += sum(sublist)
#         else:
#             count += sublist
#     return count

# Ejercicio 98: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 10.
# Conceptos: Bucles, condicionales.
def multiply_ten():
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"{i} is a multiple of 10")
        else:
            print(i)
multiply_ten()

# Ejercicio 99: Crea una función que reciba una cadena y devuelva la misma cadena en mayúsculas y minúsculas alternadas.
# Conceptos: Manipulación de strings, bucles.
def alternate_case(string):
    if not isinstance(string, str):
        raise TypeError("I only accept words")
    elif string == "":
        return "the string is empty"
    from string import ascii_letters as aph
    for i in string:
        if i not in aph:
            return f"I only accept letters, there are numbers or special characters: {i}"
            break
    return string.upper(), string.lower()
print(alternate_case("eric"))

# def alternate_case(string):
#     if not isinstance(string, str):
#         raise TypeError("I only accept words")
#     result = []
#     for i, char in enumerate(string):
#         if i % 2 == 0:
#             result.append(char.upper())
#         else:
#             result.append(char.lower())
#     return ''.join(result)


# Ejercicio 100: Escribe un programa que encuentre el promedio de una lista de números.
# Conceptos: Listas, funciones.
def average(numbers):
    if not isinstance(numbers, list) and not all(isinstance(n, int) for n in numbers):
        raise TypeError("I need a list with only numbers")
    elif not numbers:
        return "the list is empty"
    count = 0
    for i in range(0, len(numbers)):
        count += numbers[i]
    return count / len(numbers)
data_numbers = [rd(1, 100) for i in range(8)]
print(average(data_numbers))
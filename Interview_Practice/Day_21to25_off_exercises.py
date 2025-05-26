# Día 21
# Ejercicio 101: Crea una función que reciba una lista y devuelva el segundo elemento más grande.
# Conceptos: Listas, funciones.
def second(numbers):
    if not numbers:
        return "the list is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        return "I need a list with oinly numbers"
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers) -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers[-2]
print(second([25, 14, 58, 1, 500]))

# Ejercicio 102: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 4 por "Cuatro".
# Conceptos: Bucles, condicionales.
def Multiply_of_four():
    for var in range(1, 101):
        if var % 4 == 0:
            print("Cuatro")
        print(var)
Multiply_of_four()

# Ejercicio 103: Crea una función que encuentre la mediana de una lista.
# Conceptos: Listas, ordenamiento.
# La mediana de una lista es el valor que se encuentra en el centro cuando los datos están ordenados de menor a mayor, es util en 
def The_median_of_a_list(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int)for i in numbers):
        raise TypeError("I need a list with only numbers")
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers) -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] 
    aux = len(numbers) // 2 # saco la mitad
    if len(numbers) % 2 == 0:
        # even is par in spanish
        return (numbers[aux- 1] + numbers[aux]) / 2
    return numbers[aux]
    
        
import random 
data = [random.randint(1, 500) for i in range(9)]
print(The_median_of_a_list(data))

# Ejercicio 104: Escribe un programa que imprima la serie de Fibonacci hasta n, donde n es ingresado por el usuario.
# Conceptos: Recursividad, bucles.
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("I need a number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    fibo, a, b = [], 0, 1
    for i in range(0, n):
        a, b = b, b + a
        fibo.append(a)
    return fibo
print(fibonacci(10))

# Ejercicio 105: Crea una función que verifique si una lista está ordenada.
# Conceptos: Listas, bucles.
def verify_sorted(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int)for i in numbers):
        raise TypeError("I need a list with only numbers")
    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
print(verify_sorted([1, 89, 3, 4]))


# Día 22
# Ejercicio 106: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 6 como "Seis".
# Conceptos: Bucles, condicionales.
def Multiply_of_six():
    for var in range(1, 101):
        if var % 6 == 0:
            print("Seis")
        print(var)
Multiply_of_six()

# Ejercicio 107: Crea una función que reciba una lista y devuelva la lista ordenada en orden descendente.
# Conceptos: Listas, funciones.
def Descending_order(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int)for i in numbers):
        raise TypeError("I need a list with only numbers")
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers) -i -1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
print(Descending_order([25, 14, 58, 1, 500]))

# Ejercicio 108: Escribe un programa que encuentre el número de palabras en una cadena de texto.
# Conceptos: Manipulación de strings, funciones.
def count_words(string):
    if not isinstance(string, str):
        raise TypeError("I need a string")
    words = string.split()
    return len(words)
print(count_words("Hello, I am a string"))

# Ejercicio 109: Crea una función que reciba una lista de números y devuelva la suma de los números pares.
# Conceptos: Listas, bucles.
def even_sum(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I need a list with onoy numbers")
    elif not numbers:
        return 0
    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            count += numbers[i]
    return count

data_1 = [random.randint(1, 100) for x in range(10)]
print(even_sum(data_1))

# Ejercicio 110: Escribe un programa que imprima el cuadrado de los números del 1 al 10.
# Conceptos: Bucles, matemáticas.
def square_nums():
    aux = [i ** 2 for i in range(1, 11)]
    print(aux)
square_nums()


# Día 23
# Ejercicio 111: Crea una función que reciba un número y devuelva True si es un número de Armstrong.
# Conceptos: Matemáticas, funciones. 
# Un número de Armstrong o número narcisista: es un número natural de n dígitos que es igual a la suma de sus dígitos elevados a la n-ésima potencia(cantidad de digitos)
def Armstrong_Numbers(num):
    if not isinstance(num, int):
        raise TypeError("I need a number")
    cont, aux = 0, str(num)
    for i in aux:
        cont += int(i) ** len(aux)
    if cont == num:
        return True
    else:
        return False
print(Armstrong_Numbers(9474))

# Ejercicio 112: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 9 como "Nueve".
# Conceptos: Bucles, condicionales.
def Multiply_of_nine():
    for var in range(1, 101):
        if var % 9 == 0:
            print("Nueve")
        print(var)
Multiply_of_nine()

# Ejercicio 113: Crea una función que encuentre la suma de los dígitos de un número.
# Conceptos: Manipulación de strings, funciones.
def sum_digits(num):
    if not isinstance(num, int):
        raise TypeError("I need a number")
    num = str(num)
    cont = 0
    for i in num:
        cont += int(i)
    return cont
print(sum_digits(12345))

# Ejercicio 114: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 12 por "Docena".
# Conceptos: Bucles, condicionales.
def Multiply_of_twelve():
    for var in range(1, 101):
        if var % 12 == 0:
            print("Docena")
        print(var)
Multiply_of_twelve()

# Ejercicio 115: Crea una función que reciba una lista y devuelva el número de elementos únicos.
# Conceptos: Listas, funciones.
def unique_elements(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I need a list with only numbers")
    unique = set(numbers)
    return len(unique)
print(unique_elements([1, 2, 3, 4, 5, 1, 2, 3]))



# Día 24
# Ejercicio 116: Escribe un programa que imprima todos los números del 1 al 100 que son divisibles por 3 y 5.
# Conceptos: Bucles, condicionales.
def Multiply_of_three_and_five():
    for var in range(1, 101):
        if var % 3 == 0 and var % 5 == 0:
            print(var)
Multiply_of_three_and_five()

# Ejercicio 117: Crea una función que reciba una cadena y devuelva la cantidad de consonantes.
# Conceptos: Manipulación de strings, bucles.
def consonants(string):
    if not isinstance(string, str):
        raise TypeError("I only accept phrases")
    cons = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    aux = 0
    for i in string:
        if i in cons:
            aux += 1
    return f"the amount of consonats in the phrase is: {aux}"
print(consonants("murcielago"))

# Ejercicio 118: Escribe un programa que imprima una lista de números en orden inverso.
# Conceptos: Listas, bucles.
def invert_sort(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I need a list with only numbers")
    elif not numbers:
        return 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers) -i -1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
data_2 = [random.randint(1, 10000) for i in range(20)] # reacciona lento con 10000 datos y con 100mil no puede, limite 5mil
print(invert_sort(data_2))

# Ejercicio 119: Crea una función que encuentre el producto de todos los elementos en una lista.
# Conceptos: Listas, funciones.
import math
def product(numbers):
    return math.prod(numbers)
data_3 = [random.randint(1, 8) for i in range(5)]
print(product(data_3))

# Ejercicio 120: Escribe un programa que imprima un triángulo de asteriscos de altura n.
# Conceptos: Bucles, impresión.
def triangule(n):
    if not isinstance(n, int):
        raise TypeError("I only accept a num")
    for i in range(1, n + 1):
        space = " " * (n - i)
        aux = "*" * (2 * i - 1)
        print(space + aux)
triangule(10)


# Día 25
# Ejercicio 121: Crea una función que verifique si una cadena es un pangrama (contiene todas las letras del alfabeto).
# Conceptos: Manipulación de strings, funciones.
def Pangrama(Phrase):
    import string
    if not Phrase:
        return "The space is empty"
    elif not isinstance(Phrase, str):
        raise TypeError("ERROR: I ONLY ACCEPT WORDS")
    aux, count = string.ascii_lowercase, set()
    for x in Phrase.lower():
        if x in aux:
            count.add(x)
    return len(count) == 26 

print(Pangrama("Benjamín pidió una bebida de kiwi y fresa por favor y gracias ¡exquisita elección señor Heinz"))
print(Pangrama("Benjamín pidió una bebida de kiwi y fresa"))


# Ejercicio 122: Escribe un programa que imprima los primeros n números de la serie de Fibonacci.
# Conceptos: Bucles, recursividad.
def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("I need a positive integer")
    fibo, a, b = [], 0, 1
    for i in range(0, n):
        a, b = b, b + a
        fibo.append(a)
    return fibo
print(fibonacci(10))

# Ejercicio 123: Crea una función que reciba dos listas y devuelva los elementos comunes.
# Conceptos: Listas, funciones.
def common_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("I need two lists")
    common = set(list1) & set(list2)
    return list(common)
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

# Ejercicio 124: Escribe un programa que cuente las palabras en una frase ingresada por el usuario.
# Conceptos: Manipulación de strings, funciones.
def count_words(phrase):
    if not isinstance(phrase, str):
        raise TypeError("I need a string")
    words = phrase.split()
    return len(words)
print(count_words("Hello, I am a string with several words"))

# Ejercicio 125: Crea una función que reciba una lista y devuelva la lista sin elementos duplicados.
# Conceptos: Listas, funciones.
def remove_duplicates(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I need a list with only numbers")
    return list(set(numbers))
print(remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3]))
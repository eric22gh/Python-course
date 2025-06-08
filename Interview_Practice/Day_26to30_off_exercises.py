# Día 26

# Ejercicio 126: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 15 como "FizzBuzz".
# Conceptos: Bucles, condicionales.
def Multiply_of_15():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)
            
Multiply_of_15()

# Ejercicio 127: Crea una función que encuentre el índice del primer elemento mayor que un valor dado en una lista.
# Conceptos: Listas, bucles.
def Firts_Index(numbers, value):
    if len(numbers) == 0 and not value:
        return "ERROR: I EXPECTED TWO ITEMS AND I GOT ONE OR NONE"
    elif not all(isinstance(n, int) for n in numbers) or not isinstance(value, int):
        raise TypeError("I ONLY ACCEPT NUMBERS")
    for i in range(0, len(numbers)):
        if numbers[i] > value:
            return f"Index: {i}" 
            break
print(Firts_Index([1, 5, 10, 200, 300, 9], 101))

# Ejercicio 128: Escribe un programa que imprima el reverso de una lista.
# Conceptos: Listas, bucles.
def reverse_list(numbers):
    if len(numbers) == 0:
        print("THE LIST IS EMPTY")
    print(numbers[::-1])
    
reverse_list([1, 5, 10, 200, "eric", 300, 9])

# Ejercicio 129: Crea una función que reciba una cadena y devuelva el número de caracteres únicos.
# Conceptos: Manipulación de strings, funciones.
def Unique_Characters(string):
    if string == None:
        return "I did not recive no word"
    elif not isinstance(string, str):
        raise TypeError("I only accept words")
    aux = [i for i in string]
    return len(set(aux))
print(Unique_Characters("moon"))

# Ejercicio 130: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n.
# Conceptos: Bucles, impresión.
def Square(n):
    if not isinstance(n, int):
        raise TypeError("I only accept a num")
    for i in range(1, n + 1 ):
        space = " " * (n - 1)
        aux = "*" * (3 * n -1)
        print(space + aux)
Square(6)
    


# Día 27
# Ejercicio 131: Crea una función que verifique si un número es un cuadrado perfecto.
# Conceptos: Matemáticas, funciones.
# Un número es un cuadrado perfecto cuando puede expresarse como el cuadrado de un número entero, 
# es decir sin numeros mas que el 0 despues del punto.
def Perfect_square(n):
    import math
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    aux = math.sqrt(n)
    return aux.is_integer()
    # print(36 ** 0.5)
    
print(Perfect_square(36))

# Ejercicio 132: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 7 por "Siete".
# Conceptos: Bucles, condicionales.
def Replace_7():
    for i in range(1, 101):
        if i % 7 == 0:
            print("Siete")
        else:
            print(i)
Replace_7()

# Ejercicio 133: Crea una función que reciba una lista y devuelva la lista ordenada alfabéticamente.
# Conceptos: Listas, funciones.
def Alphabetic_Sort2(elements):
    if len(elements) == 0:
        return "The list is empty"
    elif not all(isinstance(i, str) for i in elements):
        raise TypeError("I only accept strings")
    for i in range(0, len(elements)):
        for j in range(0, len(elements) -i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements

print(Alphabetic_Sort2(["eric", "Helen", "Alvarez", "Carro", "Zoe", "Ariana", "Beto", "Cecilia", "Diana"]))


# Ejercicio 134: Escribe un programa que cuente el número de letras mayúsculas en una cadena.
# Conceptos: Manipulación de strings, bucles.
def Mayuzcula_count(strings):
    from string import ascii_uppercase as Ml
    if not isinstance(strings, str):
        raise TypeError("I only accept words")
    count = 0
    for i in strings:
        if i in Ml:
            count += 1
    return count

print(Mayuzcula_count("MoOnL"))

# Ejercicio 135: Crea una función que encuentre el máximo y mínimo de una lista.
# Conceptos: Listas, funciones.
def Max_MIn(elements):
    for i in range(0, len(elements)):
        for j in range(0, len(elements) -i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements[-1], elements[0]
print(Max_MIn([8, 5, 22, 563, 45, 2, 33, 74, 1]))



# Día 28
# Ejercicio 136: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 8 como "Ocho".
# Conceptos: Bucles, condicionales.
def Replace_8():
    for i in range(1, 101):
        if i % 8 == 0:
            print("Ocho")
        else:
            print(i)
            
Replace_8()

# Ejercicio 137: Crea una función que reciba una cadena y devuelva el número de palabras que comienzan con una vocal.
# Conceptos: Manipulación de strings, funciones.
def vowel_words(list_words):
    if len(list_words) == None:
        return "The list is empty"
    elif not all(isinstance(x, str) for x in list_words):
        raise TypeError("I only accept words in the list")
    elif not isinstance(list_words, list):
        raise TypeError("I only accept a list")
    Total = 0
    vowel = "aeiou"
    for i in range(0, len(list_words)):
        if list_words[i][0].lower() in vowel:
            Total += 1
    return Total
print(vowel_words(["aire", "perdigon", "ira", "uva"]))

# Ejercicio 138: Escribe un programa que imprima la suma de los números del 1 al 100.
# Conceptos: Bucles, suma.
def Sum_1_to_100():
    total = 0
    for i in range(1, 101):
        total += i
    return total

print(Sum_1_to_100())

# Ejercicio 139: Crea una función que reciba una lista y devuelva el elemento más frecuente.
# Conceptos: Listas, funciones.
def common_element(list_elemente):
    if len(list_elemente) == 0:
        return "The list is empty"
    elif not isinstance(list_elemente, list):
        raise TypeError("I only accept a list")
    aux = {}
    for element in list_elemente:
        if element in aux:
            aux[element] += 1
        else:
            aux[element] = 1
    # max_clave = None
    # max_valor = float('-inf')
    # for key, value in aux.items():
    #     if value > max_valor:
    #         max_clave, max_valor = key, value
    max_clave, max_valor = max(aux.items(), key=lambda item: item[1])
    print(f"The element with the higher frecuentcy is: {max_clave}, with: {max_valor}")

common_element(["arma", "uva", "rosa", "arma"])

# Ejercicio 140: Escribe un programa que imprima una pirámide de números.
# Conceptos: Bucles, impresión.
def triangule_numbers(n):
    for i in range(0, n + 1):
        space = "  " * (n - 1)
        nums = str(i) * (1 * i)
        print(space + nums)
triangule_numbers(9)


# Día 29
# Ejercicio 141: Crea una función que encuentre el primer carácter no repetido en una cadena.
# Conceptos: Manipulación de strings, bucles.
def Firt_character(string):
    if string == None:
        return "empty space"
    elif not isinstance(string, str):
        raise TypeError("I only accept strings")
    aux = []
    for i in  string:
        if i in aux:
            return f"The firt repeated character is: {i}"
            break
        aux.append(i)
print(Firt_character("arancar"))
            

# Ejercicio 142: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 2 por "Dos".
# Conceptos: Bucles, condicionales.
def Replace_2():
    for i in range(1, 101):
        if i % 2 == 0:
            print("Dos")
        else:
            print(i)
            
Replace_2()

# Ejercicio 143: Crea una función que reciba una lista y devuelva la suma de los elementos en posiciones pares.
# Conceptos: Listas, funciones.
def sum_of_Even_positions(numbers):
    if len(numbers) == 0:
        return "The list is empty"
    elif not isinstance(numbers, list):
        raise TypeError("I only accept a list")
    count = 0
    for i in range(0, len(numbers)):
        if i % 2 ==0:
            count += numbers[i]
    return count
print(sum_of_Even_positions([100, 2, 4, 8, 1]))

# Ejercicio 144: Escribe un programa que cuente las vocales en una cadena ingresada por el usuario.
# Conceptos: Manipulación de strings, funciones.
# def Vowels_count(string):
#     if len(string) == 0:
#         return "The string is empty"
#     elif not isinstance(string, str):
#         raise TypeError("I only accept a string")
#     elif not string.isalpha(): # isalpha(): Returns True if all characters in the string are alphabetic
#         raise TypeError("I only accept alphabetical words")
#     count = 0
#     for i in string:
#         if i in "aeiouAEIOU":
#             count += 1
#     return count

# print(Vowels_count(str(input("Write a word: "))))

# Ejercicio 145: Crea una función que reciba un número y devuelva su representación en formato binario.
# Conceptos: Matemáticas, funciones.
def Binary(number):
    if not isinstance(number, int):
        raise TypeError("I only accept integers")
    if number < 0:
        raise ValueError("The number must be greater than 0")
    elif not number:
        return "0"
    return bin(number)[2:]  # Retorna la representación binaria sin el prefijo '0b'

print(Binary(10))



# Día 30
# Ejercicio 146: Escribe un programa que imprima la tabla de multiplicar de un número ingresado por el usuario.
# Conceptos: Bucles, impresión.
# def Multiplication_table(number):
#     if not isinstance(number, int):
#         raise TypeError("I only accept integers")
#     elif number < 0:
#         raise ValueError("The number must be greater than 0")
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")
        
# Multiplication_table(int(input("Enter a number: ")))


# Ejercicio 147: Crea una función que encuentre el número de palabras en una frase que tienen más de 3 letras.
# Conceptos: Manipulación de strings, funciones.
def Three_Or_more_words(Pharse):
    aux, count = Pharse.split(), 0
    if len(aux) == 0:
        return "Empty"
    elif not isinstance(Pharse, str):
        raise TypeError("I only accept words")
    for i in range(0, len(aux)):
        if len(aux[i]) > 3:
            count += 1
    return f"You have: {count} words that have 3 or more letters"
        
print(Three_Or_more_words("Hello my name is eric and hate you"))

# Ejercicio 148: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 11 por "Once".
# Conceptos: Bucles, condicionales.
def Replace_11():
    for i in range(1, 101):
        if i % 11 == 0:
            print("Once")
        else:
            print(i)
Replace_11()

# Ejercicio 149: Crea una función que reciba una lista y devuelva la lista con los elementos duplicados eliminados.
# Conceptos: Listas, funciones.
def Erase_Duplicades_From_List(elements):
    if len(elements) == 0:
        return "The list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    return list(set(elements))

print(Erase_Duplicades_From_List([89, "eric", 89, 1, 22, "helen", "eric"]))

# Ejercicio 150: Escribe un programa que imprima un triángulo de asteriscos invertido.
# Conceptos: Bucles, impresión.
def Invert_triangule(n):
    if n == None:
        return "The space us empty"
    elif not isinstance(n, int):
        raise TypeError("I only accept numbers")
    # for i in range(n, 0, -1):
    #     print(" " * (n - i) + "*" * i)
    aux = n 
    for i in range(0, n + 1):
        point = "*" * (aux)
        space = " " * (n)
        aux -= 1
        print(space + point)
Invert_triangule(5)
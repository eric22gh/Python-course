# Día 36

# Ejercicio 176: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 19 como "Diecinueve".
# Conceptos: Bucles, condicionales.
def Diecinueve():
    for i in range(1, 101):
        if i % 19 == 0:
            print("Diecinueve")
        print(i)
Diecinueve()

# Ejercicio 177: Crea una función que reciba una cadena y devuelva el número de palabras que terminan en 's'.
# Conceptos: Manipulación de strings, funciones.
def WordWithS(words):
    aux = words.split()
    lux = 0
    for i in aux:
        if i[-1].lower() == "s":
            lux += 1
    if lux == 0:
        return "There are no words that end with 's'"
    return lux
print(WordWithS("hola me gustas mucho marcoS"))
            

# Ejercicio 178: Escribe un programa que imprima el cuadrado de los números del 1 al 20.
# Conceptos: Bucles, matemáticas.
def NumSquare():
    return [x ** 2 for x in range(1, 21)]
print(NumSquare())

# Ejercicio 179: Crea una función que reciba una lista y devuelva la suma de los elementos en posiciones impares.
# Conceptos: Listas, funciones.
def OddSums(list):
    aux = 0
    for i in range(0, len(list)):
        if list[i] % 2 != 0:
            aux += list[i]
    return aux
print(OddSums([5, 6, 10, 89, 45, 100, 6, 22, 30, 10]))
            

# Ejercicio 180: Escribe un programa que imprima una pirámide de asteriscos de altura n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def PrintPyramid(n):
    for i in range(1, n + 1):
        Space = ' ' * (n - i)
        Asterisks = '*' * (2 * i - 1)
        print(Space + Asterisks)
PrintPyramid(n = int(input("Ingrese la altura de la pirámide: ")))



# Día 37
# Ejercicio 181: Crea una función que verifique si una cadena es un palindrome ignorando espacios y mayúsculas.
# Conceptos: Manipulación de strings, funciones.
# Palindrome es una palabra que se lee igual al derecho y al revez
def Palindrome(word):
    if not word:
        return "the word is empty"
    elif not isinstance(word, str):
        raise TypeError("I only accept text")
    aux = word.replace(" ", "")
    return aux.lower() == aux[::-1].lower()
print(Palindrome("Amo la paloma"))

# Ejercicio 182: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 20 por "Veinte".
# Conceptos: Bucles, condicionales.
def MultiplyOffTwenty():
    for i in range(1, 101):
        if i % 20 == 0:
            print(f"{i}- Veinte")
            continue
        print(i)
MultiplyOffTwenty()

# Ejercicio 183: Crea una función que encuentre la suma de los elementos en una lista de listas.
# Conceptos: Listas, bucles anidados.
def SumListOfLists(elements):
    if not elements:
        return "The list of lists are empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept lists")
    aux = 0
    for Lists in elements:
        for list1 in Lists:
            aux += list1
    return f"The sum of elements is {aux}"
data = [
    [1, 2, 5],
    [1, 20, 50],
    [1, 200, 500]
]
print(SumListOfLists(data))            

# Ejercicio 184: Escribe un programa que cuente cuántas letras hay en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CountLetters(string):
    if not string:
        return "The string is empty"
    elif not isinstance(string, str):
        raise TypeError("I only accept text")
    aux = 0
    for i in string:
        if i.isalpha(): # Check if the character is a letter
            aux += 1
    return f"The number of letters in the string is {aux}"
print(CountLetters("Hola, ¿cómo estás?")) 

# Ejercicio 185: Crea una función que reciba un número y devuelva True si es un número perfecto.
# Conceptos: Matemáticas, funciones. 
# Un número perfecto es un número entero positivo que es igual a la suma de sus divisores positivos, excluyendo el propio número.
def PerfectNum(n):
    if not n:
        return "the num is empty"
    elif not isinstance(n, int):
        raise TypeError("I only accept number")
    elif n < 1:
        return "I only accept positive nums"
    aux = 0
    for i in range(1, n + 1):
        if i < n:
            if n % i == 0:
                aux += i
    return aux == n
print(PerfectNum(28))



# Día 38
# Ejercicio 186: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 21 como "Veintiuno"
# Conceptos: Bucles, condicionales.
def MultiplyOfTwentyOne():
    for i in range(1, 101):
        if i % 21 == 0:
            print(f"{i}- Veintiuno")
            continue
        print(i)
MultiplyOfTwentyOne()

# Ejercicio 187: Crea una función que reciba una lista y devuelva el promedio de los números.
# Conceptos: Listas, funciones.
def Averague(elements):
    return sum(elements) / len(elements) if elements else 0
print(Averague([52, 56, 45, 1, 100, 89]))

# Ejercicio 188: Escribe un programa que imprima la suma de los números del 1 al 100 que son múltiplos de 5.
# Conceptos: Bucles, matemáticas.
def SumOfMultiplesOfFive():
    aux = 0
    for i in range(1, 101):
        if i % 5 == 0:
            aux += i
    return aux
print(SumOfMultiplesOfFive())

# Ejercicio 189: Crea una función que reciba una cadena y devuelva la misma cadena sin consonantes.
# Conceptos: Manipulación de strings, funciones.
def RemoveConsonants(string):
    if not string:
        return "The string is empty"
    elif not isinstance(string, str):
        raise TypeError("I only accept text")
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char in vowels])
print(RemoveConsonants("Hola, ¿cómo estás?"))

# Ejercicio 190: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def SquareAsterisk(n):
    for i in range(0, n):
        space = " " * n
        asterisk = "*" * n 
        print(space + asterisk)
SquareAsterisk(4)



# Día 39
# Ejercicio 191: Crea una función que verifique si dos cadenas son anagramas.
# Conceptos: Manipulación de strings, funciones.
# Un anagrama es cuando dos palabras o frases se reorganizando sus letras y siguen iguales iguales.
def Anagram(word1, word2):
    if not word1 or not word2:
        return "One or both words are empty"
    elif  not (word1.isalpha() and word2.isalpha()):
        return "One or both off the words have a special character, I can not accept it"
    else:
        return sorted(word1.lower()) == sorted(word2.lower())
print(Anagram("riesgo","sergio"))

# Ejercicio 192: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 22 por "Veintidós".
# Conceptos: Bucles, condicionales.
def MultiplyOfTwentyTwo():
    for i in range(1, 101):
        if i % 22 == 0:
            print(f"{i}- Veintidós")
            continue
        print(i)
MultiplyOfTwentyTwo()

# Ejercicio 193: Crea una función que encuentre el número de elementos en una lista que son menores que un valor dado.
# Conceptos: Listas, funciones.
def SmallerThanValue(elements, Value):
    if not elements:
        return "The list is empty"
    elif not Value:
        return "the value is empty"
    aux = 0
    for i in range(0, len(elements)):
        if elements[i] < Value:
            aux+= 1
    return f"The amount of elements smaller than {Value} is: {aux}"
print(SmallerThanValue([56, 2, 4, 100, 8, 1], 5))

def SmallerThanValue(elements, Value):
    if not elements:
        return "The list is empty"
    
    count = sum(1 for x in elements if x < Value)
    return f"The amount of elements smaller than {Value} is: {count}"
print(SmallerThanValue([56, 2, 4, 100, 8, 1], 5))


# Ejercicio 194: Escribe un programa que cuente cuántas vocales hay en una cadena ingresada por el usuario.
# Conceptos: Manipulación de strings, funciones.
def CountVowels(Phrase):
    vowels = "aeiou"
    aux = 0
    for i in range(0, len(Phrase)):
        if Phrase[i].lower() in vowels:
            aux += 1
    return aux
print(CountVowels("muercielago"))

# Ejercicio 195: Crea una función que reciba un número y devuelva su representación en formato octal.
# Conceptos: Matemáticas, funciones.
# octal es un sistema de numeración en base 8, usa dígitos del 0 al 7. Es utilizado en programación y permisos Unix/Linux y también para trabajar con potencias de 2.
def OctalNum(n):
    if not n:
        return "the number is empty"
    elif n <= 0:
        return "I only accept positive numbers"
    return oct(n)
print(OctalNum(8))


# Día 40
# Ejercicio 196: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 23 como "Veintitrés".
# Conceptos: Bucles, condicionales.
def MultiplyOfTwentyThree():
    for i in range(1, 101):
        if i % 23 == 0:
            print(f"{i}- Veintitrés")
            continue
        print(i)
MultiplyOfTwentyThree() 

# Ejercicio 197: Crea una función que reciba una cadena y devuelva el número de caracteres alfabéticos.
# Conceptos: Manipulación de strings, funciones.
def CountAlphabeticChars(string):
    if not string:
        return "The string is empty"
    elif not isinstance(string, str):
        raise TypeError("I only accept text")
    aux = 0
    for i in string:
        if i.isalpha():  # Check if the character is a letter
            aux += 1
    return f"The number of alphabetic characters in the string is {aux}"
print(CountAlphabeticChars("Hola, ¿cómo estás?"))

# Ejercicio 198: Escribe un programa que imprima la suma de los números del 1 al 100 que son múltiplos de 3.
# Conceptos: Bucles, matemáticas.
def SumOfMultiplesOfThree():
    aux = 0
    for i in range(1, 101):
        if i % 3 == 0:
            aux += i
    return aux
print(SumOfMultiplesOfThree())

# Ejercicio 199: Crea una función que reciba una lista y devuelva la lista con los elementos en orden aleatorio.
# Conceptos: Listas, funciones.
import random
def RandomOrder(elements):
    if not elements:
        return "The list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept lists")
    random.shuffle(elements) # Shuffle mezcla los elementos de una lista, modifica la lista original.
    return elements

print(RandomOrder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Ejercicio 200: Escribe un programa que imprima un triángulo de números donde cada fila contenga el número de la fila.
# Conceptos: Bucles, impresión.
def NumberTriangle(n):
    for i in range(1, n + 1):
        space = ' ' * (n - i)
        numbers = ' '.join(str(i) for _ in range(i))
        print(space + numbers)
NumberTriangle(8)
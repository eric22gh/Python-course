# Día 46

# Ejercicio 226: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 29 por "Veintinueve".
# Conceptos: Bucles, condicionales.
def MultiplyTwentyNine():
    for num in range(1, 101):
        if num % 29 == 0:
            print("Veintinueve")
        print(num)
MultiplyTwentyNine()

# Ejercicio 227: Crea una función que encuentre la cantidad de palabras que comienzan con una consonante en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CountOfCosonants(Phrase):
    consonant = "aeuiouAEUIOU"
    auc = 0
    for word in Phrase.split():
        if word[0] not in consonant:
            auc += 1
    return auc
print(CountOfCosonants("Hello, my name is Eric"))

# Ejercicio 228: Escribe un programa que imprima la suma de los números del 1 al 100 que son múltiplos de 7.
# Conceptos: Bucles, matemáticas.
def SumOFSevenMultiply():
    aux = 0
    for num in range(1, 101):
        if num % 7 == 0:
            aux += num
    return aux
print(SumOFSevenMultiply())

# Ejercicio 229: Crea una función que reciba una cadena y devuelva la misma cadena sin espacios.
# Conceptos: Manipulación de strings, funciones.
def ReplaceSpace(Phrase):
    return Phrase.replace(" ", "")
print(ReplaceSpace("Hell o, E ric Hernande z"))

# Ejercicio 230: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def Square(n):
    for i in range(0, n - 1):
        space = " " * n
        astericks = "*" * n
        print(space +  astericks)
Square(5)


# Día 47
# Ejercicio 231: Crea una función que verifique si un número es un número de Kaprekar (el cuadrado del número se puede dividir en dos partes que suman el número).
# Conceptos: Matemáticas, funciones.
# un número de Kaprekarque al ser elevado al cuadrado puede dividirse en dos partes cuya suma da como resultado el mismo número original
def KaprekarNum(Num):
    if Num < 1:
        raise ValueError("The number must be greater than 0")
    aux1 = str(Num ** 2) # numero elevado, se convierte en string para que sea manejable con slashing
    aux2 = int(len(aux1) / 2)# se saca la mitad de el digito, para que sea escalable
    if int(aux1[:aux2]) + int(aux1[aux2:]) == Num: # con la mitad de el digito se hace manipulacion de strings y ala vez se covierten en numeros para que se sumen y comparen
        return f"{Num} is a Kaprekar"
    return f"{Num} is not a Kaprekar"
print(KaprekarNum(999))

# Ejercicio 233: Crea una función que reciba una lista y devuelva el número de elementos que son mayores que un valor dado.
# Conceptos: Listas, funciones.
def GreaterThanNum(List, Num):
    return len([x for x in List if x > Num])
print(GreaterThanNum([1, 2, 3, 4, 5], 3))

# Ejercicio 234: Escribe un programa que cuente cuántas letras hay en una cadena ingresada por el usuario, excluyendo espacios.
# Conceptos: Manipulación de strings, funciones.
def CountLetters(Phrase):
    return len([letter for letter in Phrase.replace(" ", "")])
print(CountLetters("M y na me is Eri c Edw ard s"))

# Ejercicio 235: Crea una función que reciba un número y devuelva su representación en formato binario.
# Conceptos: Matemáticas, funciones.
def BinaryNumber(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    return bin(n)
print(BinaryNumber(5))


# Día 48
# Ejercicio 237: Crea una función que encuentre el número de palabras que terminan en 'a' en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CountEndLetters(Phrase):
    cleaned = Phrase.replace(".","").replace(",","").lower()
    return len([x for x in cleaned.split() if x[-1] == "a"])
print(CountEndLetters("hello, my name is Erica ArayA "))

# Ejercicio 238: Escribe un programa que imprima la suma de los números del 1 al 100 que son múltiplos de 8.
# Conceptos: Bucles, matemáticas.
def SumMultiplyOfeighty():
    return sum([x for x in range(1, 101) if x % 8 == 0])
print(SumMultiplyOfeighty())

# Ejercicio 239: Crea una función que reciba una cadena y devuelva la misma cadena sin vocales.
# Conceptos: Manipulación de strings, funciones.
def WithOutvowels(Phrase):
    vowels = "aeiouAEIOU"
    return "".join([ l for l in Phrase if l not in vowels])
print(WithOutvowels("Hello moto"))

# Ejercicio 240: Escribe un programa que imprima un triángulo de números donde cada fila contenga el número de la fila.
# Conceptos: Bucles, impresión.
def TrianguleOfNumbers(n):
    for x in range(1, n + 1):
        space = " " * (n)
        numbers = str(x) * (x)
        print(space +  numbers)
TrianguleOfNumbers(5)


# Día 49
# Ejercicio 241: Crea una función que verifique si un número es un número de Smith.
# Conceptos: Matemáticas, funciones.
#Un número de Smith es un número compuesto (no primo) que tiene una propiedad curiosa: la suma de sus dígitos es igual a la suma de los dígitos de sus factores primos,
def SmithNumber(n):
    import math
    if n <= 1:
        return False
    for a in range(2, math.isqrt(n) + 1):
        if n % a == 0:
            sumDigits = sum([int(i) for i in str(n)])
            factores = []
            divide = 2 # no se puede dividir un numero en 1
            while n > 1: # n va a bajar
                while n % divide == 0:
                    factores.append(divide)
                    n //= divide # aqui se actualiza el valor de n
                divide += 1
            if sumDigits == sum(factores):
                return "This is a smith number"
            else:
                return "It is not a smith number"
    return "the number is a prime number so is not a smith number"

print(SmithNumber(378))

# Ejercicio 243: Crea una función que reciba una lista y devuelva el número de elementos que son negativos.
# Conceptos: Listas, funciones.
def CounthNegativeNumbers(numbers):
    return len([i for i in numbers if i < 0])
print(CounthNegativeNumbers([-1, 22, -10, -100]))

# Ejercicio 244: Escribe un programa que cuente cuántas palabras hay en una frase ingresada por el usuario, excluyendo signos de puntuación.
# Conceptos: Manipulación de strings, funciones.
def CountWords(Phrase):
    import string
    cleaned = Phrase.translate(str.maketrans("", "", string.punctuation)) # translate se usa para eliminar signos de puntuacion 
    # y str.maketrans crea una tabla de traduccion
    return len(cleaned.split())
print(CountWords("Hello, my name is Eric!"))

# Ejercicio 245: Crea una función que reciba un número y devuelva True si es un número de Narciso (un número que es igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
# Conceptos: Matemáticas, funciones.
# Un número de Narciso o tambien llamado Amstrong es un número que es igual a la suma de sus dígitos elevados a la potencia del número de dígitos.
def NarcisoNumber(n):
    if n < 0:
        raise ValueError("The number must be greater than 0")
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum(d ** power for d in digits)
print(NarcisoNumber(153)) 

# Día 50
# Ejercicio 249: Crea una función que reciba una cadena y devuelva la misma cadena sin caracteres especiales.
# Conceptos: Manipulación de strings, funciones.
def WithoutSpecialCharacters(Phrase):
    import re
    return re.sub(r'[^a-zA-Z0-9\s]', '', Phrase)  # Elimina caracteres especiales, dejando letras, números y espacios
print(WithoutSpecialCharacters("Hello, my name is Eric! @2023"))

# Ejercicio 250: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def SquareOfAsterisks(n):
    for i in range(n):
        print('*' * n)
SquareOfAsterisks(5)
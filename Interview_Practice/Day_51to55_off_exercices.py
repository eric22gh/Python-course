# Día 51
# Ejercicio 251: Crea una función que verifique si un número es un número de Lychrel (un número que no se convierte en un palíndromo tras un número determinado de iteraciones).
# Conceptos: Matemáticas, funciones.
# Un número de Lychrel es un número natural que no ha demostrado formar un palíndromo mediante el proceso reverse and add, 
# incluso después de millones de iteraciones
def VerifyLychrel(number, max = 1000):
    for _ in range(max):
        aux = int(str(number)[::-1])
        number = number + aux
        if str(number) == str(number)[::-1]:
            return False
    return True
print(VerifyLychrel(196))

# Ejercicio 253: Crea una función que reciba una lista y devuelva el número de elementos que son ceros.
# Conceptos: Listas, funciones.
def CountZero(numbers):
    aux = 0
    for i in range(0, len(numbers)):
        if numbers[i] == 0:
            aux += 1
    return aux
print(CountZero([1, 23, 0, 0]))

# Ejercicio 254: Escribe un programa que cuente cuántas palabras hay en una frase ingresada por el usuario, excluyendo números.
# Conceptos: Manipulación de strings, funciones.
def CountWords(Phrase):
    import re
    clean = re.sub("\d+", "", Phrase)
    aux = 0
    for words in clean.split():
        aux += 1
    return aux
print(CountWords(input("Introduce de Phrase: ")))

# Ejercicio 255: Crea una función que reciba un número y devuelva True si es un número de Friedman (un número que puede ser expresado como una expresión aritmética de sus dígitos).
# Conceptos: Matemáticas, funciones.
# Número de Friedman es un numero que usando sus dijitos y alguna operacion aritmeticas basicas dan como resultado el mismo numero
import itertools
import operator
operadores = ['+', '-', '*', '//', '**']
def generar_expresiones(digitos):
    expresiones = []
    # Generar todas las formas de insertar operadores entre dígitos
    for ops in itertools.product(operadores, repeat=len(digitos)-1):
        partes = []
        for i in range(len(digitos)):
            partes.append(digitos[i])
            if i < len(ops):
                partes.append(ops[i])
        expresiones.append(''.join(partes))
    return expresiones

def es_friedman(numero):
    str_num = str(numero)
    permutaciones = set(itertools.permutations(str_num))
    for perm in permutaciones:
        if perm[0] == '0':
            continue  # evitar números con ceros iniciales
        expresiones = generar_expresiones(perm)
        for expr in expresiones:
            try:
                if eval(expr) == numero and expr != str(numero):
                    print(f"✔️ {numero} = {expr}")
                    return True
            except:
                continue
    return False
print(es_friedman(25))


# Día 52

# Ejercicio 257: Crea una función que encuentre el número de palabras que comienzan con una vocal en una cadena.
# Conceptos: Manipulación de strings, funciones.
def FindWords(Phrase):
    lux, vowels, sux = 0, "aeiou", Phrase.split()
    for i in range(0, len(sux)):
        if sux[i][0].lower() in vowels:
            lux += 1
    return lux
print(FindWords("hello everyone, my name is eric hernandez Edwards, okay"))

# Ejercicio 259: Crea una función que reciba una cadena y devuelva la misma cadena sin letras en mayúscula.
# Conceptos: Manipulación de strings, funciones.
def withOutUpperletters(phrase):
    from string import ascii_uppercase as Upper
    return "".join([letter for letter in phrase if letter not in Upper])
    
print(withOutUpperletters("Hello everyone, my name is Eric hernandez Edwards"))

# Ejercicio 260: Escribe un programa que imprima un triángulo de asteriscos de altura n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def Triangule(n):
    for i in range(0, n + 1):
        space = " " * (n - i)
        ast = "*" * (2 * i - 1)
        print(space + ast)
Triangule(5)


# Día 53
# Ejercicio 261: Crea una función que verifique si un número es un número de Kaprekar (la suma de sus dígitos al cuadrado puede ser dividida en dos partes que suman el número original).
# Conceptos: Matemáticas, funciones.
# un número de Kaprekar es un número especial que, al ser elevado al cuadrado, puede dividirse en dos partes cuya suma da como resultado el mismo número original
def Kaprekar(n):
    aux = str(n ** 2)
    divide = int(len(aux)/2)
    if int(aux[:divide]) + int(aux[divide:]) == n:
        return "It is a Kaprekar number"
    return "It is not a Kaprekar number"
    
print(Kaprekar(45))

# Ejercicio 263: Crea una función que reciba una lista y devuelva el número de elementos que son primos.
# Conceptos: Listas, funciones.
def PrimeNUmber(elements):
    import math
    aux = 0
    for n in elements:
        if n <= 1:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(int(n))) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            aux += 1
    return aux
print(PrimeNUmber([3, 5, 7, 11, 13, 15, 18]))

# Ejercicio 264: Escribe un programa que cuente cuántas letras hay en una cadena ingresada por el usuario, excluyendo espacios y signos de puntuación.
# Conceptos: Manipulación de strings, funciones.
def CountLetters(Phrase):
    import re 
    cleaned = re.sub(r"[\s\W]", "", Phrase)
    return len(cleaned)
print(CountLetters("Hel lo."))

# Ejercicio 265: Crea una función que reciba un número y devuelva True si es un número de Harshad (un número que es divisible por la suma de sus dígitos).
# Conceptos: Matemáticas, funciones.
def HarshadNum(n):
    aux = 0
    for i in str(n):
        aux += int(i)
    if n % aux == 0:
        return True
    return False
print(HarshadNum(18))


# Día 54
# Ejercicio 267: Crea una función que encuentre el número de palabras que terminan en 'o' en una cadena.
# Conceptos: Manipulación de strings, funciones.
def WordsEndsWithO(Phrase):
    lux, sux = 0, Phrase.split()
    for i in range(0, len(sux)):
        if sux[i][-1].lower() == "o":
            lux += 1
    return lux
print(WordsEndsWithO("hello everyone, my name is eric hernandez Edwards, okay"))

# Ejercicio 269: Crea una función que reciba una cadena y devuelva la misma cadena sin dígitos.
# Conceptos: Manipulación de strings, funciones.
def withoutDigits(phrase):
    return "".join([letter for letter in phrase if not letter.isdigit()])
print(withoutDigits("Hello everyone, my nam89e is Eric hernandez Edwards 1234"))

# Ejercicio 270: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def Square(n):
    for i in range(0, n):
        print("*" * n)
Square(5)


# Día 55
# Ejercicio 271: Crea una función que verifique si un número es un número de Smith (un número compuesto cuya suma de dígitos es igual a la suma de los dígitos de sus factores primos).
# Conceptos: Matemáticas, funciones.
def SmithNumber(n):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    if n < 2:
        return False
    prime_factors = []
    original_sum = sum_of_digits(n)
    for i in range(2, n + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    # Sumar los dígitos de los factores primos
    factors_sum = sum(sum_of_digits(factor) for factor in prime_factors)
    return original_sum == factors_sum
print(SmithNumber(4)) 

# Ejercicio 273: Crea una función que reciba una lista y devuelva el número de elementos que son negativos.
# Conceptos: Listas, funciones.
def NegativeNums(elements):
    return len([n for n in elements if n < 0])
print(NegativeNums([-1, 22, -50, 10, 2, 30, -10]))

# Ejercicio 274: Escribe un programa que cuente cuántas palabras hay en una frase ingresada por el usuario, excluyendo signos de puntuación.
# Conceptos: Manipulación de strings, funciones.
def CountWords(Phrase):
    from string import punctuation as pn
    cleaned = "".join([ n for n in Phrase if n not in pn])
    return len(cleaned.split())
    
print(CountWords("Hello, my name. is eric."))

# Ejercicio 275: Crea una función que reciba un número y devuelva True si es un número de Narciso (un número que es igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
# Conceptos: Matemáticas, funciones.
def NarcissisticNumber(n):
    num = str(n)
    lux = len(num)
    aux = 0
    for i in num:
        aux += int(i) ** lux
    return aux == n
print(NarcissisticNumber(153))
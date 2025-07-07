# Día 41

# Ejercicio 201: Crea una función que verifique si un número es un número de Fibonacci.
# Conceptos: Matemáticas, funciones.
# un numero es fibonnaci si algunas de los resultados de las formulas se le saca la raiz y da como resultado es un numero entero
def fibonnaci(n):
    a, b, fibo = 0, 1, []
    for i in range(1, n):
        a, b = b, b + a
        fibo.append(a)
    return fibo
print(fibonnaci(10))

def If_Fibonacci(n):
    if not n:
        return "The number is empty"
    elif n < 0:
        return "I dont accept negative numbers"
    elif not isinstance(n, int):
        raise TypeError("I only accept numbers")
    else:
        import math
        aux = 5 * n ** 2 + 4 # 5n2 - 4....formulas para  ver si un numero es fibonacci
        root = math.sqrt(aux)
        if root.is_integer():
            return "It is a fibonacci number"
        return "It is not a fibonacci number"
    
print(If_Fibonacci(21))

# Ejercicio 202: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 24 por "Veinticuatro".
# Conceptos: Bucles, condicionales.
def replace_multiples_of_24():
    for i in range(1, 101):
        if i % 24 == 0:
            print("Veinticuatro")
        else:
            print(i)
replace_multiples_of_24()

# Ejercicio 203: Crea una función que encuentre el número de palabras en una frase que contienen una letra específica.
# Conceptos: Manipulación de strings, funciones.
def FindWordsWithLetter(words, letter):
    if not words or not letter:
        return "One or both of elements are empty"
    elif not isinstance(words, str) or not isinstance(letter, str):
        raise TypeError("I only accept text")
    aux = 0
    for word in words.split():
        if letter.lower() in word.lower():
            aux += 1
    return aux
        
print(FindWordsWithLetter("hola, mi nombre es eric Hernandez edwards", "a"))

# Ejercicio 204: Escribe un programa que imprima la suma de los números del 1 al 100 que son múltiplos de 4.
# Conceptos: Bucles, matemáticas.
def sum_multiples_of_4():
    total = 0
    for i in range(1, 101):
        if i % 4 == 0:
            total += i
    return total
print(sum_multiples_of_4())

# Ejercicio 205: Crea una función que reciba un número y devuelva la suma de sus dígitos.
# Conceptos: Manipulación de strings, funciones.
def SumOfDigits(n):
    aux = 0
    for i in str(n):
        aux += int(i)
    return aux
print(SumOfDigits(1005))

# Día 42
# Ejercicio 206: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 25 por "Veinticinco".
# Conceptos: Bucles, condicionales.
def replace_multiples_of_25():
    for i in range(1, 101):
        if i % 25 == 0:
            print("Veinticinco")
        else:
            print(i)
replace_multiples_of_25()

# Ejercicio 207: Crea una función que encuentre la longitud de la lista más corta en una lista de listas.
# Conceptos: Listas, funciones.
def LenghtOFListOflists(elements):
    aux = elements[0]
    for list in elements:
        if len(list) < len(aux):
            aux = list
    return len(aux)
data = [
    [89, 56, 52, 23, 12, 45, 10],
    [89, 56, 52],
    [89, 56, 52, 23, 57, 21],
    [89, 56],
    [89, 56, 52, 23, 100, 569, 22, 12]  
]
print(LenghtOFListOflists(data))

# Ejercicio 208: Escribe un programa que cuente cuántas veces aparece un carácter específico en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CountCaracters(Phrase, caracter):
    aux = 0
    for i in Phrase.split():
        if i.lower() == caracter.lower():
            aux += 1
    return aux
print(CountCaracters("hello my name is eric hernandez.... hello people","Hello"))

# Ejercicio 209: Crea una función que reciba una lista y devuelva el promedio de los números en posiciones pares.
# Conceptos: Listas, funciones.
def AverageOfEvenIndexed(numbers):
    even_index_sum = 0
    count = 0
    for i in range(len(numbers)):
        if i % 2 == 0: 
            even_index_sum += numbers[i]
            count += 1
    return even_index_sum / count if count > 0 else 0

print(AverageOfEvenIndexed([23, 56, 22, 16, 2, 4, 8, 100, 94]))
        
# Ejercicio 210: Escribe un programa que imprima un cuadrado de números, donde cada fila contenga el número de la fila.
# Conceptos: Bucles, impresión.
def print_square(n):
    for i in range(1, n + 1):
        print(" ".join(str(i) * n))
print_square(5)


# Día 43
# Ejercicio 211: Crea una función que verifique si un número es un número feliz.
# Conceptos: Matemáticas, funciones.
# Un número feliz es un número que, al sumar los cuadrados de sus dígitos repetidamente, eventualmente da como resultado 1. Si eso sucede, se dice que es “feliz”. Si no, es “infeliz”. 
def HappyNum(num):
    aux = 0
    for i in str(num):
        aux += int(i) ** 2
        if aux == 1:
            return "It is a Happy number"
        return "It is not a Happy number"
    return HappyNum(aux)   
        
print(HappyNum(42))       

def happynum2(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        aux = 0
        for i in str(num):
            aux += int(i) ** 2
        num = aux
    if num == 1:
        return "It is a Happy number"
    return "It is not a Happy number"
print(happynum2(42))
            

# Ejercicio 212: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 26 como "Veintiséis".
# Conceptos: Bucles, condicionales.
def replace_multiples_of_26():
    for i in range(1, 101):
        if i % 26 == 0:
            print("Veintiséis")
        else:
            print(i)
replace_multiples_of_26()

# Ejercicio 213: Crea una función que reciba una cadena y devuelva el número de palabras que contienen una vocal específica.
# Conceptos: Manipulación de strings, funciones.
def CountWordsWithVowel(phrase, vowel):
    if not phrase or not vowel:
        return "One or both of elements are empty"
    elif not isinstance(phrase, str) or not isinstance(vowel, str):
        raise TypeError("I only accept text")
    aux = 0
    for word in phrase.split():
        if vowel.lower() in word.lower():
            aux += 1
    return aux
print(CountWordsWithVowel("hola, mi nombre es eric Hernandez edwards", "a"))

# Ejercicio 214: Escribe un programa que cuente cuántas letras hay en una cadena ingresada por el usuario.
# Conceptos: Manipulación de strings, funciones.
def CounthLetters(Phrase):
    import string
    aux = 0
    if not Phrase:
        return "The phrase is empty"
    elif not isinstance(Phrase, str):
        raise TypeError("I only accept text")
    for letters in Phrase:
        if letters not in string.punctuation and letters != " ":
            aux += 1
    return aux 
print(CounthLetters("hola, mi nombre es eric Hernandez edwards."))

# Ejercicio 215: Crea una función que reciba un número y devuelva su representación en formato hexadecimal.
# Conceptos: Matemáticas, funciones.
def HexaDecimal(num):
    if not num:  
        return "The space is empty"
    elif not isinstance(num, int):
        raise TypeError("I Only accept numbers")
    return hex(num)
print(HexaDecimal(45))


# Día 44

# Ejercicio 217: Crea una función que encuentre el número de elementos en una lista que son divisibles por un valor dado.
# Conceptos: Listas, funciones.
def DivisibleElememnts(elements, Value):
    auc = []
    for nux in elements:
        if nux % Value == 0:
            auc.append(nux)
    return len(auc)
import random
data = [random.randint(1, 1000) for x in range(8)]
print(DivisibleElememnts(data, 22))

# Ejercicio 219: Crea una función que reciba una cadena y devuelva la misma cadena sin números.
# Conceptos: Manipulación de strings, funciones.
def ReplaceNumbers(Phrase):
    nums = "1234567890"
    aux = "".join( lux for lux in Phrase if lux not in nums)
    return aux
print(ReplaceNumbers("hola10 eric"))

# Ejercicio 220: Escribe un programa que imprima un triángulo invertido de asteriscos de altura n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def Triangule(n):
    for i in range(0, n + 1):
        space = " " * (n + i)
        nums = "*" * (n - i)
        print(space + nums)
Triangule(5)

# Día 45
# Ejercicio 221: Crea una función que verifique si un número es un número de Harshad (divisible por la suma de sus dígitos).
# Conceptos: Matemáticas, funciones. 
# Un número de Harshad (o número de Niven) es un número entero que es divisible por la suma de sus dígitos
def HarshadNumber(Harshad):
    aux = 0
    for i in str(Harshad):
        aux += int(i)
    return "It is a harshad num" if Harshad % aux == 0 else "It is not a harshad number"
print(HarshadNumber(27))


# Ejercicio 223: Crea una función que reciba una lista y devuelva el número de elementos que son pares.
# Conceptos: Listas, funciones.
def EvenNumber(elements):
    aux = []
    for num in elements:
        if  num % 2 == 0:
            aux.append(num)
    return len(aux)
datas = [random.randint(1, 1500) for x in range(20)]
print(EvenNumber(datas))


# Ejercicio 225: Crea una función que reciba un número y devuelva True si es un número abundante (la suma de sus divisores propios es mayor que el número).
# Conceptos: Matemáticas, funciones.
# Un número abundante es un número entero positivo cuya suma de sus divisores propios (es decir, todos los divisores excepto él mismo) es mayor que el número en sí
def AbundantNumber(n):
    aux, num  = 0, 1
    while num < n:
        if n % num == 0:
            aux += n
        num += 1
    return True if aux > n else False
print(AbundantNumber(12))

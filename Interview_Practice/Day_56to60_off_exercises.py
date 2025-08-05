# Día 56

# Ejercicio 277: Crea una función que encuentre el número de palabras que comienzan con una consonante en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CountConsonantWords(Strings):
    aux = 0
    vowels = "aeiou"
    clean = list(Strings.split())
    for word in clean:
        if word[0].lower() not in vowels:
            aux += 1
    return aux
print(CountConsonantWords("Hello MR. Eric Hernandez Edwards"))

# Ejercicio 279: Crea una función que reciba una cadena y devuelva la misma cadena sin caracteres especiales.
# Conceptos: Manipulación de strings, funciones.
def WithOut(string):
    import re
    if not string:
        return None
    elif not isinstance(string, str):
        raise TypeError("I only accept text")
    clean = re.sub(r"[^\w\s]", "", string)
    return clean
print(WithOut("Hello MR. Eri@c Hernandez Edwa/rds"))

# Ejercicio 280: Escribe un programa que imprima un triángulo de asteriscos de altura n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def TrianguleAterisk(n):
    for i in range(1, n + 1):
        space = " " * (n)
        asterisk = "*" * (i)
        print(space +  asterisk)
        
TrianguleAterisk(5)



# Día 57
# Ejercicio 281: Crea una función que verifique si un número es un número de Kaprekar.
# Conceptos: Matemáticas, funciones.
# Kaprekar: es un número entero positivo n tal que, si se eleva al cuadrado y se divide en dos partes, la suma de esas partes es igual a n.
def IsKaprekar(n):
    if n < 0:
        return False
    square = str(n ** 2)
    d = len(str(n))
    left = int(square[:-d]) if square[:-d] else 0
    right = int(square[-d:])
    return left + right == n

# Ejercicio 283: Crea una función que reciba una lista y devuelva el número de elementos que son ceros.
# Conceptos: Listas, funciones.
def CountZeros(lst):
    if not isinstance(lst, list):
        raise TypeError("I only accept lists")
    return lst.count(0)
print(CountZeros([0, 1, 2, 0, 3, 0, 4]))

# Ejercicio 284: Escribe un programa que cuente cuántas palabras hay en una frase ingresada por el usuario, excluyendo números.
# Conceptos: Manipulación de strings, funciones.
def CountWordsWithoutNumbers(phrase):
    if not isinstance(phrase, str):
        raise TypeError("I only accept strings")
    import re
    cleaned_phrase = re.sub(r'\d+', '', phrase)  # Remove numbers
    words = cleaned_phrase.split()
    return len(words)
print(CountWordsWithoutNumbers("Hello 123 worl8d 456"))

# Ejercicio 285: Crea una función que reciba un número y devuelva True si es un número de Harshad.
# Conceptos: Matemáticas, funciones.
def IsHarshad(n):
    if n <= 0:
        return False
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0
print(IsHarshad(18)) 

print("eric")
# Día 58

# Ejercicio 287: Crea una función que encuentre el número de palabras que terminan en 'e' en una cadena.
# Conceptos: Manipulación de strings, funciones.
def EndWithE(elements):
    if not elements:
        return "The list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    return len([str(e) for e in elements if e[-1].lower() == "e"])
print(EndWithE(["eric", "pera", "perone", "Pene", "penE"]))


# Ejercicio 289: Crea una función que reciba una cadena y devuelva la misma cadena sin números.
# Conceptos: Manipulación de strings, funciones.
def WithOutNUmbers(Phrase):
    import re
    clean = re.sub(r"[\d]", "", Phrase)
    return clean
print(WithOutNUmbers("Hola8, soy Eric89 hernandez 8 Edwards7"))

# Ejercicio 290: Escribe un programa que imprima un cuadrado de asteriscos de tamaño n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def AsteriskSquare(n):
    for i in range(n):
        space = " " * (n - i - 1)
        square = "*" * (n)
        print(space + square)
AsteriskSquare(5)


# Día 59
# Ejercicio 291: Crea una función que verifique si un número es un número de Smith.
# Conceptos: Matemáticas, funciones.
# es un número compuesto (no primo) que tiene una propiedad curiosa: la suma de sus dígitos es igual a la suma de los dígitos de sus factores primos.
def IsSmith(n):
    if n < 2:
        return False
    def prime_factors(n):
        factors, d = [], 2
        while d * d <= n:
            while (n % d) == 0:
                factors.append(d)
                n //= d 
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    factors = prime_factors(n)
    if len(factors) == 1:
        return False  # n is prime
    digit_sum = lambda x: sum(int(d) for d in str(x)) # Suma de los dígitos
    # Verifica si la suma de los dígitos de n es igual a la suma de los dígitos de sus factores primos
    return digit_sum(n) == sum(digit_sum(factor) for factor in factors)
print(IsSmith(4))  # True, porque 4 = 2 * 2 y la suma de los dígitos es 4

# Ejercicio 293: Crea una función que reciba una lista y devuelva el número de elementos que son primos.
# Conceptos: Listas, funciones.
def CountPrimes(lst):
    if not isinstance(lst, list):
        raise TypeError("I only accept lists")
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(1 for x in lst if is_prime(x))
print(CountPrimes([2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Ejercicio 294: Escribe un programa que cuente cuántas letras hay en una cadena ingresada por el usuario, excluyendo espacios.
# Conceptos: Manipulación de strings, funciones.
def CountLetters(phrase):
    if not isinstance(phrase, str):
        raise TypeError("I only accept strings")
    return len(phrase.replace(" ", ""))
print(CountLetters("Hello Eric Hernandez Edwards"))

# Ejercicio 295: Crea una función que reciba un número y devuelva True si es un número de Friedman.
# Conceptos: Matemáticas, funciones.
# es un numero que usando sus dijitos y alguna operacion aritmetica basica dan como resultado el mismo numero
def IsFriedman(n):
    if n < 0:
        return False
    from itertools import permutations
    digits = str(n)
    for perm in permutations(digits):
        for op in ['+', '-', '*', '/']:
            expr = ''.join(perm)
            try:
                if eval(expr) == n:
                    return True
            except ZeroDivisionError:
                continue
    return False
print(IsFriedman(25))  # True, porque 2 + 5 = 7 y 2 * 5 = 10, pero no es un número de Friedman

# Día 60

# Ejercicio 297: Crea una función que encuentre el número de palabras que contienen la letra 'i' en una cadena.
# Conceptos: Manipulación de strings, funciones.
def CoincidenWith_i(Phrase):
    if not Phrase:
        return -1
    elif not isinstance(Phrase, str):
        raise TypeError("I Only accept text")
    words = Phrase.lower().split()
    return len([ str(n) for n  in words if "i" in n])
print(CoincidenWith_i("hello, my name is Eric"))

# Ejercicio 299: Crea una función que reciba una cadena y devuelva la misma cadena sin caracteres especiales.
# Conceptos: Manipulación de strings, funciones.
def WithOUtSpecialsCaracters(Phrase):
    import re 
    if not Phrase:
        return None
    elif not isinstance(Phrase, str):
        raise TypeError("I only accept text")
    return "".join([re.sub(r"[^\w\s]", "", Phrase)])
print(WithOUtSpecialsCaracters("hello# my name. is% eric"))

# Ejercicio 300: Escribe un programa que imprima un triángulo de asteriscos de altura n, donde n es ingresado por el usuario.
# Conceptos: Bucles, impresión.
def TrianguleAsterisk(n):
    for i in range(0, n + 1):
        space = " " * (n - i)
        triangule = "*" * (i)
        print(space +  triangule)
TrianguleAsterisk(5)

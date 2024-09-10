# Día 9: Comprensión de Listas y Generadores
# Son formas concisas y eficientes de crear y manipular listas y secuencias.

# Tips del Tema
# Comprensión de listas: Una forma concisa de crear listas nuevas aplicando una expresión a cada elemento de una secuencia. 
# Esto permite filtrar y transformar datos de manera rápida y legible.

# Generadores: producen elementos uno a la vez y son utilizados para manejar grandes secuencias de datos de manera eficiente. 
# A diferencia de las listas que almacenan todos los elementos en memoria, los generadores producen elementos sobre la marcha, 
# ahorrando memoria y mejorando el rendimiento.

# Comprensión de Listas: una accion a cada elemento de la lista, 
# Utilízalas siempre que necesites crear una lista transformando o filtrando otra lista u otra secuencia iterable.

# Crear una lista de elevados de números del 1 al 10
elevados = [x**2 for x in range(1, 11)]
cubo = [x ** 3 for x in range(1, 10)]
print(elevados)  

multi = [r*3 for r in range(1, 5)] # hace una lista de 1 al 5 y multiplica cada elemento de la lista x 3
print(multi)

# Filtrar números pares de una lista
pares = [x for x in range(1, 11) if x % 2 == 0]
impares = [i for i in range(1, 15) if i % 2 != 0]
print(pares)  

# filtrar numeros impares de una lista
impar = [i for i in range(1,24) if i % 2 == 1]
print(impar)

# filtrar numeros pares de una lista
par = [a for a in range(1,24) if a % 2 == 0]
print(par)

# Generadores: Empléalos cuando necesites iterar sobre grandes cantidades de datos de manera eficiente, 
# especialmente si los datos no caben fácilmente en la memoria disponible.

# Generador simple que produce números del 1 al 5
def generador():
    for i in range(1, 6):
        yield i  # devuelve los números del 1 al 5 

gen = generador()
for numero in gen:
    print(numero)  

############################################# Ejercicios
# Ejercicio 1: Usa comprensión de listas para crear una lista de los cuadrados de los números del 1 al 10.
p = [e ** 2 for e in range(1,11)]
print(p)

# Ejercicio 2: Usa comprensión de listas para crear una lista de los números pares del 1 al 20.
z = [i for i in range(1,21) if i % 2 == 0]
print(z)

# Ejercicio 3: Usa comprensión de listas para crear una lista de las primeras letras de cada palabra en una lista de palabras.
lost = ["eric", "alex", "petras", "athenas"]
list = [l[0] for l in lost if l] # [0] es la primera letra de cada vez que se itera l
print(list)

# Ejercicio 4: Usa comprensión de listas para filtrar los números mayores a 5 de una lista de números.
n = [u for u in range(1,10) if u > 5 ]
print(n)

# Ejercicio 5: Define un generador que produzca los primeros 10 números de Fibonacci. 
def fibonacci():
    a, b = 0, 1 # valores
    for _ in range(10):
        yield a
        a, b = b, a + b # formula de fibo

fibo = fibonacci()
for numb in fibo:
    print(numb)

# Ejercicio 6: Define un generador que produzca los números pares del 1 al 20.
def num_pares():
    for x in range(1,21):
        if x % 2 == 0:
            yield x

pares = num_pares()
for pop in pares:
    print(pop)

# Ejercicio 7: Define un generador que produzca las letras de una cadena una por una.
cadena = "eric"
def letra():
    for a in cadena:
        yield a

letrs = letra()
for let in letrs:
    print(let)

# Ejercicio 8: Define un generador que produzca números impares del 1 al 15.
def impars():
    for num in range(1,16):
        if num % 2 == 1:
            yield num

impar = impars()
for impares in impar:
    print(impares)

# Ejercicio 9 (Teoría): ¿Qué es la comprensión de listas y en qué se diferencia de los bucles tradicionales?
# con el se puede realizar una accion sobre cada elemento del bucle y son mas compactos que los bucles for,
# en cambio el bucle solo itera sobre los elemntos en la lista y no realiza ninguna accion y se usan para operaciones de bucle mas complejas.

# Ejercicio 10 (Práctica): Escribe un programa que use un generador para producir los primeros 5 números primos.
def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 es primo
    if num % 2 == 0:
        return False  # Los números pares mayores que 2 no son primos
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generador_primos():
    """Generador que produce los primeros 5 números primos."""
    num = 2
    contador = 0
    while contador < 5:
        if es_primo(num):
            yield num
            contador += 1
        num += 1

# Ejemplo de uso del generador
primos = generador_primos()
for primo in primos:
    print(primo)

# Ejercicio 11: Usa comprensión de listas para crear una lista con los cubos de los números del 1 al 10.
cubos = [n ** 3 for n in range(1, 11)]
print(cubos)

# Ejercicio 12: Usa comprensión de listas para crear una lista con los números divisibles por 3 entre 1 y 30.
por_3 = [x for x in range(1, 31) if x % 3 == 0]
print(por_3)

# Ejercicio 13: Usa comprensión de listas para crear una lista que contenga la longitud de cada palabra en una lista de palabras.
palabra = ["eric", "arbol", "pez", "rojo"]
conteo = [len(p) for p in palabra]
print(conteo)

# Ejercicio 14: Usa comprensión de listas para crear una lista de los números impares entre 10 y 50.
imp = [i for i in range(10, 50) if i % 2 != 0] # crean la lista en el momento y es mejor que una lista creada manualmente porque la misma guarda datos en memoria.
print(imp)

# Ejercicio 15: Define un generador que produzca los múltiplos de 5 del 1 al 50.
def multi():
    for i in range(1, 51):
        if i % 5 == 0:
            yield i # permite que los valores se generen a medida que son necesarios, lo que ahorra memoria comparado con una lista.
dato = multi()
for multiplo in dato:
    print(multiplo)
# m = [n for n in dato] # darlos en una lista
# print(m) 

# Ejercicio 16: Define un generador que produzca los cuadrados de los números impares entre 1 y 20.
def cuadrado():
    for cuadrado in range(1, 20):
        if cuadrado % 2 != 0:
            yield cuadrado ** 2
dato = cuadrado()
for x in dato:
    print(x)

# Ejercicio 17: Define un generador que produzca los caracteres de una cadena al revés, uno por uno.
def alrevez(cadena):
    for caracter in cadena[::-1]:
        yield caracter
dato = alrevez("eric")
for x in dato:
    print(x)

# Ejercicio 18: Usa comprensión de listas para crear una lista de los números que son tanto divisibles por 2 como por 3 entre 1 y 100.
numero = [n for n in range(1, 100) if n % 2 == 0 and n % 3 == 0]
print(numero)

# Ejercicio 19: Define un generador que produzca las primeras 6 potencias de 2.
def potencias():
    for i in range(6):
        yield i ** 2
dato = potencias()
for x in dato:
    print(x)

# Ejercicio 20: Usa comprensión de listas para filtrar las palabras que tienen más de 4 letras en una lista de palabras.
frutas = ["manzana", "banana", "cereza", "limon", "pera"]
palabras = [p for p in frutas if len(p) > 4 ]
print(palabras)
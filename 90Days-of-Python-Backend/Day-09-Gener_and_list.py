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
print(elevados)  

multi = [r*3 for r in range(1, 5)] # hace una lista de 1 al 5 y multiplica cada elemento de la lista x 3
print(multi)

# Filtrar números pares de una lista
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]

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
        yield i  # devuelve cada número del 1 al 5 uno por uno

# Usar el generador
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
list = [l[0] for l in lost if l]
print(list)

# Ejercicio 4: Usa comprensión de listas para filtrar los números mayores a 5 de una lista de números.
n = [u for u in range(1,10) if u > 5 ]
print(n)

# Ejercicio 5: Define un generador que produzca los primeros 10 números de Fibonacci. 
# def fibonacci():
#     for z in range(1,11):
#         z += 2
#         yield z
# fibo = fibonacci()
# for numb in fibo:
#     print(numb)
def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

# Ejemplo de uso
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

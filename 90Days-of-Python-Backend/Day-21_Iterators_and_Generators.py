# Día 21: Iteradores y Generadores

# Iteradores y generadores en Python, herramientas poderosas para manejar secuencias de datos de manera eficiente.

# 1. Iteradores:
#    - Un iterador es un objeto que implementa los métodos `__iter__()` y `__next__()`.
#    - Puedes obtener un iterador de cualquier objeto iterable (como listas, tuplas, diccionarios, etc.) usando la función `iter()`.
#    - El método `next()` se usa para obtener el siguiente elemento del iterador, y lanza una excepción `StopIteration` cuando no hay más elementos.
#    - Son objetos que permiten recorrer todos los elementos de una colección, como listas o tuplas.
#    - Se obtienen llamando a la función `iter()` sobre una colección.
#    - La función `next()` se usa para obtener el siguiente elemento del iterador.

# 2. Generadores:
#    - Los generadores son funciones que devuelven un objeto iterador con una secuencia de valores.
#    - En lugar de `return`, usan la palabra clave `yield` para producir un valor y pausar la ejecución de la función, manteniendo su estado para la siguiente llamada.
#    - Los generadores son más eficientes en términos de memoria que las listas, especialmente para grandes secuencias de datos, ya que producen los elementos sobre la marcha.
#    - Son una forma especial de iterador que se define con una función y la palabra clave `yield`, permitiendo producir una secuencia de valores sobre la marcha.
#    - Son útiles para trabajar con grandes secuencias de datos sin necesidad de almacenarlos en memoria.

# 3. Generadores de Expresión:
#    - Son una forma concisa de crear generadores usando una sintaxis similar a las listas de comprensión, pero con paréntesis en lugar de corchetes.
#    - Al igual que las funciones generadoras, producen elementos uno a uno según se necesiten.

# Crear y Usar Iteradores
numeros = [1, 2, 3, 4, 5]

# Obtener un iterador de la lista
iterador = iter(numeros)
# print(iterador) no da el dato

# Usar next() para obtener elementos del iterador
print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3
print(next(iterador))  # Salida: 4
print(next(iterador))  # Salida: 5
# print(next(iterador)) # Si tratamos de obtener otro elemento, se lanzará una excepción StopIteration
# por que la lista llega hasta 5 por eso el error

# Crear y Usar Generadores
def contador(max):
    n = 1
    while n <= max:
        yield n
        n += 1
contador(10)

# Usar el generador
for numero in contador(5):
    print(numero)

# Generadores de Expresión
gen_exp = (x*x for x in range(5)) # gen_exp tiene varios rerultados por el bucle for, entoces hay que iterarlo 

# Usar el generador de expresión
for cuadrado in gen_exp:
    print(cuadrado)
    # Salida:
    # 0
    # 1
    # 4
    # 9
    # 16


# Ejercicios Avanzados

# Generador de Números Primos:
def generador_primos():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

primos = generador_primos()
for _ in range(10):
    print(next(primos))
    # Salida: los primeros 10 números primos

# Generador de Fibonacci:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
    # Salida: los primeros 10 números de la secuencia de Fibonacci

# Generador de Líneas de un Archivo:
def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()

# for linea in leer_lineas('archivo.txt'): lee cada linea del archivo
#     print(linea)

######### ejercicios
# Ejercicio 1: Crea un iterador para una lista de cadenas de texto y usa next() para mostrar los dos primeros elementos.
lista = ["edwards", "alajuela" ,"hernandez", "costarica", "arhenas"]
texto = iter(lista)
print(next(texto))
print(next(texto))
    
# Ejercicio 2: Escribe una función que tome una lista y devuelva un iterador para recorrer la lista.
def recorrer(lista):
    tex = iter(lista)
    for i in tex:
        print(i) 
recorrer(lista = ["alajuela", "costarica", "arhenas"])

# Ejercicio 3: Define un generador que produzca los primeros n números pares.
def generador_pares(n):
    for i in range(n):
        yield i * 2
n = 10 # numero de veces o vueltas
for par in generador_pares(n):
    print(par)

# Ejercicio 4: Define un generador que produzca los primeros n números impares.
def generador_impares(n):
    for i in range(n):
        yield i * 2 + 1

n = 10 
for impar in generador_impares(n):
    print(impar)

# Ejercicio 5: Escribe una función que tome un número n y devuelva un generador que produzca los números de Fibonacci hasta n.
n = 10
a = 0
b = 1
suma = 0 # para iniciar
print(a,b, end=" ")
while True:
    suma = a + b 
    a = b # se calcula el valor
    b = suma # se calcula el valor
    if suma < n: # hasta el numero n
        print(suma, end=" ")
    else:
        break
# formula de fibonaci f0 = f1 + f2

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Uso del generador
n = 15
for num in fibonacci(n):
    print(num, end=" ")


# Ejercicio 6: Define un generador de expresión que produzca los cubos de los números del 1 al 10.
al_cubo = (x ** 3 for x in range(0, 11))
for cubo in al_cubo:
    print(cubo)

# Ejercicio 7: Escribe una función que use un generador para producir los números primos menores a n.
n = 15
def gen_primos(n):
    for i in range(2, n):
        es_primo = True  # Suponemos que i es primo
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:  
                es_primo = False  
                break
        if es_primo:
            yield i  # Genera el número primo

for primo in gen_primos(15):
    print(f"numero: {primo} es un numero primo")

# Ejercicio 8: Escribe una función que use un generador para producir los cuadrados de los números de una lista.
def cuadrado_num(lista):
    for i in lista:
        yield i ** 2
for cuadrado in cuadrado_num([5, 8, 9, 4, 3]):
    print(cuadrado)

# Ejercicio 9 (Teoría): ¿Qué es un iterador y un generador en Python y cuáles son las diferencias entre ellos?
# los itineradores y generadores son excelentes herramientas para manejar una secuencia de datos en python, con el iterador puedes 
# datos o objetos de cualquier iterable (como listas, tuplas, diccionarios, etc.) en cambio los generadores tiene funciones como 
# yield permite que la función continúe su ejecución en una llamada futura.

# Ejercicio 10 (Práctica): Escribe un programa que use un generador para producir los primeros n números 
# de la secuencia de Fibonacci y los almacene en una lista.
lista_vacia = []
n = 20
a = 0
b = 1
suma = 0
while True:
    suma = a + b
    a = b
    b = suma
    if suma < n:
        lista_vacia.append(suma)
    else:
        print(lista_vacia)
        break
########## o
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

lista_v = list(fibonacci_gen(15)) # hacer fibo 15 veces
print(lista_v)

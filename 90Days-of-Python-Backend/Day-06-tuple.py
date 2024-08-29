# Día 6: Tuplas y Operaciones con Tuplas
# Las tuplas en Python son colecciones ordenadas e inmutables de elementos. Son similares a las listas, 
# pero con la diferencia clave de que no se pueden modificar después de su creación.
# Esto las hace útiles para almacenar datos que no deben cambiar a lo largo del programa.

# Tips del Tema
# Se crean utilizando paréntesis ().
# Pueden contener elementos de diferentes tipos de datos (int, float, str, bool, etc.)

# Los elementos de una tupla se acceden mediante índices, que comienzan en 0.
# Usos Comunes:

# Almacenar datos heterogéneos.
# Utilizar como claves en diccionarios (dado que son inmutables).
# Desempaquetar múltiples valores de una función.

# tupla
colores = ("rojo", "verde", "azul", "negro")

# Acceso a elementos
print(colores[0])  
print(colores[1]) 
print(colores[2])
print(colores[3])  

####### Desempaquetado de Tuplas
rojo, verde, azul, negro = colores
print(rojo)   
print(verde) 
print(negro)
print(azul)   

####### Operaciones Comunes con Tuplas

# Concatenación:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = (10, 55, 100)
tupla_concatenada = tupla1 + tupla2
print(tupla3 + tupla1)
print(tupla_concatenada)  

# Repetición:
tupla = ("a", "b")
tupla_repetida = tupla * 3
print(tupla3 * 2)
print(tupla_repetida)  

# Verificación de existencia:
tupla = (1, 2, 3, 4)
print(2 in tupla)  
print(5 in tupla) 
print(50 in tupla) 

# Conversión entre listas y tuplas:
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla) 

nueva_lista = list(tupla)
print(nueva_lista) 

####### Tuplas anidadas:
# Puedes tener tuplas dentro de otras tuplas.

tupla_anidada = (1, (2, 3), (4, 5, 6))
print(tupla_anidada[1]) 
print(tupla_anidada[1][0]) 

# Desempaquetado avanzado:
# Puedes desempaquetar tuplas de manera avanzada para capturar múltiples valores.

tupla = (1, 2, 3, 4, 5, 10)
a, b, *c = tupla # c va a imprimir todos los valores despues de el.
print(a)  
print(b)  
print(c)  

# Métodos Comunes de Tuplas
# count()

tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(2))  
print(tupla.count(4))  
print(tupla.count(5))  
print(tupla.count(6))  

# 2. index(): 
tupla = (1, 2, 3, 2, 4, 3, 5)
print(tupla.index(2)) 
print(tupla.index(3))  
print(tupla.index(4))  

# Longitud de la tupla:
tupla = (1, 2, 3, 4)
print(len(tupla)) 

# min() y max(): Devuelven el valor mínimo y máximo en la tupla.
tupla = (1, 2, 3, 4, 5)
print(min(tupla))  
print(max(tupla))  

# sum(): Devuelve la suma de los elementos de la tupla.
tupla = (1, 2, 3, 4, 5)
print(sum(tupla))  

# sorted(): Devuelve una lista con los elementos de la tupla ordenados.
tupla = (3, 1, 4, 1, 5, 9, 2)
print(sorted(tupla))  

# any() y all(): Verifican condiciones sobre los elementos de la tupla.
tupla = (1, 2, 0)
print(any(tupla))  # any si hay un elemento en la lista distinto de 0
print(all(tupla))  # all false  si almenos un elemento en la lista es 0
print(tupla)

# Ejercicios
# Ejercicio 1: Crea una tupla con tus colores favoritos y muéstrala.
tuples = ("rojo", "cafe", "negro", "celeste")
print(tuples)

# Ejercicio 2: Accede y muestra el primer elemento de la tupla.
tuples = ("rojo", "cafe", "negro", "celeste")
print(tuples[0])

# Ejercicio 3: Intenta cambiar un elemento de la tupla y observa el resultado.
# tuples[0] = "blanco" da error porque las tuplas son inmutables, hay que covertirla en una lista para cambiar el valor
print(tuples[0])

tupl = list(tuples) # covirtiendo tupla a lista
print(type(tupl))
tupl[0] = "blanco"
print(tupl)

eric = tuple(tupl) # convirtiendo nueva lista en tupla
print(type(eric))
print(eric)

# Ejercicio 4: Desempaqueta una tupla con cuatro números y muéstralos.
numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = numeros
print(uno)
print(cuatro)

# Ejercicio 5: Define una función que tome una tupla de números y devuelva su suma.
numeros = (1, 2, 3, 4, 100)
def su (numeros):
    return sum(numeros)

print(su(numeros))

# Ejercicio 6: Define una función que tome una tupla de números y devuelva el número máximo.
numeros = (1, 2, 3, 4, 100)
def maximo (numeros):
    return max(numeros)

print(maximo(numeros))

# Ejercicio 7: Define una función que tome una tupla de números y devuelva el número mínimo.
numeros = (1, 2, 3, 4, 100)
def minimo(numeros):
    return min(numeros)
print(minimo(numeros))

# Ejercicio 8: Define una función que tome una tupla de números y devuelva su promedio.
numeros = (1, 2, 3, 4, 100, 22, 1000)
def promedio(numeros):
    return sum(numeros) / len(numeros)
print(promedio(numeros))

# Ejercicio 9 (Teoría): ¿Qué es una tupla y cuándo sería más apropiado usar una tupla en lugar de una lista?
# Una tupla contiene datos ordenados q pueden ser str, float, bool, int. pero no se pueden cambiar, 
# es bueno usarlo cuando se requiran elementos q no van a cambiar.

# Ejercicio 10 (Práctica): Escribe un programa que tome tres coordenadas de un punto (x, y, z) 
# como una tupla y calcule la distancia desde el origen (0, 0, 0).
# distancia = raiz((x2 -x1)**2 + (y2 - y1)**2 + (z2 + z1)**2)
origen2 = ( int(input("ingrese la distancia:")), int(input("ingrese la distancia:")), int(input("ingrese la distancia:")))
x2 = origen2[0]
y2 = origen2[1]
z2 = origen2[2]
x1, y1, z1 = 0

distancia = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 + z1) ** 2 # formula para sacar la distancia

import math
raiz = math.sqrt(distancia)
print(raiz)

# o
dist = distancia ** 0.5
print(dist)

# Ejercicio 11: Crear Tupla de Pares
# Define una tupla con pares de números y muestra la suma de cada par.
# Ejemplo de tupla: ((1, 2), (3, 4), (5, 6))
def sumar_tuples(tuplas):
    sums = []
    for tupla in tuplas:
        sums.append(sum(tupla))
    return tuple(sums)

dato = sumar_tuples(((5, 5), (8, 5), (1, 2)))
print(dato)

# Ejercicio 12: Tupla de Nombres
# Define una tupla con nombres de personas y muestra cuántos nombres tienen más de 5 caracteres.
tupla = ("Alex", "Jonathan", "Emily", "Michael")
count = 0
for n in tupla:
    if len(n) > 5:
        count += 1
print(f"Cantidad de nombres con más de 5 caracteres son: {count}")

# Ejercicio 13: Concatenación y Repetición
# Crea dos tuplas con números y concaténalas. Luego, repite la tupla resultante tres veces.
tupl = (1, 5, 69, 5, 22, 7)
tupl2 = (10, 2, 9, 51, 2, 70)
concatenar = tupl + tupl2
print(concatenar * 3)

# Ejercicio 14: Buscar en Tupla
# Define una tupla con diferentes frutas y verifica si la fruta "manzana" está en la tupla.
tupla = ("banana", "manzana", "naranja", "pera", "sandia")
print("manzana" in tupla)

# Ejercicio 15: Tupla de Fechas
# Define una tupla con fechas en formato (día, mes, año) y muestra las fechas ordenadas por año.
# Ejemplo de tupla: ((5, 7, 2023), (15, 3, 2022), (10, 11, 2024))
fechas = ((1, 5, 2024), (2, 8, 2022), (5, 9, 1998), (1, 2, 1995))
tupla_ordenda = sorted(fechas, key=lambda x: x[2],)
for dia, mes, año in tupla_ordenda:
    print(dia, mes, año)

# Ejercicio 16: Desempaquetado de Tupla
# Define una tupla con una lista de números y desempaqueta los primeros tres números en variables separadas.
tupla1 = (10, 20, 30, 40, 50)
z, x, v, *n = tupla1
print(z, x, v)

# Ejercicio 17: Contar Elementos en Tupla
# Define una tupla con una mezcla de números y strings, y cuenta cuántos de los elementos son strings.
# Ejemplo de tupla: (1, "hello", 2, "world", 3)
t = ("eric", 22, 5, "edwards", 10, "brazil", "paris")
contador = 0
for tuples in t:
    if isinstance(tuples, str):
        contador += 1  
print(contador)

# Ejercicio 18: Conversiones
# Convierte una lista de números en una tupla y luego convierte la tupla de nuevo en una lista.
# Ejemplo de lista: [1, 2, 3, 4]
lista1 = [1, 5, 89]
tupla5 = tuple(lista1)
lista1 = list(tupla5)

# Ejercicio 19: Tupla Anidada
# Define una tupla que contiene otra tupla y un número. Muestra el segundo elemento de la tupla anidada.
# Ejemplo de tupla: ((1, 2, 3), 4)
tup = ((1, 5, 8, 9), 7)
print(tup[0][1])

# Ejercicio 20: Tupla de Tuplas
# Define una tupla que contiene varias tuplas, cada una con dos elementos. Muestra el primer elemento de cada tupla interna.
# Ejemplo de tupla: ((1, 2), (3, 4), (5, 6))
tupla_anidada = ((1, 2), (5, 8), (9, 8))
for primer, segundo in tupla_anidada:
    print(primer)
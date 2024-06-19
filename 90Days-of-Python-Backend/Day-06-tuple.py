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
print(tupla.count(2))  # Salida: 2
print(tupla.count(4))  # Salida: 3
print(tupla.count(5))  # Salida: 1
print(tupla.count(6))  # Salida: 0

# 2. index(): 
tupla = (1, 2, 3, 2, 4, 3, 5)
print(tupla.index(2))  # Salida: 1
print(tupla.index(3))  # Salida: 2
print(tupla.index(4))  # Salida: 4

# Longitud de la tupla:
tupla = (1, 2, 3, 4)
print(len(tupla)) 

# min() y max(): Devuelven el valor mínimo y máximo en la tupla.
tupla = (1, 2, 3, 4, 5)
print(min(tupla))  # Salida: 1
print(max(tupla))  # Salida: 5

# sum(): Devuelve la suma de los elementos de la tupla.
tupla = (1, 2, 3, 4, 5)
print(sum(tupla))  # Salida: 15

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
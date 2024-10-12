# Definición del Tema
# Tuplas una estructura de datos en Python similar a las listas, pero con la característica clave de que son inmutables. 
# Esto significa que, una vez que se crea una tupla, sus elementos no pueden ser modificados.

# Tips del Tema
# Tuplas: Son colecciones ordenadas de elementos que pueden ser de diferentes tipos. Se definen usando paréntesis ().
# Inmutabilidad: Una vez que se crea una tupla, no puedes modificar, añadir o eliminar elementos.
# Uso: Las tuplas son útiles para representar datos que no deben cambiar a lo largo del tiempo, como coordenadas, registros de datos, etc.

# Fundamentos del Tema con Código
# Crear y Acceder a Tuplas:
coordenadas = (10, 20)
print(coordenadas[0])  
print(coordenadas[1])  

# Desempaquetar una tupla
x, y = coordenadas
print(x)  
print(y)  

################ Operaciones Comunes con Tuplas:

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  

# Repetir tuplas
tupla_repetida = (0,) * 4
print(tupla_repetida) 

# Contar elementos en una tupla
print(tupla_concatenada.count(2))  

# Encontrar el índice de un elemento
print(tupla_concatenada.index(4)) 

################# Tuplas con Funciones y Bucles:
def calcular_area(base, altura):
    return base * altura
dimensiones = (5, 10)
area = calcular_area(*dimensiones)
print(area)  

# Iterar sobre una lista de tuplas
pares = [(1, 2), (3, 4), (5, 6)] # lista de tuplas
for (x, y) in pares:
    print(f"x: {x}, y: {y}")

# Convertir entre listas y tuplas
lista = [7, 8, 9]
tupla = tuple(lista)
print(tupla)  
lista_recuperada = list(tupla)
print(lista_recuperada)  

############## desempaquetado 
tupla = (10, 20, 30)
a, b, c = tupla
print(a)  
print(b)  
print(c)  

# 2. Implementa una función que tome una lista de tuplas, donde cada tupla contiene un nombre y una edad, y devuelva una lista de nombres ordenados por edad (de menor a mayor).
def ordenar_por_edad(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
    return [nombre for nombre, edad in lista_ordenada]

personas = [("Ana", 30), ("Luis", 25), ("Marta", 35)]
nombres_ordenados = ordenar_por_edad(personas)
print(nombres_ordenados) 

# tupla anidada 
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada[1][2])  # [1] el primero es para escoger que tupla ya que hay de 3 y el [2] es para escoger el elemento interno de la tupla ya escogida.

# ############ Ejercicios
# Ejercicio 1: Crea una tupla con los nombres de 5 colores y muestra el nombre del segundo color.
tuples = ("rojo", "negro", "verde", "cafe", "blanco")
print(tuples[1])

# Ejercicio 2: Intenta modificar un elemento de la tupla del ejercicio 1 y observa el error que se produce.
#tuples[3] = "celeste"
print(tuples) # error: TypeError: 'tuple' object does not support item assignment

# Ejercicio 3: Desempaqueta la tupla del ejercicio 1 en variables individuales y muestra cada variable.
a, b, c, d, f = tuples
print(a)
print(b)
print(c)
print(d)
print(f)

# Ejercicio 4: Convierte la lista de ciudades del ejercicio 1 del Día 17 a una tupla y muestra la tupla resultante.
ciudades = ["Sanjose", "Edimburgo", "Lima", "Oslo", "Berlin"]
tupli = tuple(ciudades)
print(tupli)

# Ejercicio 5: Escribe una función que tome una lista de números y devuelva una tupla con el mínimo y el máximo número de la lista.
def number_max_min(lista):
    list = tuple(lista)
    maximo = max(list)
    minimo = min(list)
    return (minimo, maximo)
print(number_max_min(lista = [22, 10, 58, 2, 587, 54]))

# Ejercicio 6: Escribe una función que tome una tupla de cadenas de texto y devuelva una nueva tupla con las cadenas en mayúsculas.
def tupla_mayuz(tupli):
    pop = [x.upper() for x in tupli]
    new_tuple = tuple(pop)
    return new_tuple

print(tupla_mayuz(tupli = ("Sanjose", "Edimburgo", "Lima", "Oslo", "Berlin")))

# Ejercicio 7: Escribe una función que tome dos tuplas y devuelva una nueva tupla que contenga solo los elementos comunes a ambas tuplas.
def comunes(tupla1, tupla2):
    sets = tuple(set(tupla1) & set(tupla2))
    return sets
print(comunes(tupla1 = (22, 5, 8, 10, 56), tupla2 = (22, 23, 6, 56, 100)))

# Ejercicio 8: Escribe una función que tome una tupla de números y devuelva una lista con los números en orden inverso.
def inverse(tuplo):
    lis = list(tuplo)
    lis.reverse()
    return lis
print(inverse(tuplo = (22, 23, 6, 56, 100)))

# Ejercicio 9 (Teoría): ¿Qué es una tupla en Python y cómo se diferencia de una lista?
# una tupla es un conjunto de dato inmutable en python que se usa cuando se requieren que los datos no cambien, 
# su principal diferencia con las lista es que ellas son mutables, osea que se puede reasignar su valor, en cambio
# con las tuplas no se puede dada su inmutabilidad.
 
# Ejercicio 10 (Práctica): Escribe un programa que tome una lista de tuplas, donde cada tupla contenga el nombre y la edad de una persona, 
# y devuelva una lista de nombres de las personas mayores de 18 años.
personas = (("alex", 52), ("eric", 15), ("greivin", 17), ("rad", 25), ("carlos", 30))
def mayores(personas):
    for name, age in personas:
        if age > 18:
            print(f"Esta perosona de nombre: {name} y de edad: {age} es mayor de 18 años")

mayores(personas = (("alex", 52), ("eric", 15), ("greivin", 17), ("rad", 25), ("carlos", 30)))

# Ejercicio 11: 
# Crea una tupla con cinco números enteros y encuentra la suma de todos los elementos.
import random
tu = tuple(random.randint(1, 100)for t in range(5))
suma_tupla = sum(tu)
print(f"Tupla creada: {tu}")
print(f"la suma total de todos los elementos de la tupla es: {suma_tupla}")

# Ejercicio 12: 
# Dada una tupla con números enteros, escribe un programa que imprima solo los números impares.
#tupla_numeros = tuple(random.randint(1, 50)for n in range(10)if n % 2 != 0) # asi no se hace porque el condicional no afecta a la tupla si no que al rango de 10
# no es recomendable juntar lista, tuplas de comprensiones con condicionales
tupla_numeros = tuple(random.randint(1, 50)for n in range(10))
numeros_impares = tuple(n for n in tupla_numeros if n % 2 != 0)
print(f"Tupla: {tupla_numeros}")
print(f"Números impares de la tupla: {numeros_impares}")

# Ejercicio 13: 
# Escribe una función que reciba dos tuplas y devuelva una nueva tupla que contenga los elementos 
# de la primera tupla que no están en la segunda.
def diferencia(tupla1, tupla2):
    new = tuple(set(tupla1).difference(set(tupla2)))
    return f"esta es la nueva tupla: {new}"
dato = diferencia((1, 5, 6, 8, 78),(1, 5, 4, 8, 7))
print(dato)

# Ejercicio 14: 
# Convierte una tupla de cadenas de texto en una sola cadena donde los elementos estén separados por comas.
tupla_text = ("eric", "calvin", "edwards")
cadenas = ", ".join(tupla_text)
print(cadenas)

# Ejercicio 15: 
# Dada una tupla de números enteros, escribe una función que devuelva el promedio de sus elementos.
def promedio(tupla_promedio):
    if len(tupla_promedio) == 0:
        return "La tupla está vacía, no se puede calcular el promedio."
    divisor = len(tupla_promedio)
    numero = sum(tupla_promedio)
    resultado = numero / divisor
    return f"El promedio de los elementos de la tupla es: {resultado:.1f}"
dato = promedio(tuple(random.randint(1, 50) for n in range(10)))
print(dato)

# Ejercicio 16: 
# Escribe un programa que encuentre el elemento más frecuente en una tupla de números.
from collections import Counter
numeros = (1, 5, 9, 89, 5, 22, 8)
contador = Counter(numeros)
comun, frecuencia = contador.most_common(1)[0] # cuenta los elementos y cuenta tambien la frecuencia...comun guarda el (1) y frecuencia guarda el [0]
print(f"El elemento mas comun es: {comun}, con una frecuencia de {frecuencia}")

# Ejercicio 17: 
# Dada una tupla de tuplas (cada tupla contiene un nombre y una puntuación), ordena las tuplas en función de la puntuación de mayor a menor.
tuplas_general =(
    ("eric", 89),
    ("helen", 9),
    ("carlos", 22),
    ("victor", 1),
    ("alex", 2)
)
tupla_ordenada = sorted(tuplas_general, key=lambda x:x[1], reverse=True)
print(tuple(tupla_ordenada))

# Ejercicio 18: 
# Crea una tupla con los nombres de varios países y muestra los países que empiezan con la letra 'E'.
paises = ("españa", "brasil", "costa rica", "Eslovenia", "estonia", "nigeria")
for letra in paises:
   if letra[0].lower() == "e":
        print(letra)

# Ejercicio 19: 
# Escribe una función que reciba una tupla de números y devuelva una nueva tupla con solo los números positivos.
def positive(tupla):
    positives = tuple(x for x in tupla if x > 0)
    return positives
dato = positive(tuple(random.randint(-50, 50) for n in range(8)))
print(dato)

# Ejercicio 20: 
# Dada una lista de tuplas que contienen nombre y edad, convierte la lista en una tupla y encuentra 
# la persona de mayor edad.
lista_tuplas = [
    ("eric", 56),
    ("maria", 80),
    ("helen", 42),
    ("alex", 26)
]
persona_mayor = max(lista_tuplas, key= lambda x:x[1])
print(persona_mayor)
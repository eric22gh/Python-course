# Día 17: Estructuras de Datos - Listas

# Las listas en Python son colecciones ordenadas de elementos que pueden ser de diferentes 
# tipos (números, cadenas, objetos, etc.). Son mutables, lo que significa que puedes cambiar sus elementos después de la creación. 
# Los elementos se acceden mediante índices, que comienzan en 0.

# Tips del Tema
# Listas: Son colecciones ordenadas de elementos que pueden ser de diferentes tipos.
# Índices: Los elementos de una lista se acceden mediante índices, que empiezan en 0.
# Mutabilidad: Las listas son mutables, lo que significa que sus elementos pueden cambiarse después de la creación.

############# Crear y Acceder a Listas

frutas = ["manzana", "banana", "cereza"]

# Acceder a Elementos de la Lista
print(frutas[0]) 
print(frutas[1]) 

# Modificar un Elemento de la Lista
frutas[1] = "pera"
print(frutas)  

########### Operaciones Comunes con Listas

# Añadir Elementos a la Lista
frutas.append("naranja")
print(frutas)  

# Insertar Elementos en una Posición Específica
frutas.insert(1, "plátano")
print(frutas)  

# Eliminar Elementos de la Lista
frutas.remove("pera")
print(frutas)  

# Eliminar el Último Elemento de la Lista
frutas.pop()
print(frutas)  

# Obtener la Longitud de la Lista
print(len(frutas))  

################ Operaciones Avanzadas con Listas

# Slicing (Segmentación)
# lista = ['manzana', 'plátano', 'cereza']

sublista = frutas[1:3]
print(sublista)  

# Concatenar Listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)  # Salida: [1, 2, 3, 4, 5, 6]

# Repetir Listas
lista_repetida = [0] * 4
print(lista_repetida)  # Salida: [0, 0, 0, 0]

# Ordenar Listas
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
print(numeros)  

# Ordenar Listas en Orden Descendente
numeros.sort(reverse=True)
print(numeros)  

# Invertir una Lista
numeros.reverse()
print(numeros)  

# Contar Elementos en una Lista
print(frutas.count("plátano"))  

# Encontrar el Índice de un Elemento
print(frutas.index("cereza"))  

############### Uso de Listas con Funciones y Bucles

# Usar Listas en Funciones
def sumar_lista(lista):
    return sum(lista)

numeros = [1, 2, 3, 4]
print(sumar_lista(numeros))  

# List Comprehensions
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrar Listas con List Comprehensions
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [num for num in numeros if num % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8]

par = [number for number in range(20) if number % 2 == 0]
print(f"Estos son los numeros pares de la lista: {par}")

# Aplicar Funciones a Listas
def doble(x):
    return x * 2

numeros = [1, 2, 3, 4]
dobles = list(map(doble, numeros))
print(dobles)  # Salida: [2, 4, 6, 8]

# Reducir Listas a un Solo Valor
from functools import reduce

def multiplicar(x, y):
    return x * y

numeros = [1, 2, 3, 4]
producto = reduce(multiplicar, numeros) # se multiplican por ellos
print(producto)  # Salida: 24

############# Crea una lista de nombres y usa un bucle for para imprimir cada nombre en mayúsculas.
nombres = ["ana", "luis", "marta"]
for nombre in nombres:
    print(nombre.upper())

############# Implementa una función que tome una lista de números y devuelva una lista de sus cuadrados.
def cuadrados_lista(lista):
    return [x**2 for x in lista]

numeros = [1, 2, 3, 4]
print(cuadrados_lista(numeros))  # Salida: [1, 4, 9, 16]

############# Usa una list comprehension para crear una lista de números impares del 1 al 20.
impares = [x for x in range(1, 21) if x % 2 != 0] # distinto de(!=)
print(impares) 

############## Dado un conjunto de números, encuentra y devuelve el número más grande usando una función de reducción.
numeros = [10, 20, 4, 45, 99]
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  

################################# Ejercicios
# Ejercicio 1: Crea una lista con los nombres de 5 ciudades y muestra el nombre de la tercera ciudad.
ciudades = ["Sanjose", "Edimburgo", "Lima", "Oslo", "Berlin"]
print(ciudades[2])

# Ejercicio 2: Modifica el nombre de la segunda ciudad en la lista del ejercicio 1 y muestra la lista actualizada.
ciudades[1] = "Athenas"
print(ciudades)

# Ejercicio 3: Añade dos ciudades más a la lista del ejercicio 1 y muestra la lista actualizada.
ciudades.append("Rekiavk")
ciudades.append("Ankara")
print(ciudades)

# Ejercicio 4: Elimina la primera ciudad de la lista del ejercicio 1 y muestra la lista actualizada.
ciudades.remove("Sanjose")
print(ciudades)

# Ejercicio 5: Escribe una función que tome una lista de números y devuelva el mayor número de la lista.
def mayor_num(lista10):
    return max(lista10)
numero = mayor_num(lista10 = [10, 500, 1230, 22, 52, 986, 2, 8])
print(f"Este es el numero mayor de la lista: {numero}")

# Ejercicio 6: Escribe una función que tome una lista de números y devuelva una nueva lista con los números en orden inverso.
def reverson(lista22):
    return lista22[::-1]

nueva_lista = reverson(lista22 = [10, 500, 1230, 22, 52, 986, 2, 8])
print(nueva_lista)

# Ejercicio 7: Escribe una función que tome dos listas y devuelva una nueva lista que contenga solo los elementos comunes a ambas listas.
def elementos_comunes(lista1 , lista2):
    return list(set(lista1) & set(lista2))

elementos = elementos_comunes(lista1=[1, 5004, 123, 12, 5, 96, 2, 8], lista2=[10, 5000, 1230, 22, 52, 986, 2, 8])
print(f"estos son los elementos comunes en ambas listas: {elementos}")

# Ejercicio 8: Escribe una función que tome una lista de cadenas de texto y devuelva una nueva lista con las cadenas en mayúsculas.
def lista_mayuscula(lista):
    nueva_lista = [names.upper() for names in lista]
    return nueva_lista

mayus = lista_mayuscula(["eric", "san jose", "ankara", "futbol"])
print(mayus)

# Ejercicio 9 (Teoría): ¿Qué es una lista en Python y cómo se diferencia de otras estructuras de datos como las tuplas?
# las lista son datos de diferentes tipos que son mutables y desordenados, a diferencia de otros tipos de datos que pueden ser inmutables, 
# ordenados o no permitir todo tipos de elementos.

# Ejercicio 10 (Práctica): Escribe un programa que tome una lista de números, elimine los duplicados y devuelva una lista con los elementos únicos,
#  en el mismo orden en que aparecieron por primera vez.
lista =[1, 5004, 123, 123, 12, 5, 5, 96, 2, 8, 8]
lista_sin_duplicados = []
for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(lista_sin_duplicados)


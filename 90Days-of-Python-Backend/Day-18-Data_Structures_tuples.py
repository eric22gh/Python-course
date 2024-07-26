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

# Usar tuplas en funciones
def calcular_area(base, altura):
    return base * altura

# Tupla como argumento de función
dimensiones = (5, 10)
area = calcular_area(*dimensiones)
print(area)  

# Iterar sobre una lista de tuplas
pares = [(1, 2), (3, 4), (5, 6)]
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

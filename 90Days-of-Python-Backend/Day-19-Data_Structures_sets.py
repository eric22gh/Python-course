###### Estructura de datos conjuntos #####

# Definición del Tema
# Conjuntos: Es una estructura de datos que permite almacenar colecciones de elementos únicos y no ordenados.

# Tips del Tema
# Conjuntos: Son colecciones de elementos únicos y no ordenados.
# Operaciones de conjuntos: Soportan operaciones matemáticas como unión(|), intersección(&) y diferencia.
# Mutabilidad: Los conjuntos son mutables, pero sus elementos deben ser inmutables (por ejemplo, números, cadenas de texto, tuplas).

# Crear un conjunto
numeros = {1, 2, 3, 4, 5}

# Añadir un elemento al conjunto
numeros.add(6)
numeros.add(7)
print(numeros)  

# Eliminar un elemento del conjunto
numeros.remove(3)
print(numeros)  

# Comprobar si un elemento está en el conjunto
print(4 in numeros)  
print(3 in numeros)  
print(6 in numeros)

# Operaciones de Conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}

# Unión de conjuntos
union = pares | impares
print(union)  

# Intersección de conjuntos
interseccion = pares & impares # devuelve un nuevo conjunto que contiene solo los elementos que son comunes en ambos conjuntos.
print(interseccion)  # saldra vacio porque no hay elementos comunes en los 2 conjuntos

# Diferencia de conjuntos
diferencia = pares - {2, 4} # no va imprimir en pantalla los numeros  2, 4
print("eric")
print(diferencia)  

# Diferencia simétrica de conjuntos
print("edwards")
diferencia_simetrica = pares ^ {4, 6, 8, 10}
print(diferencia_simetrica)  

# Programa que tome dos listas y devuelva una lista de elementos únicos que están en ambas listas.
def elementos_unicos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccion = conjunto1 & conjunto2
    return list(interseccion)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_unicos(lista1, lista2)
print(resultado)  

# función que reciba una cadena de texto y devuelva una lista con todos los caracteres únicos en la cadena.
def caracteres_unicos(cadena):
    return list(set(cadena))

cadena = "abracadabra"
resultado = caracteres_unicos(cadena)
print(resultado)  

# Programa que tome una lista de números y devuelva True si hay elementos duplicados y False si todos son únicos.
def hay_duplicados(lista):
    return len(lista) != len(set(lista))

numeros = [1, 2, 3, 4, 5, 3]
print(hay_duplicados(numeros))  

numeros = [1, 2, 3, 4, 5]
print(hay_duplicados(numeros))  

# Programa que elimine los elementos duplicados de una lista manteniendo el orden original de los elementos.
def eliminar_duplicados(lista):
    conjunto = set()
    lista_unica = []
    for elemento in lista:
        if elemento not in conjunto:
            lista_unica.append(elemento)
            conjunto.add(elemento)
    return lista_unica

numeros = [1, 2, 3, 4, 5, 3, 2, 1]
resultado = eliminar_duplicados(numeros)
print(resultado)  

################# ejercicios 
# Ejercicio 1: Crea un conjunto con los números del 1 al 5 y muestra el conjunto.
setss = {1, 2, 3, 4, 5}
print(setss)

# Ejercicio 2: Añade el número 6 al conjunto del ejercicio 1 y muestra el conjunto actualizado.
setss.add(6)
print(setss)

# Ejercicio 3: Elimina el número 3 del conjunto del ejercicio 1 y muestra el conjunto actualizado.
setss.remove(3)
print(setss)

# Ejercicio 4: Escribe una función que tome dos conjuntos y devuelva su unión.
def union_sets(conjunto_1, conjunto_2):
    union = conjunto_1 | conjunto_2
    # lista = list(union)
    # lista.sort()
    # union2 = set(lista)
    return union
result = union_sets({22, 56, 89, 23},{10, 5, 6,3})
print(result)

# Ejercicio 5: Escribe una función que tome dos conjuntos y devuelva su intersección.
def interseccion_set(conjunto_4, conjunto_3):
    intersecc = conjunto_4.intersection(conjunto_3)
    return intersecc
res = interseccion_set({2, 5, 8, 6}, {2, 10, 8, 100, 6})
print(f"los 2 conjuntos tienen una interseccion en: {res}")

# Ejercicio 6: Escribe una función que tome dos conjuntos y devuelva su diferencia.
def diferencia_set(conjunto_7, conjunto_8):
    diferent = conjunto_7.difference(conjunto_8)
    return diferent
print(diferencia_set({2, 5, 8, 6}, {2, 10, 8, 100, 6}))

# Ejercicio 7: Escribe una función que tome dos conjuntos y devuelva su diferencia simétrica.
def symmetric_difference(conjunto_9, conjunto_10):
    resultado = conjunto_9.symmetric_difference(conjunto_10)
    return resultado
print(symmetric_difference({2, 5, 8, 6}, {2, 10, 8, 100, 6}))

# Ejercicio 8: Escribe una función que tome un conjunto de números y devuelva una lista con los números ordenados.
def order_set(set_1):
    lista_1 = list(set_1)
    lista_1.sort()
    return lista_1
print(order_set((22, 1, 0, 100, 23, 5, 10, 93)))

# Ejercicio 9 (Teoría): ¿Qué es un conjunto en Python y cómo se diferencia de una lista y una tupla?
# un conjunto es una estructura de dato mutable, no ordenada y unicos en python, sirve para tener datos no duplicados y su diferencia principal con las tuplas 
# es que las tuplas son inmutables, mientras que los conjuntos son mutables.

# Ejercicio 10 (Práctica): Escribe un programa que tome una lista de números con elementos duplicados y devuelva una lista con los elementos únicos 
# en el mismo orden en que aparecieron por primera vez, utilizando conjuntos.
lista2 = [22, 10, 1, 100, 22, 5, 1, 50, 96, 5, 1000]
new_list = []
seen = set()
for numero in lista2:
    if numero not in new_list:
        seen.add(numero)
        new_list.append(numero)
print(type(new_list))
print(new_list)

# Ejercicio 11:
# Crea un conjunto con cinco palabras y muestra solo las palabras que tengan más de cuatro letras.
import random, string
set_palabras = {"".join(random.choices(string.ascii_letters, k=random.randint(2, 6)))for x in range(5)}
mayor_4 = {l for l in set_palabras if len(l) > 4}
print(mayor_4)

# Ejercicio 12:
# Dado un conjunto de números enteros, escribe un programa que elimine todos los números pares del conjunto.
set_numeros = {random.randint(1, 100)for n in range(8)}
impares = {p for p in set_numeros if p % 2 != 0}
print(impares)

# Ejercicio 13:
# Escribe una función que reciba dos conjuntos y devuelva True si uno es subconjunto del otro, y False en caso contrario.
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
sub_conjunto = set(random.sample(list(conjunto), k=random.randint(1, len(conjunto))))
def verify(conjunto, sub_conjunto):
    return sub_conjunto.issubset(conjunto) # issubset() es para verificar subconjuntos.
datos = verify(conjunto, sub_conjunto)
datos1 = verify(conjunto, {15, 30, 85})
print(datos1)
print(datos)

# Ejercicio 14:
# Escribe un programa que convierta una lista con elementos duplicados en un conjunto y muestre cuántos elementos únicos hay.
lista_numeros = [1, 56, 89, 22, 89, 5, 1, 23, 77, 54, 10, 5]
set_unicos = set(lista_numeros)
print(f"esta es la cantidad de elementos unicos en el conjunto: {len(set_unicos)}")

# Ejercicio 15:
# Escribe una función que tome un conjunto de números y devuelva un nuevo conjunto con los cuadrados de cada número.
def elevar_numero(conjunto_numeros):
    new_set = {num ** 2 for num in conjunto_numeros}
    return new_set
data = elevar_numero({1, 56, 89, 22, 89, 5, 1, 23, 77, 54, 10, 5})
print(data)

# Ejercicio 16:
# Escribe una función que tome dos conjuntos y verifique si ambos conjuntos tienen al menos un elemento en común.
def comun(conjunto1, conjunto2):
    elemento_comun = conjunto1.intersection(conjunto2)
    if elemento_comun:
        return f"El elemento que tienen en comun los 2 conjuntos es: {elemento_comun}"
    else:
        return "No tienen ningun elemento en comun"
datos = comun({1,5,8,4},{2, 10, 20, 7, 1})
print(datos)

# Ejercicio 17:
# Dado un conjunto de números, elimina el elemento más pequeño del conjunto y muestra el conjunto resultante.
conjunto_1 = {56, 89, 22, 89, 5, 1, 23, 77, 54, 10, 5}
if conjunto_1: 
    elemento_menor = min(conjunto_1)
    conjunto_1.remove(elemento_menor)
    print(conjunto_1)
else:
    print("El conjunto está vacío.")

# Ejercicio 18:
# Escribe una función que reciba una lista de palabras y devuelva un conjunto con las palabras que empiezan con vocales.
def palabras (lista_palabras):
    vocales = "aeiou"
    cojunto_palabras = set()
    for palabras in lista_palabras:
        if palabras[0].lower() in vocales:
            cojunto_palabras.add(palabras)
    return cojunto_palabras
dat = palabras(["eric", "rosa", "helen", "argentina", "noruega", "escocia"])
print(dat)

# Ejercicio 19:
# Dado un conjunto de números, escribe un programa que devuelva el número de elementos que son múltiplos de 3.
set_multiplos = set(random.randint(1, 100)for n in range(10))
for multiplos in set_multiplos:
    if multiplos % 3 == 0:
        print(multiplos)
        
# Ejercicio 20:
# Escribe un programa que tome dos conjuntos de números y verifique si son disjuntos (es decir, si no tienen elementos en común).
set_1 = {1, 56, 28, 89, 22, 21, 10, 23, 30}
set_2 = {1, 56, 97, 85, 27, 35, 10, 23, 30}
if set_1.isdisjoint(set_2): # isdisjoint(): comprueba si los conjuntos no tienen elementos en común
    print("Los dos conjuntos son disjuntos ya que no tienen elementos en común.")
else:
    elementos_comunes = set_1.intersection(set_2)
    print(f"Los dos conjuntos sí tienen elementos en común y son: {elementos_comunes}")
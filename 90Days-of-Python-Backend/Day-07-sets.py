# Día 7: Conjuntos y Operaciones con Conjuntos

# Definición del Tema
# Son colecciones desordenadas de elementos únicos y inmutables.

# Tips del Tema
# son colecciones de elementos únicos, sin orden específico.
# permiten operaciones matemáticas como unión, intersección y diferencia.
# Métodos importantes incluyen add(), remove(), union(), intersection(), y difference().

# metodos de un conjunto
frutas = {"manzana", "banana", "cereza"}

# # Añadir un elemento
# frutas.add("durazno")
# # frutas[0] = "pera" # da error porque son inmutables
# print(frutas)  

# conjunto = set()

# conjunto.add(1)
# conjunto.add(2)
# conjunto.add(3)
# conjunto.add("eric")
# conjunto.add(5.2)
# conjunto.add(False) # se pone de primero porque set, da elementos ordenados

# print(conjunto) 

# # Eliminar un elemento
# frutas.remove("banana")
# print(frutas)  

# # Eliminar un elemento existente
# conjunto.discard(3)
# print(conjunto)  

# conjunto.discard(10)  # No lanza error, Intentar eliminar un elemento que no existe
# print(conjunto) 

# # Verificar pertenencia
# print("manzana" in frutas) 
# print("banana" in frutas)   

# # Limpiar el conjunto
# # conjunto.clear()
# # print(conjunto)  

# #Devuelve un nuevo set con los que unio anteriormente.
# setA = {1,100, 2, 3}
# setB = {3, 4, 5}
# set_union = setA.union(setB)
# print(set_union) 

# # devuelve un conjunto de los elementos que estan en las 2 listas
# set_intersection = setA.intersection(setB)
# print(set_intersection) 

# # Devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo.
# set_difference = setA.difference(setB)
# print(set_difference) 


# # Devuelve un nuevo conjunto con los elementos que están en uno de los conjuntos, pero no en ambos.
# set_sym_diff = setA.symmetric_difference(setB)
# print(set_sym_diff)  

# ############ conjuntos o sets mutables
# # también existen conjuntos inmutables llamados frozenset. Estos conjuntos no pueden ser modificados después de su creación.

# # Crear un frozenset
# conjunto_inmutable = frozenset([1, 2, 3, 3]) # crea una lista y la convierte en set
# print(conjunto_inmutable)  # da solo un 3 porque no admite elementos duplicados

# # conjunto_inmutable.add(4)  # da error

# # Lista con elementos duplicados
# lista = [1, 2, 2, 3, 4, 4, 5]
# # Convertir lista a conjunto para eliminar duplicados
# conjunto = set(lista)
# print(conjunto) 

# # Convertir de nuevo a lista
# lista_sin_duplicados = list(conjunto)
# print(lista_sin_duplicados + lista)  

# lol = lista_sin_duplicados + lista
# print(type(lol))
# print(lol)

# lal = set(lol)
# print(type(lal))
# print(lal)

# ################## Ejercicios
# # Ejercicio 1: Crea un conjunto de tus colores favoritos y muéstralo.
# colores = {"rojo", "negro", "verde", "turquesa", "cafe"}
# print(colores)

# # Ejercicio 2: Añade un nuevo color al conjunto y muéstralo.
# colores = {"rojo", "negro", "verde", "turquesa", "cafe"}
# colores.add("blanco")
# print(colores)

# # Ejercicio 3: Elimina un color del conjunto y muéstralo.
# colores.discard("verde")
# print(colores)

# # Ejercicio 4: Verifica si un color específico está en el conjunto.
# for color in colores:
#     print(color)
#     if color == "verde":
#         print(f"encontre el color: {color}")
# else:
#     print(f"el color:{color} no esta en la lista")

# # Ejercicio 5: Realiza la unión de dos conjuntos de números y muéstrala.
# num1 = {1, 55, 5, 80}
# num2 = {10, 100, 62, 22}
# union_de_sets = num1.union(num2)
# print(union_de_sets)

# # Ejercicio 6: Realiza la intersección de dos conjuntos de números y muéstrala.
# num1 = {1, 55, 5, 80}
# num3 = {23, 63, 5}
# insertion = num1.intersection(num3)
# print(insertion)

# # Ejercicio 7: Realiza la diferencia de dos conjuntos de números y muéstrala.
# num1 = {1, 55, 5,100, 80}
# num5 = {1, 55, 5, 80, 44,}
# diferencia = num1.symmetric_difference(num5)
# print(diferencia)

# # Ejercicio 8: Define una función que tome dos conjuntos y devuelva su intersección.
# set1 = {1, 5, 3, 55, 2}
# set2 = {1, 5, 3, 56, 20, 80}
# def interseccion (set1,set2):
#     inter = set1.intersection(set2)
#     print(f"los numeros que se intersecan son:{inter}")

# interseccion(set1,set2)

# # Ejercicio 9 (Teoría): ¿Qué es un conjunto y cuáles son sus características principales?
# # un conjunto es un tipo de dato utilizado para ocaciones en donde no se necesitan datos duplicados, 
# # sus caracteristicas son: son mutales, permite operaciones aritmeticas, no son ordenados y no admiten duplicados.

# # Ejercicio 10 (Práctica): Escribe un programa que tome dos listas de números, las convierta en conjuntos y muestre su intersección.
# lista1 = [22, 5, 100, 55, 68]
# lista2 = [33, 4, 8, 69, 29, 68]
# def covert (lista1,lista2):
#     conversion = set(lista1)
#     conversion2 = set(lista2)
#     intersec = conversion.intersection(conversion2)
#     print(f"la lista1 y la lista2 se intersecan en:{intersec}")

# covert(lista1,lista2)

# Ejercicio 11: Crea un conjunto con los primeros 15 números enteros y elimina todos los números divisibles por 5.
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
new_ = list(conjunto)
for num in new_: # cuando se itera con for datos int de un conjunto, los datos ya no sigen siendo sets, por lo tanto las funciones de set ya no tiene efecto.
    if num % 5 == 0:
        new_.remove(num)
        conjunto = set(new_)
print(conjunto)

# Ejercicio 12: Define una función que tome un conjunto y devuelva un nuevo conjunto con los elementos en orden alfabético (si son cadenas) 
# o en orden numérico (si son números).
def new_set(dato):
    lista = sorted(dato)
    return set(lista)

dato = new_set({"rojo", "negro", "verde", "turquesa", "cafe"})
print(dato)

# Ejercicio 13: Dado un conjunto de números, muestra todos los números menores que 10.
# sets1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# for numbers in sets1:
#     if numbers < 10:
#         print(numbers) # no es bueno imprimir adentro de bucles.

sets1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
numebers_less_10 = set()
for num in sets1:
    if num < 10:
        numebers_less_10.add(num)  
print(numebers_less_10)

# Ejercicio 14: Crea dos conjuntos de números y muestra la diferencia simétrica entre ellos.
set3 = {1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15}
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15}
print(set3.symmetric_difference(set4))

# Ejercicio 15: Define una función que tome dos conjuntos y devuelva un conjunto con los elementos que están en ambos conjuntos, 
# pero eliminando los elementos que aparecen más de una vez.
def new_set(set7, set8):
    data = set7.intersection(set8)
    return data

data = new_set({1, 5, 6, 23, 23, 5, 10, 57, 10}, {1, 10, 5, 100, 10, 88, 5, 7})
print(data)

# Ejercicio 16: Crea un conjunto de letters del alfabeto y muestra solo las letters que aparecen en las palabras "hello" y "world".
data1 = set("abcdefghijklmnopqrstuvwxyz")
hello = set("hello world")
resultado = data1.intersection(hello) # datos que son de hello y estan presentes en data1

for letter in resultado:
    print(letter)

# Ejercicio 17: Crea dos conjuntos de palabras y muestra el conjunto de palabras que están en el primer conjunto pero no en el segundo, en orden alfabético.
set5 = {"rojo", "negro", "verde", "turquesa", "cafe", "arco", "abba"}
set0 = {"rojo", "negro", "verde", "turquesa", "blanco", "flecha", "artur"}
data10 = set5.difference(set0)
new_list = list(data10)
new_list.sort()
print(new_list)

# Ejercicio 18: Dado un conjunto con valores duplicados, convierte el conjunto a una lista, elimina duplicados y luego vuelve a convertirlo a un conjunto.
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 3, 14, 5}
list_1 = list(set_1)  
new_set_1 = set(list_1)  # set elimina los duplicados automaticamente
print(new_set_1) 

# Ejercicio 19: Define una función que tome un conjunto de números y devuelva un nuevo conjunto con los cuadrados de cada número.
def cuadrados_set(sets):
    return {number ** 2 for number in sets}
data = cuadrados_set({1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 3, 14, 5})
print(data)

# Ejercicio 20: Crea un conjunto de números del 1 al 50 y muestra solo los números que son múltiplos de 7.
set_for = set()
for set_created in range(1, 51):
    calculo = set_created % 7
    if calculo == 0:
        set_for.add(set_created)
print(set_for)

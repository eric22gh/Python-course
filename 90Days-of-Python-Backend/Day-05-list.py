# Día 5: Listas y Operaciones con Listas
# Las listas son una estructura de datos fundamental en Python. Son colecciones ordenadas y mutables, 
# lo que significa que puedes modificar su contenido después de crearlas. 
# Cada elemento en una lista tiene una posición o índice, comenzando desde 0.

# Tips del Tema
# Las listas se definen usando corchetes [] y los elementos se separan por comas.

# Índices:
# Los índices comienzan en 0. El primer elemento de la lista tiene índice 0, el segundo tiene índice 1, y así sucesivamente.
# Los índices negativos se utilizan para acceder a los elementos desde el final de la lista, con -1 refiriéndose al último elemento.

# Métodos de listas:
# append(): Agrega un elemento al final de la lista.
# remove(): Elimina la primera aparición de un elemento específico.
# sort(): Ordena los elementos de la lista en orden ascendente.
# reverse(): Invierte el orden de los elementos en la lista.
# pop(): Elimina y devuelve el elemento en la posición especificada.
# copy(): Devuelve una copia superficial de la lista.
# extend(): Agrega todos los elementos de otra lista.

# Acceso a elementos
frutas = ["manzana", "banana", "cereza", "limon"]
print(frutas[0])  
print(frutas[1])  
print(frutas[2])  
print(frutas)

# Agregar un elemento al final de la lista
frutas.append("durazno")
print(frutas) 

# Eliminar un elemento específico
frutas.remove("banana")
print(frutas)  

# elimina y devuelve el elemento en la posición especificada. Si no se especifica una posición, elimina y devuelve el último elemento.
frutas = ["manzana", "banana", "cereza"]
fruta_eliminada = frutas.pop(1)
print(fruta_eliminada)  #
print(frutas)  

ultima_fruta = frutas.pop()
print(ultima_fruta) 
print(frutas)  

# Ordenar la lista
frutas.sort()
print(frutas)  

#invierte el orden de los elementos en la lista.
frutas = ["manzana", "banana", "cereza"]
frutas.reverse()
print(frutas)  

frutas.insert(1, "kiwi")  # Inserta "kiwi" en la posición 1
print(frutas)  

print(len(frutas)) # devuelve cuantos elementos hay en una lista

#devuelve el número de veces que un elemento aparece en la lista.
frutas = ["manzana", "banana", "cereza", "manzana"]
print(frutas.count("manzana")) 

#devuelve una copia superficial de la lista.
frutas = ["manzana", "banana", "cereza"]
frutas_copia = frutas.copy()
print(frutas_copia) 

# elimina todos los elementos de la lista.
# frutas = ["manzana", "banana", "cereza"]
# frutas.clear()
# print(frutas) 

# extiende la lista agregando todos los elementos de otra lista.
frutas = ["manzana", "banana"]
otras_frutas = ["cereza", "durazno"]
frutas.extend(otras_frutas)
print(frutas) 

#devuelve el índice del primer elemento con el valor especificado.
frutas = ["manzana", "banana", "cereza"]
print(frutas.index("banana"))  

#Concatenar Listas
otras_frutas = ["pera", "uva"]
todas_las_frutas = frutas + otras_frutas
print(todas_las_frutas) 

# seccionar listas
print(frutas[1:3]) 

# verificar la existencia de un elemento
print("manzana" in frutas)  
print("banana" in frutas)  

# iterar sobre una lista
for fruta in frutas:
    print(fruta)

############ Ejercicios
# Ejercicio 1: Crea una lista de tus verduras favoritas y muéstrala.
verduras = ["papa", "camote", "pepino", "remolacha", "yuca"]
print(verduras)

# Ejercicio 2: Añade una nueva elemento a la lista y muéstrala.
verduras.append("tiquisque")
print(verduras)

verduras.insert(1, "calabaza")
print(verduras)

# Ejercicio 3: Elimina un elemento de la lista y muéstrala.
verduras.remove("camote")
print(verduras)

verduras.pop(0)
print(verduras)

# Ejercicio 4: Ordena la lista de frutas alfabéticamente y muéstrala.
verduras.sort()
print(verduras)

# Ejercicio 5: Define una lista de números y calcula su suma.
numeros = [1, 22, 56, 60, 100]
suma = 0
for num in numeros:
    suma +=  num
print(suma)
    
# Ejercicio 6: Define una lista de números y encuentra el número máximo.
numeross = [1, 22, 2000, 80, 56, 60, 100, 1000]
for z in numeross:
    print(z)
eric = max(numeross)
print(eric)

# Ejercicio 7: Define una lista de números y encuentra el número mínimo.
numeross1 = [1, 22, 2000, 80, 56, 60, 100, 1000]
for a in numeross1:
    print(a)
minimo = min(numeross1)
print(minimo)

# Ejercicio 8: Define una lista de números y calcula su promedio.
numeross2 = [1, 22, 2000, 80, 56, 60, 100, 1000]
suma = sum(numeross2)
promedio = suma / len(numeross2)
print(promedio)

# Ejercicio 9 (Teoría): ¿Qué es una lista y cómo se diferencia de una tupla en Python?
# las listas y la tuplas pueden guardar valores de tipo: int, float, str, bool, 
# sin embargo las listas son mutables y las tuplas son inmutables(no se pueden modificar)

# Ejercicio 10 (Práctica): Escribe un programa que pida al usuario varios nombres y los almacene en una lista. 
# Luego, ordena la lista alfabéticamente y muéstrala.
name = [input("escribe la palabra:"), input("escribe la segunda palabra:"), input("escribe la tercera palabra:"), input("escribe la cuarta palabra:")]
print(name)
name.sort()
print(name)

####### o
names = []
while True:
    nombre = input("Ingresa un nombre (o presiona la tecla espacio para terminar): ")
    if nombre == " ":
        break # darle la tecla espacio para terminar el bucle
    names.append(nombre)

dato = names.sort()
print(dato)
print("Nombres ordenados alfabéticamente:")
for nombre in names:
    print(nombre) # imprimirlo sin corchetes
print(names)

# Ejercicio 11: Contar Elementos
# Crea una lista con números enteros y cuenta cuántos elementos son mayores a 10.
numeros = [10, 56, 98, 5, 2, 68, 100]
lista = []
for number in numeros:
    if number > 10: 
        lista.append(number)
contar = len(lista)
print(f"los numeros mayores a 10 en la lista son: {contar}")

# Ejercicio 12: Filtrar Elementos
# Define una lista de números y crea una nueva lista que contenga solo los números pares.
numeros = [10, 56, 98, 5, 2, 68]
new_list = []
for number in numeros:
    if number % 2 == 0:
        new_list.append(number)
print(new_list)

# Ejercicio 13: Eliminar Duplicados
# Crea una lista con elementos duplicados y elimina los duplicados manteniendo el orden original.
lista = [1, 10, 55, 55, 22, 100, 8, 100, 1]
lista_new = []
for n in lista:
    if n not in lista_new:
        lista_new.append(n)
print(lista_new)
##### o
vista = set()
lista_n = []
for n in lista:
    if n not in vista:
        vista.add(n)
        lista_n.append(n)
print(lista_n)

# Ejercicio 14: Números Comunes
# Dadas dos listas, encuentra los números que aparecen en ambas listas.
lista1 = [1, 10, 55, 22, 100, 8, 108]
lista2 = [1, 10, 77, 55, 22, 100, 8]
comunes = set(lista1).intersection(lista2)
print(comunes)

# Ejercicio 15: Reverso
# Define una lista de strings y crea una nueva lista con los strings en orden inverso.
cadena = ["xebra", "zebra", "leon", "araña", "tigre", "dinosaurio"]
cadena.reverse()
print(cadena)

# Ejercicio 16: Producto de Elementos
# Crea una lista de números y calcula el producto de todos los elementos en la lista.
# El producto de una lista de números es el resultado de multiplicar todos esos números entre sí. Por ejemplo, si tienes la lista de números 
# 2,3,4 el producto sería 2 × 3 × 4 = 24 / El producto de un número se refiere al resultado de multiplicar ese número por otro.
numeros = [2, 3, 4, 5]
multi = 1
for num in numeros: 
    multi *= num
print(multi)

# Ejercicio 17: Sumar Elementos en un Rango
# Dada una lista de números, suma solo los elementos que están en un rango específico (por ejemplo, entre 10 y 20).
def sumar_lista(lista):
    lust = []
    for num in lista:
        if 10 < num < 20:
            lust.append(num)
    return sum(lust)
dato = sumar_lista([2, 11, 15, 18, 22, 55])    
print(dato)

# Ejercicio 18: Crear una Lista de Cuadrados
# Crea una lista con números enteros y genera una nueva lista con el cuadrado de cada número.
lista = [2, 11, 15, 18, 22, 55]
new = []
for n in lista:
    cuadrado = n ** 2
    new.append(cuadrado)
print(new)

# Ejercicio 19: Lista de Longitud Par
# Define una lista de strings y crea una nueva lista con solo aquellos strings cuya longitud es par.
dato = ["xebra", "zebra", "leon", "araña", "tigre", "dinosaurio"]
new = []
for n in dato:
    contar = len(n)
    if contar % 2 == 0:
        new.append(contar)
print(new)

########### 
dato = ["xebra", "zebra", "leon", "araña", "tigre", "dinosaurio"]
new_ = []
for n in dato:
    if len(n) % 2 == 0:
        new_.append(n)
print(new_)

# Ejercicio 20: Sumar Posiciones
# Dada una lista de números, crea una lista donde cada elemento sea la suma de los números en todas las posiciones anteriores.
lista = [2, 11, 22, 55]
hub = []
suma = 0
for p in lista:
    suma += p
    hub.append(suma)
print(hub)
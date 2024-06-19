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

# Fundamentos del Tema con Código

# Definición de una lista
frutas = ["manzana", "banana", "cereza", "limon"]
# Acceso a elementos
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: banana
print(frutas[2])  # Salida: cereza
print(frutas)

# Métodos Comunes de Listas

# Agregar un elemento al final de la lista
frutas.append("durazno")
print(frutas) 

# Eliminar un elemento específico
frutas.remove("banana")
print(frutas)  

# elimina y devuelve el elemento en la posición especificada. Si no se especifica una posición, elimina y devuelve el último elemento.
frutas = ["manzana", "banana", "cereza"]
fruta_eliminada = frutas.pop(1)
print(fruta_eliminada)  # Salida: banana
print(frutas)  # Salida: ['manzana', 'cereza']

ultima_fruta = frutas.pop()
print(ultima_fruta)  # Salida: cereza
print(frutas)  # Salida: ['manzana']

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
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'durazno']

#devuelve el índice del primer elemento con el valor especificado.
frutas = ["manzana", "banana", "cereza"]
print(frutas.index("banana"))  # Salida: 1

#Concatenar Listas
otras_frutas = ["pera", "uva"]
todas_las_frutas = frutas + otras_frutas
print(todas_las_frutas)  # Salida: ['manzana', 'kiwi', 'cereza', 'durazno', 'pera', 'uva']

# seccionar listas
print(frutas[1:3])  # Salida: ['kiwi', 'cereza']

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
        break
    names.append(nombre)

names.sort()
print("Nombres ordenados alfabéticamente:")
for nombre in names:
    print(nombre) # imprimirlo sin corchetes

print(names)



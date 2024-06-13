# Funciones en Python
# Son bloques de código reutilizables que nos permiten
# encapsular una serie de instrucciones bajo un nombre y ejecutarlas cuando las necesitemos. 
# Esto promueve la modularidad y la reutilización del código, lo cual es fundamental en el desarrollo de software.

# Tips del Tema
# Definición de funciones: Se usa la palabra clave def para definir una función.
# Parámetros y argumentos: Las funciones pueden tomar parámetros para generalizar su comportamiento.
# Valor de retorno: Las funciones pueden devolver valores usando la palabra clave return.

# Ejemplo
def saludar():
    print("¡Hola, Edwards!")

# Llamada a la función
saludar() 
print(saludar) # no se puede, por lo menos asi.

####### Funciones con Parámetros

def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# Llamada a la función con un argumento
saludar("Ana")  # Salida: ¡Hola, Ana!

def name(nam): # parametro va adentro
    print(f"hola, {nam}")
name("hernandez")

###### Funciones con Valor de Retorno

def suma(a, b):
    return a + b # permite que el resultado de la función sea utilizado en otras partes del programa.

# Llamada a la función y almacenamiento del resultado en una variable
resultado = suma(5, 3)
print(resultado)  

def resta(a, b):
    return a - b

rest = resta(10, 5)
print(rest)


# Función con parámetro opcional y valor de retorno
def calcular_descuento(total, descuento=0.1): # el descuento es en float
    return total * (1 - descuento)

# Llamada a la función y almacenamiento del resultado
total_con_descuento = calcular_descuento(100, 0.2)  # Aplica un 20% de descuento
print(f"Total con descuento: ${total_con_descuento:.2f}")

# formula en programacion para el descuento: total×(1−descuento)

#########################

# Ejercicios

# Ejercicio 1: Define una función que tome dos números y devuelva su suma.
def sun(i, o):
    return i + o
pop = sun(5, 36)
print(pop)

# Ejercicio 2: Define una función que tome una cadena y la imprima en mayúsculas.
def pal(nombre):
    return nombre.upper() # todo mayuscula
nombre_mayuscula = pal("edwards")
nombre_mayuscula1 = pal("hernandez")
nombre_mayuscula3 = pal("eric")

print(nombre_mayuscula)
print(nombre_mayuscula1)
print(nombre_mayuscula3)

# upper(): Convierte todos los caracteres de la cadena a mayúsculas.
# lower(): Convierte todos los caracteres de la cadena a minúsculas.
# len(): cuantos caracteres tiene una cadena
# capitalize(): Convierte la primera letra de la cadena a mayúscula y las demás a minúsculas.
# title(): Convierte la primera letra de cada palabra a mayúscula.
# strip(): Elimina los espacios en blanco al inicio y al final de la cadena.
# lstrip(): Elimina los espacios en blanco al inicio de la cadena.
# rstrip(): Elimina los espacios en blanco al final de la cadena.
# split(): Divide la cadena en una lista usando el delimitador especificado (por defecto, el espacio).
# join(): Une los elementos de una lista en una cadena, utilizando un separador especificado.
# replace(): Reemplaza todas las apariciones de una subcadena por otra subcadena.
# find(): Devuelve el índice de la primera aparición de una subcadena. Devuelve -1 si no se encuentra.
# index(): Igual que find(), pero lanza una excepción si la subcadena no se encuentra.
# startswith(): Devuelve True si la cadena comienza con la subcadena especificada.
# endswith(): Devuelve True si la cadena termina con la subcadena especificada.
# count(): Devuelve el número de veces que una subcadena aparece en la cadena.
# format(): Formatea la cadena usando placeholders.
# isalpha(): Devuelve True si todos los caracteres en la cadena son letras.
# isdigit(): Devuelve True si todos los caracteres en la cadena son dígitos.
# isalnum(): Devuelve True si todos los caracteres en la cadena son letras o dígitos.
# islower(): Devuelve True si todos los caracteres en la cadena están en minúsculas.
# isupper(): Devuelve True si todos los caracteres en la cadena están en mayúsculas.

# Ejercicio 3: Define una función que tome un número y devuelva su cuadrado.
# el cuadrado de un numero lado x hancho o numero elevado a la 2
def cuadrado(o):
    return o ** 2
cuadra = cuadrado(5)
cuadra1 = cuadrado(10)
cuadra2 = cuadrado(20)

print(cuadra)
print(cuadra1)
print(cuadra2)
# print(f"el cuadrado de {o} es {cuadra}")

# Ejercicio 4: Define una función que tome una lista de números y devuelva su promedio.
def promedio(k, h, l):
    numeros = k + h + l
    return numeros / 3
promedy = promedio(10,10,10)
promedy1 = promedio(100,20,30)
promedy2 = promedio(15,22,66)
print(promedy)
print(promedy1)
print(promedy2)

# Versión mejorada para aceptar una lista de números y calcular el promedio
def promedio_lista(numeros):
    suma = sum(numeros)
    return suma / len(numeros) if len(numeros) > 0 else 0

# Ejemplos de uso con listas de números
promedio_lista_1 = promedio_lista([10, 10, 10, 40])
promedio_lista_2 = promedio_lista([100, 20, 30])
promedio_lista_3 = promedio_lista([15, 22, 66])

print(promedio_lista_1)  
print(promedio_lista_2)  
print(promedio_lista_3)  


# Ejercicio 5: Define una función que tome una lista de palabras y devuelva la más larga.
def contar(a):
    return len(a)

count = contar("hernandez")
count1 = contar("ericjbvkdbvb")
count2 = contar("edwards")

if count > count1 and count > count2:
    print("hernandez es el que tiene mas letras")
elif count == count1 and count == count2:
    print("hernandez tiene las mismas letras que los demas")
elif count1 > count and count1 > count2:
    print("ericjbvkdbvb es el que tiene mas letras")
elif count1 == count and count1 == count2:
    print("ericjbvkdbvb tiene las mismas letras que los demas")
elif count2 > count and count2 > count1:
    print("edwards es el que tiene mas letras" )
elif count2 == count and count2 == count1:
    print("edwards tiene las mismas letras que los demas")
else:
    print("no e encontraron las letras")
###############################################
def palabra_mas_larga(lista_palabras):
    palabra_mas_larga = ""
    longitud_mas_larga = 0

    for palabra in lista_palabras:
        longitud_actual = len(palabra)
        if longitud_actual > longitud_mas_larga:
            palabra_mas_larga = palabra
            longitud_mas_larga = longitud_actual

    return palabra_mas_larga

# Ejemplos de uso con diferentes listas de palabras
palabras_1 = ["hernandez", "ericjbvkdbvb", "edwards"]
palabras_2 = ["python", "programacion", "lenguaje"]

palabra_larga_1 = palabra_mas_larga(palabras_1)
palabra_larga_2 = palabra_mas_larga(palabras_2)

print("En la lista 1, la palabra más larga es:", palabra_larga_1)
print("En la lista 2, la palabra más larga es:", palabra_larga_2)

# Ejercicio 6: Define una función que tome una cadena y devuelva la cantidad de vocales.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

numero_vocales = contar_vocales("murcielago")
print(f"Número de vocales en la cadena: {numero_vocales}") 

# Ejercicio 7: Define una función que tome una lista y devuelva una nueva lista con los elementos únicos.
def elementos_unicos(lista):
    # Utilizamos un conjunto para mantener los elementos únicos
    elementos_unicos = set(lista)
    # Convertimos el conjunto de nuevo a lista (si se necesita mantener el orden original)
    lista_unicos = list(elementos_unicos)
    return lista_unicos

lista1 = ["pipa", "mango", "banano", "manzana", "manzana"] # lista acepta duplicados, set no
lista2 = ["eric", "edwards", "hernandez", "eric", "edwards"]

resultado1 = elementos_unicos(lista1)
resultado2 = elementos_unicos(lista2)

print("Lista original 1:", lista1)
print("Lista con elementos únicos 1:", resultado1)

print("Lista original 2:", lista2)
print("Lista con elementos únicos 2:", resultado2)

# Ejercicio 8: Define una función que tome un número y devuelva True si es primo y False en caso contrario.

# Definicion: Un número primo es un número natural mayor que 1 que solo puede ser dividido de manera exacta (sin dejar residuo) por 1 y por sí mismo. 
# Es decir, no tiene divisores positivos adicionales aparte de 1 y de sí mismo.

def primo(numero):
    #numero = input(int("Ingrese el numero:"))
    resul22 = numero % 2
    if resul22 == 1: # para sacar el numero primo
        print(True, numero,"es un numero primo")
    else:
        print(False, numero,"no es un numero primo")
primo(42)
primo(43)
primo(47)

# Ejercicio 9 (Teoría): ¿Qué es una función y para qué se utiliza en programación?

# Es un bloque de código independiente y reutilizable que realiza una tarea específica. Las funciones permiten dividir
# un programa grande en partes más pequeñas y manejables, cada una de las cuales realiza una operación concreta.
# Al encapsular tareas en funciones, el código se vuelve más modular, más fácil de leer, mantener y depurar.

# Ejercicio 10 (Práctica): Escribe un programa que pida al usuario una cadena y use una función para contar las consonantes.
def contar_consonantes(string):
    consonates = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"
    counter = 0
    for look in string:
        if look.lower() in consonates:
            counter += 1
    return counter
consonantes = contar_consonantes("murcielago")
print(f"El numero de consonates es:{consonantes}")
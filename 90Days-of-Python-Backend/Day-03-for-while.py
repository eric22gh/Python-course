# Día 3: Estructuras de Control - Bucles
# Definición del Tema
# bucles for y while, que nos permiten ejecutar un bloque de código repetidamente.

# Tips del Tema
# Bucle for: Utilizado para iterar(buscar) sobre una secuencia (lista, tupla, diccionario, conjunto o cadena).
# Bucle while: Repite un bloque de código mientras una condición sea verdadera, lo repite infinitamente si no le ponemos contador
# Interrupciones de bucle: Las sentencias break y continue pueden controlar el flujo de los bucles.
# break detener el bucle y continue que siga

# Fundamentos del Tema con Código

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)  
# El bucle for itera sobre cada elemento en la lista frutas e imprime cada uno de ellos.

#La función range() se utiliza a menudo para generar una secuencia de números.
for i in range(5):
    print(i)  # Imprime números del 0 al 4

# for puede tener una cláusula else. El bloque else se ejecuta cuando el bucle se completa normalmente.
# Ejemplo de bucle for con else
for i in range(5):
    print(i)
else:
    print("Bucle completado")

#####################

# Bucle while repite una acción mientras una condición sea True. 

i = 0
while i < 5:
    print(i)  # Imprime números del 0 al 4
    i += 1    # Incrementa i en 1 en cada iteración

# while también puede tener una cláusula else
# Ejemplo de bucle while con else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Bucle completado")

###############

# Interrupciones de Bucle: pueden controlar el flujo de los bucles utilizando las declaraciones break y continue.
# break termina el bucle actual de inmediato.

for i in range(10): # for no lleva contador
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)  # Imprime números del 0 al 4
# En este ejemplo, el bucle for se interrumpe cuando i es igual a 5, por lo que solo se imprimen los números del 0 al 4.

# La declaración continue salta a la siguiente iteración del bucle.
# Ejemplo de uso de continue
for i in range(10):
    if i == 5:
        continue  # Salta el resto del bucle cuando i es 5
    print(i)  # Imprime números del 0 al 9 excepto 5

################ Ejercicios

# Ejercicio 1: Escribe un programa que imprima los números del 1 al 10 usando un bucle for.
for numeros in range(1,11):
    print(numeros)

# Ejercicio 2: Escribe un programa que imprima los números del 1 al 10 usando un bucle while.
a = 1
while a < 11 and 1:
    print(a)
    a += 1

# Ejercicio 3: Escribe un programa que imprima los números pares del 1 al 20 usando un bucle for.
for eric in range(1,21):
    if eric % 2 == 0:
        print(eric)

# Ejercicio 4: Escribe un programa que imprima los números impares del 1 al 20 usando un bucle while.
z = 0
while z < 21:
    z += 1
    if z % 2 == 1:
        print(z)

# Ejercicio 5: Escribe un programa que calcule la suma de los primeros 100 números naturales usando un bucle for.
suma = 0
for num in range(1,101):
    suma += num # acomular la suma de los numeros naturales
print("La suma de los primeros 100 números naturales es:", suma)

# Ejercicio 6: Escribe un programa que calcule la suma de los primeros 100 números naturales usando un bucle while.
w = 0
sums = 0
while w < 101:
    sums += w # acomular la suma de los numeros naturales
    w += 1
print("La suma de los primeros 100 números naturales es:", suma)

# Ejercicio 7: Escribe un programa que imprima los elementos de una lista de frutas usando un bucle for.
fru = ["tomate", "banano", "sandia", "pipa", "mango"]
for listas in fru:
    print(listas)

# Ejercicio 8: Escribe un programa que imprima los caracteres de una cadena usando un bucle for.
st = "edwards"
for al in range.__str__(st):
    print(al)

t = "hernandez"
for lop in t:
    print(lop)

# Ejercicio 9 (Teoría): ¿Cuál es la diferencia entre un bucle for y un bucle while?
# el bucle while repite numeros mientras una condicion sea cierta y el bucle for busca o itera sobre una lista, conjunto...etc

# Ejercicio 10 (Práctica): Escribe un programa que pida al usuario un número y calcule su factorial usando un bucle while.
# factorial de un numero es multiplicar el numero por todos sus numeros anteriores positivos.
user = int(input("Ingrese el numero:"))
factory = 1
while user > 0:
    factory *= user
    user -= 1 #asegurarse de que, en cada iteración, se esté avanzando hacia un número más pequeño
print("El factorial de", user, "es:", factory)

###### otra opcion
import math
factorial = math.factorial(user)
print(factorial)

# Ejercicio 11: Imprimir Números en Rango
# Escribe un programa que imprima los números del 5 al 15 usando un bucle for.
for num in range(5, 16):
    print(num)

# Ejercicio 12: Imprimir Números Descendentes
# Escribe un programa que imprima los números del 20 al 10 en orden descendente usando un bucle while.
num = 20
while num >= 10:
    print(num)
    num -= 1

# Ejercicio 13: Imprimir Tabla de Multiplicar
# Escribe un programa que imprima la tabla de multiplicar del 7 usando un bucle for.
tabla = 7
for number in range(1, 12):
    print(tabla * number)

# Ejercicio 14: Imprimir Valores Pares en Lista
# Escribe un programa que imprima solo los valores pares de una lista de números usando un bucle for.
pares = 2
for numeros in range(1, 20):
    if numeros % pares == 0:
        print(f"este numero: {numeros} es par")

# Ejercicio 15: Contar Números Impares
# Escribe un programa que cuente cuántos números impares hay en una lista de números usando un bucle while.
pares = 2
impares = []
for lista_inpar in range(1, 30):
    if lista_inpar % pares != 0:
        impares.append(lista_inpar)
conteo = len(impares)
print(f"el numero de impares en la lista de numeros es: {conteo}")

nume = 0
impar = []
pares = 2
while nume < 30:
    nume += 1
    if nume % pares != 0:
        impar.append(nume)
cantidad = len(impar)
print(f"el numero de impares en la lista de numeros es: {cantidad}")

# Ejercicio 16: Imprimir Cadenas en Lista
# Escribe un programa que imprima cada cadena en una lista de cadenas usando un bucle for.
lista = ["eric", "edwards", "hernandez"]
for cadena in lista:
    print([cadena])

# Ejercicio 17: Sumar Números en Lista
# Escribe un programa que calcule la suma de todos los números en una lista usando un bucle while.
numero = 0
suma_total = 0
while numero < 10:
    numero += 1
    suma_total += numero 
print(suma_total)

# Ejercicio 18: Encontrar Mínimo en Lista
# Escribe un programa que encuentre el valor mínimo en una lista de números usando un bucle for.
lista_min = []
for numero in range(5, 45):
    lista_min.append(numero)
numero_minimo = min(lista_min)
print(numero_minimo)

# Ejercicio 19: Generar Secuencia de Fibonacci
# Escribe un programa que genere y imprima los primeros 10 números de la secuencia de Fibonacci usando un bucle while.
a, b = 0, 1
n = 0
while n < 10:
    print(a)
    a, b = b, a + b
    n += 1

# Ejercicio 20: Verificar Número Primo
# Escribe un programa que verifique si un número ingresado por el usuario es primo usando un bucle for.
for i in range(1, 20):
    if i % 2 == 0:
        print(f"este es un numero primo: {i}")
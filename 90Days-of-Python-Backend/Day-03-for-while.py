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
    print(fruta)  # Imprime cada fruta en la lista
# El bucle for itera sobre cada elemento en la lista frutas e imprime cada uno de ellos.

#La función range() se utiliza a menudo para generar una secuencia de números. cuando necesitas repetir algo un número específico de veces.
for i in range(5):
    print(i)  # Imprime números del 0 al 4

# for puede tener una cláusula else. El bloque else se ejecuta cuando el bucle se completa normalmente (es decir, no se interrumpe con break).
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

for i in range(10): # a for no hay que ponerle contador
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

#######################################

# Ejercicios

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
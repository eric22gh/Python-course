# Día 2: Estructuras de Control - Condicionales
# condicionales if, elif y else. Estas estructuras nos permiten ejecutar código de manera selectiva basado en condiciones.

# Tips del Tema
# Condicionales: Permiten tomar decisiones en el programa basadas en condiciones.
# Indentación: Python usa la indentación (espacios o tabulaciones) para definir bloques de código.
# Operadores de comparación: Incluyen ==, !=, >, <, >=, <=.

# ejemplo

# Condicionales en Python

a = 5
b = 3

# if: se utiliza para ejecutar un bloque de código si una condición es verdadera.
if a > b:
    print("a es mayor que b") 

# if-else: permite ejecutar un bloque de código si la condición es verdadera y otro bloque si la condición es falsa.
if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")  

# if-elif-else: se utiliza para verificar múltiples condiciones. elif significa "else if".
if a == b:
    print("a es igual a b")
elif a > b:
    print("a es mayor que b")  
else:
    print("a es menor que b")  

# Condicionales anidados: se pueden anidar condicionales dentro de otros condicionales.

if a > b:
    if a > 0: # siendo un numero negativa en la unica forma que sea menor a 0
        print("a es un número positivo mayor que b")  
    else:
        print("a no es un número positivo, pero es mayor que b")
else:
    print("a no es mayor que b")

# Operadores lógicos en condicionales: and, or, not
x = 10
y = 20
z = 30

# and: se utiliza para comprobar si dos o más condiciones son verdaderas.
if x < y and y < z:
    print("x es menor que y y y es menor que z")  

# or: se utiliza para comprobar si al menos una de varias condiciones es verdadera.
if x < y or y > z:
    print("x es menor que y o y es mayor que z")  

# not: se utiliza para invertir el valor de una condición.
if not (x > z):
    print("x no es mayor que z")  

# Condicionales con valores booleanos
is_sunny = True

if is_sunny:
    print("Está soleado")  # Se ejecuta si is_sunny es verdadero
else:
    print("No está soleado")  # Se ejecuta si is_sunny es falso

# Comparación de cadenas
nombre = "Alice"

if nombre == "Alice":
    print("Hola, Alice!")  # Se ejecuta si la cadena nombre es igual a "Alice"
else:
    print("No eres Alice")

# Comparación de listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

if lista1 == lista2:
    print("Las listas son iguales")  # Se ejecuta si lista1 es igual a lista2
else:
    print("Las listas no son iguales")

# Uso de "in" para comprobar pertenencia
elemento = 2

if elemento in lista1:
    print("El elemento está en la lista")  # Se ejecuta si elemento está en lista1
else:
    print("El elemento no está en la lista")

# Condicionales con diccionarios
diccionario = {"clave1": "valor1", "clave2": "valor2"}

if "clave1" in diccionario:
    print("La clave1 está en el diccionario")  # Se ejecuta si "clave1" es una clave en diccionario
else:
    print("La clave1 no está en el diccionario")

##################################

# Ejercicios

# Ejercicio 1: Escribe un programa que verifique si un número es positivo, negativo o cero.
num = -1
if num > 0:
    print("el",num,"es un numero positivo")
elif num == 0:
    print("el",num,"es un 0")
else:
    print("el",num,"es un numero negativo")

# Ejercicio 2: Escribe un programa que verifique si un número es par o impar.
n = 3
opera =  n % 2
if opera == 0:
    print("El",n,"es un numero par")
else:
    print("El",n,"es un numero impar")

# Ejercicio 3: Escribe un programa que tome la edad de una persona y determine si es un niño, adolescente, adulto o anciano.
age = 2

if age >= 1 and 12 >= age:
    print("es un niño")

elif age >= 13 and 18 >= age:
    print("es un adolecente")

elif age >= 19 and 60 >= age:
    print("es un adulto")

elif age >= 61 and 100 >= age:
    print("es un anciano")

else:
    print("edad invalida")

# Ejercicio 4: Escribe un programa que pida al usuario un número y verifique si está en el rango de 1 a 10.
num2 = 200
if num2 >= 1 and 10 >= num2:
    print(num2,"Esta en el rango del 1 al 10")
else:
    print("No esta en el rango del 1 al 10")

# Ejercicio 5: Escribe un programa que determine el mayor de tres números ingresados por el usuario.
num1 = 30
num2 = 22
num3 = 10

if num1 >= num2 and num1 >= num3:
    print("El mayor número es:",num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor número es:",num2)
else:
    print("El mayor número es:",num3)

# Ejercicio 6: Escribe un programa que verifique si un número es divisible por 3 y 5.
mu1 = 14
mu2 = 54
resul1 = mu1 % 3
resul2 = mu1 % 5
resul3 = mu2 % 3
resul4 = mu2 % 5

if resul1 == 0 and resul2 == 0:
    print("El número", mu1, "es divisible entre 3 y 5")
elif resul1 == 0:
    print("El número", mu1, "es divisible entre 3")
elif resul2 == 0:
    print("El número", mu1, "es divisible entre 5")
else:
    print("El número", mu1, "no es divisible entre 3 ni 5")

if resul3 == 0 and resul4 == 0:
    print("El número", mu2, "es divisible entre 3 y 5")
elif resul3 == 0:
    print("El número", mu2, "es divisible entre 3")
elif resul4 == 0:
    print("El número", mu2, "es divisible entre 5")
else:
    print("El número", mu2, "no es divisible entre 3 ni 5")

# Ejercicio 7: Escribe un programa que tome una letra como entrada y verifique si es una vocal o una consonante.
vocal = "o"
if vocal == "a":
    print("es una vocal")
elif vocal == "b":
    print("es una vocal")
elif vocal == "e":
    print("es una vocal")
elif vocal == "i":
    print("es una vocal")
elif vocal == "o":
    print("es una vocal")
else:
    print("es una consonante")
###################################
vocal = "o"
vocales = "aeiou"

if vocal in vocales:
    print("es una vocal")
else:
    print("es una consonante")

# Ejercicio 8: Escribe un programa que tome dos números y determine si uno es múltiplo del otro.
ber1 = 24
ber2 = 6
result = ber1 % ber2
print(result)
if result == 0:
    print("los 2 numeros son multiplos")
else:
    print("No son multiplos")

# Ejercicio 9 (Teoría): ¿Qué operador usarías para verificar si dos valores son iguales en Python?
# usaria el operador de igualdad 5 == 5

# Ejercicio 10 (Práctica): Escribe un programa que pida al usuario su calificación (de 0 a 100) 
# y muestre si está aprobado (>= 60) o reprobado.
nota = 70
if nota >= 60 and 100 >= nota:
    print("aprobado")
elif nota >= 1 and 59 >= nota:
    print("reprobado")
else:
    print("nota erronea")

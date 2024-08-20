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

#if: se utiliza para ejecutar un bloque de código si una condición es verdadera.
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

############ Ejercicios
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

# Ejercicio 11: Verificación de Trimestre
# Escribe un programa que tome un número del 1 al 12 (representando un mes) y determine en qué trimestre del año cae.
numero_mes = int(input("ingrese el numero del mes: "))
trimestre_1 = 1, 2, 3
trimestre_2 = 4, 5, 6
trimestre_3 = 7, 8, 9
trimestre_4 = 10, 11, 12
if numero_mes in trimestre_1:
    print(f"el numero: {numero_mes} se encuentra en el primer trimestre del año")
elif numero_mes in trimestre_2:
    print(f"el numero: {numero_mes} se encuentra en el segundo trimestre del año")
elif numero_mes in trimestre_3:
    print(f"el numero: {numero_mes} se encuentra en el tercer trimestre del año")
elif numero_mes in trimestre_4:
    print(f"el numero: {numero_mes} se encuentra en el cuarto trimestre del año")
else:
    print("ingrese un numero del mes correcto del 1 al 12")

# Ejercicio 12: Categoría de Peso
# Escribe un programa que clasifique a una persona en una categoría de peso según su IMC (Índice de Masa Corporal). 
# Utiliza las siguientes categorías:
# - Menor a 18.5: Bajo peso, 18.5 a 24.9: Peso normal, 25 a 29.9: Sobrepeso, 30 o más: Obesidad
imc = float(input("Ingrese su IMC: "))
if imc <= 18.5:
    print("la persona este baja de peso")
elif 18.5 <= imc <= 24.9:
    print("la persona tiene peso normal")
elif 25 <= imc <= 29.9:
    print("la persona tiene sobrepeso")
elif imc >= 30:
    print("la persona tiene obesidad")
else:
    print("ingres un imc correcto")

# Ejercicio 13: Clasificación de Edad con Rangos Específicos
# Modifica el programa de la edad para incluir un rango adicional: 0-1 año es "Bebé", 2-4 años es "Preescolar".
age = 2
if age < 1:
    print("es un bebe")

elif age >= 2 and 4 >= age:
    print("es un preescolar")

elif age >= 5 and 12 >= age:
    print("es un niño")

elif age >= 13 and 18 >= age:
    print("es un adolecente")

elif age >= 19 and 60 >= age:
    print("es un adulto")

elif age >= 61 and 100 >= age:
    print("es un anciano")

else:
    print("edad invalida")

# Ejercicio 14: Categoría de Artículo
# Escribe un programa que determine la categoría de un artículo basado en su precio:
# - Menor a $10: Económico, $10 a $50: Moderado, Más de $50: Costoso
precio = int(input("ingrese el precio en dolares: "))
if precio < 10:
    print(" es un articulo economico")
elif precio > 10 and 50 >= precio:
    print("es un articulo moderado")
elif precio > 50:
    print("es un articulo costoso")
else:
    print("ingrese un valor valido")

# Ejercicio 15: Verificación de Año Bisiesto
# Escribe un programa que verifique si un año ingresado por el usuario es bisiesto.
# Un año es bisiesto si es divisible entre 4, pero no entre 100, excepto si es divisible entre 400.
# 2021%4 # 0 si es bisiesto
# 2021%100 # 1 es bisiesto
# 2021%400 # 0 no es bisiesto
año = int(input("ingrese el año:"))
condicion_1 = año % 4
condicion_2 = año % 100
condicion_3 = año % 400
if condicion_1 == 0 and condicion_2 > 0 and condicion_3 > 0:
    print(f"el año: {año} es un año bisiesto")

else:
    print(f"el año: {año} no es un año bisiesto")

# Ejercicio 16: Elegibilidad para Voto
# Escribe un programa que determine si una persona es elegible para votar en función de su edad y ciudadanía.
# La persona debe tener al menos 18 años y ser ciudadano para votar.
edad = 18
ciudadano = "NO"
if edad >= 18 and ciudadano.lower() == "si":
    print("el ciudadano puede votar")
else:
    print("el ciudadano no puede votar")

# Ejercicio 17: Comparación de Fechas
# Escribe un programa que compare dos fechas en formato de cadena (por ejemplo, "2024-08-19") y determine cuál es más reciente.
from datetime import datetime
fecha_1 = "2024-08-19"
fecha_2 = "2028-08-10"
fecha_1_new = datetime.strptime(fecha_1, "%Y-%m-%d")
fecha_2_new = datetime.strptime(fecha_2, "%Y-%m-%d")
if fecha_1_new > fecha_2_new:
    print(f"la {fecha_1} es mas reciente que la {fecha_2}")
elif fecha_2_new > fecha_1_new:
    print(f"la {fecha_2} es mas reciente que la {fecha_1}")
else:
    print("Ambas fechas son iguales")

# Ejercicio 18: Número en Rango de Decenas
# Escribe un programa que determine si un número está en el rango de una decena específica (por ejemplo, 10-19, 20-29, etc.).
num = 20
if num >= 0 and 9 > num:
    print("esta en la primera decena")
elif num >= 10 and 19 > num:
    print("esta en la segunda decena")
elif num >= 20 and 29 > num:
    print("esta en la tercera decena")
elif num >= 30 and 39 > num:
    print("esta en la cuarta decena")
else:
    print("esta en la quinta decena o en las siguientes")

# Ejercicio 19: Determinar Día de la Semana
# Escribe un programa que tome un número del 1 al 7 y determine qué día de la semana representa (1: Lunes, 2: Martes, etc.).
numero = 5
if numero == 1:
    print("el dia de la semana es lunes")
elif numero == 2:
    print("el dia de la semana es martes")
elif numero == 3:
    print("el dia de la semana es miercoles")
elif numero == 4:
    print("el dia de la semana es jueves")
elif numero == 5:
    print("el dia de la semana es viernes")
elif numero == 6:
    print("el dia de la semana es sabado")
elif numero == 7:
    print("el dia de la semana es domingo")
else:
    print("ingrese un numero valido (del 1 al 7)")

# Ejercicio 20: Juego de Adivinanza de Número
# Escribe un programa que genere un número aleatorio entre 1 y 100 y pida al usuario adivinarlo.
# El programa debe indicar si la adivinanza es demasiado baja, alta o correcta.
import random
numero_secreto = random.randint(1, 100)
adivinar = int(input("ingrese su numero (entre el 1 y 100): "))
if adivinar < 1 or adivinar > 100:
    print("El número debe estar entre 1 y 100.")
elif adivinar < numero_secreto:
    print("Número muy bajo")
elif adivinar > numero_secreto:
    print("Número muy alto")
else:
    print(f"¡Correcto! El número secreto es: {adivinar}")
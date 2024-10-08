# Día 1: Introducción a la Programación y Conceptos Básicos de Python
# Hoy comenzaremos con los conceptos básicos de la programación y los fundamentos de Python. 
# Aprenderemos sobre variables, tipos de datos y operaciones. 

# Tips del Tema
# Variables: Las variables son contenedores para almacenar datos. En Python, no necesitas declarar el tipo de variable, 
# el intérprete lo hace automáticamente.
# Tipos de datos: Los tipos de datos comunes en Python incluyen int(enteros), float(números flotantes), 
# str (cadenas de texto), y bool (valores booleanos).
# Operaciones: Python soporta operaciones aritméticas básicas como suma, resta, multiplicación y división.

# Variables y Tipos de Datos

# Declaración de variables
integer = 10        # Variable de tipo entero (int)
float = 10.5     # Variable de tipo flotante (float)
string = "Hola"     # Variable de tipo cadena (str)
bool = True     # Variable de tipo booleano (bool)

#Imprimir variables y tipos
print(integer)       # Salida: 10
print(type(integer)) # Salida: <class 'int'>

print(float)      # Salida: 10.5
print(type(float))# Salida: <class 'float'>

print(string)        # Salida: Hola
print(type(string))  # Salida: <class 'str'>

print(bool)      # Salida: True
print(type(bool))# Salida: <class 'bool'>

###### Operaciones

# Operadores aritméticos
a = 5
b = 3

suma = a + b             # Suma: añade dos valores.
resta = a - b            # Resta: sustrae un valor de otro.
multiplicacion = a * b   # Multiplicación: multiplica dos valores.
division = a / b         # División: divide un valor por otro, retorna un número decimal.
potencia = a ** b        # Potenciación: eleva un número a la potencia de otro.
division_entera = a // b # División entera: divide un valor por otro y redondea hacia abajo al entero más cercano, numeros impares
modulo = a % b           # Módulo: obtiene el resto de la división de un valor por otro,
#                          numeros pares y saca mutiplos. si la operacion da 0 es un multiplo, numero par y divisible

print("Suma:", suma)               # Suma: 5 + 3 = 8
print("Resta:", resta)             # Resta: 5 - 3 = 2
print("Multiplicación:", multiplicacion) # Multiplicación: 5 * 3 = 15
print("División:", division)       # División: 5 / 3 = 1.6666666666666667
print("Potenciación:", potencia)           # Potenciación: 5 ** 3 = 125
print("División entera:", division_entera) # División entera: 5 // 3 = 1
print("Módulo:", modulo)                   # Módulo: 5 % 3 = 2

# Operadores de comparación
igual = (a == b)           # Igual a: comprueba si dos valores son iguales.
diferente = (a != b)       # Diferente de: comprueba si dos valores son diferentes.
mayor_que = (a > b)        # Mayor que: comprueba si el valor de la izquierda es mayor que el de la derecha.
menor_que = (a < b)        # Menor que: comprueba si el valor de la izquierda es menor que el de la derecha.
mayor_o_igual = (a >= b)   # Mayor o igual que: comprueba si el valor de la izquierda es mayor o igual que el de la derecha.
menor_o_igual = (a <= b)   # Menor o igual que: comprueba si el valor de la izquierda es menor o igual que el de la derecha.

print("Igual a:", igual)                     # Salida: Igual a: False
print("Diferente de:", diferente)            # Salida: Diferente de: True
print("Mayor que:", mayor_que)               # Salida: Mayor que: True
print("Menor que:", menor_que)               # Salida: Menor que: False
print("Mayor o igual que:", mayor_o_igual)   # Salida: Mayor o igual que: True
print("Menor o igual que:", menor_o_igual)   # Salida: Menor o igual que: False

# Operadores lógicos
y_logico = (a > 2 and b < 5)   # devuelve True si ambas condiciones son verdaderas.
o_logico = (a > 2 or b > 5)    # devuelve True si al menos una de las condiciones es verdadera.
no_logico = not(5 > 2)         # invierte el valor lógico.

print("AND lógico:", y_logico)   # Salida: AND lógico: True
print("OR lógico:", o_logico)    # Salida: OR lógico: True
print("NOT lógico:", no_logico)  # Salida: NOT lógico: False

# Operadores de asignación
a += 1  # Suma y asigna: a = a + 1, a ya no va a valer 5 si no que vale 6
b *= 2  # Multiplica y asigna: b = b * 2
a -= 2  # Resta y asigna: a = a - 2
b /= 3  # Divide y asigna: b = b / 3

print("Suma y asigna:", a)        # Salida: Suma y asigna: 6
print("Multiplica y asigna:", b)  # Salida: Multiplica y asigna: 6

print("Resta y asigna:", a)       # Salida: Resta y asigna: 4
print("Divide y asigna:", b)      # Salida: Divide y asigna: 2.0

#####################

# Ejercicios

#  Declara una variable de tipo entero, asígnale un valor y muéstralo por pantalla.
z = 8
print("el valor de la variable z es:", z)

#  Declara una variable de tipo cadena, asígnale un valor y muéstralo por pantalla.
x = "eric hernandez edwards"
print("mi nombre es:", x)

#  Declara una variable de tipo booleano, asígnale un valor y muéstralo por pantalla.
y = True
print("es falso o", y)

#  Realiza una operación de suma con dos números y muestra el resultado.
p = 8
o = 10
result = p + o
print(result)

#  Realiza una operación de resta con dos números y muestra el resultado.
print("el resultado de la resta es:", p - o)

#  Realiza una operación de multiplicación con dos números y muestra el resultado.
print("el resultado de la multiplicacion es:", p * o)

#  Realiza una operación de división con dos números y muestra el resultado.
print("el resultado de la divisio es:", p / o)

#  Declara una variable de tipo float, asígnale un valor y muestra el tipo de dato usando la función type().
f = 2.0 
print("el tipo de variable es:" + str(type(f))) # solo se puede concatenar strings

# (Teoría): ¿Cuál es la diferencia entre una variable de tipo int y una de tipo float?
# las variables de tipo int o integer representan numeros enteros sin decimal y 
# las variables de tipo float representa los numeros decimales

# (laboratorio): Escribe un programa que pida al usuario que introduzca dos números y muestre la suma, resta, multiplicación y división de ambos.
t = int(input("introduce el primer numero:"))
r = int(input("introduce el segundo numero:"))
sum = t + r
rest = t - r
multi = t * r
div = t / r
print("el resultado de la suma es:", sum)
print("el resultado de la resta es:", rest)
print("el resultado de la multiplicacion es:", multi)
print("el resultado de la division es:", div)

# Ejercicio 11: Realiza una operación de división con dos números y muestra el resultado.
print(8/6)

# Ejercicio 12: Declara una variable de tipo booleano, asígnale un valor y realiza una operación lógica utilizando la negación (not).
valor = True
value = False
print(not(valor))
print(not(value))

# Ejercicio 13: Escribe un programa que tome dos números como entrada y determine cuál es mayor.
numero1 = 80
numero2 = 9
if numero1 > numero2:
    print(f"el numero: {numero1} es el mayor")

elif numero1 < numero2:
    print(f"el numero: {numero2} es el mayor")

else:
    print("Ambos números son iguales.")

# Ejercicio 14: Calcula el resultado de elevar un número a una potencia usando el operador ** y muestra el resultado.
print(numero1 ** numero2)

# Ejercicio 15: Declara una variable de tipo cadena, concatena otra cadena a ella y muestra el resultado.
cadena = "hola Eric"
print(cadena + " hernandez")
print(f"{cadena} edwards")

# Ejercicio 16: Declara dos variables de tipo entero, realiza una operación de módulo entre ellas y muestra el resultado.
var = 10
var2 = 3
print(var % var2)

# Ejercicio 17: Crea una variable de tipo float, conviértela a entero, y muestra ambos valores.
var_float = 20.0
var_inter = int(var_float)
print(var_float)
print(var_inter)

# Ejercicio 18: Declara una variable de tipo cadena y muestra su longitud usando la función len().
string = "edwards"
print(len(string))

# Ejercicio 19: Escribe un programa que tome dos números como entrada y determine si son iguales.
number = 80
number1 = 8
if number == number1:
    print(f"los numeros {number} y {number1} son iguales")
else:
    print(f"los numeros {number} y {number1} no son iguales")

# Ejercicio 20: Declara una variable de tipo entero, multiplícala por sí misma (cuadrado) y muestra el resultado.
variable = 7 
print(variable ** 2) # da el mismo resultado que print(variable * variable)
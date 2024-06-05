# Día 2: Variables y Tipos de Datos
# Definición del tema:
# Las variables son contenedores para almacenar valores de datos. Python soporta varios tipos de datos como enteros, 
# flotantes, cadenas y booleanos.

# Tips:

# Los nombres de variables deben ser descriptivos y no pueden comenzar con un número.
# Usa type() para verificar el tipo de una variable.
# Las cadenas pueden ser delimitadas por comillas simples o dobles.

#ejemplo:

# Declaración de variables
nombre = "eric"
edad = 25
altura = 1.75
es_estudiante = True

# Uso de type()
print(type(nombre))  # <class 'str'>
print(type(edad))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(es_estudiante))  # <class 'bool'>

# Ejercicios:

# Declara variables de diferentes tipos (entero, flotante, cadena, booleano) y usa print() para mostrarlas.
name = "edwards" 
age = 30
alt = 1.80
estudia = True
print(name)
print(age)
print(alt)
print(estudia)
print("Mi Nombre es:",name,"y mi altura es:",alt,"tengo una edad de:", age,"años","y mi estado de estudio es:",estudia)
# Convierte una cadena que representa un número a un entero y suma dos números.
a = int("2")
b = 4
print(b+a)

print("escribe el numero")
num1 = int(input(""))
print("escribe el segundo numero")
num2 = int(input(""))
print(num1 + num1)
# Declara una variable booleana y usa una estructura condicional para imprimir mensajes diferentes.
pop = 2.5
if pop > 1.5:
    print("es mayor")
else:
    print("no es mayor")
#####
pop = 1.0
if pop > 1.5:
    print("es mayor")
else:
    print("no es mayor")
# Escribe un programa que solicite una cadena y un número, luego repite la cadena ese número de veces.
a = "eric"
b = int(input(""))
print(a*b)

# # Explica la diferencia entre variables globales y locales con un ejemplo.
# Variables Globales
# Definición: Son aquellas que se declaran fuera de cualquier función y están disponibles
# para cualquier parte del código, incluidas las funciones.
# ####
# Variables Locales
# Definición: Son aquellas que se declaran dentro de una función y solo son accesibles dentro de esa función.

# Variable global
x = 10
def funcion():
    # Variable local
    y = 5
    print("Dentro de la función, x =", x)
    print("Dentro de la función, y =", y)

funcion()

print("Fuera de la función, x =", x)
# lo siguiente dará un error porque y no está definida fuera de la función
#print("Fuera de la función, y =", y)


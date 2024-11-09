# Día 26: Introducción a las Estructuras de Datos y Algoritmos

# Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. Su sintaxis clara y su enfoque en la legibilidad lo hacen ideal para principiantes.
# Para comenzar a trabajar con Python, se recomienda usar un entorno de desarrollo como Visual Studio Code (VS Code) o PyCharm.

# Tips y Buenas Prácticas:
# Utiliza entornos virtuales (venv) para evitar conflictos entre proyectos.
# Comenta tu código para que otros (o tú mismo en el futuro) puedan entenderlo fácilmente.
# Sigue las convenciones de estilo de Python (PEP 8) para mantener tu código limpio y legible.

# Ejercicios De Repaso:

# 1- Escribe un programa que imprima tu nombre y edad.
print("Mi nombre es Eric Hernandez y tengo 30 años")

# 2- Crea un script que tome tu nombre como entrada y lo imprima en mayúsculas.
nombre = "Eric Hernandez"
print(nombre.upper())

# 3- Desarrolla un programa que calcule el área de un círculo dado su radio.
# formula: area_circulo = pi * radio ** 2
import math
radio = 8 
area = math.pi * radio ** 2
print(f"El area del circulo es: {area:.2f}")

# 4- Escribe un programa que imprima la fecha y hora actuales.
import datetime
now = datetime.datetime.now()
print(f"La fecha y hora actuales son: {now}")

# 5- Crea un programa que genere un número aleatorio entre 1 y 100.
import random
aleatorio = random.randint(1, 100)
print(f"El numero aleatorio es: {aleatorio}")

# 6- Escribe un programa que convierta un número de Celsius a Fahrenheit.
# formula: fahrenheit = (celsius * 9/5) + 32
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura de {celsius} grados Celsius en Fahrenheit es: {fahrenheit}")

# 7-Crea un script que imprima los primeros 10 números de la serie Fibonacci.
# formula: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
lista = []
for i in range(10):
    lista.append(fibonacci(i))
print(lista)

#########
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

lista = fibonacci(20)
print(lista)

# 8- Desarrolla un programa que calcule la suma de los primeros 100 números naturales.
coteo = 0
for n in range(1, 101):
    coteo += n
print(coteo)
####

n = 1000
suma = n * (n + 1) // 2
print(suma)

# 9- Escribe un programa que imprima una tabla de multiplicar para un número ingresado.
numero = 7
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 10- Crea un programa que cuente cuántas palabras hay en una frase ingresada.
frase = "Mi nombre es Eric Hernandez"
print(len(frase.split(" ")))

# 11- Desarrolla un programa que encuentre el máximo entre tres números ingresados.
numeros = 22, 331, 89
print(max(numeros))

# 12- Escribe un programa que imprima los números del 1 al 10.
for numeros in range(1, 11):
    print(numeros)

# 13- Crea un programa que imprima un mensaje dependiendo de la edad ingresada.
edad = 2
if edad > 18:
    print("Eres mayor de edad")
elif 17 > edad > 12:
    print("Eres adolescente")
elif edad < 11:
    print("eres un nino")

else:
    print("error")

# Mini Proyectos:
# Un script que tome tu nombre y lo imprima en diferentes formatos (mayúsculas, minúsculas).
nombre = "Eric Hernandez Edwards"
minuscula = nombre.lower()
mayuscula = nombre.upper()
print(f"Nombre en minuscula: {minuscula} y en mayuscula: {mayuscula}")

# Un programa que calcule el área de diferentes figuras geométricas (círculo, cuadrado, triángulo).
# circulo = pi * radio ** 2
# cuadrado = l * l
# triangulo = b * h / 2
class Geometria:
    def __init__(self, medida):
        self.medida = medida
    
    def circulo(self):
        area = math.pi * self.medida ** 2
        return f"La medida del area de el circulo es: {area:.2f}"
    
    def cuadrado(self):
        area = self.medida * self.medida
        return f"La medida del area de el cuadrado es: {area:.2f}"
    
    def triangulo(self, altura):
        area = self.medida * altura / 2
        return f"La medida del area de el triangulo es: {area:.2f}"
dato = Geometria(4)
print(dato.circulo())
print(dato.cuadrado())
print(dato.triangulo(6))
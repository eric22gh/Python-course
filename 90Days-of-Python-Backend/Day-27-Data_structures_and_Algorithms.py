# Día 27: Sintaxis básica y tipos de datos (números, cadenas)

#Teoría:
# Python tiene varios tipos de datos básicos: enteros (int), flotantes (float), cadenas (str), y booleanos (bool). 
# La conversión entre tipos es común y se puede realizar utilizando funciones como int(), float(), y str().
# tipos de datos:

# Enteros (int): Representan números enteros sin decimales.
var = 10
print(type(var))

# Flotantes (float): Representan números con decimales.
var = 10.5
print(type(var))

# Cadenas (str): Representan cadenas de texto.
var = "hola"
print(type(var))

# Booleanos (bool): Representan valores booleanos (True o False).
var = True
print(type(var))

# Operaciones aritméticas:
a = 5
b = 3
suma = a + b # sumar 2 valores
print(f'Suma: {suma}')

resta = a - b # resta 2 valores
print(f'Resta: {resta}')

multiplicacion = a * b # multiplica 2 valores
print(f'Multiplicación: {multiplicacion}')

division = a / b # divide 2 valores
print(f'División: {division}')

potencia = a ** b # elevar un valor a la potencia de otro
print(f'Potenciación: {potencia}')

division_entera = a // b # divide 2 valores y lo redondea hacia abajo
print(f'División entera: {division_entera}')

modulo = a % b # obtener el resto de una división, se usa para sacar numeros pares, numeros impares, saca mutiplos, si la operacion da 0 es un multiplo.
print(f'Módulo: {modulo}')

# Operadores de comparación: 
print(a == b) # igual a: comprueba si dos valores son iguales.
print(a != b) # diferente de: comprueba si dos valores son diferentes.
print(a > b) # mayor que: comprueba si a  es mayor que b.
print(a < b) # menor que: comprueba si a es menor que b.
print(a >= b) # mayor o igual que: comprueba si a es mayor o igual que b.
print(a <= b) # menor o igual que: comprueba si a es menor o igual que b.

# Operadores lógicos:
print(a > 2 and b < 5) # devuelve True si ambas condiciones son verdaderas.
print(a > 2 or b > 5) # devuelve True si al menos una de las condiciones es verdadera.
print(not(5 > 2)) # invierte el valor lógico.

# Operadores de asignación:
a += 1 # Suma y asigna: a + 1, a ya no vale 5 si no que vale 6
b *= 2 # Multiplica y asigna: b = b * 2
a -= 2 # Resta y asigna: a = a - 2
b /= 3 # Divide y asigna: b = b / 3

# Operadores de pertenencia:
lista = [1, 2, 3, 4, 5]
pertenece = (1 in lista) # comprueba si un elemento pertenece a una lista.
no_pertenece = (10 not in lista) # comprueba si un elemento no pertenece a una lista.

# Operadores de identidad:
a = 5
b = 5
identico = (a is b) # comprueba si dos variables apuntan al mismo objeto.
no_identico = (a is not b) # comprueba si dos variables no apuntan al mismo objeto.

# conversión entre tipos:
entero = 10
flotante = 3.14
cadena = "10"
entero_convertido = int(cadena) # convierte la cadena "10" en un entero.
flotante_convertido = float(entero) # convierte el entero 10 en un flotante.

# Uso de Números:
# Cálculo de impuestos sobre la renta
salario = 50000
tasa_impuesto = 0.2
impuesto = salario * tasa_impuesto
print(f'Impuesto sobre la renta: {impuesto}')

# Manipulación de Cadenas:
# Análisis de texto
texto = "El rápido zorro marrón salta sobre el perro perezoso"
palabras = texto.split() # divide con comillas las palabras en una cadena de texto
print(f'Número de palabras: {len(palabras)}')

# Contar la frecuencia de letras
frecuencia = {}
for letra in texto:
    if letra.isalpha():  # contar letras
        frecuencia[letra] = frecuencia.get(letra, 0) + 1
print(f'Frecuencia de letras: {frecuencia}')
#### o ####
from collections import Counter
print(Counter(texto))

# Tips y Buenas Prácticas:
# Utiliza la función type() para verificar el tipo de datos de una variable.
# Al trabajar con cadenas, usa métodos como .strip(), .lower(), y .upper() para limpiar y formatear datos.
# Siempre valida la entrada del usuario para evitar errores.

# Ejercicios:
# 1- Crea dos variables numéricas y calcula su suma, resta, multiplicación y división.
num_1 = 8
num_2 = 6
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)

# 2- Escribe un programa que convierta una cadena de texto a mayúsculas y minúsculas.
frase = "Eric Hernandez edwards"
print(frase.lower())
print(frase.upper())

# 3- Crea una cadena que contenga tu nombre y apellido, y luego imprímela.
frase = "Eric Hernandez edwards"
print(frase)

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
frase = f"{nombre} {apellido}"
print(frase)

# 4- Escribe un programa que calcule el área de un rectángulo (base y altura como entradas).
base = int(input("Ingrese el valor de la base: "))
altura = int(input("Ingrese el valor de la altura: "))
print(f"El area de el rectangunlo es: {base * altura}")

# 5- Crea una cadena que contenga una frase y reemplaza una palabra por otra.
frase = "Eric Hernandez Edwards"
reemplazo = "Calvin"
print(frase.replace("Hernandez", reemplazo))

# 6- Escribe un programa que convierta un número de Fahrenheit a Celsius.
F = 38
formula = (F - 32) * 5/9
print(f"{formula:.2f}")

# 7- Crea una lista de tus colores favoritos e imprímela.
colores = ["verde", "negro", "azul", "turquesa"]
print(colores)

# 8- Escribe un programa que imprima el resto de la división de dos números.
print(num_1 % num_2)

# 9- Crea un programa que calcule el promedio de tres números.
numeros = 1, 89, 25
suma = sum(numeros)
divisor = len(numeros)
promedio = suma / divisor
print(f"el promedio es: {promedio:.2f}")

# 10- Escribe un programa que imprima la longitud de una cadena.
string = "Hoy es sabado nueve de noviembre del 2024"
print(len(string))

# 11- Crea un programa que verifique si una cadena es un palíndromo.
# palindromo: si ponemos al revez una palabra tiene el mismo significado
frase = "amo la paloma "
frase = frase.replace(" ", "").lower()
frase_1 = frase[::-1]
if frase == frase_1:
    print(f"La frase: {frase}, si es un palindromo")

else:
    print(f"La frase: {frase}, no es un palindromo")

# 12- Escribe un programa que cuente cuántas veces aparece una letra en una cadena.
from collections import Counter
kadena = "Murcielago adulto extinto de alaska"
conteo = Counter(kadena.replace(" ", ""))
letra = "e"
cantidad = conteo.get(letra, 0) 
print(f"La letra '{letra}' aparece {cantidad} veces en la cadena.")

# 13- Crea un programa que imprima los números del 1 al 10 en forma de lista.
lista_numeros = [n for n in range(1, 100)]
print(lista_numeros)

# 14- Escribe un programa que imprima un mensaje dependiendo de la edad ingresada.
edad = 7
if edad > 18:
    print("es mayor de edad")
elif 17 > edad > 12:
    print("es un preadolesente")
elif 11 > edad > 6:
    print("es un niño")
else:
    print("es un bebe")

# 15- Crea un programa que imprima la secuencia de Fibonacci hasta un número dado.
def fibonacci(n):
    list_fibo = []
    a = 0
    b = 1
    for x in range(n):
        list_fibo.append(a)
        a, b = b, b + a
    return list_fibo

fibo = fibonacci(10)
print(fibo)

def fibon(p):
    s = 0
    o = 1
    li = []
    for _ in range(p):
        li.append(s)
        s, o = o, s + o
    return li
resul = fibon(20)
print(resul)

def fibonnacci(n):
    a = 0
    b = 1
    fibo_list = []
    for _ in range(n):
        fibo_list.append(a)
        a, b = b, b + a
    return fibo_list
dato = fibonnacci(20)
print(dato)

#### anagrama: una frase conforma otra frase distinta pero con las mismas letras
def anagrama(frase_1, frase_2):
    frase_1.replace(" ","").lower()
    frase_2.replace(" ","").lower()
    lista_1 = list(frase_1)
    lista_2 = list(frase_2)
    lista_1.sort()
    lista_2.sort()
    if lista_1 == lista_2:
        print("Las frases son anagramas")
    else:
        print("las frases no son anagramas")
dato = anagrama("amor", "aroma")

# Mini Proyectos:
# Crea un conversor de temperaturas (Celsius a Fahrenheit y viceversa).
# fahrenheit a celsius (F - 32) * 5/9
# celsius a fahrenheit = (celsius * 9/5) + 32
class Temperaturas:
    def __init__(self):
        pass
        
    def fahrenheit_a_celsius(self, grado):
        formula = (grado - 32) * 5/9
        return f"El resultado de convertir: {grado} grados farenheit a celsius es: {formula:.1f} grados"
    
    def celsius_a_fahrenheit(self, grado):
        formula = (grado * 9/5) + 32
        return f"El resultado de convertir: {grado} grados celsius a farenheit es: {formula:.1f} grados"
    
Tem = Temperaturas()
print(Tem.celsius_a_fahrenheit(27))
print(Tem.fahrenheit_a_celsius(82))

# Desarrolla un programa que calcule el perímetro de diferentes figuras geométricas.
# circulo pi * diametro, cuadrado 4 * L, rectangulo 2 * (b + a), triangulo suma de sus lados
class Perimetro:
    def __init__(self):
        pass
    
    def circulo(self, diametro):
        import math
        formula = math.pi * diametro
        return f"El perimetro de el circulo es: {formula:.1f}"
    
    def cuadrado(self, lado):
        formula = 4 * lado
        return f"El perimetro de el cuadrado es: {formula:.1f}"
    
    def rectangulo(self, base, altura):
        formula = 2 * (base + altura)
        return f"El perimetro de el rectangulo es: {formula:.1f}"
    
    def triangulo(self, lado_1, lado_2, lado_3):
        formula = lado_1 + lado_2 + lado_3
        return f"El perimetro de el triangulo es: {formula:.1f}"
    
formulas = Perimetro()
print(formulas.circulo(4))
print(formulas.cuadrado(5))
print(formulas.rectangulo(4,6))
print(formulas.triangulo(4,8,6))
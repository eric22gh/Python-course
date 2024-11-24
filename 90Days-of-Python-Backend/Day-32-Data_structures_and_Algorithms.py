# Día 32: Comprensiones de listas

# Teoría:
# Las comprensiones de listas son una forma concisa y eficiente de crear listas en Python. Permiten aplicar una expresión a cada elemento 
# de una colección y filtrar elementos en una sola línea de código. Esto no solo reduce la cantidad de código, sino que también mejora la legibilidad.
# La sintaxis básica es: [expresión for elemento in iterable if condición].

# Tips y Buenas Prácticas:
# Utiliza comprensiones de listas para mejorar la legibilidad y eficiencia de tu código.
# Asegúrate de que la expresión sea clara; si se vuelve demasiado compleja, considera usar un bucle tradicional.
# Puedes anidar comprensiones de listas, pero hazlo con cuidado para mantener la legibilidad.

# Ejemplos:
# Generar una lista de cuadrados:
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]
print("Cuadrados:", cuadrados)

# Filtrar números pares:
numeros = range(1, 21)
pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)

# Convertir temperaturas de Celsius a Fahrenheit:
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperaturas en Fahrenheit:", fahrenheit)

# Contar las vocales en una cadena:
cadena = "hola mundo"
vocales = [letra for letra in cadena if letra in "aeiou"]
print("Vocales:", vocales)

# Generar una lista de nombres con mayúsculas:
nombres = ["juan", "maria", "pedro"]
mayusculas = [nombre.upper() for nombre in nombres]
print("Nombres en mayúsculas:", mayusculas)

# Generar una lista de palabras con su longitud:
palabras = ["hola", "mundo", "python"]
longitudes = [len(palabra) for palabra in palabras]
print("Longitudes de palabras:", longitudes)

# Convertir euros a dolares:
euros = [10, 20, 30, 40, 50]
dolares = [eu * 1.1 for eu in euros]
print("Dólares:", dolares)

# Ejercicios:
# 1- Crea una lista de números del 1 al 10 y genera una nueva lista con sus cubos.
number = [n for n in range(1, 10)]
cubos = [c ** 3 for c in number]
print(cubos)

# 2- Filtra una lista de nombres y crea una nueva lista con aquellos que tienen más de 5 letras.
names = ["juan", "maria", "pedro", "alexander", "luz"]
letra_5 = [n for n in names if len(n) > 5]
print(letra_5)

for n in names:
    mayores = len(n)
    if mayores > 5:
        print(n)

# 3- Genera una lista de números del 1 al 50 que sean múltiplos de 3.
multiplos_3 = [n for n in range(1, 50) if n % 3 == 0]
print(multiplos_3)

# 4- Crea una lista de palabras y genera una nueva lista con la longitud de cada palabra.
palabras = ["hola", "mundo", "python"]
longitud = [ len(l) for l in palabras]
print(longitud)

# 5- Convierte una lista de valores en euros a dólares (suponiendo 1 euro = 1.1 dólares).
eu = 1.1
valores = [52, 5, 23, 4, 89]
dolares = [d * eu for d in valores]
print(dolares)

# 6- Crea una lista de números y genera una nueva lista con los números que son mayores que 10.
import random
num = [random.randint(1, 100) for n in range(10)] 
mayor_10 = [n for n in num if n > 10]
print(mayor_10)

# 7- Escribe un programa que convierta una lista de cadenas a mayúsculas.
cadenas = ["eric", "hernandez", "helen", "calvin"]
mayus = [m.upper() for m in cadenas]
print(mayus)

# 8- Genera una lista de números del 1 al 100 y filtra los que son divisibles por 5.
divisibles = [n for n in range(1, 100) if n % 5 == 0]
print(divisibles)

# 9- Crea una lista de nombres y genera una nueva lista que contenga solo los nombres que empiezan con 'A'.
cadenas = ["eric", "hernandez", "helen", "calvin", "arelis", "alex"]
letra_A = [ a for a in cadenas if a[0].capitalize() == "A"]
print(letra_A)

# 10- Convierte una lista de temperaturas en Kelvin a Celsius.
# formula = k - 273.15
grados_kelvin = [300, 1000, 100, 562, 369, 897]
grados_celsius = [n - 273.15 for n in grados_kelvin]
for tem in grados_celsius:
    print(f"{tem:.2f}")

# 11- Crea una lista de números y genera una nueva lista con el doble de cada número.
numb = [n * 2 for n in range(1, 25)]
print(numb)

# 12- Filtra una lista de palabras para obtener solo aquellas que contienen la letra 'e'.
cadenas = ["eric", "hernandez", "helen", "calvin", "arelis", "alex"]
letra_e = [e for e in cadenas if "e" in e]
print(letra_e)

# 13- Crea una lista de números y genera una lista con los que son menores que 50.
me = [random.randint(1, 100) for n in range(8)]
menores = [n for n in me if n < 50]
print(menores)

# 14- Escribe un programa que genere una lista de los primeros 10 números de la serie Fibonacci.
def fibonacci(n):
    if n <= 0:
        return "Error: n debe ser un número entero positivo."
    if isinstance(n, int):
        a = 0
        b = 1
        fibo = []
        for _ in range(n):
            fibo.append(a)
            a, b = b, b + a
        return fibo
dato = fibonacci(10)
print(dato)

# 15- Crea una lista de fechas en formato "DD/MM" y genera una nueva lista con el formato "MM-DD".
def convertir_fechas(fechas):
    fechas_convertidas = []
    for fecha in fechas:
        if len(fecha) == 5 and fecha[2] == '/':
            dia, mes = fecha.split("/")
            fechas_convertidas.append(f"{mes}-{dia}")
        else:
            fechas_convertidas.append("Error: Formato inválido")
    return fechas_convertidas

fechas_2 = convertir_fechas(["01/01", "02/02", "03/03", "04/04", "05/05", "06/06", "07/07", "08/08", "09/09", "10/10"])
print(fechas_2)

# Mini Proyectos:
# Desarrolla un programa que genere una lista de números primos hasta un número dado utilizando comprensiones de listas.
def primos(n):
    return [p for p in range(2, (n + 1)) if p % 2 == 0]
dato = primos(25)
print(dato)

# Crea un programa que tome una lista de palabras y genere una lista de las palabras que son palíndromos.
# una palabra es un palindromo cuando se lee igual al derecho y al revez
def palindrome(palabras_):
        import re
        if not isinstance(palabras_, list):
            raise ValueError("La entrada debe ser una lista de palabras.")
        words = [re.sub(r"[ ,;.:\d]", "", p).lower() for p in palabras_]
        palindromos = [palabra for palabra in words if palabra == palabra[::-1]]
        return palindromos
dato = palindrome(["ala", "oso", "apipa", "ano na", "zona", "todo", "aviva"])
print(dato)

def palindromo(palabras_):
        import re
        word = [re.sub(r"[ ,;:.\d]","", palabra).lower() for palabra in palabras_ if re.sub(r"[ ,;:.\d]","", palabra).lower() == re.sub(r"[ ,;:.\d]","", palabra[::-1]).lower()]
        return word
dato = palindromo(["ala", "oso", "apipa", "ano na", "zona", "todo", "aviva:"])
print(dato)
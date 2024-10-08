# Día 16: Módulos y Paquetes
# En Python, módulos y paquetes son conceptos fundamentales para organizar y reutilizar el código de manera eficiente.

# Módulos: Son archivos individuales que contienen definiciones y declaraciones en Python, como funciones, clases y variables.
# Paquetes: Son colecciones de módulos organizados en directorios. Los paquetes facilitan la organización de módulos relacionados en una estructura jerárquica.

# Tips del Tema
# Módulos: Un módulo es un archivo con extensión .py que contiene definiciones y declaraciones en Python.
# Importación: Los módulos se importan usando las palabras clave import y from, lo que permite reutilizar funciones, clases y variables definidas en el módulo.

# Paquetes: Un paquete es un directorio que contiene un archivo especial llamado __init__.py (aunque puede estar vacío) y otros módulos.
# Estructura: Los paquetes pueden contener subpaquetes, permitiendo una estructura jerárquica de módulos.

# Módulos con dependencias: Un módulo puede depender de otros módulos. Asegúrate de importar los módulos necesarios en la parte superior del archivo.

# Módulos de terceros: Además de módulos y paquetes personalizados, Python tiene una vasta colección de módulos de terceros 
# que puedes instalar y usar, como requests para hacer solicitudes HTTP o numpy para cálculos numéricos.

################### Importar Módulos

# Importar un módulo completo
import math

import my_module.module2

print(math.sqrt(16))  # Salida: 4.0

# Importar una función específica de un módulo
from math import sqrt

print(sqrt(25))  # Salida: 5.0

# Importar un módulo con un alias
import math as m

print(m.pow(2, 3))  # Salida: 8.0

##### Crear y Usar Módulos Propios

# import mi_modulo # crear un archivo mi_modulo y ponerle el siguiente codigo

# # mi_modulo.py
# def saludar(nombre):
#     return f"Hola, {nombre}!"
# PI = 3.1416

# #### despues en otro archivo llamar a ese modulo, de la siguiente manera:
# print(mi_modulo.saludar("Mundo")) 
# print(mi_modulo.PI)                


######### Crear y Usar Paquetes

# my_module/
#     modulo1.py ## en cada archivo poner un codigo(funcion)
#     modulo2.py

from my_module import modulo1, module2
print(modulo1.saludar("alex"))
print(module2.hello("edwards"))

########## Paquetes anidados: Los paquetes pueden contener subpaquetes, creando una estructura de directorios más compleja.

# mi_paquete/
#     __init__.py
#     subpaquete/
#         __init__.py
#         modulo3.py

################# Ejercicios
# Ejercicio 1: Crea un paquete llamado operaciones.py que contenga funciones para sumar, restar, multiplicar y dividir dos números. 
# Luego, importa y usa estas funciones en otro archivo.
from my_module import operaciones
print(operaciones.suma(50, 50))
print(operaciones.dividir(20, 50))
print(operaciones.resta(20, 50))
print(operaciones.multiplicar(20, 50))

# Ejercicio 2: Crea un paquete llamado my_module que contenga dos módulos: circulo.py y rectangulo.py. 
# Cada módulo debe tener funciones para calcular el área y el perímetro de la figura correspondiente. 
# Luego, importa y usa estas funciones en otro archivo.
from my_module import circulo, rectangulo
print(circulo.area_circulo(4))
print(circulo.perimetro_circulo(4))
print(rectangulo.area_rectangunlo(4, 3))
print(rectangulo.perimetro_rectangulo(4, 3))

# Ejercicio 3: Define un módulo llamado utilidades.py que contenga una función para contar las palabras en una cadena de texto. 
# Luego, importa y usa esta función en otro archivo.
import utilidades as contar
print(contar.contar_palabras("eric alexander hernandez Edwards"))

# Ejercicio 4: Crea un módulo llamado utilidades.py que contenga funciones para convertir entre diferentes unidades de medida (por ejemplo,
# kilómetros a millas y viceversa). Luego, importa y usa estas funciones en otro archivo.
import utilidades as coversion
print(coversion.kilometros_millas(4))
print(coversion.millas_kilometros(5))

# Ejercicio 5: Define un paquete llamado my_module que contenga dos módulos: ingresos.py y gastos.py. 
# Cada módulo debe tener funciones para calcular los ingresos y gastos totales, respectivamente. 
# Luego, importa y usa estas funciones en otro archivo.
from my_module import gastos, ingresos
print(gastos.calculo_de_gastos(10000, 800000))
print(ingresos.calculo_ingresos(1000000, 10300))

# Ejercicio 6: Crea un módulo llamado utilidades.py que contenga funciones para obtener la fecha y hora actuales en diferentes formatos. 
# Luego, importa y usa estas funciones en otro archivo.
import utilidades as fecha_o_hora
print(fecha_o_hora.fecha_actual(""))
print(fecha_o_hora.hora_actual(""))

# Ejercicio 7: Define un módulo llamado utilidades.py que contenga funciones para manipular cadenas de texto 
# (por ejemplo, convertir a mayúsculas, minúsculas, etc.). Luego, importa y usa estas funciones en otro archivo.
import utilidades as manipular
print(manipular.manipular_mayuzcula("mUrCiElAgOs"))
print(manipular.manipular_minuscula("mUrCiElAgOs"))
print(manipular.manipular_letra_capital("mUrCiElAgOs"))

# Ejercicio 8: Crea un paquete llamado my_module que contenga dos módulos: promedio.py y mediana.py. 
# Cada módulo debe tener funciones para calcular el promedio y la mediana de una lista de números, respectivamente. 
# Luego, importa y usa estas funciones en otro archivo.
from my_module import mediana, promedio
print(mediana.calcular_mediana([5, 10, 55, 69, 20, 56, 223]))
print(promedio.promedio_lista([5, 10, 55, 69, 20, 56, 223]))

# Ejercicio 9 (Teoría): ¿Qué son los módulos y paquetes en Python y cómo facilitan la organización y reutilización del código?
# los modulos Son archivos individuales que contienen definiciones y declaraciones en Python.
# los paquetes Son colecciones de módulos organizados en directorios....los 2 juntos ayudan a la organizacion y reutilizacion del codigo.

# Ejercicio 10 (Práctica): Escribe un programa que defina un paquete my_module con módulos matematicas.py y cadenas.py. 
# El módulo matematicas.py debe contener funciones para operaciones matemáticas básicas y el módulo cadenas.py debe contener funciones 
# para manipulación de cadenas. Importa y usa estas funciones en otro archivo.
from my_module import cadenas, matematicas
print(matematicas.suma(10,53))
print(matematicas.resta(100,53))
print(matematicas.multiplicar(10,53))
print(matematicas.dividir(100,53))
print(cadenas.manipular_mayus("hErNaNdEz"))
print(cadenas.manipular_minus("hErNaNdEz"))

# Ejercicio 11: Utiliza el módulo datetime junto con funciones para imprimir la fecha y hora actuales y calcular la diferencia entre dos fechas.
# Módulo: datetime; para manipular fechas, horas y realizar cálculos con fechas de una manera sencilla
import datetime, time
def datos_horas(fecha1, fecha2):
    # hora = time.strftime("%H:%M:%S")
    hora = datetime.datetime.now().time()
    diferencia = fecha1 - fecha2
    return F"La hora actual es: {hora} y la diferencia entre las fechas ingresadas es de: {diferencia.days} dias"

fecha1 = datetime.date(2024, 9, 29)
fecha2 = datetime.date(2023, 10, 22)
datos = datos_horas(fecha1, fecha2)
print(datos)

# Ejercicio 12: Usa el módulo os para crear un script que verifique si un archivo específico existe en el directorio actual y si no, lo cree.
# Módulo: os; interactuar con el sistema operativo, permitiendo acceder y manipular el sistema de archivos, crear, eliminar 
# y verificar la existencia de archivos y directorios
import os 
file = "eric.txt"
try:
    if os.path.exists(file):
        print(F"El archivo: {file} existe")
    else:
        with open(file, "w") as f:
            f.write("Este archivo es nuevo")
except Exception as e:
    print(f"Error al manipular el archivo: {e}")

# Ejercicio 13: Utiliza el módulo random junto con bucles para generar una lista de 10 números aleatorios y luego imprimir el mayor y el menor.
# Módulo: random:  generar números aleatorios, que se pueden utilizar en diferentes tipos de aplicaciones, como simulaciones, 
# juegos y selección aleatoria de elementos.
import random
numeros = [random.randint(1,100) for nu in range(10)]
print(max(numeros))
print(min(numeros))

# Ejercicio 14: Usa el módulo sys para recibir dos argumentos de la línea de comandos, sumarlos e imprimir el resultado.
# Módulo: sys; funciones y variables que se usan para manipular diferentes partes del entorno del intérprete de Python. 
import sys
# Verifica que se hayan proporcionado los argumentos
if len(sys.argv) != 3:
    print("Por favor, proporcione dos números como argumentos.")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Ambos argumentos deben ser números enteros.")

# Ejercicio 15: Utiliza el módulo math junto con condicionales para verificar si un número es primo y, si no lo es, calcular su factorial.
# Módulo: math; proporciona acceso a funciones matemáticas avanzadas. La función math.factorial(n) 
# devuelve el factorial de un número entero no negativo
import math
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numero = 7
if es_primo(numero):
    print(f"El número {numero} es un número primo.")
else:
    print(f"El número {numero} no es primo. Su factorial es: {math.factorial(numero)}")

# Ejercicio 16: Usa el módulo collections para contar las apariciones de cada carácter en una cadena de texto ingresada por el usuario.
# Módulo: collections (Counter); parte de la biblioteca estándar de Python y proporciona tipos de datos especializados 
# como Counter, deque, OrderedDict.
from collections import Counter
string = "hernandez"
print(Counter(string))

# Ejercicio 17: Utiliza el módulo json junto con diccionarios para almacenar información de un estudiante (nombre, edad, notas), convertirlo en JSON y luego imprimirlo.
# Módulo: json; Permite trabajar con datos en formato JSON
import json
estudiante = {
    "nombre": "Marcos",
    "edad": 20,
    "notas": [85, 90, 78, 92]
}
estudiante_json = json.dumps(estudiante, indent=4)
print(estudiante_json)
# NOTA:json.dumps() para convertir un diccionario de Python en una cadena JSON si necesitas exportar los datos nuevamente a JSON.

# Ejercicio 18: Usa el módulo calendar para imprimir el calendario del mes actual y determinar si un año ingresado por el usuario es bisiesto.
# Módulo: calendar
import calendar 
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatmonth(2024, 9))

year = 2023
if calendar.isleap(year):
    print(F"el ano: {year} es un año bisiesto")
else:
    print(F"el ano: {year} no es un año bisiesto")

# for day in calendar.day_name: # obtener los dias de la semana
#     print(day)

# Ejercicio 19: Utiliza el módulo statistics junto con listas para calcular la media, mediana y desviación estándar de una lista de números ingresada por el usuario.
# Módulo: statistics: proporciona funciones para realizar cálculos estadísticos básicos, como la media, mediana, moda y desviación estándar.
import statistics 
print(statistics.mean([1, 500, 56, 89]))
print(statistics.median([1, 500, 56, 89]))
print(statistics.stdev([1, 500, 56, 89]))

###### o
numeros = input("Ingrese una lista de números separados por comas: ")
lista_numeros = [float(num) for num in numeros.split(",")]
print(f"La media es: {statistics.mean(lista_numeros)}")
print(f"La mediana es: {statistics.median(lista_numeros)}")
print(f"La desviación estándar es: {statistics.stdev(lista_numeros)}")

# Ejercicio 20: Usa el módulo itertools para generar todas las combinaciones posibles de una lista de tres elementos y luego imprimirlas.
# Módulo: itertools; permite crear combinaciones, permutaciones y productorias, así como realizar operaciones eficientes sobre grandes secuencias de datos.
import itertools
lista = [20, 56, 89]
for r in range(1, len(lista) + 1):
    print(f"Combinaciones de tamaño {r}: {list(itertools.combinations(lista, r))}")

print(list(itertools.combinations(lista, 2)))

# Ejercicio 21: Utiliza el módulo re (expresiones regulares) para validar si un correo electrónico ingresado por el usuario tiene el formato correcto.
# Módulo: re; para trabajar con expresiones regulares en Python, son útiles para validar formatos (como correos, números de teléfono, etc.) 
import re
correos = "pop@gmail.com, pita.com, eric.rh@hotmail.com"
patron = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
correos_lista = correos.split(", ")
validos = [correo for correo in correos_lista if re.match(patron, correo)]
print(f"Correos válidos: {validos}")

# Ejercicio 22: Usa el módulo time junto con un bucle para medir cuánto tiempo tarda en calcularse la suma de los primeros 10000 números naturales.
# Módulo: time; trabajar con funciones relacionadas con el tiempo, como medir la duración de eventos, realizar pausas en la ejecución del programa, y obtener la hora y fecha actual.
import time 
start_time = time.perf_counter()
lista_n = [int(numeros) for numeros in range(1, 10001)]
print(sum(lista_n))
end_time = time.perf_counter()
duracion = end_time - start_time
print(F"el tiempo que dura el bucle en calcular la suma es de: {duracion:.5f}")

# Ejercicio 23: Utiliza el módulo hashlib para generar un hash SHA-256 de una contraseña ingresada por el usuario y luego imprimirlo.
# Módulo: hashlib; funciones de hashing criptográficas para generar resúmenes de mensajes o "hashes" a partir de datos. 
# Estos hashes son representaciones únicas y de longitud fija, ideales para proteger contraseñas o verificar la integridad de datos
import hashlib 
contraseña = "hola mundo"
hash_256 = hashlib.sha256()
hash_256.update(contraseña.encode())
result = hash_256.hexdigest()
print(result)

# Ejercicio 24: Usa el módulo csv junto con listas para guardar los datos de 5 empleados (nombre, edad, salario) en un archivo CSV y luego leerlos.
# Módulo: csv; permite leer y escribir archivos en formato CSV (Comma-Separated Values), 
# que es un formato ampliamente utilizado para almacenar datos tabulares en archivos de texto
import csv
empleados = [
    ["nombre", "edad", "salario"],
    ["Eric", 30, 180000],
    ["alex", 25, 556000],
    ["helen", 35, 250000]
]
with open("empleados.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(empleados)

with open("empleados.csv", "r") as file:
    reader = csv.reader(file)
    for read in reader:
        print(read)

# Ejercicio 25: Utiliza el módulo pathlib para verificar si un directorio existe y, si no, crearlo y agregar un archivo con un mensaje de bienvenida.
# Módulo: pathlib; proporciona una forma orientada a objetos de trabajar con rutas de archivos y directorios. 
# Facilita las operaciones comunes del sistema de archivos como verificar si un archivo o directorio existe, crear directorios, leer o escribir archivos, y mucho más. 
# Además, permite manejar rutas de manera multiplataforma sin necesidad de preocuparse por las diferencias entre sistemas operativos.
from pathlib import Path
directorio_nuevo = Path("mi_directorio")
if directorio_nuevo.exists():
    print("el directorio si existe")
else:
    directorio_nuevo.mkdir()
    print("el directorio fue creado")

archivo = directorio_nuevo / "mensaje.txt"
archivo.write_text("¡Bienvenido a tu nuevo directorio!")
print(f"El archivo '{archivo.name}' fue creado con un mensaje de bienvenida.")

# Ejercicio 26: Usa el módulo urllib para realizar una solicitud HTTP a una página web y contar cuántas veces aparece una palabra específica en la respuesta.
# Módulo: urllib; mediante solicitudes HTTP y FTP. Proporciona funciones para abrir, leer y enviar datos a través de internet. 
# Su submódulo urllib.request es particularmente útil para realizar solicitudes a páginas web, 
import urllib.request, re

with urllib.request.urlopen('https://www.python.org/') as response:
    html_content = response.read().decode('utf-8')

palabra = "Python"
ocurrencias = re.findall(rf"\b{palabra}\b", html_content)
print(f"La palabra '{palabra}' aparece {len(ocurrencias)} veces en la página.")

# Ejercicio 27: Utiliza el módulo configparser junto con funciones para leer un archivo de configuración y mostrar el valor de una clave específica.
# Módulo: configparser: para configurar y leer archivos.INI en windows
import configparser
config_eric = configparser.ConfigParser()

config_eric['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
}
config_eric['forge.example'] = {'User': 'hg'}
config_eric['topsecret.server.example'] = {'Port': '50022', 'ForwardX11': 'no'}

with open('mi_config.ini', 'w') as configfile:
    config_eric.write(configfile)

def read_cofig_init(archivo, seccion, clave):
    config_eric.read(archivo)
    try:
        return config_eric[seccion][clave]
    except KeyError:
        return f"La sección '{seccion}' o la clave '{clave}' no existe."

dato = read_cofig_init('mi_config.ini', 'DEFAULT', 'ServerAliveInterval' )
print(dato)
config_eric.read('mi_config.ini')
# print(config_eric['forge.example']['User'])
# print(config_eric['topsecret.server.example']['port'])
# print(config_eric['DEFAULT']['compressionlevel'])

# Ejercicio 28: Usa el módulo zipfile junto con pathlib para comprimir un archivo existente en el sistema y luego descomprimirlo.
# Módulo: zipfile; permite crear, leer, escribir y extraer archivos ZIP. Este formato de archivo es ampliamente utilizado para 
# comprimir y descomprimir múltiples archivos.
import zipfile
from pathlib import Path
archivo_eric = Path("eric.txt")
if archivo_eric.exists():
    with zipfile.ZipFile("mi_archivo.zip", "w") as my_zip:
        my_zip.write(archivo_eric)
else:
    print("el archivo no existe")

try:
    with zipfile.ZipFile("mi_archivo.zip", "r") as my_zip:
        my_zip.extractall("extraido")  # Carpeta de extracción
        print("El archivo fue descomprimido correctamente.")
except FileNotFoundError:
    print("El archivo ZIP no existe.")
except zipfile.BadZipFile:
    print("El archivo ZIP está corrupto.")
    
# print(archivo_eric.exists())
# print(archivo_eric.is_file())

# Ejercicio 29: Utiliza el módulo logging junto con estructuras de control para registrar eventos en un archivo cuando ocurra un error al dividir dos números.
# Módulo: logging; herramienta esencial para registrar eventos, errores, advertencias y otros mensajes en aplicaciones de Python.
import logging
logging.basicConfig(filename='mi_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def dividir_numeros(a, b):
    try:
        resultado = a / b
        logging.info(f'División: {a} / {b} = {resultado}')
        return resultado
    except ZeroDivisionError:
        logging.error('Error: División por cero')
        return None

dividir_numeros(10, 2) 
dividir_numeros(10, 0) 

# Ejercicio 30: Usa el módulo subprocess junto con condicionales para ejecutar un comando del sistema operativo dependiendo del sistema en el que se ejecute (Windows o Linux).
# Módulo: subprocess
import subprocess, platform
sistema = platform.system()
if sistema == "Windows":
    comando = "dir"
elif sistema == "Linux" or sistema == "Darwin":  # 'Darwin' para macOS
    comando = "ls"
else:
    print("Sistema operativo no soportado.")
    exit()

resultado = subprocess.run(comando, stdout=subprocess.PIPE, shell=True, text=True)
print(resultado.stdout)
print(f"El comando '{comando}' se ejecutó en {sistema}.")


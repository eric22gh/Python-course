##### modulos; donde tenemos codigo, cualquier archivo .py

#import my_module
# my_module.sumvalue(55,56,23)
# my_module.restavalue(52,6,5)

from my_module import sumvalue, restavalue
sumvalue(55,56,23)
restavalue(52,6,5)

############ modulos por sistema

# Módulos Integrados

# sys: Proporciona acceso a variables y funciones relacionadas con el intérprete de Python.
import sys
print(sys.version)  # Imprime la versión de Python


# os: Proporciona una forma de interactuar con el sistema operativo.
import os
print(os.getcwd())  # Imprime el directorio de trabajo actual


# math: Ofrece funciones matemáticas como trigonometría, logaritmos y operaciones de raíz.
import math
print(math.pi) # valor del numero pi
print(math.sqrt(100)) # raiz
print(math.pow(100)) # la potencia

from math import pi as PI_ERIC 
print(PI_ERIC)
print(math.sqrt(16))  # Imprime la raíz cuadrada de 16


# random: Permite generar números aleatorios y realizar selecciones aleatorias.
import random
print(random.randint(1, 10))  # Imprime un número entero aleatorio entre 1 y 10


# datetime: Proporciona clases para manipular fechas y tiempos.
import datetime
print(datetime.datetime.now())  # Imprime la fecha y hora actual


# json: Permite trabajar con datos en formato JSON.
import json
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)  # Imprime el diccionario {'name': 'John', 'age': 30}


# re: Ofrece soporte para expresiones regulares.
import re
pattern = r'\d+'
string = '123abc'
match = re.match(pattern, string)
print(match.group())  # Imprime '123' si hay un match


# collections: Proporciona contenedores de datos especializados.
from collections import Counter
print(Counter(['a', 'b', 'a']))  # Imprime Counter({'a': 2, 'b': 1})


# itertools: Ofrece herramientas para crear iteradores.
import itertools
print(list(itertools.chain([1, 2, 3], [4, 5, 6])))  # Imprime [1, 2, 3, 4, 5, 6]


# functools: Proporciona funciones de orden superior para trabajar con otras funciones.
import functools
result = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(result)  # Imprime 10


############################## Módulos Externos (Requieren instalación con pip)


# requests: Facilita el envío de solicitudes HTTP en Python.
import requests
response = requests.get('https://api.example.com/data')
print(response.status_code)  # Imprime el código de estado de la respuesta


# scipy: Proporciona algoritmos y herramientas para matemáticas avanzadas, ciencias e ingeniería.
# import scipy.integrate
# result = scipy.integrate.quad(lambda x: x**2, 0, 1)
# print(result)  # Imprime el resultado de la integración


# Django: Framework de alto nivel para el desarrollo rápido de aplicaciones web.
# Este ejemplo es conceptual, normalmente se ejecuta en un entorno de proyecto Django.
# Ejecutar 'django-admin startproject mysite' para iniciar un nuevo proyecto de Django.


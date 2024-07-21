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




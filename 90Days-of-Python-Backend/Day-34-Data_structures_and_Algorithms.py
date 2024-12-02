# Día 34: Comparación entre listas y tuplas
# Teoría:
# Aunque tanto las listas como las tuplas se utilizan para almacenar colecciones de elementos, tienen diferencias clave:
# Mutabilidad: Las listas son mutables (puedes cambiar sus elementos), mientras que las tuplas son inmutables 
# (no puedes cambiar sus elementos después de crearlas).
# Sintaxis: Las listas se definen con corchetes [], mientras que las tuplas se definen con paréntesis ().
# Uso: Usa listas cuando necesites una colección de elementos que pueda cambiar. 
# Usa tuplas cuando los elementos no deben cambiar, lo que puede ayudar a mejorar el rendimiento.

# # Tips y Buenas Prácticas:
# Utiliza listas cuando necesites una colección de elementos que puede cambiar.
# Opta por tuplas cuando la colección debe permanecer constante, lo que puede ayudar a mejorar el rendimiento.
# Recuerda que las tuplas pueden ser utilizadas como claves en diccionarios, mientras que las listas no.

# Ejemplos:
# Uso de Listas:
lista_frutas = ['manzana', 'banana', 'naranja']
lista_frutas.append('kiwi')
print("Lista de frutas:", lista_frutas)

# Uso de Tuplas:
tupla_frutas = ('manzana', 'banana', 'naranja')
# tupla_frutas.append('kiwi')  # Esto generará un error, por append es un metodo de una lista y tuplas_frutas es una tupla
print("Tupla de frutas:", tupla_frutas)

# tuplas como claves en diccionarios:
diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
clave = 'clave2'
print(f'El valor asociado a la clave "{clave}" es: {diccionario[clave]}')

import time
# Comparar tiempos de acceso
lista = [i for i in range(15)]
tupla = tuple([i for i in range(15)])

start = time.time()
print(lista)
end = time.time()
print(f'Acceso a lista tomó: {start - end} segundos')

start = time.time()
print(tupla)
end = time.time()
print(f'Acceso a tupla tomó: {start - end} segundos')

# Ejercicios:
# 1- Crea una lista y una tupla con los mismos elementos y compara sus longitudes.
lista_elementos = [1, 2, 3, 4, 5]
tupla_elementos = (1, 2, 3, 4, 5)
print(f'La longitud de la lista es: {len(lista_elementos)} y la longitud de la tupla es: {len(tupla_elementos)}')

# 2- Intenta modificar un elemento de la lista y de la tupla.
try:
    lista_elementos[2] = 10
    tupla_elementos[2] = 10
    print(f'El tercer elemento de la lista es: {lista_elementos[2]} y el tercer elemento de la tupla es: {tupla_elementos[2]}')
except TypeError as e:
    print(f'Error: {e}')

# 3- Crea un diccionario que use tuplas como claves y listas como valores.
diccionario = {'clave1': [1, 2, 3], 'clave2': [4, 5, 6], 'clave3': [7, 8, 9]}
print(diccionario['clave3'])

# 4- Escribe un programa que determine si un elemento está en una lista y en una tupla.
def esta_en_lista(elemento, lista):
    return elemento in lista

def esta_en_tupla(elemento, tupla):
    return elemento in tupla

print(esta_en_lista(5, [1, 2, 3, 4, 5]))
print(esta_en_tupla(5, (1, 2, 3, 4, 5)))

# 5- Compara el tiempo de ejecución de agregar elementos a una lista y a una tupla.
import time
start = time.time()
lista = []
for i in range(-50, 100):
    lista.append(i)
end = time.time()
print(f"El tiempo de ejecución de agregar elementos a una lista es: {start - end} segundos")

start = time.time()
tupla = ()
for i in range(-50, 100):
    tupla = tupla + (i,)
end = time.time()
print(f"El tiempo de ejecución de agregar elementos a una tupla es: {start - end} segundos")

# 6- Crea una lista de nombres y una tupla con los mismos nombres, luego imprime ambos.
lista_nombres = ['alex', 'eric', 'greivin', 'rad', 'carlos']
tupla_nombres = ('alex', 'eric', 'greivin', 'rad', 'carlos')
print(f'Los nombres de la lista son: {lista_nombres} y los nombres de la tupla son: {tupla_nombres}')

# 7- Escribe un programa que use una lista para almacenar calificaciones y una tupla para almacenar el promedio.
calificaciones = [89, 9, 22, 1, 2]
promedio = sum(calificaciones) / len(calificaciones)
print(f'El promedio de las calificaciones es: {promedio}')

# 8- Crea un programa que imprima todos los elementos de una lista y una tupla.
lista_elementos = [1, 2, 3, 4, 5]
tupla_elementos = (1, 2, 3, 4, 5)
print(f'Los elementos de la lista son: {lista_elementos} y los elementos de la tupla son: {tupla_elementos}')

# 9- Desarrolla un programa que almacene datos de estudiantes en listas y tuplas y compare los métodos de acceso.
estudoiantes = ['alex', 'eric', 'greivin', 'rad', 'carlos']
estudoiantes_tupla = ('alex', 'eric', 'greivin', 'rad', 'carlos')
print(f'Los estudiantes son: {estudoiantes} y los estudiantes son: {estudoiantes_tupla}')

# 10- Crea un programa que convierta una lista de números a una tupla y viceversa.
lista_numeros = [1, 2, 3, 4, 5]
tupla_numeros = tuple(lista_numeros)
print(f'Los numeros de la lista son: {lista_numeros} y los numeros de la tupla son: {tupla_numeros}')

# 11- Escribe un programa que verifique si una tupla está contenida en una lista.
def esta_contenida(tupla, lista):
    return all(elemento in lista for elemento in tupla) # all() devuelve True si todos los elementos de la tupla estan en la lista

print(esta_contenida((1, 2, 30), [1, 2, 3, 4, 5]))

def esta_contenida(tupla, lista):
    return any(elemento in lista for elemento in tupla) # any() devuelve True si al menos un elemento de la tupla esta en la lista

print(esta_contenida((1, 2, 30), [1, 2, 3, 4, 5]))

# 12- Crea una lista de palabras y una tupla con las longitudes de esas palabras.
lista_palabras = ['alex', 'eric', 'greivin', 'rad', 'carlos']
tupla_palabras = tuple([len(palabra) for palabra in lista_palabras])
print(f"Las palabras de la lista son: {lista_palabras} y las longitudes son: {tupla_palabras}")

# 13- Desarrolla un programa que use una lista para almacenar temperaturas y una tupla para almacenar la temperatura máxima y mínima.
temperaturas = [20, 21, 22, 23, 24]
temperaturas_max = max(temperaturas)
temperaturas_min = min(temperaturas)
print(f"Las temperaturas son: {temperaturas} y la temperatura maxima es: {temperaturas_max} y la temperatura minima es: {temperaturas_min}")

# 14- Escribe un programa que imprima el primer elemento de una lista y de una tupla.
lista_elementos = [1, 2, 3, 4, 5]
tupla_elementos = (1, 2, 3, 4, 5)
print(f"El primer elemento de la lista es: {lista_elementos[0]} y el primer elemento de la tupla es: {tupla_elementos[0]}")

# 15- Crea un programa que almacene varios registros de empleados usando listas y tuplas.
empleados = [
    ('Alex', 20, 'Desarrollador'),
    ('Eric', 22, 'Disenador'),
    ('Greivin', 22, 'Desarrollador'),
    ('Rad', 22, 'Desarrollador'),
    ('Carlos', 22, 'Desarrollador')
]

for empleado in empleados:
    print(f"El empleado {empleado[0]} tiene {empleado[1]} años y es {empleado[2]}")

# Mini Proyectos:
# Desarrolla un programa que gestione un conjunto de datos utilizando tanto listas como tuplas, mostrando las diferencias en su uso.
class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

estudiantes = [
    Estudiante('Alex', 20, 'Desarrollador'),
    Estudiante('Eric', 22, 'Disenador'),
    Estudiante('Greivin', 22, 'Desarrollador'),
    Estudiante('Rad', 22, 'Desarrollador'),
    Estudiante('Carlos', 22, 'Desarrollador')
]

for estudiante in estudiantes:
    print(f"El estudiante {estudiante.nombre} tiene {estudiante.edad} años y es {estudiante.curso}")


# Crea un programa que almacene las calificaciones de los estudiantes en tuplas y permita calcular el promedio usando listas.
class AlmacenaCalificaciones:
    def __init__(self, calificaciones):
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

calificaciones = [89, 9, 22, 1, 2]
almacena_calificaciones = AlmacenaCalificaciones(calificaciones)
print(f"El promedio de las calificaciones es: {almacena_calificaciones.calcular_promedio()}")
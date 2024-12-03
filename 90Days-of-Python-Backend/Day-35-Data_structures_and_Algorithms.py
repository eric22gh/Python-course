# Día 35: Ejercicios prácticos sobre listas y tuplas

# Este día se dedicará a la práctica intensiva de los conceptos aprendidos sobre listas y tuplas. 
# Se realizarán ejercicios que refuercen el conocimiento de los métodos, comprensiones, y las diferencias entre estas estructuras de datos.

# Ejercicios:
# 1- Crea una lista de números y utiliza comprensiones para generar una nueva lista con los números al cuadrado
import random
num = [random.randint(1, 100) for n in range(8)]
num_cuadrado = [n ** 2 for n in num]
print(num_cuadrado)

# 2- Crea una tupla que contenga varios elementos y luego convierte esa tupla en una lista.
tupla_num = tuple([random.randint(100, 250) for n in range(10)])
lista_num = list(tupla_num)
print(type(lista_num))

# 3- Escribe un programa que recorra una lista de nombres y genere una lista de tuplas con el nombre y su longitud.
def name_longitud(lista):
    nombres = lista
    longitud = tuple([len(n) for n in nombres])
    return f"Estos son los nombre: {nombres} y las longitudes de cada una: {longitud}"

print(name_longitud(["alex", "eric", "greivin", "rad", "carlos"]))

# 4- Crea un programa que reciba una lista de temperaturas y genere una tupla con las temperaturas máximas y mínimas.
temperaturas = [25, 89, 56, 23, 15, 27]
max_min = ({max(temperaturas)}, {min(temperaturas)})
print(max_min)

# 5- Desarrolla un programa que tome una lista de productos y sus precios, y genere una lista de tuplas con el nombre del producto 
# y su precio con un descuento del 10%.
def aplicar_descuento(lista_productos, descuento):
    productos_con_descuento = []
    for producto, precio in lista_productos:
        precio_con_descuento = precio - (precio * descuento) 
        new_tuple = (producto, round(precio_con_descuento, 2)) 
        productos_con_descuento.append(new_tuple)
    return productos_con_descuento

lista_productos = [
    ["pala", 250],
    ["tornillos", 20],
    ["cierra", 25000],
    ["lamina", 1150],
    ["zinc", 150]
]

descuento = 0.10
resultado = aplicar_descuento(lista_productos, descuento)
for producto, precio in resultado:
    print(f"Producto: {producto}, Precio con Descuento: {precio}")

# 6- Crea una lista de números y utiliza una comprensión de lista para filtrar solo los números negativos.
numeros = [random.randint(-100, 100) for n in range(10)]
negativos = [n for n in numeros if n < 0]
print(negativos)

# 7- Escribe un programa que tome una lista de palabras y genere una nueva lista con las palabras que contienen la letra 'a'.
palabras = ["alex", "eric", "greivin", "rad", "carlos"]
letra_a = [n for n in palabras if n[0] == "a"]
print(letra_a)

# 8- Crea una tupla con las coordenadas de un punto y calcula la distancia desde el origen. 
import math
punto = (random.randint(1, 100), random.randint(1, 100))
distancia = math.sqrt(punto[0] ** 2 + punto[1] ** 2) # sqrt para sacar la raiz y ** 2 para elevar al cuadrado
print(f"La distancia desde el origen es: {distancia} y las coordenadas son: {punto}")

# 9- Desarrolla un programa que permita al usuario ingresar varios números y los almacene en una lista, luego convierta esa lista en una tupla.
numeros = []
while True:
    num = int(input("Ingrese un numero o si quires salir ingresa 0: "))
    numeros.append(num)
    if num == 0:
        break
numeros_tupla = tuple(numeros)
print(numeros_tupla)

# 10- Crea un programa que imprima los elementos de una lista en orden inverso utilizando una tupla.
numeros = [1, 2, 3, 4, 5]
numeros_tupla = tuple(numeros)
print(numeros_tupla[::-1])

# 11- Escribe un programa que almacene datos de varios libros en tuplas y las imprima.
libros = [
    ("Libro 1", "Autor 1", 2022),
    ("Libro 2", "Autor 2", 2022),
    ("Libro 3", "Autor 3", 2022),
    ("Libro 4", "Autor 4", 2022),
    ("Libro 5", "Autor 5", 2022)
]

for libro in libros:
    print(libro)

# 12- Crea una lista de estudiantes y una tupla con sus calificaciones, luego imprime el promedio.
estudiantes = ["alex", "eric", "greivin", "rad", "carlos"]
calificaciones = tuple([random.randint(50, 100) for n in range(5)])
promedio = sum(calificaciones) / len(calificaciones)
print(f"El promedio de todos los estudiantes es: {promedio}")

# 13- Desarrolla un programa que almacene elementos en una lista y verifique si un elemento específico está presente.
elementos = []
while True:
    try:
        ele = int(input("Ingrese un elemento o 0 para detener: "))
        if ele == 0:
            break
        else:
            elementos.append(ele)
            print("elemento guardado\n")
    except ValueError:
        print("El valor ingresado no es valido\n")

for i, e in enumerate(elementos, start=1):
    print(f"Este es el elemento {i} de la lista: {e}")
try:
    item = int(input("ingrese el elemento que desea verificar: "))
    if item in elementos:
        print(f"Este elemento: {item} esta en la lista")
    else:
        print(f"Este elemento: {item} no esta en la lista")
except ValueError:
    print("El valor ingresado no es valido")

# 14- Crea una lista de precios y genera una nueva lista con precios redondeados al entero más cercano.
precios = [23.4, 15.3, 101.1, 253.8]
for price in precios:
    redondear = round(price)
    print(f"Numero: {price}, redondeado al entero mas cercano: {redondear}")

# 15- Escribe un programa que imprima la longitud de cada tupla en una lista de tuplas.
lista_tuplas = [
    ("eric"),
    ("helen"),
    ("maria"),
    ("marcos"),
    ("alex")
]
for l in lista_tuplas:
    conteo = len(l)
    print(f"La longitud de cada tupla es: {conteo}")

# Mini Proyectos:
# Crea un programa que simule un sistema de gestión de biblioteca utilizando listas para almacenar libros y tuplas para almacenar 
# la información de cada libro. El programa debe permitir agregar, eliminar y listar libros.
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.anio_publicacion}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

biblioteca = Biblioteca()

while True:
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Listar libros")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio_publicacion = input("Ingrese el anio de publicacion del libro: ")
        libro = Libro(titulo.capitalize(), autor.capitalize(), anio_publicacion)
        biblioteca.agregar_libro(libro)
        print("Libro agregado exitosamente\n")
    elif opcion == "2":
        biblioteca.listar_libros()
        if biblioteca.libros:
            titulo = input("Ingrese el titulo del libro que desea eliminar: ")
            for libro in biblioteca.libros:
                if libro.titulo == titulo:
                    biblioteca.eliminar_libro(libro)
                    print("Libro eliminado exitosamente\n")
                    break
                else:
                    print("Libro no encontrado\n")
        else:
            print("No hay libros en la biblioteca\n")
    elif opcion == "3":
        biblioteca.listar_libros()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")

# Desarrolla un programa que gestione una lista de contactos utilizando listas y tuplas, permitiendo agregar, eliminar y mostrar contactos.
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, contacto):
        self.contactos.remove(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

agenda = Agenda()

while True:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        contacto = Contacto(nombre, telefono)
        agenda.agregar_contacto(contacto)
        print("Contacto agregado exitosamente\n")
    elif opcion == "2":
        agenda.mostrar_contactos()
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        for contacto in agenda.contactos:
            if contacto.nombre == nombre:
                agenda.eliminar_contacto(contacto)
                print("Contacto eliminado exitosamente\n")
                break
    elif opcion == "3":
        agenda.mostrar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")
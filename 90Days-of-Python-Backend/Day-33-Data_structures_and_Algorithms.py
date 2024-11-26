# Día 33: Introducción a las tuplas y sus usos

# Teoría:
# Las tuplas son colecciones ordenadas e inmutables en Python. Esto significa que, una vez creadas, no puedes modificar sus elementos. 
# Se utilizan para almacenar múltiples elementos en una sola variable y son útiles cuando se necesita asegurar que los datos no cambien.
# Las tuplas se definen utilizando paréntesis () y pueden contener diferentes tipos de datos.

# Tips y Buenas Prácticas:
# Usa tuplas cuando necesites ALMACENAR DATOS QUE NO DEBEN CAMBIAR, como coordenadas o registros.
# Las tuplas pueden contener diferentes tipos de datos, pero asegúrate de que su uso sea coherente.
# REQUERDA QUE, AUNQUE LAS TUPLAS SON INMUTABLES, PUEDE CONTENER LISTAS U OTROS OBJETOS MUTABLES

# Ejemplos:
# Almacenamiento de Coordenadas:
coordenadas = (10.0, 20.0)
print(f'Coordenadas: {coordenadas}')

# Registro de Datos:
empleado = ('Juan', 'Pérez', 30, 'Desarrollador')
print(f'Empleado: {empleado}')

# Acceso a Elementos:
nombre, apellido, edad, puesto = empleado
print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Puesto: {puesto}')

# Concatenación de Tuplas:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(f'Tupla 3: {tupla3}')

# Repetición de Tuplas:
tupla_repetida = tupla1 * 3
print(f'Tupla Repetida: {tupla_repetida}')

# Longitud de Tuplas:
longitud = len(tupla1)
print(f'Longitud: {longitud}')

# Contenido de Tuplas:
contenido = tuple([1, 2, 3, 4, 5])
print(f'Contenido: {contenido}')

# Recorrido de Tuplas:
for elemento in tupla1:
    print(elemento)

# Busqueda de Elementos:
if 3 in tupla1:
    print('El elemento 3 esta presente en la tupla')

# Comparación de Tuplas:
tupla4 = (1, 2, 3)
tupla5 = (1, 2, 3)
print(tupla4 == tupla5)

# Tuplas como Claves en Diccionarios:
diccionario = {'clave1': (1, 2, 3), 'clave2': (4, 5, 6)}
print(f'Diccionario: {diccionario}')

# Tuplas como Elementos en Listas:
lista = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(f'Lista: {lista}')

# Tuplas como Elementos en Conjuntos:
conjunto = {(1, 2, 3), (4, 5, 6), (7, 8, 9, 9)}
print(f'Conjunto: {conjunto}') # ES UN set pero con elementos duplicados, porque por dentro hay una tupla con elementos duplicados

# metodos de tuplas:
# count(): Devuelve el número de veces que aparece un elemento en la tupla.
print(tupla1.count(2))

# index(): Devuelve la posición de un elemento en la tupla.
print(tupla1.index(2))

# len(): Devuelve la longitud de la tupla.
print(len(tupla1))

# max(): Devuelve el elemento máximo de la tupla.
print(max(tupla1))

# min(): Devuelve el elemento mínimo de la tupla.
print(min(tupla1))

# sorted(): Devuelve una nueva tupla con los elementos de la tupla ordenados.
print(sorted(tupla1))

# sum(): Devuelve la suma de los elementos de la tupla.
print(sum(tupla1))

# agregar un elemento a una tupla:
tupla = (1, 2, 3)
tupla = tupla + (22, "hola",)
print(f'tupla: {tupla}')

# eliminar un elemento de una tupla:
tupla = (1, 2, 3, 4, 5)
tupla = tupla[:2] # de el 2 para atras
# tupla[3:] de el 3 en adelante
print(f'tupla: {tupla}')

# Ejercicios:
# 1- Crea una tupla que almacene la información de un libro (título, autor, año).
información = ("El Cuervo", "Gabriel Garcia", 1978)
titulo, autor, año = información
print(f"El titulo es: {titulo}, del autor: {autor} y es de el año: {año}")

# 2- Intenta modificar un elemento de una tupla (debería generar un error).
try:
    información[2] = 2000
    print(información)
except TypeError as e:
    print(f"Error: No se puede modificar un elemento de una tupla. Detalle del error: {e}")

# 3- Crea una tupla con varias coordenadas y recorrela para imprimir cada coordenada.
coordenada = (10.2, 52.3, 69.5, 22.10)
for i, coor in enumerate(coordenada, start=1):
    print(f"{i}- {coor}")

# 4- Escribe un programa que intercambie dos variables utilizando tuplas.
def variable(a, b, tupla):
    tupla = list(tupla)
    tupla[0] = a
    tupla[1] = b
    tupla = tuple(tupla)
    return f"Esta es la nueva tupla: {tupla}"
dato = variable(22, 58, (10.2, 52.3, 69.5, 22.10))
print(dato)

# 5- Crea una tupla con varios elementos y calcula la suma de los números enteros en ella.
numeros = tuple([n for n in range(-10, (10 + 1))])
enteros = sum(n for n in numeros if n > 0)
print(enteros)

# 6- Crea una tupla con los días de la semana y muestra el tercer día.
def dia_semana(day):
    import calendar
    if not isinstance(day, int): # si no es un integer laza el error
        raise TypeError("El dato ingresado debe de ser un numero entero")
    if day in range(1, 8):
        d = day - 1
        dia =  tuple(calendar.day_name)
        return f"El dia numero: {day} de la semana es: {dia[d]}"
    else:
        return "Numero invalido, tiene que ser del 1 al 7"
dato = dia_semana(3)
print(dato)

# 7- Escribe un programa que almacene datos de un estudiante (nombre, edad, grado) en una tupla.
# nombre = input("ingrese el nombre")
# edad = int(input("ingrese la edad:"))
# grado = int(input("ingrese el grados"))
# estudiante = (nombre, edad, grado)
# print(estudiante)

# 8- Crea una tupla con valores de temperatura y encuentra la temperatura máxima y mínima.
temperatura = (20.2, 3.2, 56.4, 100.3, 45.1)
print(f"temperatura maxima es: {max(temperatura)} y la temperatura minima es: {min(temperatura)}")

# 9- Desarrolla un programa que tome una lista de nombres y los almacene en una tupla.
nombres = ["eric", "helen", "luis"]
tu = []
for dato in nombres:
    tu.append(dato)
new_tuple = tuple(tu)
print(new_tuple)

# 10- Crea una tupla con los meses del año y muestra la longitud de la tupla.
import calendar, re
meses = tuple(calendar.month_name[1:])
print(len(meses))

# 11- Escribe un programa que convierta una lista de números en una tupla.
import random
def lista_tupla(numbers):
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("los datos tienen que ser numeros")
    tupla_numeros = tuple(numbers)
    return tupla_numeros
dato = lista_tupla([random.randint(1, 100) for n in range(5)])
print(dato)

# 12- Crea una tupla que contenga diferentes tipos de datos y muestra cada tipo.
tupla_tipos = (2, 5.6, True, "eric")
for t in tupla_tipos:
    print(type(t))

# 13- Escribe un programa que imprima los elementos de una tupla en orden inverso.
def tupla_inversa(tup):
    nueva = tup[::-1]
    return nueva
tupla_tipos = (2, 5.6, True, "eric")
dato = tupla_inversa(tupla_tipos)
print(dato)

# 14- Crea una tupla con los nombres de tus amigos y muestra el segundo amigo.
amigos = ("maria", "carlos", "luis", "laura")
print(amigos[1])

# 15- Desarrolla un programa que almacene información de varios productos en tuplas.
class Productos():
    def __init__(self):
        self.almacenar = ()
        pass

    def guardar(self, product):
        if not isinstance(product, str):
            raise TypeError("Solo se acepta texto")
        lista_tupla2 = list(self.almacenar)
        lista_tupla2.append(product)
        self.almacenar = tuple(lista_tupla2)
        return "Producto guardado"
    
    def mostrar(self):
        if not self.almacenar:
            return "No hay productos"
        return "\n".join((f"{a}- {productos}")for a, productos in enumerate(self.almacenar, start=1))
    
    def eliminar(self, pro):
        try: 
            lista_tupla2 = list(self.almacenar)
            lista_tupla2.remove(pro.capitalize())
            self.almacenar = tuple(lista_tupla2)
            return f"Producto: {pro} elimindado"
        except ValueError:
            return "Producto no encontrado"
 
admin = Productos()
while True:
    print(
        "\n Bienvenidos a mi almacenador de productos \n"
        "1- Agregar producto \n"
        "2- Mostrar producto \n"
        "3- Eliminar productos \n"
        "4- Salir \n"
    )
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el producto: "))
        print(admin.guardar(texto.capitalize()))
    elif numero == 2:
        print(admin.mostrar())
    elif numero == 3:
        print(admin.mostrar())
        texto = str(input("ingrese la tarea que desea eliminar: "))
        print(admin.eliminar(texto.capitalize()))
    elif numero == 4:
        print("Muchas Gracias por usar mi gestor...Saliendo")
        break
    else:
        print("Ingrese un numero valido...del 1 al 4")

# anagrama: dos palabras son anagramas si contienen las mismas letras en diferente orden
def anagrama(palabra1, palabra2):
    import re 
    palabra1 = re.sub(r"[ ,;.:\d]","", palabra1.lower()) 
    palabra2 = re.sub(r"[ ,;.:\d]","", palabra2.lower())
    if sorted(palabra1) == sorted(palabra2):
        return "Las 2 palabras son anagramas"
    else:
        return "Las 2 palabras no son anagramas"
print(anagrama("hola ", "aloh"))

#Palindromo: una palabra que se lee igual al derecho y al reves
def palindromo(palabra):
    palabra = re.sub(r"[ ,;.:\d]","", palabra.lower())
    if palabra == palabra[::-1]:
        return "Es un palindromo"
    else:
        return "No es un palindromo"
print(palindromo("hola"))

# Secuencia de fibonnaci: una secuencia de numeros donde el siguiente numero es la suma de los dos anteriores
def fibonacci(n):
    a, b = 0, 1 
    lis = []
    for i in range(n):
        lis.append(a)
        a, b = b, a + b
    return lis
print(fibonacci(10))

# Mini Proyectos:
# Desarrolla un programa que almacene información de varios empleados en tuplas y permita mostrar sus datos. 
class Empleados():
    def __init__(self):
        self.almacenar = ()
        pass

    def guardar(self, empleado):
        if not isinstance(empleado, str):
            raise TypeError("Solo se acepta texto")
        lista_empleados = list(self.almacenar)
        lista_empleados.append(empleado.capitalize())
        self.almacenar = tuple(lista_empleados)
        return "Empleado guardado"
    
    def mostrar(self):
        if not self.almacenar:
            return "No hay empleados"
        return "\n".join((f"{e}- {empleados}")for e, empleados in enumerate(self.almacenar, start=1))
    
    def eliminar(self, emp):
        try:
            lista_empleados = list(self.almacenar)
            lista_empleados.remove(emp.capitalize())
            self.almacenar = tuple(lista_empleados)
            return f"Empleado: {emp} elimindado"
        except ValueError:
            return "Empleado no encontrado"
 
ad_empleados = Empleados()
while True:
    print(
        "\n Bienvenidos a mi almacenador de empleados \n"
        "1- Agregar empleado \n"
        "2- Mostrar empleado \n"
        "3- Eliminar empleados \n"
        "4- Salir \n"
    )
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el empleado: "))
        print(ad_empleados.guardar(texto.capitalize()))
        print(f"Empleado: {texto} guardado")
    elif numero == 2:
        print(ad_empleados.mostrar())
    elif numero == 3:
        print(ad_empleados.mostrar())
        texto = str(input("ingrese el empleado que desea eliminar: "))
        print(ad_empleados.eliminar(texto.capitalize()))
    elif numero == 4:    
        print("Muchas Gracias por usar mi gestor...Saliendo")
        break
    else:
        print("Ingrese un numero valido...del 1 al 4")

# Crea un programa que gestione un inventario utilizando tuplas para representar productos.
class Inventario():
    def __init__(self):
        self.almacenar = ()
        pass

    def guardar(self, producto):
        if not isinstance(producto, str):
            raise TypeError("Solo se acepta texto")
        lista_tupla2 = list(self.almacenar)
        lista_tupla2.append(producto)
        self.almacenar = tuple(lista_tupla2)
        return "Producto guardado"
    
    def mostrar(self):
        if not self.almacenar:
            return "No hay productos"
        return "\n".join((f"{a}- {productos}")for a, productos in enumerate(self.almacenar, start=1))
    
    def eliminar(self, pro):
        try:
            lista_tupla2 = list(self.almacenar)
            lista_tupla2.remove(pro.capitalize())
            self.almacenar = tuple(lista_tupla2)
            return f"Producto: {pro} elimindado"
        except ValueError:
            return "Producto no encontrado"
    
inventario = Inventario()
while True:
    print(
        "\n Bienvenidos a mi almacenador de productos \n"
        "1- Agregar producto \n"
        "2- Mostrar producto \n"
        "3- Eliminar productos \n"
        "4- Salir \n"
    )
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el producto: "))
        print(inventario.guardar(texto.capitalize()))
    elif numero == 2:
        print(inventario.mostrar())
    elif numero == 3:
        print(inventario.mostrar())
        texto = str(input("ingrese la tarea que desea eliminar: "))
        print(inventario.eliminar(texto.capitalize()))
    elif numero == 4:
        print("Muchas Gracias por usar mi gestor...Saliendo")
        break
    else:
        print("Ingrese un numero valido...del 1 al 4")
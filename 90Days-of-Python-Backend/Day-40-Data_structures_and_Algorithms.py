# Día 40: Ejercicios prácticos sobre conjuntos y diccionarios

# Teoría:
# Este día se dedicará a la práctica intensiva de los conceptos aprendidos sobre conjuntos y diccionarios. 
# Se realizarán ejercicios que refuercen el conocimiento de operaciones, métodos y el uso de estas estructuras de datos.

# Ejercicios:
# 1- Crea un conjunto de números y un diccionario con sus cuadrados.
conjunto = {1, 2, 3, 4, 5}
diccionario = {num: num**2 for num in conjunto}
print(diccionario)

# 2- Realiza operaciones de unión e intersección entre dos conjuntos y almacena los resultados en un diccionario.
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
conjunto_union = conjunto1.union(conjunto2)
conjunto_interseccion = conjunto1.intersection(conjunto2)
diccionario = {"union": conjunto_union, "interseccion": conjunto_interseccion}
print(diccionario)

# 3- Crea un diccionario que almacene la frecuencia de elementos en un conjunto.
conjunto = {1, 2, 3, 4, 5, 5, 5}
import collections
diccionario = collections.Counter(conjunto)
print(diccionario)

# 4- Desarrolla un programa que permita al usuario ingresar varios elementos y los almacene en un conjunto.
# def almacenar_elementos(elementos):
#     conjunto = set()
#     for elemento in elementos:
#         conjunto.add(elemento)
#     return conjunto

# elementos = input("Ingrese varios elementos separados por comas: ").split(",").strip().split()
# conjunto = almacenar_elementos(elementos)
# print(conjunto)

# 5- Crea un conjunto de palabras y un diccionario que almacene la longitud de cada palabra.
conjunto = {"hola", "mundo", "python"}
diccionario = {palabra: len(palabra) for palabra in conjunto}
print(diccionario)

# 6- Escribe un programa que combine dos conjuntos y almacene los resultados en un diccionario.
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
conjunto_union = conjunto1.union(conjunto2)
diccionario_resultado = {num: num for num in conjunto_union}
print(diccionario_resultado)

# 7- Crea un diccionario que almacene información sobre varias ciudades y permite al usuario consultar sus datos.
class Cuidades:
    def __init__(self):
        self.cuidades = {
            "ciudad1": "bogota",
            "ciudad2": "medellin",
            "ciudad3": "cali",
            "ciudad4": "barranquilla",
            "ciudad5": "ibague",
        }

    def consultar_ciudad(self, ciudad):
        if ciudad in self.cuidades:
            return self.cuidades[ciudad]
        else:
            return "Ciudad no encontrada"
        
cuidades = Cuidades()
ciudad = input("Ingrese el nombre de la ciudad: ")
print(cuidades.consultar_ciudad(ciudad))

# 8- Desarrolla un programa que analice dos listas de estudiantes y muestre los que están en ambas listas utilizando conjuntos.
def analizar_estudiantes(estudiantes1, estudiantes2):
    estudiantes_interseccion = estudiantes1.intersection(estudiantes2)
    
    return estudiantes_interseccion

estudiantes1 = {"Juan", "Maria", "Pedro"}
estudiantes2 = {"Maria", "Luis", "Ana"}

estudiantes_interseccion = analizar_estudiantes(estudiantes1, estudiantes2)

print("Estudiantes en ambas listas:")
for estudiante in estudiantes_interseccion:
    print(estudiante)

# 9- Crea un conjunto de frutas y un diccionario que almacene la cantidad de cada fruta.
frutas = {"manzana", "banana", "cereza", "cereza"}
diccionario = collections.Counter(frutas)
print(diccionario)

# 10- Escribe un programa que utilice un conjunto para eliminar duplicados de una lista y almacene los resultados en un diccionario.
def eliminar_duplicados(lista):
    conjunto = set()
    diccionario = {}
    for elemento in lista:
        if elemento not in conjunto:
            conjunto.add(elemento)
            diccionario[elemento] = 1
        else:
            diccionario[elemento] += 1
    return diccionario

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
diccionario = eliminar_duplicados(lista)
print(diccionario)

# 11- Crea un diccionario que almacene los precios de varios productos y permite al usuario actualizar un precio.
def actualizar_precio(productos):
    for producto, precio in productos.items():
        print(f"{producto}: {precio}")
    producto_actualizar = input("Ingrese el producto a actualizar: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    productos[producto_actualizar] = nuevo_precio
    return productos

productos = {
    "producto1": 10.99,
    "producto2": 5.99,
    "producto3": 8.99
}
print(actualizar_precio(productos))

# 12- Desarrolla un programa que utilice un conjunto para almacenar números únicos y un diccionario para contar sus ocurrencias.
def contar_numeros_unicos(conjunto):
    diccionario = {}
    for numero in conjunto:
        if numero not in diccionario:
            diccionario[numero] = 1
        else:
            diccionario[numero] += 1
    return diccionario

conjunto = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
diccionario = contar_numeros_unicos(conjunto)
print(diccionario)

# 13- Crea un conjunto de letras y un diccionario que almacene cuántas veces aparece cada letra en una cadena de texto.
letras = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "f", "g", "h", "i", "j", "k", "l", "m" }
diccionario = {letra: letra.count(letra) for letra in letras}
print(diccionario)

# 14- Escribe un programa que combine dos diccionarios y elimine las claves duplicadas.
def combinar_diccionarios(diccionario1, diccionario2):
    return diccionario1 | diccionario2

diccionario1 = {"argentina": "buenos aires", "colombia": "bogota"}
diccionario2 = {"peru": "lima", "colombia": "cartagena"}
diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
print(diccionario_combinado)

# 15- Crea un conjunto y un diccionario que almacene la relación entre estudiantes y sus calificaciones.
from random import randint
estudiantes = {"estudiante1", "estudiante2", "estudiante3"}
calificaciones = {estudiante: randint(1, 10) for estudiante in estudiantes}
print(calificaciones)

# Mini Proyectos:
# Crea un programa que gestione un club de lectura utilizando conjuntos para evitar duplicados de libros y diccionarios para almacenar información sobre cada libro.
class ClubLectura:
    def __init__(self):
        self.libros = set()
        self.libros_disponibles = {}
    
    def agregar_libro(self, libro, autor, anio_publicacion):
        if libro not in self.libros:
            self.libros.add(libro)
            self.libros_disponibles[libro] = {"autor": autor, "anio_publicacion": anio_publicacion}
            return f"Libro {libro} agregado correctamente."
        elif libro in self.libros:
            return f"El libro {libro} ya esta en el club de lectura."
        else:
            return "Error al agregar el libro."
            
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            del self.libros_disponibles[libro]
        else:
            print(f"El libro {libro} no esta en el club de lectura.")

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join((f"{e}- Libro: {libro['titulo']}, Autor: {libro['autor']}, Anio de publicacion: {libro['anio_publicacion']}")for e, libro in enumerate(self.libros, start=1))
club_lectura = ClubLectura()
while True:
    print("\nMenu:")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Mostrar libros")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        libro = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio_publicacion = input("Ingrese el anio de publicacion del libro: ")
        print(club_lectura.agregar_libro(libro, autor, anio_publicacion))
    elif opcion == 2:
        libro = input("Ingrese el titulo del libro a eliminar: ")
        club_lectura.eliminar_libro(libro)
    elif opcion == 3:
        print(club_lectura.mostrar_libros())
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")

# Desarrolla un programa que almacene las preferencias de música de un grupo de personas utilizando conjuntos y diccionarios para organizar los datos.
class Preferencias:
    def __init__(self):
        self.preferencias = {}
    
    def agregar_preferencia(self, persona, preferencia):
        if persona not in self.preferencias:
            self.preferencias[persona] = set()
        self.preferencias[persona].add(preferencia)
    
    def mostrar_preferencias(self):
        if not self.preferencias:
            return "No hay preferencias registradas."
        return "\n".join((f"{persona}: {preference}")for persona, preferences in self.preferencias.items() for preference in preferences)
    
    def eliminar_preferencia(self, persona, preferencia):
        if persona in self.preferencias and preferencia in self.preferencias[persona]:
            self.preferencias[persona].remove(preferencia)
            return "Preferencia eliminada correctamente."
        return "La preferencia no estaba registrada."
    
preferencias = Preferencias()
while True:
    print("\nMenu:")
    print("1. Agregar preferencia")
    print("2. Eliminar preferencia")
    print("3. Mostrar preferencias")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        persona = input("Ingrese el nombre de la persona: ")
        preferencia = input("Ingrese la preferencia de musica: ")
        preferencias.agregar_preferencia(persona, preferencia)
    elif opcion == 2:
        persona = input("Ingrese el nombre de la persona: ")
        preferencia = input("Ingrese la preferencia de musica a eliminar: ")
        print(preferencias.eliminar_preferencia(persona, preferencia))
    elif opcion == 3:
        print(preferencias.mostrar_preferencias())
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")
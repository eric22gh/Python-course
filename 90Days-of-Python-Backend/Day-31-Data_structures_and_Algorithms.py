# Día 31: Métodos de listas
# Teoría:
# Las listas son colecciones ordenadas y mutables en Python, lo que significa que puedes modificar su contenido. 
# Los métodos de listas permiten manipular sus elementos de diversas maneras. Aquí hay algunos de los métodos más utilizados:

# .append(elemento): Agrega un elemento al final de la lista.
# .extend(iterable): Agrega todos los elementos de un iterable (como otra lista) al final de la lista.
# .insert(indice, elemento): Inserta un elemento en una posición específica.
# .remove(elemento): Elimina la primera aparición de un elemento.
# .pop(indice): Elimina y devuelve el elemento en la posición especificada (o el último elemento si no se especifica).
# .sort(): Ordena los elementos de la lista.
# .reverse(): Invierte el orden de los elementos en la lista.
# .clear(): Elimina todos los elementos de la lista.

# Tips y Buenas Prácticas:
# Utiliza .append() para agregar un solo elemento al final de la lista.
# Usa .extend() para agregar múltiples elementos desde otra lista.
# Evita modificar la lista mientras la recorres; considera crear una copia si es necesario para evitar errores.

#ejemplo
# Agregar tareas
tareas = []
tareas.append('Comprar leche')
tareas.append('Estudiar Python')
print(tareas)

# Insertar una tarea en una posición específica
tareas.insert(1, 'Hacer ejercicio')
print("Lista de tareas después de insertar:", tareas)

# Eliminar una tarea
tareas.remove('Comprar leche')
print("Lista de tareas después de eliminar:", tareas)

# eliminar la última tarea
tarea_finalizada = tareas.pop()
print("Lista de tareas actualizada:", tareas)

# Ordenar tareas
tareas.sort()
print("Lista de tareas ordenada:", tareas)

# Invertir el orden de las tareas
tareas.reverse()
print("Lista de tareas invertida:", tareas)

# Copiar una lista
tareas_copia = tareas.copy()
print("Copia de la lista de tareas:", tareas_copia)

# Contar el número de veces que aparece un elemento
tareas_copia.count('Hacer ejercicio')

# Encontrar el índice de un elemento
tareas_copia.index('Hacer ejercicio')

# Contar el número de elementos en la lista
num_elementos = len(tareas)
print("Número de elementos en la lista:", num_elementos)

# extendiendo listas
tareas = ['Comprar leche', 'Estudiar Python']
tareas_2 = ['Hacer ejercicio', 'Lavar el carro']
tareas.extend(tareas_2)

# Iterar sobre una lista
for tarea in tareas:
    print("Tarea:", tarea)

# Limpiar la lista de tareas
tareas.clear()
print("Lista de tareas limpiada:", tareas)

# Ejercicios:
# 1- Crea una lista de tus frutas favoritas y añade una más.
frutas = ["manzana", "pera", "banano"]
frutas.insert(1, "melocoton")
frutas.append("pera")
print(frutas)

# 2- Elimina una fruta de la lista y muestra la lista actualizada.
frutas.remove("manzana")
print(frutas)

# 3 Inserta una nueva fruta en la segunda posición de la lista.
frutas.insert(1, "mora")
print(frutas)

# 4- Ordena la lista de frutas alfabéticamente.
frutas.sort()
print(frutas)

# 5- Crea un programa que cuente cuántas veces aparece un elemento en una lista.
contar = {}
for elemento in frutas:
    if elemento in contar:
        contar[elemento] += 1
    else:
        contar[elemento] = 1
if contar:
    for fruta, numero in contar.items():
        print(f"Hay una cantidad de: {numero} de: {fruta} en la lista")
else:
    print("La lista de frutas está vacía.")

# 6- Crea una lista de números del 1 al 20 y utiliza un bucle para imprimir solo los números impares.
impares = [x for x in range(1,20)if x % 2 != 0]
print(impares)

# 7- Escribe un programa que sume todos los elementos de una lista de precios.
precios = [200000, 1200, 200, 56520]
print(f"Suma total de la lista de precios: {sum(precios):.2f}")

# 8- Crea una lista que contenga los días de la semana y muéstrala.
dias = ["Lunes", "Martes", "Miercoles", "jueves", "viernes", "Sabado", "Domingo"]
for i, day in enumerate(dias, start=1):
    print(f"El dia {i} de la semana es: {day}")

import calendar
dias = list(calendar.day_name)
print(f"Dias: {dias}")

# 9- Implementa un programa que elimine los elementos duplicados de una lista.
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Martes", "Sabado", "Miercoles"]
new = list(set(lista))
print(new.sort())

# 10- Crea una lista de nombres y utiliza un bucle para imprimir cada nombre en una línea separada.
nombres = ["eric", "helen", "karol", "carlos"]
for name in nombres:
    print(name)

# 11- Escribe un programa que encuentre el índice de un elemento en una lista.
names = ["eric", "helen", "karol", "alex"]
def indice(i):
    try:
        if i.lower() not in names:
            return "No se encuentra en la lista"
        else:
            indice = names.index(i)
            return f"\n el elemento: {i} se encuentra en el indice: {indice} de la lista"
    except AttributeError as e:
        return f"\nERRor: {e}"
data = indice("helen")
print(data)

# 12- Crea una lista de calificaciones y calcula el promedio.
calificaciones = [85.6, 75.2, 88.5, 91.4, 61.5]
promedio = sum(calificaciones)/len(calificaciones)
print(f"El promedio de calificaciones es: {promedio:.2f}")

# 13- Escribe un programa que verifique si un elemento está en la lista.
print(22 in calificaciones)

# 14- Crea un programa que combine dos listas en una sola.
calificaciones.extend(nombres)
print(calificaciones)

# 15- Desarrolla un programa que imprima la lista en orden inverso.
nombres.reverse()
print(nombres)

#### fibonacci
def fibonacci(n):
    a = 0
    b = 1
    fibo = []
    for _ in range(n):
        fibo.append(a)
        a, b = b, b + a
    return fibo
dato = fibonacci(15)
print(dato)
#### anagrama: 2 palabras son anagramas cuando contienen las mismas letras pero su significado es distinto
def anagramas(frase_1, frase_2):
    import re
    word1 = list(sorted(re.sub(r"[ ,;.:\d]","", frase_1).lower()))
    word2 = list(sorted(re.sub(r"[ ,;.:\d]","", frase_2).lower()))
    if word1 == word2:
        return f"Estas 2 palabras si son anagramas"
    else:
        return f"Estas 2 palabras no son anagramas"
frases = anagramas("mani","imal")    
print(frases)
### Palindromo: una frase es un palindromo cuando se lee igual al derecho y al revez.
def palindromo(frase):
    import re
    frase1 = re.sub(r"[ ,;.:_\d]","",frase).lower()
    frase2 = frase1[::-1]
    if frase1 == frase2:
        return "La frase o palabra es un palindromo"
    else:
        return "No es un palindromo"
data = palindromo("amo la paloma")
print(data)

# Mini Proyectos:
# Desarrolla un gestor de tareas que permita agregar, eliminar y mostrar tareas, guardando las tareas en un archivo.
class Tareas:
    def __init__(self):
        self.gestor = []
        self.cargar_tareas()
        pass

    def cargar_tareas(self):
        try:
            with open("Tareas.txt", "r") as file: # leer las tareas que hay en el archivo y pasarlas al gestor
                self.gestor = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # Si el archivo no existe, se inicia la lista vacía
            self.gestor = []

    def agregar_tarea(self, tarea):
        try:
            self.gestor.append(tarea.capitalize())
            with open("Tareas.txt", "a") as file:
                data = file.write(tarea.capitalize() + "\n") # averiguar como hacer que todas la tareas queden escritas en el file de texto
            return "Muchas gracias, Tarea añadida"
        except (TypeError, ValueError) as e:
            return f"Error: {e}"
    def Mostrar_tarea(self):
        if not self.gestor:
            return "administrador de tareas vacio"
        return "\n".join([f"{i}- {pendientes}"for i, pendientes in enumerate(self.gestor, start=1)])
    def eliminar_tarea(self, tarea):
            try:
                self.gestor.remove(tarea.capitalize())
                # para eliminar las tareas en el archivo, despues de borrarlas el no va a tener nada que escribir, 
                # entonces va a escribir en blanco o sea nada.
                with open("Tareas.txt", "w") as file:
                    for tarea in self.gestor:
                        file.write(tarea + "\n")
                return "Tarea borrada, muchas gracias"
            except ValueError: 
                return "Tarea no encontrada, no se pudo eliminar"

admin = Tareas() 
while True:
    print(
        "\n Bienvenidos a mi gestor de tareas \n"
        "1- Agregar Tareas \n"
        "2- Mostrar Tareas \n"
        "3- Eliminar Tareas \n"
        "4- Salir \n"
    )
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese la tarea: "))
        print(admin.agregar_tarea(texto.capitalize()))
    elif numero == 2:
        print(admin.Mostrar_tarea())
    elif numero == 3:
        print(admin.Mostrar_tarea())
        texto = str(input("ingrese la tarea que desea eliminar: "))
        print(admin.eliminar_tarea(texto.capitalize()))
    elif numero == 4:
        print("Muchas Gracias por usar mi gestor...Saliendo")
        break
    else:
        print("Ingrese un numero valido...del 1 al 4")

# Crea un programa que gestione una lista de compras y permita al usuario añadir, eliminar y mostrar productos.
class Compras:
    def __init__(self):
        self.gestor_compras = []
        pass
    def agregar_producto(self, producto):
        try:
            self.gestor_compras.append(producto.capitalize())
            return "Muchas gracias, Compra añadida"
        except (TypeError, ValueError) as e:
            return f"Error: {e}"
    def Mostrar_producto(self):
        if not self.gestor_compras:
            return "Gestor de compras vacio"
        return "\n".join([f"{i}- {pendientes}"for i, pendientes in enumerate(self.gestor_compras, start=1)])
    def eliminar_producto(self, producto):
            self.gestor_compras.remove(producto.capitalize())
            return "Producto borrado, muchas gracias"

admin = Compras() 
while True:
    print(
        "\n Bienvenidos a mi gestor de compras \n"
        "1- Agregar producto \n"
        "2- Mostrar producto \n"
        "3- Eliminar producto \n"
        "4- Salir \n"
    )
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el producto: "))
        print(admin.agregar_producto(texto))
    elif numero == 2:
        print(admin.Mostrar_producto())
    elif numero == 3:
        print(admin.Mostrar_producto())
        texto = str(input("ingrese el producto que desea eliminar: "))
        print(admin.eliminar_producto(texto))
    elif numero == 4:
        print("Muchas Gracias por usar mi gestor...Saliendo")
        break
    else:
        print("Ingrese un numero valido...del 1 al 4")
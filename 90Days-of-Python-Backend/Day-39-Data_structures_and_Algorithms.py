# Día 39: Métodos útiles de diccionarios
# Teoría:
# Los diccionarios en Python tienen varios métodos útiles que permiten manipular y consultar sus elementos. Algunos de los métodos más comunes son:
# .keys(): Retorna una vista de las claves del diccionario.
# .values(): Retorna una vista de los valores del diccionario.
# .items(): Retorna una vista de los pares clave-valor del diccionario.
# .update(otro_diccionario): Actualiza el diccionario con los pares clave-valor de otro diccionario.
# .pop(clave): Elimina la clave y retorna su valor.
# .clear(): Elimina todos los elementos del diccionario.

# Tips y Buenas Prácticas:
# Usa .get() para acceder a valores de un diccionario de manera segura, evitando errores si la clave no existe.
# Evita modificar un diccionario mientras lo recorres; considera crear una copia si es necesario.
# Utiliza .update() para combinar diccionarios de manera eficiente.

# Ejemplos Reales:
# Uso de Métodos de Diccionarios:
empleado = {
    'nombre': 'Juan',
    'edad': 30,
    'cargo': 'Desarrollador'
}

# Obtener claves
claves = empleado.keys()
print("Claves:", claves)

# Obtener valores
valores = empleado.values()
print("Valores:", valores)

# Obtener pares clave-valor
items = empleado.items()
print("Items:", items)

# Actualizar diccionario
empleado.update({'salario': 50000})
print("Empleado actualizado:", empleado)

# Eliminar y retornar un valor
edad = empleado.pop('edad')
print("Edad eliminada:", edad)
print("Empleado después de eliminar edad:", empleado)

# Ejercicios:
# 1- Crea un diccionario y utiliza .keys() para imprimir todas las claves.
diccionarios = { 
    "name": "alex",
    "age": 20,
    "country": "colombia",
    "city": "bogota",
    "ocupation": "estudiante"
}
print(diccionarios.keys())

# 2- Utiliza .values() para imprimir todos los valores de un diccionario.
diccionarios = { 
    "name": "alex",
    "age": 20,
    "country": "colombia",
    "city": "bogota",
    "ocupation": "estudiante"
}
print(diccionarios.values())

# 3- Crea un diccionario y utiliza .items() para imprimir todos los pares clave-valor.
full_name = {
    "first_name": "alex",
    "last_name": "hernandez",
    "age": 20,
    "country": "Costa Rica",
    "City": "Limon",
    "ocupation": "estudiante"
}
print(full_name.items())

# 4- Desarrolla un programa que combine dos diccionarios utilizando .update().
def combinar_diccionarios(diccionario1, diccionario2):
    diccionario1.update(diccionario2)
    return diccionario1

diccionario1 = {"clave1": "valor1", "clave2": "valor2"}
diccionario2 = {"clave3": "valor3", "clave4": "valor4"}
resultado = combinar_diccionarios(diccionario1, diccionario2)
print(resultado)

# 5- Crea un diccionario y utiliza .pop() para eliminar una clave específica.
new_dict = {
    "Pais": "nigeria",
    "ciudad": "lagos",
    "Habitantes": 100
}

new_dict.pop("Habitantes")
print(new_dict)

# 6- Escribe un programa que limpie un diccionario utilizando .clear().
def limpiar_diccionario(diccionario):
    diccionario.clear()
    return diccionario
new_dict = {
    "Pais": "nigeria",
    "ciudad": "lagos",
    "Habitantes": 100
}
print(limpiar_diccionario(new_dict))

# 7- Crea un diccionario de estudiantes y utiliza un bucle para imprimir cada clave y su valor.
estudiantes = {
    "estudiante1": "alex",
    "estudiante2": "alejandro",
    "estudiante3": "andrea",
    "estudiante4": "andres",
    "estudiante5": "angel"
}

for clave, valor in estudiantes.items():
    print(f"Clave: {clave}, Valor: {valor}")

# 8- Agrega un nuevo par clave-valor a un diccionario y muestra el resultado.
estudiantes["estudiante6"] = "jose"
print(estudiantes)

# 9- Crea un diccionario con datos de productos y actualiza el precio de uno de ellos.
productos = {
    "pala": {"nombre": "pala", "precio": 20000},
    "tornillo": {"nombre": "tornillo", "precio": 200},
    "martillo": {"nombre": "martillo", "precio": 2000},
    "cinta": {"nombre": "cinta", "precio": 2500}
}

productos["cinta"]["precio"] = 25
print(productos)

# 10- Desarrolla un programa que imprima el número de claves en un diccionario.
def cantidad_claves(diccionario):
    catidad = len(diccionario)
    return f"La cantidad de claves es: {catidad}"
print(cantidad_claves(productos))

# 11- Crea un diccionario con información de varias ciudades y muestra sus nombres.
ciudades = {
    "ciudad1": "bogota",
    "ciudad2": "medellin",
    "ciudad3": "cali",
    "ciudad4": "bucaramanga",
    "ciudad5": "ibague"
}
for i, ciudad in enumerate(ciudades.values(), start=1):
    print(f"La ciudad numero {i} es: {ciudad}")

# 12- Escribe un programa que verifique si una clave está en un diccionario utilizando .get().
def verificar_clave(diccionario, clave):
    if clave in diccionario:
        return True
    else:
        return False

print(verificar_clave(ciudades, "medellin"))

# 13- Crea un diccionario y utiliza un bucle para contar cuántas veces aparece cada valor.
def contar_valores(diccionario):
    contador = {}
    for fruta, cantidad in diccionario.items():
        if cantidad in contador:
            contador[cantidad] += 1
        else:
            contador[cantidad] = 1

    for clave, valor in contador.items():
        print(f"El valor {clave} aparece {valor} veces")

diccionario = {
    "manzana": 5,
    "banana": 3,
    "cereza": 2,
    "durazno": 1,
    "kiwi": 5
}
contar_valores(diccionario)

# 14- Desarrolla un programa que combine dos listas en un diccionario, usando los elementos de la primera lista como claves y los de la segunda como valores.
def combinar_listas_en_diccionario(lista1, lista2):
    diccionario = {}
    for i in range(len(lista1)):
        diccionario[lista1[i]] = lista2[i]
    return diccionario

lista1 = ["negro", "rojo", "azul", "verde", "amarillo"]
lista2 = [25000, 50000, 100000, 150000, 200000]

print(combinar_listas_en_diccionario(lista1, lista2))
# lista_1 = ("negro", "rojo", "azul", "verde", "amarillo")
# dic_colores = {
#     lista_1 : (25000, 50000, 100000, 150000, 200000)
# }

# print(dic_colores[lista_1])

# 15- Crea un diccionario y utiliza un bucle para imprimir todos los valores en orden inverso.
def imprimir_valores_en_orden_inverso(diccionario):
    valores = list(diccionario.values())
    valores.reverse()
    print(valores)

diccionario = {
    "manzana": 5,
    "banana": 3,
    "cereza": 2,
    "durazno": 1,
    "kiwi": 6
}

imprimir_valores_en_orden_inverso(diccionario)

# Mini Proyectos:
# Desarrolla un programa que gestione un registro de empleados utilizando diccionarios y permita agregar, eliminar y buscar empleados.
class RegistroEmpleados:
    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, nombre, edad):
        self.empleados[empleado[nombre]] = edad
        print(f"Empleado {nombre} agregado correctamente.")

    def eliminar_empleado(self, nombre):
        if nombre in self.empleados:
            del self.empleados[nombre]
            print(f"Empleado {nombre} eliminado correctamente.")
        else:
            print(f"Empleado {nombre} no encontrado.")

    def buscar_empleado(self, nombre):
        if nombre in self.empleados:
            return self.empleados[nombre]
        else:
            return None
        
    def mostrar_empleados(self):
        if not self.empleados:
            return "No hay empleados registrados."
        return "\n".join((f"{e}- Empleado: {empleados}, Edad: {edad}")for e, (empleados, edad) in enumerate(self.empleados, start=1))
    
administrador = RegistroEmpleados()
while True:
    print("\nMenu:")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Buscar empleado")
    print("4. Mostrar empleados")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del empleado: ")
        edad = input("Ingrese la edad del empleado: ")
        print(administrador.agregar_empleado(nombre, edad))
    elif opcion == 2:
        nombre = input("Ingrese el nombre del empleado a eliminar: ")
        print(administrador.eliminar_empleado(nombre))
    elif opcion == 3:
        administrador.mostrar_empleados()
        nombre = input("Ingrese el nombre del empleado a buscar: ")
        empleado_encontrado = administrador.buscar_empleado(nombre)
        print(empleado_encontrado)
    elif opcion == 4:
        print(administrador.mostrar_empleados())
    elif opcion == 5:
        break
    else:
        print("Opcion no valida")

# Crea un programa que almacene información de libros en un diccionario y permita consultar sus detalles.
class almacenar_libros:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, titulo, autor, anio_publicacion):
        self.libros[titulo] = {"autor": autor, "anio_publicacion": anio_publicacion}
        print(f"Libro {titulo} agregado correctamente.")

    def consultar_libro(self, titulo):
        if titulo in self.libros:
            return self.libros[titulo]
        else:
            return "Libro no encontrado."
        
    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join((f"{e}- Libro: {libro['titulo']}, Autor: {libro['autor']}, Anio de publicacion: {libro['anio_publicacion']}")for e, libro in enumerate(self.libros, start=1))

libros = almacenar_libros()
while True:
    print("\nMenu:")
    print("1. Agregar libro")
    print("2. Consultar libro")
    print("3. Mostrar libros")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio_publicacion = input("Ingrese el anio de publicacion del libro: ")
        print(libros.agregar_libro(titulo, autor, anio_publicacion))
    elif opcion == 2:
        libros.mostrar_libros()
        titulo = input("Ingrese el titulo del libro a consultar: ")
        print(libros.consultar_libro(titulo))
    elif opcion == 3:
        print(libros.mostrar_libros())
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")
# Día 38: Claves y valores en diccionarios

# Teoría:
# Los diccionarios en Python son colecciones desordenadas de pares clave-valor. Cada clave es única y 
# se utiliza para acceder a su valor asociado. Los diccionarios se definen utilizando llaves {}.
# La sintaxis básica para crear un diccionario es: diccionario = {clave1: valor1, clave2: valor2}.
# Puedes acceder a los valores utilizando la clave correspondiente: valor = diccionario[clave].

# Tips y Buenas Prácticas:
# Usa claves que sean inmutables (como cadenas, números o tuplas).
# Evita usar claves duplicadas; si lo haces, la última asignación sobrescribirá la anterior.
# Utiliza diccionarios para almacenar datos relacionados, como registros de empleados o configuraciones.

# Uso de Diccionarios:
empleado = {
    'nombre': 'Juan',
    'edad': 30,
    'cargo': 'Desarrollador'
}

print("Nombre:", empleado['nombre'])
print("Edad:", empleado['edad'])
print("Cargo:", empleado['cargo'])

# Agregar un nuevo elemento al diccionario
empleado['salario'] = 5000

# Eliminar un elemento del diccionario
del empleado['edad']

# Verificar si una clave existe en el diccionario
if 'nombre' in empleado:
    print("El empleado tiene un nombre.")

# Iterar sobre las claves y valores del diccionario
for clave, valor in empleado.items():
    print(clave, ":", valor)

# tuplas como claves en diccionarios, es una buena opcion ya que las tuplas no aceptan duplicados y las claves son tienen que ser unicas
tupla = ('nombre', 'edad', 'cargo')
diccionario = {
    tupla: ('Juan', 30, 'Desarrollador')
}
print(diccionario[tupla])

nombre, edad, cargo = diccionario[tupla]
print(f"Nombre: {nombre}, Edad: {edad}, Cargo: {cargo}")

# Ejercicios:
# 1- Crea un diccionario que almacene información sobre un libro (título, autor, año).
almacenar_libro = {'titulo': 'El Senor de los Anillos', 'autor': 'J.R.R. Tolkien', 'año': 1954}
print(almacenar_libro)

# 2- Accede a un valor en un diccionario utilizando su clave.
print(almacenar_libro['titulo'])
print(almacenar_libro.get('autor'))

# 3- Agrega una nueva clave y valor a un diccionario existente.
almacenar_libro['editorial'] = 'Penguin'
almacenar_libro.update({'Precio': 1000})
print(almacenar_libro)

# 4- Elimina una clave y su valor de un diccionario.
almacenar_libro.pop('editorial')
print(almacenar_libro)

# 5- Crea un diccionario con varios elementos y verifica si una clave específica existe.
def verificar_clave(clave, diccionario):
    return clave in diccionario
dato = elementos_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "cargo": "Desarrollador",
    "lenguajes" : ['Python', 'Java', 'C++'],
    "salario": 5000
}
print(verificar_clave('test', dato))

# 6- Escribe un programa que imprima todas las claves de un diccionario.
def imprimir_claves(diccionario):
    for i, j in enumerate(diccionario.keys(), start=1):
        print(f"La clave {i} es: {j}")
imprimir_claves({
    "nombre": "Juan",
    "edad": 30,
    "cargo": "Desarrollador",
    "lenguajes" : ['Python', 'Java', 'C++'],
    "salario": 5000
})

# 7- Crea un diccionario que almacene los precios de varios productos.
def almacenar_precios():
    precios = {}

    while True:
        print("*** bienvenido a mi almacen de precios ****")
        print("menu de opciones")
        print("1. Agregar Producto y precio")
        print("2. mostrar productos y precios")
        print("3. eliminar producto y precio")
        print("4. editar precio de un producto")
        print("5. Salir")
        opcion = int(input("ingresa una opcion: "))
        if opcion == 1:
            producto = input("ingresa el nombre del producto: ")
            precio = float(input("ingresa el precio del producto: "))
            precios[producto] = precio
            print("Producto agregado exitosamente\n")
        elif opcion == 2:
            for producto, precio in precios.items():
                print(f"producto: {producto}, precio: {precio}")
        elif opcion == 3:
            producto = input("ingresa el nombre del producto a eliminar: ")
            if producto in precios:
                del precios[producto]
                print("Producto eliminado exitosamente\n")
            else:
                print("Producto no encontrado\n")
        elif opcion == 4:
            producto = input("ingresa el nombre del producto a editar: ")
            if producto in precios:
                nuevo_precio = float(input("ingresa el nuevo precio del producto: "))
                precios[producto] = nuevo_precio
                print("Precio editado exitosamente\n")
            else:
                print("Producto no encontrado\n")
        elif opcion == 5:
            print("Gracias por usar mi almacen de precios...saliendo")
            break
        else:
            print("opcion no valida")

almacenar_precios()

# 8- Accede a un valor en un diccionario utilizando el método .get().
new_dict = {
    "nombre": "Juan",
    "edad": 30,
    "cargo": "Desarrollador",
    "lenguajes" : ['Python', 'Java', 'C++'],
    "salario": 5000
}
print(new_dict.get('nombre'))

# 9- Crea un diccionario de estudiantes y sus calificaciones.
diccionario_estudiantes = {
    "estudiante1": 90,
    "estudiante2": 85,
    "estudiante3": 92,
    "estudiante4": 88
}
print(diccionario_estudiantes)

# 10- Desarrolla un programa que imprima todos los valores de un diccionario.
def valores_diccionario(diccionario):
    for i in diccionario.values():
        print(i)
valores_diccionario(diccionario_estudiantes)

# 11- Crea un diccionario con datos de un empleado y actualiza su edad.
empleados = {
    "nombre": "Juan",
    "edad": 30,
    "cargo": "Desarrollador",
    "lenguajes" : ['Python', 'Java', 'C++'],
    "salario": 5000
}
empleados['edad'] = 31
print(empleados)

# 12- Escribe un programa que muestre la longitud de un diccionario.
def longitud_diccionario(diccionario):
    print(f"La longitud del diccionario es de: {len(diccionario)}")
longitud_diccionario(empleados)

# 13- Crea un diccionario y utiliza un bucle para imprimir cada clave y su valor.
def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"Clave: {clave}, Valor: {valor}")
imprimir_diccionario(empleados)

# 14- Agrega un nuevo par clave-valor a un diccionario existente.
empleados['Nacionalidad'] = 'Colombiano'
print(empleados)

# 15- Escribe un programa que combine dos diccionarios.
diccionario1 = {
    "clave1": "valor1",
    "clave2": "valor2"
}
diccionario2 = {
    "clave3": "valor3",
    "clave4": "valor4"
}
diccionario3 = {**diccionario1, **diccionario2}
diccionario4 = {diccionario1 | diccionario2}
print(diccionario3)

# Mini Proyectos:
# Desarrolla un programa que gestione un inventario utilizando diccionarios para almacenar productos y sus cantidades.
class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        if isinstance(cantidad, int) and isinstance(producto.capitalize(), str):
            self.inventario[producto] = cantidad
            print(f"Se ha agregado {cantidad} {producto} al inventario.")
        else:
            print("El producto debe ser un texto y la cantidad debe ser un entero.")

    def mostrar_inventario(self):
        print("Inventario:")
        if not self.inventario:
            print("El inventario esta vacio.")
        return "\n".join([f"{i}- Producto: {producto}: y su cantidad es: {cantidad}" for i, (producto, cantidad) in enumerate(self.inventario.items(), start=1)])

    def buscar_producto(self, producto):
        if producto in self.inventario:
            return self.inventario[producto]
        else:
            return "Producto no encontrado"

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            del self.inventario[producto]
            print(f"Se ha eliminado {producto} del inventario.")
        else:
            print(f"{producto} no se encuentra en el inventario.")

inventario = Inventario()
while True:
    print("\n Bienvenidos a mi almacenador de productos \n"
          "1- Agregar producto \n"
          "2- Mostrar producto \n"
          "3- Eliminar productos \n"
          "4- Salir \n")
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el producto: "))
        cantidad = int(input("ingrese la cantidad del producto: "))
        print(inventario.agregar_producto(texto.capitalize(), cantidad))
    elif numero == 2:
        print(inventario.mostrar_inventario())
    elif numero == 3:
        print(inventario.mostrar_inventario())
        texto = str(input("ingrese el producto que desea eliminar: "))
        print(inventario.eliminar_producto(texto.capitalize()))
    elif numero == 4:
        break
    else:
        print("Opcion no valida")

# Crea un programa que almacene información de estudiantes en un diccionario y permita consultar sus calificaciones.
class Estudiante:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, calificacion):
        self.estudiantes[nombre] = calificacion

    def consultar_calificacion(self, nombre):
        if nombre in self.estudiantes:
            return self.estudiantes[nombre]
        else:
            return "Estudiante no encontrado"

estudiante = Estudiante()
while True:
    print("\n Bienvenidos a mi almacenador de estudiantes \n"
          "1- Agregar estudiante \n"
          "2- Consultar calificacion \n"
          "3- Salir \n")
    numero = int(input("Ingrese el numero que desea: "))
    if numero == 1:
        texto = str(input("ingrese el nombre del estudiante: "))
        calificacion = float(input("ingrese la calificacion del estudiante: "))
        print(estudiante.agregar_estudiante(texto.capitalize(), calificacion))
    elif numero == 2:
        print(estudiante.mostrar_inventario())
        texto = str(input("ingrese el nombre del estudiante que desea consultar: "))
        print(estudiante.consultar_calificacion(texto.capitalize()))
    elif numero == 3:
        break
    else:
        print("Opcion no valida")

# Día 8: Diccionarios y Operaciones con Diccionarios

# son estructuras de datos desordenadas y mutables que almacenan pares clave-valor. 
# Cada clave en un diccionario debe ser única y puede ser de cualquier tipo inmutable (como cadenas, números o tuplas). 
# Los valores asociados a las claves pueden ser de cualquier tipo y mutables o inmutables.

# Tips del Tema
# Definición de diccionarios: Los diccionarios son colecciones desordenadas y mutables de pares clave-valor.
# Acceso a elementos: Los valores en un diccionario se acceden mediante sus claves.
# Métodos de diccionarios: Métodos importantes incluyen get(), keys(), values(), items(), update(), y pop().

# Definición de un diccionario
estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Acceso a elementos
print(estudiante["nombre"]) 
print(estudiante["edad"])    
print(estudiante["carrera"]) 

########### Métodos Comunes de Diccionarios
# Obtener todas las claves
claves = estudiante.keys()
print(claves)  

# Obtener todos los valores
valores = estudiante.values()
print(valores)  

# Obtener todos los pares clave-valor
items = estudiante.items()
print(items)  

#crear una nueva tabla con un solo valor de otra tabla
my_rop = estudiante.fromkeys(("edad",31))
print(my_rop)

estudiante.get("name") # da el valor de ese indice

# Actualizar un valor
estudiante["edad"] = 21
print(estudiante)  

# Añadir un nuevo par clave-valor
estudiante["promedio"] = 9.5
print(estudiante)  

# Eliminar un elemento
valor_eliminado = estudiante.pop("promedio")
print(estudiante)  
print("Valor eliminado:", valor_eliminado)  

estudiantes = [
    {"nombre": "Ana", "edad": 22, "carrera": "Biología"},
    {"nombre": "Pedro", "edad": 27, "carrera": "Ingeniería"},
    {"nombre": "María", "edad": 20, "carrera": "Matemáticas"}
]

estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Lista para almacenar estudiantes menores de 25 años
estudiantes_jovenes = []
# Iterar sobre cada estudiante en la lista de estudiantes
for estudiante in estudiantes:
    # Verificar si el estudiante tiene menos de 25 años
    if estudiante["edad"] < 25:
        # Agregar al estudiante a estudiantes_jovenes
        estudiantes_jovenes.append(estudiante)

# Mostrar el resultado
print("Estudiantes menores de 25 años:")
for estudiante in estudiantes_jovenes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Carrera: {estudiante['carrera']}")

####################### Ejercicios
# Ejercicio 1: Crea un diccionario con información sobre ti (nombre, edad, ciudad) y muéstralo.
persona = {
    "nombre" : "eric",
    "apellido" : "edwards",
    "edad" : 30,
    "ciudad" : "limon"
}

print(persona)

# Ejercicio 2: Añade una nueva clave y valor a tu diccionario y muéstralo.
persona["pais"] = "costa rica"
print(persona)

# Ejercicio 3: Actualiza un valor en tu diccionario y muéstralo.
persona["edad"] = 55
print(persona)

# Ejercicio 4: Elimina una clave de tu diccionario y muéstralo.
persona.pop("ciudad")
print(persona)

# Ejercicio 5: Define una función que tome un diccionario y devuelva una lista de sus claves.
def dics_keys(persona):
    keys_list = list(persona.keys())
    return keys_list

# Ejemplo de uso
persona = {
    "nombre": "eric",
    "apellido": "edwards",
    "edad": 30,
    "ciudad": "limon"
}

claves = dics_keys(persona)
print(claves)

# Ejercicio 6: Define una función que tome un diccionario y devuelva una lista de sus valores.
dic = {
    "name" : "eric",
    "apellido" : "edwards",
    "edad" : 30,
    "ciudad" : "limon"
}
def convertir(dic):
    lista = list(dic.values())
    print(f"Estos son los valores de la nueva lista: {lista}")
convertir(dic)

# Ejercicio 7: Define una función que tome un diccionario y devuelva una lista de sus pares clave-valor.
dic2 = {
    "name" : "eric",
    "apellido" : "edwards",
    "edad" : 30,
    "ciudad" : "limon"
}
def dic_item(dic2):
    item = list(dic2.items())
    print(f"esta es la lista de los clave-valor del dic: {item}")
dic_item(dic2)

# Ejercicio 8: Define una función que tome dos diccionarios y los combine.
dic3 = {
    "name" : "alex",
    "apellido" : "perz",
    "edad" : 30,
    "ciudad" : "limon"
}

dic4 = {
    "name" : "elarya",
    "apellido" : "targelan",
    "edad" : 40,
    "ciudad" : "limon"
}
def union_dic(dic3,dic4):
    union = dic3 | dic4
    print(f"este es el resultado de la union de dic3 y dic4: {union}")
union_dic(dic3,dic4)

# Ejercicio 9 (Teoría): ¿Qué es un diccionario y cómo se diferencia de una lista?
# son un conjunto de datos mutables, de clave-valor y de claves unicas. Se distingen de las lista porque las listas no son datos de clave-valor

# Ejercicio 10 (Práctica): Escribe un programa que tome una cadena y cuente la frecuencia de cada carácter usando un diccionario.
cadena = "gelsenkirsen"
diccionario = {}
for conteo in cadena.lower():
    if conteo in diccionario:
        diccionario[conteo] += 1
    else:
        diccionario[conteo] = 1
print(diccionario)

# Ejercicio 11: Crea un diccionario que contenga información sobre un automóvil (marca, modelo, año) y muestra el valor de cada clave.
automovil = {
    "marca" : "toyota",
    "modelo" : "prius",
    "año" : 2015
}
for clave, valor in automovil.items():
    print(f"{clave}: {valor}")

# Ejercicio 12: Define una función que tome un diccionario de contactos (nombre y número de teléfono) y devuelva el número de teléfono de un contacto dado.
contacto = {
    "marco": "85-89-89-56",
    "lisa": "85-89-90-56",
    "eric": "85-22-89-56",
    "luis": "85-89-10-56"
}
print(contacto.keys())
def agenda_telefonico(dato):
    nombre = contacto.get(dato.lower())
    if nombre:
        return f"El número de teléfono de {dato} es: {nombre}"
    else:
        return f"No se encontró el número de teléfono para {dato}."
    
dato = agenda_telefonico(str(input("escribe el nombre: ")))
print(dato)

# Ejercicio 13: Actualiza el valor de una clave en un diccionario de productos (nombre y precio) y muestra el diccionario actualizado.
productos = { # cada clave debe de ser unica
    "pala": {"nombre": "pala", "precio": 20000},
    "tornillo": {"nombre": "tornillo", "precio": 200},
    "martillo": {"nombre": "martillo", "precio": 2000},
    "cinta": {"nombre": "cinta", "precio": 2500}
}
productos["cinta"].update({"precio" : 25})
# productos["cinta"]["precio"] = 25

for nombre, producto in productos.items():
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

# Ejercicio 14: Define una función que tome un diccionario con claves como categorías de productos (electrónica, ropa) y valores como listas de productos,
# y devuelva una lista de todos los productos.
def diccionario_v(dato):
    dato_new = list(dato["electronica"] | dato["ropa"])
    return dato_new

dato = diccionario_v({
    "electronica" : {"televisor", "refrigerador", "olla", " cafetera"},
    "ropa" : {"gorras", "capas", "camisas", "blusas", "pantalones"}
})
print(dato)

# Ejercicio 15: Crea un diccionario que almacene la cantidad de artículos vendidos por cada vendedor en una tienda, 
# y muestra el nombre del vendedor que más artículos ha vendido.
articulos = {
    "marcos" : {"ventas" : 200, "articulo" : "pala"},
    "luis" : {"ventas" : 20, "articulo" : "cierra"},
    "carmen" : {"ventas" : 1000, "articulo" : "clavo"},
    "marta" : {"ventas" : 2000, "articulo" : "tornillo"},
    "marco" : {"ventas" : 210, "articulo" : "pico"}
}
mayor_ventas = None
vendedor_max = None
for vendedor, datos in articulos.items():
    if mayor_ventas is None or datos["ventas"] > mayor_ventas:
        mayor_ventas = datos["ventas"]
        vendedor_max = vendedor
if vendedor_max:
    print(f"El vendedor con más ventas es: {vendedor_max} con {mayor_ventas} ventas, y vendió: {articulos[vendedor_max]['articulo']}")

# Ejercicio 16: Define una función que tome un diccionario con claves como nombres de estudiantes y valores como sus notas en un examen, 
# y devuelva una lista de estudiantes que tienen una nota mayor a un valor dado.
def students(dato, valor):
    new_list = []
    for estudiantes, nota in dato.items():
        if nota > valor:
            new_list.append(estudiantes)
            new_list.append(nota)
    return new_list
        
dato = students({
    "alvaro" : 56,
    "luis" : 66,
    "marta" : 56,
    "carlos" : 46,
    "marcos" : 80,
}, 70)
print(dato)

# Ejercicio 17: Crea un diccionario que contenga el nombre de varias personas y sus edades, y muestra los nombres de las personas que son mayores de 30 años.
personas = {
    "marcos" : {"edad" : 23},
    "paula" : {"edad" : 33},
    "carlos" : {"edad" : 22},
    "maria" : {"edad" : 36},
    "eric" : {"edad" : 18}
}
for nombre, edad in personas.items():
    if edad['edad'] > 30:
        print(f"La persona: {nombre} tiene una edad de: {edad['edad']}")

# Ejercicio 18: Define una función que tome dos diccionarios y devuelva un nuevo diccionario que combine los pares clave-valor de ambos diccionarios. 
# Si una clave aparece en ambos diccionarios, debe conservar el valor del segundo diccionario.
def combinar_diccionarios(dict1, dict2):
    return dict2 | dict1

personas1 = {
    "marcos": {"edad": 23},
    "paula": {"edad": 33},
    "carlos": {"edad": 22},
    "maria": {"edad": 36},
    "eric": {"edad": 18}
}
personas2 = {
    "marcos": {"edad": 22},
    "laura": {"edad": 33},
    "karl": {"edad": 22},
    "paul": {"edad": 36},
    "alex": {"edad": 18}
}

nuevo_diccionario = combinar_diccionarios(personas1, personas2)
print(nuevo_diccionario)

# Ejercicio 19: Dado un diccionario con claves como códigos de productos y valores como nombres de productos, 
# crea una función que devuelva el nombre del producto dado un código de producto.
def buscar_producto(digito, productos):
    return productos.get(digito, "Código equivocado") # buscar el prod en el codigo
prod = {
    8965: "arroz",
    2265: "azúcar",
    8065: "papas",
    8225: "frijoles",
    8967: "atún"
}
print("este es el inventario de los codigos:")
for code in prod.keys():
    print(code)

digito = int(input("Escribe el código del producto: "))
resultado = buscar_producto(digito, prod)
print(f"Producto: {resultado}")

# Ejercicio 20: Crea un diccionario que almacene la frecuencia de cada letra en una cadena de texto, y muestra el diccionario resultante.
# el metodo replace crea una nueva cadena con los metodos aplicados, osea que no lo aplica directamente a la cadena anterior.
frecuencia = {}
cadena = "eric hernandez"
for letra in cadena.replace(" ", ""):
    if letra in frecuencia:
        frecuencia[letra] += 1 
    else:
        frecuencia[letra] = 1 
print(frecuencia)



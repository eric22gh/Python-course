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




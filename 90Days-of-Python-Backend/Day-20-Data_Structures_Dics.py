# Día 20: Estructuras de Datos - Diccionarios

# Definición del Tema
# Es una estructura de datos que permite almacenar pares clave-valor.

# Tips del Tema
# Diccionarios: Son colecciones de pares clave-valor.
# Claves únicas: Las claves deben ser únicas y de un tipo inmutable (por ejemplo, cadenas, números, tuplas).
# Mutabilidad: Los diccionarios son mutables y pueden modificarse después de su creación.

# Crear un diccionario
estudiantes = {"Alice": 25, "Bob": 22, "Charlie": 23}

# Acceder a un valor por su clave
print(estudiantes["Alice"]) 

# Añadir un nuevo par clave-valor
estudiantes["David"] = 21
print(estudiantes)  

# Modificar un valor existente
estudiantes["Alice"] = 26
print(estudiantes)  

# Eliminar un par clave-valor
del estudiantes["Bob"]
print(estudiantes)  

######### Operaciones Comunes con Diccionarios

# Obtener todas las claves
print(estudiantes.keys())  

# Obtener todos los valores
print(estudiantes.values())  

# Obtener todos los pares clave-valor
print(estudiantes.items())  

# Comprobar si una clave está en el diccionario
print("Alice" in estudiantes)  
print("Bob" in estudiantes)    

# Iterar sobre un diccionario
for nombre, edad in estudiantes.items():
    print(f"{nombre} tiene {edad} años.")

######## Métodos de Diccionario

# Obtener un valor con get(), devuelve None si la clave no existe
edad_de_bob = estudiantes.get("Bob")
print(edad_de_bob)  # Salida: None
print(estudiantes.get("Alice"))

# Establecer un valor por defecto si la clave no existe
estudiantes.setdefault("Eve", 20)
print(estudiantes)  # Salida: {'Alice': 26, 'Charlie': 23, 'David': 21, 'Eve': 20}

# Actualizar el diccionario con otro diccionario
nuevos_estudiantes = {"Frank": 24, "Grace": 22}
estudiantes.update(nuevos_estudiantes)
print(estudiantes)  # Salida: {'Alice': 26, 'Charlie': 23, 'David': 21, 'Eve': 20, 'Frank': 24, 'Grace': 22}

###### Contar la Frecuencia de Elementos
def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1 # como elemento esta en frecuencia, agrega uno mas si lo vuelve a encontrar.
        else:
            frecuencia[elemento] = 1
    return frecuencia

elementos = ['manzana', 'banana', 'manzana', 'naranja', 'banana', 'manzana']
print(contar_frecuencia(elementos))  # Salida: {'manzana': 3, 'banana': 2, 'naranja': 1}

####### Invertir un Diccionario
def invertir_diccionario(diccionario):
    return {valor: clave for clave, valor in diccionario.items()}

estudiantes = {"Alice": 26, "Charlie": 23, "David": 21}
diccionario_invertido = invertir_diccionario(estudiantes)
print(diccionario_invertido)  # Salida: {26: 'Alice', 23: 'Charlie', 21: 'David'}

######### Eliminar Elementos por Condición
def eliminar_bajo_umbral(diccionario, umbral):
    return {k: v for k, v in diccionario.items() if v >= umbral}

estudiantes = {"Alice": 26, "Charlie": 23, "David": 21}
estudiantes_filtrados = eliminar_bajo_umbral(estudiantes, 23)
print(estudiantes_filtrados)  # Salida: {'Alice': 26, 'Charlie': 23}

############### ejercicios
# Ejercicio 1: Crea un diccionario con los nombres y edades de 3 personas y muestra la edad de la segunda persona.
diccionario = {"alex" : 25, "ralf": 52, "lina" : 22}
print(diccionario.get("ralf"))

# Ejercicio 2: Añade una nueva persona al diccionario del ejercicio 1 y muestra el diccionario actualizado.
diccionario.update({"rosa": 33})
print(diccionario)

# Ejercicio 3: Modifica la edad de la primera persona en el diccionario del ejercicio 1 y muestra el diccionario actualizado.
diccionario.update({"alex" : 30})
print(diccionario)

# Ejercicio 4: Elimina la segunda persona del diccionario del ejercicio 1 y muestra el diccionario actualizado.
diccionario.pop("ralf")
print(diccionario)

# Ejercicio 5: Escribe una función que tome un diccionario y devuelva una lista con todas las claves del diccionario.
def dic_to_list(dic):
    # dic = dic.items() con todos sus clave-valor 
    # dic = dic.values() con solo sus valores
    lista = list(dic)
    return lista
print(dic_to_list({"nombre": "Ana", "edad": 22, "carrera": "Biología"}))

# Ejercicio 6: Escribe una función que tome un diccionario y devuelva una lista con todos los valores del diccionario.
def list_from_dics_values(dic):
    dic = dic.values()
    lista = list(dic)
    return lista
print(list_from_dics_values({"nombre": "Pedro", "edad": 27, "carrera": "Ingeniería"}))

# Ejercicio 7: Escribe una función que tome dos diccionarios y los combine en uno solo.
def join_dics(dic1, dic2):
    resultado = dic1 | dic2
    return resultado
print(join_dics(dic1 = {"nombre": "Pedro", "edad": 27, "carrera": "Ingeniería"}, dic2 = {"nombre": "Ana", "edad": 22, "carrera": "Biología"}))

# Ejercicio 8: Escribe una función que tome un diccionario y devuelva un nuevo diccionario con las claves y valores intercambiados.
def change_key_values(dic3):
    resul = {valor: clave for clave, valor in dic3.items()}
    return resul
print(change_key_values( dic3 = {"nombre": "Pedro", "edad": 27, "carrera": "Ingeniería"}))

# Ejercicio 9 (Teoría): ¿Qué es un diccionario en Python y cómo se diferencia de una lista, tupla y conjunto?
# son una especie de estructuras de datos que almacena datos con clave valor y esa es su principal diferencia con las listas, tuplas y que los conjuntos permiten 
# datos duplicados...
# tambien tiene otras carracteriticas de sus datos son mutables y las claves tienen que ser unicos.

# Ejercicio 10 (Práctica): Escribe un programa que tome una lista de diccionarios, donde cada diccionario represente a una persona con nombre y edad,
# y devuelva el nombre de la persona más joven.
empresas = [
    {"nombre":"ricardo", "nacionalidad":"brasileño", "edad":25},
    {"nombre":"alex", "nacionalidad": "griego", "edad":18},
    {"nombre":"luis", "nacionalidad": "portuguez", "edad":19},
    {"nombre":"marcos", "nacionalidad": "Costarricese", "edad":15},
    {"nombre":"marta", "nacionalidad": "argentino", "edad":22},
    {"nombre":"carlos", "nacionalidad": "hungaro", "edad":29},
    {"nombre":"carl", "nacionalidad": "español", "edad":17},
    {"nombre":"lucas", "nacionalidad": "frances", "edad":16}
]

def persona_joven(empresas):
    if not empresas:  # Verifica si la lista empresas esta vacia.
        return None
    persona_mas_joven = empresas[0] # busca el dato en la posicion 0 del dic
    for empresa in empresas: # pasamos el dic a una lista
        if empresa["edad"] < persona_mas_joven["edad"]: # compara cada edad de la lista con la que inicialmente es la mas joven
            persona_mas_joven = empresa # si en la busqueda encuenta a una persona mas joven que la actual, la actualiza
    return persona_mas_joven

joven = persona_joven(empresas)
if joven:
    print(f"La persona más joven es {joven['nombre']} con {joven['edad']} años.")
else:
    print("La lista está vacía.")
    
    

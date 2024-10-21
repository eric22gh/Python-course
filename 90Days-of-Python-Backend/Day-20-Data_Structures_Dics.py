# Día 20: Estructuras de Datos - Diccionarios

# Definición del Tema
# Es una estructura de datos que permite almacenar pares clave-valor.

# Tips del Tema
# Diccionarios: Son colecciones de pares clave-valor.
# Claves únicas: Las claves deben ser únicas y de un tipo inmutable (por ejemplo, cadenas, números, tuplas).
# Mutabilidad: Los diccionarios son mutables y pueden modificarse después de su creación.

# Crear un diccionario
estudiantes = {"Alice": 25, "Bob": 22, "Charlie": 23}

# # Acceder a un valor por su clave
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
    
# Ejercicio 11:
# Crea un diccionario que almacene el nombre y la cantidad de frutas en una tienda. Luego, escribe un programa que aumente en 10 la cantidad de una fruta dada.
frutas_tienda = {
    "manzana":5,
    "peras":7,
    "banano":6,
    "naranjas":2,
    "melon":3
}
for clave, valor in frutas_tienda.items():
    valor += 10
    frutas_tienda.update({clave : valor})
print(frutas_tienda)

############# o #########
# for clave in frutas_tienda:
#     frutas_tienda[clave] += 15
# print(frutas_tienda)
    
# Ejercicio 12:
# Escribe una función que reciba un diccionario con nombres y edades, y devuelva un nuevo diccionario con solo las personas mayores de 18 años.
new_dic = {}
def mayores_18(edades_personas):
    for personas, datos in edades_personas.items():
        if datos["edad"] > 18:
            new_dic[datos["nombre"]] = datos["edad"]     
    return new_dic
datos = mayores_18({
    "persona1" : {"nombre" : "eric", "edad" : 25},
    "persona2" : {"nombre" : "helen", "edad" : 42},
    "persona3" : {"nombre" : "maria", "edad" : 12},
    "persona4" : {"nombre" : "carlos", "edad" : 10},
    "persona5" : {"nombre" : "damaris", "edad" : 45}
})
print(datos)

# Ejercicio 13:
# Crea un diccionario con claves como el nombre de países y valores como sus capitales. 
# Escribe un programa que invierta las claves y valores (las capitales serán las claves y los países los valores).
def inverted(paises):
    try:
        new = {valor: clave for clave, valor in paises.items()}
        return new
    except Exception as e:
        return f"Error: {e}"
    
dato = inverted({
    "argentina": "Buenos aires",
    "Portugal": "Lisboa",
    "Bielorussia" : "Misnk",
    "Noruega" : "Oslo",
    "Escosia" : "Edimburgo"
})
print(dato)

# Ejercicio 14:
# Dado un diccionario que almacene nombres de estudiantes y sus calificaciones, escribe una función que calcule y 
# devuelva la calificación promedio de todos los estudiantes.
def promedio_avanzado(notas_estudiantes):
    total_notas = 0
    total_materias = 0
    for estudiantes, notas in notas_estudiantes.items():
        total_notas += sum(notas.values())
        total_materias += len(notas.values())
    promedio = total_notas / total_materias
    return F"el promedio de notas de todos los estudiantes es de: {promedio:.0F}"
    
dato = promedio_avanzado({
    "cristofer" : {"ciencias" : 89, "matematicas" : 78, "español" : 55},
    "rosa" : {"ciencias" : 99, "matematicas" : 70, "español" : 45},
    "marcos" : {"ciencias" : 80, "matematicas" : 68, "español" : 85},
    "maria" : {"ciencias" : 99, "matematicas" : 88, "español" : 95},
    "helen" : {"ciencias" : 59, "matematicas" : 58, "español" : 95}
})
print(dato)

########### otra forma #######
def prom(estudiantes):
    suma_notas = 0
    for  v in estudiantes.values():
        suma_notas += v
    cantidad = len(estudiantes.values())
    promedio = suma_notas / cantidad
    return promedio
nota = prom({
    "alex" : 85,
    "eric" : 55,
    "maria" : 65,
    "lucia" : 75,
    "carlos" : 95
})
print(nota)

# Ejercicio 15:
# Escribe un programa que combine dos diccionarios de tal manera que los valores de claves comunes se sumen.
dic_1 = {
    "valor1" : 5,
    "valor9" : 10,
    "valor3" : 50,
    "valor4" : 59,
    "valor5" : 56,
    "valor6" : 5 
}
dic_2 = {
    "valor7" : 51,
    "valor8" : 40,
    "valor9" : 500,
    "valor10" : 5,
    "valor11" : 6,
    "valor12" : 50 
}
unido = {}
for k, v in dic_1.items():
    unido[k] = v # otra forma de agregar clave-valor a un diccionario

for k, v in dic_2.items():
    if k in unido: # si alguna clave [k] esta el dicc unido
        unido[k] += v # sumele a esa clave[k] el valor[v] de la clave que a encontrado nuevamente
    else:
        unido[k] = v # de los contrario continua agregando clave y valor a unido

print(unido)

# Ejercicio 16:
# Dado un diccionario con nombres de empleados y sus salarios, escribe una función que devuelva el nombre del empleado con el salario más alto.
def salario_alto_dic(empleados):
    orden = dict(sorted(empleados.items(), key= lambda x:x[1], reverse=True))
    mejor_salario = list(orden.keys())
    return F"el empleado con mejor salario es: {mejor_salario[0]}"

# def salario_alto_dic(empleados):
#     # Usamos la función 'max()' para encontrar la clave con el valor más alto en el diccionario 'empleados'.
#     # La clave es el nombre del empleado, y el valor es el salario.
#     # El parámetro 'key=empleados.get' le dice a 'max()' que busque el máximo basándose en los valores (los salarios).
#     mejor_salario = max(empleados, key=empleados.get)
#     return f"El empleado con mejor salario es: {mejor_salario}"

dato = salario_alto_dic({
    "eric" : 250000,
    "maria" : 550000,
    "luis" : 350000,
    "carlos" : 150000,
    "helen" : 650000
})
print(dato)

# Ejercicio 17:
# Escribe una función que reciba un diccionario y devuelva una lista con todas las claves que tienen valores pares.
def pares_dic(numeros):
    lista_p = []
    for clave, valor in numeros.items():
        if valor % 2 == 0:
            lista_p.append(clave)
    return lista_p
dato = pares_dic({
    "num1" : 54,
    "num2" : 23,
    "num3" : 8,
    "num4" : 22,
    "num5" : 7
})
print(dato)

# Ejercicio 18:
# Crea un diccionario que almacene el nombre y el precio de varios productos en una tienda. Luego, escribe un programa que permita eliminar 
# un producto si su precio es mayor a un valor dado.
# UN DICCIONARIO NO SE PUEDE MODIFICAR MIENTRAS SE ITERA EN UN BUCLE FOR
monto_max = 1000
productos = {
    "pala" : 250,
    "tornillo" : 100,
    "clavos" : 50,
    "cierra" : 2050,
    "martillo" : 400,
}
claves_a_eliminar = [clave for clave, valor in productos.items() if valor > monto_max]
for clave in claves_a_eliminar: # claves_a_eliminar ya no es un diccionario
    productos.pop(clave)
print(productos)

# Ejercicio 19:
# Escribe una función que reciba un diccionario con nombres de personas y sus ciudades, y devuelva cuántas personas viven en cada ciudad.
from collections import Counter
def habitantes(personas_ciudades):
    valor = personas_ciudades.values()
    numero_habitantes = Counter(valor)
    resultado = []
    for ciudad, viven in numero_habitantes.items():
        resultado.append( f"El número de habitantes en la ciudad de {ciudad} es de: {viven}")
    return "\n".join(resultado)
    
datoss = habitantes({
    "Ana": "San José",
    "Carlos": "Limón",
    "María": "Heredia",
    "Jorge": "Cartago",
    "Lucía": "Alajuela",
    "marcos": "Alajuela",
    "eric": "Alajuela",
    "Daniel": "Puntarenas",
    "Sofía": "Guanacaste"
})
print(datoss)

# Ejercicio 20:
# Dado un diccionario con claves como nombres de estudiantes y valores como una lista de calificaciones, 
# escribe un programa que devuelva el promedio de cada estudiante.
estudiantes_calificaciones = {
    "Pedro": [85, 90, 78],
    "María": [92, 88, 95],
    "Juan": [75, 80, 83],
    "Lucía": [88, 76, 90],
    "Ana": [93, 91, 89]
}

for clave, calificaciones in estudiantes_calificaciones.items():
    suma_calificaciones = sum(calificaciones)
    conteo = len(calificaciones)
    promedio_calificaciones = suma_calificaciones / conteo
    print(f"El promedio del estudiante: {clave} es de: {promedio_calificaciones:.0f}")

# Día 45: Ordenación por mezcla (Mergesort): teoría y ejemplos

# Teoría
# Mergesort es un algoritmo de ordenación basado en la técnica de divide y vencerás. 
# Divide la lista en mitades, ordena cada mitad de forma recursiva 
# y luego mezcla las dos mitades ordenadas para formar una lista completamente ordenada.

# Tips
# Es muy eficiente para listas grandes y tiene una complejidad temporal de O(n log n).
# Visualiza el proceso de mezcla para entender mejor cómo funciona.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar la comprensión.
# Realiza pruebas con listas de diferentes tamaños y configuraciones.

def mergesort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio] # mitad izquierda
    derecha = lista[medio:] # mitad derecha
    # Ordenar recursivamente cada mitad
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    # Mezclar las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izq, der):
    resultado = []
    i = j = 0
    # Comparar elementos de ambas listas y añadir el menor
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    # Añadir los elementos restantes
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

numeros = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(numeros))

# Ejercicios
# 1- Implementa Mergesort en una lista de números enteros.
def MergeSort(elements):
    # si la lista es menor o igual a 1, retorna la lista
    if len(elements) <= 1:
        return elements
    # sacar la mitad de la lista, la mitad de la izquierda y la derecha
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    # ordenar de forma recursiva las mitades
    left = MergeSort(left)
    right = MergeSort(right)
    # mezclar las 2 mitades
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    # comparar izquierda con derecha
    while i < len(lef) and j < len(rig):
        # si un un elemento de la mitad de la izquierda es menor o igual a un elemento de la mitad derecha
        if lef[i] <= rig[j]:
            aux.append(lef[i])
            i += 1
            # se añade y se aumenta una posicion, para comparar al siquiente
        else:
            aux.append(rig[j])
            j += 1
    # anadir los elementos restantes
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux 

import random
data = [random.randint(1, 1000) for n in range(10)]
print(MergeSort(data))

# 2- Crea un método que ordene una lista de cadenas utilizando Mergesort.
def StringMergeSort(elements):
    if len(elements) <= 1:
        return elements
    # sacar la mitad, la parte izquierda y derecha de la lista
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    # ordenar recursivamente la lista
    left = StringMergeSort(left)
    right = StringMergeSort(right)
    # unir las 2 listas
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i].lower() <= rig[j].lower():
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataS = ["zebra", "sopa", "Araña", "Helen", "Ail", "abc"]
print(StringMergeSort(dataS))

# 3- Desarrolla un algoritmo que cuente el número de comparaciones realizadas durante la ordenación.
def MergeSortCount(elements):
    if len(elements) <= 1:
        return elements, 0
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left, left_count = MergeSortCount(left)
    right, right_count = MergeSortCount(right)
    merged, merge_count = mixCount(left, right)
    total_count = left_count + right_count + merge_count
    return merged, total_count
def mixCount(lef, rig):
    aux = []
    i = j = 0
    count = 0
    while i < len(lef) and j < len(rig):
        count += 1  # contar la comparación
        if lef[i] <= rig[j]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux, count
dataC = [38, 27, 43, 3, 9, 82, 10]
print(MergeSortCount(dataC))

# 4- Escribe un programa que ordene una lista de floats usando Mergesort.
def FloatsMergeSort(elements):
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = FloatsMergeSort(left)
    right = FloatsMergeSort(right)
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i] <= rig[j]:
            aux.append(lef[i]) 
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataF = [round(random.uniform(1.0, 100.0), 2) for n in range(8)]
print(FloatsMergeSort(dataF))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo utilizando Mergesort.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"
def ObjectMergeSort(elements):
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = ObjectMergeSort(left)
    right = ObjectMergeSort(right)
    return mixObjects(left, right)

def mixObjects(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i].edad <= rig[j].edad:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux
personas = [Persona("Ana", 30), Persona("Luis", 25), Persona("Carlos", 35), Persona("Marta", 28)]
print(ObjectMergeSort(personas))

# 6- Crea un método que imprima el número de intercambios realizados durante la ordenación.
def MergeSortSwaps(elements):
    if len(elements) <= 1:
        return elements, 0
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left, left_swaps = MergeSortSwaps(left)
    right, right_swaps = MergeSortSwaps(right)
    merged, merge_swaps = mixSwaps(left, right)
    total_swaps = left_swaps + right_swaps + merge_swaps
    return merged, total_swaps
def mixSwaps(lef, rig):
    aux = []
    i = j = 0
    swaps = 0
    while i < len(lef) and j < len(rig):
        if lef[i] <= rig[j]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
            swaps += (len(lef) - i)  # contar los intercambios
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux, swaps
dataS = [38, 27, 43, 3, 9, 82, 10]
print(MergeSortSwaps(dataS))
    
# 7- Escribe un programa que ordene una lista de tuplas por el primer elemento.
def TuplesMergeSort(elements):
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = TuplesMergeSort(left)
    right = TuplesMergeSort(right)
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i][0].lower() <= rig[j][0].lower():
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataT = [("engine", 190000), ("bedrock", 25000), ("wallpepar", 250), ("Box", 10), ("hammer", 2500), ("Bedrock", 25000), ("Arc", 300)]
print(TuplesMergeSort(dataT))

# 8- Implementa un algoritmo que ordene una lista de diccionarios por un valor específico.
def DicsMergeSort(elements, key):
    if len(elements) <= 1:
        return elements
    elif not key:
        raise ValueError("I need a key")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = DicsMergeSort(left, key)
    right = DicsMergeSort(right, key)
    return mix(left, right, key)

def mix(lef, rig, key):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i][key] <= rig[j][key]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataZ = [{"name": "engine", "price": 190000}, {"name": "bedrock", "price": 25000}, {"name": "wallpepar", "price": 250}, {"name": "Box", "price": 10}, {"name": "hammer", "price": 2500}, {"name": "bedrock", "price": 25000}]
print(DicsMergeSort(dataZ, "price"))

# 9- Crea un método que ordene una lista de fechas utilizando Mergesort.
def DateMergeSort(elements):
    if len(elements) <= 1:
        return elements
    elif not isinstance(elements, list):
        raise TypeError("The element must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = DateMergeSort(left)
    right = DateMergeSort(right)
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i] <= rig[j]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

data3 = ["2023-01-01", "2022-12-31", "2023-06-15", "2021-05-20", "2022-01-01"]
print(DateMergeSort(data3))

# 10- Escribe un programa que ordene una lista de números en orden descendente.
def ReverseMergeSort(elements):
    if len(elements) <= 1:
        return elements
    elif not isinstance(elements, list):
        raise TypeError("The element must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = ReverseMergeSort(left)
    right = ReverseMergeSort(right)
    return ReverseMix(left, right)

def ReverseMix(lef, rig):
    rever = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i] >= rig[j]:
            rever.append(lef[i])
            i += 1
        else:
            rever.append(rig[j])
            j += 1
    rever.extend(lef[i:])
    rever.extend(rig[j:])
    return rever

datan = [2, 89, 4, 100, 1, 22]
print(ReverseMergeSort(datan))
    
# 11- Implementa un algoritmo que ordene una lista de cadenas por su longitud utilizando Mergesort.
def LengthMergeSort(elements):
    if len(elements) <= 1:
        return elements
    elif not isinstance(elements, list):
        raise TypeError("The element must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = LengthMergeSort(left)
    right = LengthMergeSort(right)
    return LengthMix(left, right)

def LengthMix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if len(lef[i]) <= len(rig[j]):
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux
dataL = ["zebra", "sopa", "Araña", "Helen", "Ail", "abcde"]
print(LengthMergeSort(dataL))


# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y las ordene por prioridad utilizando Mergesort.
class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __repr__(self):
        return f"Tarea: {self.descripcion}, Prioridad: {self.prioridad}"
def TareaMergeSort(elements):
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = TareaMergeSort(left)
    right = TareaMergeSort(right)
    return TareaMix(left, right)

def TareaMix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i].prioridad <= rig[j].prioridad:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux
tareas = [Tarea("Hacer la compra", 2), Tarea("Lavar el coche", 3), Tarea("Estudiar Python", 1), Tarea("Ir al gimnasio", 2)]
print(TareaMergeSort(tareas))

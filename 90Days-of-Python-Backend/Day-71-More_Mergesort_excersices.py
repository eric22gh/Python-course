# Día 71: Ejercicios de Mergesort

# Teoría
# En este día, se practicarán diversas implementaciones y variaciones de Mergesort para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.

# Ejercicios
# 1- Implementa un algoritmo de Mergesort que devuelva -1 si la lista está vacía.
def MergeSort(elements, top = True):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    if len(elements) == 0:
        return -1 if top else []
    if len(elements) == 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = MergeSort(left)
    right = MergeSort(right)
    return Mix(left, right)

def Mix(lef, rig):
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

import random
data = [round(random.uniform(1.0, 100.0), 2) for n in range(15)]
print(MergeSort(data))

# 2- Escribe un programa que ordene una lista de números y retorne el número de comparaciones realizadas.
def MergeSortCount(elements):
    if not isinstance(elements, list):
        raise TypeError("the element must be a list")
    if len(elements) <= 1:
        return elements, 0
    medium = len(elements) // 2
    left = elements[:medium]
    right= elements[medium:]
    left, left_count = MergeSortCount(left)
    right, right_count  = MergeSortCount(right)
    merge, merge_count = MixC(left, right)
    total = left_count + right_count + merge_count
    return merge, total

def MixC(lef, rig):
    aux = []
    i = j = 0
    count = 0
    while i < len(lef) and j < len(rig):
        count += 1
        if lef[i] <= rig[j]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux, count
dataN = [random.randint(1, 100) for n in range(15)]
print(MergeSortCount(dataN))

# 3- Implementa un algoritmo que ordene una lista de objetos por un atributo específico y retorne la lista.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} ({self.age})"
    
def MergeSortByAttribute(elements, attribute):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = MergeSortByAttribute(left, attribute)
    right = MergeSortByAttribute(right, attribute)
    return MixByAttribute(left, right, attribute)
def MixByAttribute(lef, rig, attribute):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if getattr(lef[i], attribute) <= getattr(rig[j], attribute):
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
print(MergeSortByAttribute(people, "age"))

# 4- Desarrolla un algoritmo que ordene una lista de números en orden descendente utilizando Mergesort.
def DecendingMergeSort(elements):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = DecendingMergeSort(left)
    right = DecendingMergeSort(right)
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i] > rig[j]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

num = [random.randint(1, 1000) for _ in range(15)]
print(DecendingMergeSort(num))

# 5- Implementa un algoritmo que ordene una lista de tuplas por el segundo elemento.
def SortTuples(elements):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = SortTuples(left)
    right = SortTuples(right)
    return mix(left, right)

def mix(lef, rig):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i][1] < rig[j][1]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataT = [("Ana", 30), ("Luis", 25), ("Carlos", 35), ("Marta", 28)]
print(SortTuples(dataT))

# 6- Crea un método que ordene una lista de diccionarios por un valor específico y retorne la lista.
def SortDiccionaries(elements, Specific):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("the elements must be a list")
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = SortDiccionaries(left, Specific)
    right = SortDiccionaries(right, Specific)
    return Mixd(left, right, Specific)

def Mixd(lef, rig, Specific):
    aux = []
    i = j = 0
    while i < len(lef) and j < len(rig):
        if lef[i][Specific] < rig[j][Specific]:
            aux.append(lef[i])
            i += 1
        else:
            aux.append(rig[j])
            j += 1
    aux.extend(lef[i:])
    aux.extend(rig[j:])
    return aux

dataZ = [{"name": "engine", "price": 190000}, {"name": "bedrock", "price": 25000}, {"name": "wallpepar", "price": 250}, {"name": "Box", "price": 10}, {"name": "hammer", "price": 2500}, {"name": "bedrock", "price": 25000}]
print(SortDiccionaries(dataZ, "name"))

# Mini Proyectos
# Crea un simulador de un sistema de gestión de eventos que utilice Mergesort para organizar eventos.
class Gestor:
    def __init__(self):
        self.data_base = []
        
    def MergeSort(self, elements):
        if len(elements) <= 1:
            return elements
        medium = len(elements) // 2
        left = elements[:medium]
        right = elements[medium:]
        left = self.MergeSort(left)
        right = self.MergeSort(right)
        return self.GestorMix(left, right)
    
    def GestorMix(self, lef, rig):
        i = j = 0
        aux = []
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
    
    def Add_Events(self, event):
        if not event:
            return "There is no event to add"
        elif not isinstance(event, str):
            raise TypeError("The event must be a text")
        self.data_base.append(event)
        # assign the sorted result back to the instance list
        self.data_base = self.MergeSort(self.data_base)
        return "The event was succesfuly added"
    
    def See_Events(self):
        if len(self.data_base) == 0:
            return "There is no event to see"
        for n, eve in enumerate(self.data_base, start=1):
            print(f"{n}. {eve}")
            
    def Remove_event(self, event):
        if len(self.data_base) == 0:
            return "There is anything to remove"
        if event in self.data_base:
            self.data_base.remove(event)
            return "The event was succesfuly removed"
        else:
            return "The event was not found"
        
menu = Gestor()
menu.Add_Events("Event 1")
menu.Add_Events("Event 22")
menu.Add_Events("Event 6")
menu.Add_Events("Event 10")
menu.Add_Events("Event 4")
menu.See_Events()
print(menu.Remove_event("Event 10"))
menu.See_Events()


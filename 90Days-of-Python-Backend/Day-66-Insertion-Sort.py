# Día 66: Ordenación por inserción: teoría y ejemplos

# Teoría: La ordenación por inserción es un algoritmo que construye una lista ordenada de elementos uno a uno. 
# Se toma un elemento de la lista desordenada y se inserta en la posición correcta en la lista ordenada, 
# repitiendo el proceso hasta que todos los elementos estén ordenados.

# Tips
# Es más eficiente para listas pequeñas o casi ordenadas.
# Visualiza el proceso para entender cómo se mueven los elementos.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar la comprensión.
# Realiza pruebas con listas de diferentes tamaños y configuraciones.

# Ejemplo de Código
def ordenacion_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i] # Elemento a insertar y este es 1 = 3
        j = i - 1 # Índice del elemento anterior, osea 0 osea 5
        while j >= 0 and clave < lista[j]: # 0 >= 0 y 3 < 5
            lista[j + 1] = lista[j] # Mover el elemento mayor a la derecha, osea 5 a la posicion 1
            j -= 1 # Decrementar j, osea j = -1, el valor de j antes de el decremento es 0
        lista[j + 1] = clave # Insertar la clave en su posición correcta, osea lista[0] = 3
    return lista
lista = [5, 3, 8, 1, 2]
print(ordenacion_insercion(lista))

# Ejercicios
# 1- Implementa la ordenación por inserción en una lista de números enteros.
def InsertionSort(elements):
    n = len(elements)
    for i in range(1, n):
        key = elements[i] # segundo elementos de la list
        j = i - 1 # primer elemento de la lista
        while j >= 0 and elements[j] > key: # primer elemento sea mayor que el segundo
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key 
    return elements
print(InsertionSort([56, 4, 10, 1, 54, 12, 3]))

# 2- Crea un método que ordene una lista de cadenas utilizando ordenación por inserción.
def StringsInsertionSort(elements):
    for i in range(1, len(elements)):
        key = elements[i].lower()
        j = i - 1
        while j >= 0 and key < elements[j].lower():
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(StringsInsertionSort(["eric", "adriana", "Helen", "carlos"]))

# 3- Desarrolla un algoritmo que cuente el número de comparaciones realizadas durante la ordenación.
def Count(elements):
    aux = 0
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
            aux += 1
        elements[j + 1] = key
    return elements, aux
print(Count([56, 23, 1, 5]))

# 4- Escribe un programa que ordene una lista de floats usando ordenación por inserción.
def FloatsSort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(FloatsSort([12.0, 56.3, 1.0, 89.1, 22.3]))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo utilizando ordenación por inserción.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def ObjectsSort(people):
    for i in range(1, len(people)):
        key = people[i]
        j = i - 1
        while j >= 0 and key.age < people[j].age:
            people[j + 1] = people[j]
            j -= 1
        people[j + 1] = key
    return [(person.name, person.age) for person in people]
people = [Person("Eric", 30), Person("Adriana", 25), Person("Carlos", 35)]
print(ObjectsSort(people))

# 6- Crea un método que imprima el número de intercambios realizados durante la ordenación.
def CountSwaps(elements):
    swaps = 0
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
            swaps += 1
        elements[j + 1] = key
    return elements, swaps
print(CountSwaps([4, 3, 2, 1]))

# 7- Desarrolla un algoritmo que ordene una lista de números negativos y positivos utilizando ordenación por inserción.
def SortNUms(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(SortNUms([-5, 22, -100, 1, -10, 15]))

# 8- Escribe un programa que ordene una lista de tuplas por el primer elemento.
def SortListOfTuples(Tuples):
    for i in range(1, len(Tuples)):
        key = Tuples[i]
        j = i - 1
        while j >= 0 and key[0] < Tuples[j][0]:
            Tuples[j + 1] = Tuples[j]
            j -= 1
        Tuples[j + 1] = key
    return Tuples
print(SortListOfTuples([(100, "eric", 8), (22, "helen", 4), (1, "carlos", 4), (5, "luis", 10)]))

# 9- Implementa un algoritmo que ordene una lista de diccionarios por un valor específico.
def SortListOfDicts(dicts, Specific):
    for i in range(1, len(dicts)):
        key = dicts[i]
        j = i - 1
        while j >= 0 and key[Specific] < dicts[j][Specific]:
            dicts[j + 1] = dicts[j]
            j -= 1
        dicts[j + 1] = key
    return dicts
print(SortListOfDicts([{"name": "eric", "age": 30}, {"name": "adriana", "age": 25}, {"name": "carlos", "age": 3}], "age"))

# 10- Crea un método que ordene una lista de fechas utilizando ordenación por inserción.
from datetime import datetime
def SortDates(dates):
    for i in range(1, len(dates)):
        key = dates[i]
        j = i - 1
        while j >= 0 and key < dates[j]:
            dates[j + 1] = dates[j]
            j -= 1
        dates[j + 1] = key
    return dates
dates = [datetime(2023, 5, 17), datetime(2021, 1, 1), datetime(2022, 12, 25)]
print([date.strftime("%Y-%m-%d") for date in SortDates(dates)])

# 11- Escribe un programa que ordene una lista de números en orden descendente.
def ReverseSort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key > elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(ReverseSort([4, 30, 1, 22, 100]))

# 12- Implementa un algoritmo que ordene una lista de cadenas por su longitud utilizando ordenación por inserción.
def LeghtStringSort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and len(key) < len(elements[j]):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(LeghtStringSort(["murcielago", "carpa", "luz", "eric", "al"]))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y las ordene por prioridad utilizando ordenación por inserción.
class Task:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, description, priority):
        self.tasks.append({"description": description, "priority": priority})
        self.sort_tasks()
        
    def sort_tasks(self):
        for i in range(1, len(self.tasks)):
            key = self.tasks[i]
            j = i - 1
            while j >= 0 and key["priority"] < self.tasks[j]["priority"]:
                self.tasks[j + 1] = self.tasks[j]
                j -= 1
            self.tasks[j + 1] = key
            
    def get_tasks(self):
        for task in self.tasks:
            print(f"Task: {task['description']}, Priority: {task['priority']}")
            
    def remove_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                self.tasks.remove(task)
                break
        self.sort_tasks()
        return f"Task '{description}' removed."
    
task_manager = Task()
task_manager.add_task("Do laundry", 2)
task_manager.add_task("Complete project", 1)
task_manager.add_task("Buy groceries", 3)
task_manager.get_tasks()
print(task_manager.remove_task("Complete project"))

# Día 64: Ordenación por selección: teoría y ejemplos

# Teoría
# La ordenación por selección es un algoritmo que divide la lista en dos partes: la parte ordenada y la parte desordenada. 
# Repetidamente selecciona el elemento más pequeño (o más grande) de la parte desordenada y lo coloca al final de la parte ordenada.
# 
# Tips
# Visualiza el proceso de selección para entender mejor cómo funciona.
# Ten en cuenta que, al igual que la ordenación por burbuja, la ordenación por selección no es eficiente para listas grandes.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar la comprensión.
# Realiza pruebas con listas de diferentes tamaños y configuraciones.

def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n):
        # Encuentra el índice del elemento más pequeño
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Intercambia el elemento encontrado con el primero
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

lista = [5, 3, 8, 1, 2]
ordenada = ordenacion_seleccion(lista)
print("Lista ordenada:", ordenada)

# Ejercicios
# 1- Implementa la ordenación por selección en una lista de números enteros.
def SelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(x, int) for x in elements):
        raise TypeError("I only accept Integers numbers")
    n = len(elements)
    for i in range(n):
        IndexM = i # primer index de la lista
        for j in range(i+1, n): # este siempre va a estar un numero delante del index "i" x i + 1
            if elements[IndexM] > elements[j]: # si el segundo index elements[j] es menor que el primero elements[IndexM], se intercambian valores
                IndexM = j # se actualiza el valor de el primer index
        elements[i], elements[IndexM] = elements[IndexM], elements[i]
    return elements
print(SelectionSort([100, 1, 22, 56, 10]))

# 2- Crea un método que ordene una lista de cadenas utilizando ordenación por selección.
def SortingStrings(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept lists")
    elif not all(isinstance(s, str) for s in elements):
        raise TypeError("I only accept text")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM].lower() > elements[j].lower():
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

print(SortingStrings(["Eric", "alex", "Carlos", "Irma"]))

# 3- Desarrolla un algoritmo que cuente el número de pasadas realizadas durante la ordenación.
def CountingPasses(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept lists")
    elif not all(isinstance(x, int) for x in elements):
        raise TypeError("I only accept Integers numbers")
    n = len(elements)
    passes = 0
    for i in range(n):
        IndexM = i
        aux = False
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
                aux = True
        if aux:
            elements[i], elements[IndexM] = elements[IndexM], elements[i]
            passes += 1
    if passes == 0:
        return "The list is already sorted"
    return elements, passes

print(CountingPasses([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 4- Escribe un programa que ordene una lista de floats usando ordenación por selección.
def SortingFloats(elements):
    if not elements:
        return - 1
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif not all(isinstance(f, float) for f in elements):
        raise TypeError("I only accept decimals")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(SortingFloats([2.0, 100.2, 11.1, 22.5, 3.5, 92.29]))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo utilizando ordenación por selección.
def SortingObject(elements, attribute):
    if not elements:
        return -1
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if getattr(elements[IndexM], attribute) > getattr(elements[j], attribute):
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

class Objects:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"{self.name}: {self.price}"
    
Obj = [Objects("car", 2500), Objects("hax", 35000), Objects("window", 250), Objects("lawn", 10), Objects("row", 150)]
print(SortingObject(Obj, "price"))

# 6- Desarrolla un algoritmo que ordene una lista de números negativos y positivos utilizando ordenación por selección.
def NegativePositiveSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif not all(isinstance(x, int) for x in elements):
        raise TypeError("I need negative and positive numbers")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

print(NegativePositiveSelectionSort([100, 25, -1, -22, 52, 36, -9]))

# 7- Escribe un programa que ordene una lista de tuplas por el primer elemento.
def TupleSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list of tuples")
    elif not all(isinstance(x, tuple) for x in elements):
        raise TypeError("I need negative and positive numbers")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM][0].lower() > elements[j][0].lower():
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

print(TupleSelectionSort([("Eric", 25, "math"), ("Helen", 42, "tourist"), ("Alex", 56, "physics"), ("Bera", 22, "spanish")]))

# 8- Implementa un algoritmo que ordene una lista de diccionarios por un valor específico.
def DictSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list of tuples")
    elif not all(isinstance(x, dict) for x in elements):
        raise TypeError("I need negative and positive numbers")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if list(elements[IndexM].values())[0] > list(elements[j].values())[0]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(DictSelectionSort([{"eric" : 31}, {"Helen" : 42}, {"carlos" : 10}, {"axel" : 2}]))
            
# 9- Desarrolla un algoritmo que ordene una lista de caracteres.
def CharSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list of characters")
    elif not all(isinstance(x, str) and len(x) == 1 for x in elements):
        raise TypeError("I need a list of single characters")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(CharSelectionSort(['d', 'a', 'c', 'b']))

# 10- Escribe un programa que ordene una lista de números en orden descendente.
def DescendingSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif not all(isinstance(x, int) for x in elements):
        raise TypeError("I need integers")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] < elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(DescendingSelectionSort([5, 3, 8, 1, 2]))

# 11- Implementa un algoritmo que ordene una lista de cadenas por su longitud utilizando ordenación por selección.
def LenghtSelectionSort(elements):
    if not elements:
            return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif not all(isinstance(x, str) for x in elements):
        raise TypeError("I need integers")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if len(elements[IndexM].lower()) > len(elements[j].lower()):
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

print(LenghtSelectionSort(["eric", "bor", "edwards", "brenes", "murcielago"]))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y las ordene por prioridad utilizando ordenación por selección.
class Task:
    def __init__(self):
        self.tasks = []
        
    def Is_emepty(self):
        return len(self.tasks) == 0
        
    def SelectionSortTasks(self):
        n = len(self.tasks)
        for i in range(n):
            IndexM = i
            for j in range(i+1, n):
                if self.tasks[IndexM][1] > self.tasks[j][1]:
                    IndexM = j
            self.tasks[IndexM], self.tasks[i] = self.tasks[i], self.tasks[IndexM]
            
    def add_task(self, name, priority):
        if not isinstance(name, str):
            raise TypeError("I need a string")
        elif not isinstance(priority, int):
            raise TypeError("I need an integer")
        self.tasks.append((name, priority))
        self.SelectionSortTasks()
        
    def show_tasks(self):
        if self.Is_emepty():
            return "The task list is empty"
        u = 1
        for task in enumerate(self.tasks):    
            print(f"{u}- {task[1][0]}, Priority: {task[1][1]}")   
            u += 1
            
task_manager = Task()
task_manager.add_task("Do the laundry", 2)
task_manager.add_task("Finish the report", 1)
task_manager.add_task("Buy groceries", 3)
task_manager.show_tasks() 
# Día 37: Ordenación por burbuja: teoría y ejemplos
# Teoría: La ordenación por burbuja es uno de los algoritmos más simples. 
# Funciona comparando pares de elementos adyacentes y los intercambia si están en el orden incorrecto. 
# Este proceso se repite hasta que no se requieren más intercambios.

# Tips
# Visualiza el proceso de ordenación para entender mejor cómo funciona.
# Ten en cuenta que la ordenación por burbuja no es eficiente para listas grandes.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar la comprensión.
# Realiza pruebas con listas de diferentes tamaños y configuraciones.
# Implementación de la ordenación por burbuja en Python

def ordenacion_burbuja(lista):
    """Algoritmo de ordenación por burbuja."""
    n = len(lista) 
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista
lista = [5, 3, 100, 8, 1, 2]
ordenada = ordenacion_burbuja(lista)
print("Lista ordenada:", ordenada)


# Ejercicios
# 1- Implementa la ordenación por burbuja en una lista de números enteros.
def BubbleSort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
print(BubbleSort([14, 20, 9, 1, 10]))

# 2- Crea un método que ordene una lista de cadenas utilizando ordenación por burbuja.
def SortStrings(strings):
    s = len(strings)
    for i in range(s):
        for j in range(0, s -i -1):
            if strings[j].lower() > strings[j + 1].lower(): 
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings
print(SortStrings(["eric", "ariel", "Zambio", "Ariel"]))

# 3- Desarrolla un algoritmo que cuente el número de pasadas realizadas durante la ordenación.
def BubbleSortWithPasses(numbers):
    n = len(numbers)
    passes = 0
    for i in range(n):
        for j in range(0, n -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        passes += 1
    return numbers, passes
print(BubbleSortWithPasses([14, 20, 9, 1, 10]))

# 4- Escribe un programa que ordene una lista de floats usando ordenación por burbuja.
def BubbleSortFloats(floats):
    n = len(floats)
    for i in range(n):
        for j in range(0, n -i -1):
            if floats[j] > floats[j + 1]:
                floats[j], floats[j + 1] = floats[j + 1], floats[j]
    return floats
print(BubbleSortFloats([3.14, 2.71, 1.41, 0.577]))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo utilizando ordenación por burbuja.
def SortByAttribute(Objects, attribute):
    if not isinstance(attribute, int):
        raise ValueError("I only accept integers numbers as attribute")
    # como contar el número de atributos dentro de los objetos
    if attribute < 0 or attribute >= len(Objects[0]):
        raise ValueError("Attribute index out of range")
    n = len(Objects)
    for i in range(n):
        for j in range(0, n -i -1):
            if Objects[j][attribute] > Objects[j + 1][attribute]:
                Objects[j], Objects[j + 1] = Objects[j + 1], Objects[j]
    return Objects
obj = [("ericka", 23, "june"), ("helen", 42, "april"), ("eric", 32, "agust"), ("helenick", 53, "july")]
print(SortByAttribute(obj, 2))
     
# 6- Crea un método que optimice la ordenación por burbuja para detenerse si no se realizan intercambios.
def OptimizedBubbleSort(numbers):
    n = len(numbers)
    for i in range(n):
        aux = False # Variable para verificar si se realizaron intercambios
        # Si no se realizaron intercambios, la lista ya está ordenada
        for j in range(0, n -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                aux = True
        if not aux:  # Si no se realizaron intercambios, salimos del bucle
            break
    return numbers
print(OptimizedBubbleSort([14, 20, 9, 1, 10]))

# 7- Desarrolla un algoritmo que imprima el número de comparaciones realizadas durante la ordenación.
def BubbleSortWithComparisons(numbers):
    n = len(numbers)
    aux = 0
    for i in range(n):
        for j in range(0, n -i -1):
            aux += 1  # Incrementamos el contador de comparaciones
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers, aux
print(BubbleSortWithComparisons([14, 20, 9, 1, 10]))

# 8- Implementa un algoritmo que ordene una lista de tuplas por el primer elemento.
def SortListOftuples(elements):
    n = len(elements)
    for i in range(0, n):
        for j in range(0, n - i -1):
            if elements[j][0] < elements[j + 1][0]:
                elements[j],  elements[j + 1] = elements[j + 1], elements[j]
    return elements
list_Tuples = [('Zurika', 1993, 'agust'), ('helen', 1985, 'april'), ('helenick', 1953, 'july'), ('ericka', 1823, 'june')]
print(SortListOftuples(list_Tuples))

# 9- Crea un método que ordene una lista de diccionarios por un valor específico.
def SortListOfDics(elements, value):
    n = len(elements)
    for i in range(0, n):
        for j in range(0, n -i -1):
            if elements[j][list(elements[j].keys())[value]] > elements[j + 1][list(elements[j + 1].keys())[value]]:
                # se compara con la llave = nombre
                # el solo compara los nombres(keys) y con el valor va escoger cual es el primero(con el que va a iniciar)
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements
data = [
    {"marcos" : 42, "Agust" : 1, "note" : 75},
    {"luis" : 31, "Februry" : 10, "note" : 50},
    {"karlita" : 12, "December" : 18, "note" : 85},
    {"carmen" : 22, "May" : 1, "note" : 95}
]
print(SortListOfDics(data, 1))

# 10- Desarrolla un algoritmo que ordene una lista de fechas utilizando ordenación por burbuja.
def SortDates(dates):
    n = len(dates)
    for i in range(0, n):
        for j in range(0, n -i -1):
            if dates[j] > dates[j + 1]:
                dates[j], dates[j + 1] = dates[j + 1], dates[j]
    return dates
dates_list = ["2023-10-01", "2022-05-15", "2021-12-31", "2023-01-01"]
print(SortDates(dates_list))

# 11- Escribe un programa que ordene una lista de caracteres.
def SortCharacters(elements):
    elements = list(elements)
    n = len(elements)
    for i in range(0, n):
        aux = False
        for j in range(0, n -i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux: # si no ordena se detiene
            break
    return "".join(elements)
print(SortCharacters("#$%&/)=?¡¿'$%&!,:,_-;´´´¨?'"))

# 12- Crea un método que ordene una lista de cadenas por su longitud utilizando ordenación por burbuja.
def SortStrings(elements):
    n = len(elements)
    for i in range(0, n):
        aux = False
        for j in range(0, n -i -1):
            if len(elements[j]) > len(elements[j + 1]):
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux: # si despues de terminado el preceso no ordeno se detiene
            break
    return elements
print(SortStrings(["Eric Hernandez", "hello", "argentina", "arena black", "luz"]))

# 13- Desarrolla un algoritmo que ordene una lista de objetos complejos.
def SortComplexObjects(objects, attribute):
    n = len(objects)
    for i in range(0, n):
        aux = False
        for j in range(0, n -i -1):
            if objects[j][attribute.lower()] > objects[j + 1][attribute.lower()]:
                objects[j], objects[j + 1] = objects[j + 1], objects[j]
                aux = True
        if not aux: # si no ordena se detiene
            break
    return objects
print(SortComplexObjects([{"name": "Eric", "age": 30}, {"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}], "age"))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y las ordene por prioridad utilizando ordenación por burbuja.
def SortTask(tasks):
    n = len(tasks)
    for i in range(0, n):
        swap = False
        for j in range(0, n -i -1):
            if tasks[j]["Priority"] > tasks[j + 1]["Priority"]:
                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
                swap = True
        if not swap:
            break
    return tasks

print(SortTask([{"name": "Whast the dishes", "Priority": 37}, {"name": "mow the lawn", "Priority": 2}, {"paint": "Bob", "Priority": 30}]))
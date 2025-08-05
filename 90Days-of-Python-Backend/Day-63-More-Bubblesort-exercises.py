# Día 38: Ejercicios de ordenación por burbuja

# Teoría
# En este día, se practicarán diversas implementaciones y variaciones de la ordenación por burbuja para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.

## variacion enficiente de bubble sort
def bubble_sort(arr):
    if not arr:  # Verifica si la lista está vacía
        return -1
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if not swapped:  # Si no hubo intercambios no se necesita seguir iterando
            break
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90])) 

# Ejercicios
# 1- Implementa un algoritmo de ordenación por burbuja que devuelva -1 si la lista está vacía.
def BubbleSort(elements):
    if not elements:
        return -1
    elif not all(isinstance(a, int) for a in elements):
        raise TypeError("I only accept list with numbers")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True # cambia el valor si hubo intercambios
        if not aux:
            break
    return elements
import random
data = [random.randint(1, 100) for i in range(10)]
print(BubbleSort(data))

# 2- Crea un método que ordene una lista de enteros y retorne la lista ordenada.
def SortIntegers(Integers):
    if not Integers:
        return -1
    elif not all(isinstance(i, int) for i in Integers):
        raise TypeError("I only accept Integers")
    n = len(Integers)
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if Integers[j] > Integers[j + 1]:
                Integers[j], Integers[j + 1] = Integers[j + 1], Integers[j]
                aux = True
        if not aux:
            break
    return Integers
data = [ random.randint(-50, 50) for i in range(10)]
print(SortIntegers(data))

# 3- Desarrolla un algoritmo que ordene una lista de cadenas en orden alfabético.
def SortStrings(elements):
    if not elements:
        return -1
    elif not all(isinstance(s, str) for s in elements):
        raise TypeError("I only accept strings")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
import string
data = ["".join(random.choice(string.ascii_letters) for i in range(5)) for i in range(8)] # uno es para la cantidad de letras y el otro para los elementos
print(SortStrings(data))

# 4- Escribe un programa que ordene una lista de números y retorne el número de intercambios realizados.
def BubbleSort1(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(a, int) for a in elements):
        raise TypeError("I only accept a list of numbers")
    n = len(elements)
    sux = 0
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
                sux += 1
        if not aux:
            break
    return sux

print(BubbleSort1([10, 1, 2, 3]))
                
# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo específico y retorne la lista.
def SortObjects(objects, attribute):
    if not objects:
        return -1
    elif not isinstance(objects, list):
        raise TypeError("I only accept list")
    n = len(objects)
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if getattr(objects[j], attribute) > getattr(objects[j + 1], attribute):
                objects[j], objects[j + 1] = objects[j + 1], objects[j]
                aux = True
        if not aux:
            break
    return objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} ({self.age})"
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
print(SortObjects(people, 'age'))

# 6- Crea un método que ordene una lista de floats y retorne la lista ordenada.
def BubbleSortFloats(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, float) for i in elements):
        raise TypeError("I only accept list of floats")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(BubbleSortFloats([12.0, 11.0, 22.23, 0.1, 5.2]))

# 7- Desarrolla un algoritmo que ordene una lista de números en orden descendente utilizando ordenación por burbuja.
def BubbleSortDesending(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(x, int) for x in elements):
        raise TypeError("I only accept list with numbers")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n - i -1):
            if elements[j] < elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(BubbleSortDesending([0, 12, 23, 1, 15, 256]))

# 8- Implementa un algoritmo que ordene una lista de tuplas por el segundo elemento.
def SortingTuples(elements):
    if not elements:
        return -1
    n = len(elements)
    for i in range(0, n):
        aux = False
        for j in range(0, n - i - 1):
            if elements[j][1] > elements[j + 1][1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(SortingTuples([("eric", 100, "math"), ("alex", 22, "spanish"), ("helen", 21, "physics"), ("damaris", 55, "english")]))

# 9- Crea un método que ordene una lista de diccionarios por un valor específico y retorne la lista.
def SortingDiccionaries(elements):
    if not elements:
        return -1
    n = len(elements)
    for i in range(0, n):
        aux = False
        for j in range(0, n - i - 1):
            if list(elements[j].values())[0] > list(elements[j + 1].values())[0]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(SortingDiccionaries([{"eric" : 31}, {"helen" : 42}, {"carlos" : 10}, {"axel" : 2}]))

# 10- Desarrolla un algoritmo que ordene una lista de objetos complejos y retorne la lista.
def SortingComplexObjects(elements, attribute):
    if not elements:
        return -1
    n = len(elements)
    for i in range(0, n):
        aux = False
        for j in range(0, n - i - 1):
            if getattr(elements[j], attribute) > getattr(elements[j + 1], attribute):
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
class ComplexObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"{self.name} ({self.value})"
def create_complex_objects():
    return [ComplexObject("Object1", 10), ComplexObject("Object2", 5), ComplexObject("Object3", 15)]
objects = create_complex_objects()
print(SortingComplexObjects(objects, 'value'))


# Mini Proyectos
# Desarrolla un programa que gestione una lista de productos y los ordene por precio utilizando ordenación por burbuja.
def SortProductsByPrice(products):
    if not products:
        return -1
    elif not isinstance(products, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(p, dict) for p in products):
        raise TypeError("I only accept list of dictionaries")
    elif not all("price" in p for p in products):
        raise KeyError("Each dictionary must have a price key")
    elif not all("name" in p for p in products):
        raise KeyError("Each dictionary must have a name of the product")
    elif not all(isinstance(p['price'], (int, float)) for p in products):
        raise TypeError("I need the price to be a number")
    elif not all(isinstance(p['name'], str) for p in products):
        raise TypeError("I need the name to be a string")
    n = len(products)
    for i in range(0, n):
        aux = False
        for j in range(0, n - i - 1):
            if products[j]['price'] > products[j + 1]['price']:
                products[j], products[j + 1] = products[j + 1], products[j]
                aux = True
        if not aux:
            break
    return products
products = [
    {"name": "Product A", "price": 30},
    {"name": "Product B", "price": 20},
    {"name": "Product C", "price": 50}
]
print(SortProductsByPrice(products))

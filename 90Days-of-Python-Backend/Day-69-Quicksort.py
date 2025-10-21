# Día 69: Ejercicios de Quicksort

# Teoría: En este día, se practicarán diversas implementaciones y variaciones de Quicksort para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.

# Ejercicios
# 1- Implementa un algoritmo de Quicksort que devuelva -1 si la lista está vacía.
def Quicksort(elements):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    if not all(isinstance(aux, int) for aux in elements):
        raise TypeError("All the elements in the list must be numbers")
    if len(elements) < 1:
        return -1
    if len(elements) == 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [n for n in elements if n < pivot]
    medium = [n for n in elements if n == pivot]
    right = [n for n in elements if n > pivot]
    return Quicksort(left) + medium + Quicksort(right)

print(Quicksort([]))

# 2- Escribe un programa que ordene una lista de números y retorne el número de comparaciones realizadas.
def Quicksort_with_comparisons(elements):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    if not all(isinstance(aux, int) for aux in elements):
        raise TypeError("All the elements in the list must be numbers")
    if len(elements) <= 1:
        return elements, 0
    pivot = elements[len(elements) // 2]
    left = [n for n in elements if n < pivot]
    medium = [n for n in elements if n == pivot]
    right = [n for n in elements if n > pivot]
    left_sorted, left_comparisons = Quicksort_with_comparisons(left)
    right_sorted, right_comparisons = Quicksort_with_comparisons(right)
    total_comparisons = left_comparisons + right_comparisons + len(elements) - 1
    return left_sorted + medium + right_sorted, total_comparisons
print(Quicksort_with_comparisons([3,6,8,10,1,2,1]))

# 3- Implementa un algoritmo que ordene una lista de objetos por un atributo específico y retorne la lista.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Product: name: {self.name} and price: {self.price}"
        
def QuicksortEspecifictObject(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2].price
    left = [n for n in elements if n.price < pivot]
    medium = [n for n in elements if n.price == pivot]
    right = [n for n in elements if n.price > pivot]
    return QuicksortEspecifictObject(left) + medium + QuicksortEspecifictObject(right)

data = [Product("engine", 190000), Product("bedrock", 25000), Product("wallpepar", 250), Product("Box", 10), Product("hammer", 2500)]
print(QuicksortEspecifictObject(data))

# 4- Implementa un algoritmo que ordene una lista de tuplas por el primer elemento.
def QuicsortTuples(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2][0].lower()
    left = [n for n in elements if n[0].lower() < pivot]
    medium = [n for n in elements if n[0].lower() == pivot]
    right = [n for n in elements if n[0].lower() > pivot]
    return QuicsortTuples(left) + medium + QuicsortTuples(right)
data1 = [("engine", 190000), ("bedrock", 25000), ("wallpepar", 250), ("Box", 10), ("hammer", 2500), ("bedrock", 25000)]
print(QuicsortTuples(data1))
    

# 5- Crea un método que ordene una lista de diccionarios por un valor específico y retorne la lista.
def QuicksortDict(elements, key):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2][key]
    left = [n for n in elements if n[key] < pivot]
    medium = [n for n in elements if n[key] == pivot]
    right = [n for n in elements if n[key] > pivot]
    return QuicksortDict(left, key) + medium + QuicksortDict(right, key)
data2 = [{"name": "engine", "price": 190000}, {"name": "bedrock", "price": 25000}, {"name": "wallpepar", "price": 250}, {"name": "Box", "price": 10}, {"name": "hammer", "price": 2500}, {"name": "bedrock", "price": 25000}]
print(QuicksortDict(data2, "price"))

# 6- Desarrolla un algoritmo que ordene una lista de fechas y retorne la lista ordenada.
def QuicksortDates(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [n for n in elements if n < pivot]
    medium = [n for n in elements if n == pivot]
    right = [n for n in elements if n > pivot]
    return QuicksortDates(left) + medium + QuicksortDates(right)
data3 = ["2023-01-01", "2022-12-31", "2023-06-15", "2021-05-20", "2022-01-01"]
print(QuicksortDates(data3))

# 7- Desarrolla un algoritmo que ordene una lista de objetos complejos y retorne la lista.
class ComplexObject:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        
    def __repr__(self):
        return f"ComplexObject: name: {self.name} and attributes: {self.attributes}"
def QuicksortComplexObject(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2].name.lower()
    left = [n for n in elements if n.name.lower() < pivot]
    medium = [n for n in elements if n.name.lower() == pivot]
    right = [n for n in elements if n.name.lower() > pivot]
    return QuicksortComplexObject(left) + medium + QuicksortComplexObject(right)
data4 = [ComplexObject("engine", {"price": 190000}), ComplexObject("bedrock", {"price": 25000}), ComplexObject("wallpepar", {"price": 250}), ComplexObject("Box", {"price": 10}), ComplexObject("hammer", {"price": 2500}), ComplexObject("bedrock", {"price": 25000})]
print(QuicksortComplexObject(data4))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de productos y los ordene por precio utilizando Quicksort.
def Products(elements, key):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    pivot = elements[len(elements) // 2][key]
    left = [aux for aux in elements if aux[key] < pivot]
    medium = [aux for aux in elements if aux[key] == pivot]
    right = [aux for aux in elements if aux[key] > pivot]
    return Products(left, key) + medium + Products(right, key)

data5 = [{"name" : "knife", "price" : 25000}, 
         {"name" : "niddle", "price" : 190}, 
         {"name" : "engine", "price" : 180}, 
         {"name" : "wardrove", "price" : 19000},
         {"name" : "roof", "price" : 15000},
         {"name" : "pencil", "price" : 25}
         ]

print(Products(data5, "price"))
    

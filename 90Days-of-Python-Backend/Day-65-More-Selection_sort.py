# Día 65: Ejercicios de ordenación por selección

# Teoría
# En este día, se practicarán diversas implementaciones y variaciones de la ordenación por selección para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.


# Ejercicios
# 1- Crea un método que ordene una lista de floats y retorne la lista ordenada.
def FloatsSelectionSort(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, float) for i in elements):
        raise TypeError("I only accept floats in the list")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j  
        elements[i], elements[IndexM] = elements[IndexM], elements[i]
    return elements

print(FloatsSelectionSort([1.0, 2.0, 3.0, 4.0, 22.0, 10.1]))

# 2- Implementa un algoritmo que ordene una lista de números negativos y positivos utilizando ordenación por selección.
def SelectionSortNumbers(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, int) for i in elements):
        raise TypeError("I only accept floats in the list")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i + 1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(SelectionSortNumbers([52, -1, 2, -22, 10, 100, 12]))

# 3- Desarrolla un algoritmo que ordene una lista de números en orden descendente utilizando ordenación por selección.
def Selection(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, int) for i in elements):
        raise TypeError("I only accept floats in the list")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] < elements[j]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(Selection([52, -1, 2, -22, 10, 100, 12]))

# 4- Escribe un programa que ordene una lista de números y retorne el número de intercambios realizados.
def SelectionSortCountSwaps(elements):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, int) for i in elements):
        raise TypeError("I only accept floats in the list")
    n = len(elements)
    count = 0
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM] > elements[j]:
                IndexM = j
        elements[i], elements[IndexM] = elements[IndexM], elements[i]
        count += 1
    return elements, count
print(SelectionSortCountSwaps([52, -1, 2, -22, 10, 100, 12]))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo específico y retorne la lista.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def SelectionSortObjectsByAttribute(elements, attribute):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, Person) for i in elements):
        raise TypeError("I only accept Person objects in the list")
    elif not all(hasattr(i, attribute) for i in elements):
        raise ValueError(f"All objects must have the attribute '{attribute}'")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if getattr(elements[IndexM], attribute) > getattr(elements[j], attribute):
                IndexM = j
        elements[i], elements[IndexM] = elements[IndexM], elements[i]
    return elements
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
sorted_people = SelectionSortObjectsByAttribute(people, "age")
for person in sorted_people:
    print(f"{person.name}: {person.age}")
    

# 6- Implementa un algoritmo que ordene una lista de tuplas por el segundo elemento.
def TuplesSelectionSort(elements):
    if not elements:
        return "the list of tuples are empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list of tuples")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if elements[IndexM][1] > elements[j][1]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements

print(TuplesSelectionSort([("eric", 25, 1), ("helen", 1, 89), ("carlos", -1, 55), ("marta", 10, 45), ("luis", 11, 55)]))

# 7- Crea un método que ordene una lista de diccionarios por un valor específico y retorne la lista.
def DiccionariesSelectionSort(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list of diccionaries")
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if list(elements[IndexM].values())[0] > list(elements[j].values())[0]:
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(DiccionariesSelectionSort([{"eric" : 31}, {"helen" : 42}, {"carlos" : 10}, {"axel" : 2}]))
        
# 8- Crea un método que ordene una lista de cadenas por su longitud y retorne la lista ordenada.
def StringsSelectionSort(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list of strings")
    elif not all(isinstance(i, str) for i in elements):
        raise TypeError("I only accept strings in the list")
    elif elements == sorted(elements):
        return "The list is already sorted"
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if len(elements[IndexM]) > len(elements[j]):
                IndexM = j
        elements[IndexM], elements[i] = elements[i], elements[IndexM]
    return elements
print(StringsSelectionSort(["eric", "helen", "carlos", "axel", "marta", "luis", "ana", "jose"]))

# 9- Desarrolla un algoritmo que ordene una lista de objetos complejos y retorne la lista.
def ComplexObjectsSelectionSort(elements, attribute):
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    elif not all(hasattr(i, attribute) for i in elements):
        raise ValueError(f"All objects must have the attribute '{attribute}'")
    elif elements == sorted(elements, key=lambda x: getattr(x, attribute)):
        return "The list is already sorted"
    n = len(elements)
    for i in range(n):
        IndexM = i
        for j in range(i+1, n):
            if getattr(elements[IndexM], attribute) > getattr(elements[j], attribute):
                IndexM = j
        elements[i], elements[IndexM] = elements[IndexM], elements[i]
    return elements
class Complex:
    def __init__(self, name, value):
        self.name = name
        self.value = value
complex_list = [Complex("obj1", 5), Complex("obj2", 3), Complex("obj3", 8)]
sorted_complex = ComplexObjectsSelectionSort(complex_list, "value")
for obj in sorted_complex:
    print(f"{obj.name}: {obj.value}")
    

# Mini Proyectos
# Desarrolla un programa que gestione una lista de productos y los ordene por precio utilizando ordenación por selección.
class Products:
    def __init__(self):
        self.storage = []
        
    def Is_empty(self):
        if len(self.storage) == 0:
            return "The storage is empty"
        
    def Sort(self):
        n = len(self.storage)
        for i in range(n):
            IndexM = i
            for j in range(i+1, n):
                if self.storage[IndexM][1] > self.storage[j][1]:
                    IndexM = j
            self.storage[IndexM], self.storage[i] = self.storage[i], self.storage[IndexM]
    
    def add(self, Product, Price):
        if not Product or not Price:
            return "I need a product and a price"
        elif not isinstance(Product, str):
            raise TypeError("I need a text for products")
        elif not isinstance(Price, int):
            raise TypeError("I need a number for a price")
        self.storage.append((Product.lower(), Price))
        self.Sort()
        return "Thank you for adding"
    
    def SeeProducts(self):
        aux = 1
        for prod, num in self.storage:
            print(f"{aux}- product: {prod}, price: {num}")
            aux += 1
            
    def Delete(self, obj):
        if self.Delete():
            return "The storage is empty"
        elif not obj:
            return "I need something to delete"
        elif not isinstance(obj, str):
            raise TypeError("I only accept text")
        for prod, prices in self.storage:
            if prod == obj.lower():
                self.storage.remove((prod, prices))
        self.Sort()
        return "Thank you for delete"
    
Menu = Products()
Menu.add("boxes", 2500)
Menu.add("axes", 25000)
Menu.add("niddle", 25)
Menu.add("wood", 250)
Menu.add("hammer", 19)
Menu.SeeProducts()

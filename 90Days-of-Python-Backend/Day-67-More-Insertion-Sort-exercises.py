# Día 67: Mas ejercicios de ordenación por inserción
# Teoría: En este día, se practicarán diversas implementaciones y variaciones de la ordenación por inserción para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.


# Ejercicios
# 1- Implementa un algoritmo de ordenación por inserción que devuelva -1 si la lista está vacía.
def Insert_Sort(elements):
    if len(elements) == 0:
        return -1
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(Insert_Sort([-89, 4, 5, 100, 32, 22, 2]))

# 2- Desarrolla un algoritmo que ordene una lista de cadenas en orden alfabético.
def String_Sort(elements):
    if len(elements) == 0:
        return -1
    for i in range(1, len(elements)):
        key = elements[i].lower()
        j = i - 1
        while j >= 0 and key < elements[j].lower():
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(String_Sort(["Helen", "luz", "aspa", "Eric", "Barra", "Alo"]))

# 3- Implementa un algoritmo que ordene una lista de tuplas por el segundo elemento.
def TuplesSort(elements):
    if len(elements) == 0:
        return - 1
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j][1] > key[1]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(TuplesSort([("Eric", 56, "oct"), ("Helen", 21, "sept"), ("Carlos", 5, "may"), ("jenny", 2, "dec"), ("luis", 1, "apr")]))

# 4- Implementa un algoritmo que ordene una lista de objetos por un atributo específico y retorne la lista.      
class Warhouse:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
def SortAtribute(products):
    if len(products) == 0:
        return -1
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and key.name < products[j].name:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return [(prod.name, prod.price) for prod in products]

data = [Warhouse("hax", 250), Warhouse("hammer", 1500), Warhouse("niddle", 55), Warhouse("machine", 25000)]
print(SortAtribute(data))

# 5- Crea un método que ordene una lista de diccionarios por un valor específico y retorne la lista.
def DicsSort(elements, aux):
    if len(elements) == 0:
        return - 1
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j][aux] > key[aux]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(DicsSort([{"name" : "Eric", "Note" : 56, "Mont" : "oct"}, 
                  {"name" : "Helen", "Note" : 21, "Mont" : "sept"}, 
                  {"name" : "Carlos", "Note" : 5, "Mont" : "may"}, 
                  {"name" : "jenny", "Note" : 2, "Mont" : "dec"}, 
                  {"name" : "luis", "Note" : 1, "Mont" : "apr"}], "Mont"))

# 6- Desarrolla un algoritmo que ordene una lista de objetos complejos y retorne la lista.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
def ComplexSort(elements):
    if len(elements) == 0:
        return -1
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and (key.real < elements[j].real or (key.real == elements[j].real and key.imag < elements[j].imag)):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return [(comp.real, comp.imag) for comp in elements]
print(ComplexSort([Complex(2, 3), Complex(1, 5), Complex(2, 1), Complex(0, 4), Complex(1, 1)]))


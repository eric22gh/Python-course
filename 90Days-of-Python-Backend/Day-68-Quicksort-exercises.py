# Día 68: Ordenación rápida (Quicksort):
# 
# Teoría
# Quicksort es un algoritmo de ordenación eficiente que utiliza la técnica de divide y vencerás.
# Selecciona un "pivote" y particiona la lista en dos sublistas: una con elementos menores que el pivote y otra con elementos mayores. 
# Luego, aplica recursivamente el mismo proceso a las sublistas.
# 
# Tips
# Elige un buen pivote para optimizar el rendimiento.
# Visualiza el proceso de partición para entender mejor cómo funciona.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar la comprensión.
# Realiza pruebas con listas de diferentes tamaños y configuraciones.


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]  # Elegir el pivote
    left = [x for x in lista if x < pivot] # Particionar, crear sublistas de elementos menores al pivote
    medium = [x for x in lista if x == pivot] # Separa los elementos iguales al pivote, asi se evitan llamadas recursivas innecesarias
    right = [x for x in lista if x > pivot]# Particionar, crear sublistas de elementos mayores al pivote
    return quicksort(left) + medium + quicksort(right) # Llamada recursiva y concatenación de las sublistas ordenadas

lista = [5, 3, 8, 1, 2]
print(quicksort(lista))  

# Ejercicios
# 1- Implementa Quicksort en una lista de números enteros.
def QuicksortIntegers(elements):
    if len(elements) <= 1:
        return elements
    # cuando la if termina con return no es necesario usar else
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return QuicksortIntegers(left) + medium + QuicksortIntegers(right)

import random
data = [random.randint(1, 100) for i in range(10)]
print(QuicksortIntegers(data))

# 2- Crea un método que ordene una lista de cadenas utilizando Quicksort.
def QuicksortStrings(elements):
    if len(elements) <= 1:
        return elements
    elements = [x.capitalize() for x in elements]
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return QuicksortStrings(left) + medium + QuicksortStrings(right)
print(QuicksortStrings(["Eric", "zebra", "Helen", "carro", "Lavanderia", "Maria"]))

# 3- Desarrolla un algoritmo que cuente el número de comparaciones realizadas durante la ordenación.
def CountSort(elements):
    if len(elements) <= 1:
        return elements, 0
    pivot = elements[len(elements) // 2]
    left, count_left = CountSort([x for x in elements if x < pivot])
    medium = [x for x in elements if x == pivot]
    right, count_right = CountSort([x for x in elements if x > pivot])
    count = count_left + count_right + (len(elements) - 1)
    return left + medium + right, count

import random
data = [random.randint(1, 500) for a in range(8)]
print(CountSort(data))
    
# 4- Escribe un programa que ordene una lista de floats usando Quicksort. 
def QuicksortFloats(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return QuicksortFloats(left) + medium + QuicksortFloats(right)
print(QuicksortFloats([56, 98, 32, 1, 47, 96, 48, 36]))

# 5- Implementa un algoritmo que ordene una lista de objetos por un atributo utilizando Quicksort.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def __repr__(self):
        return f"{self.name} ({self.age})"
def QuicksortObjects(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2].age
    left = [x for x in elements if x.age < pivot]
    medium = [x for x in elements if x.age == pivot]
    right = [x for x in elements if x.age > pivot]
    return QuicksortObjects(left) + medium + QuicksortObjects(right)
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
print(QuicksortObjects(people))

# 6- Crea un método que imprima el número de intercambios realizados durante la ordenación.
# def CountQuickSort(elements):
#     if len(elements) <= 1:
#         return elements
#     pivot = elements[len(elements) // 2]
#     left = [x for x in elements if x < pivot]
#     medium = [x for x in elements if x == pivot]
#     right = [x for x in elements if x > pivot]
#     count = len([n for n in elements])
#     return count
# print(CountQuickSort([56, 5, 1, 10, 100]))

# 7- Desarrolla un algoritmo que ordene una lista de números negativos y positivos utilizando Quicksort.
def SortNegativeandPositive(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return SortNegativeandPositive(left) + medium + SortNegativeandPositive(right)
print(SortNegativeandPositive([56, 5, 1, 10, 100, -50, 56, -10, -22]))

# 8- Escribe un programa que ordene una lista de tuplas por el primer elemento.
def QuickSortTuples(elements):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("I only accept list")
    if not all(isinstance(t, tuple) for t in elements):
        raise TypeError("I only accept tuples inside the list")
    pivot = elements[len(elements) // 2][0].capitalize()
    left = [x for x in elements if x[0].capitalize() < pivot]
    medium = [x for x in elements if x[0].capitalize() == pivot]
    right = [x for x in elements if x[0].capitalize() > pivot]
    return QuickSortTuples(left) + medium + QuickSortTuples(right)

print(QuickSortTuples([("Zara", 23), ("ERic", 32), ("Zara", 23), ("helen", 43), ("carlos", 56)]))

# 9- Implementa un algoritmo que ordene una lista de diccionarios por un valor específico.
def SortDiccionaries(elements, specific):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [y for y in elements if y[specific] < pivot[specific]]
    medium = [y for y in elements if y[specific] == pivot[specific]]
    right = [y for y in elements if y[specific] > pivot[specific]]
    return SortDiccionaries(left, specific) + medium + SortDiccionaries(right, specific)
print(SortDiccionaries([{"name": "eric", "age": 30}, {"name": "adriana", "age": 25}, {"name": "carlos", "age": 3}], "name"))
# 10- Crea un método que ordene una lista de fechas utilizando Quicksort.
def SortDates(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return SortDates(left) + medium + SortDates(right)
from datetime import datetime
dates = [datetime(2023, 5, 17), datetime(2021, 6, 25), datetime(2022, 12, 1)]
print(SortDates(dates))

# 11- Desarrolla un algoritmo que ordene una lista de caracteres.
def SortCharacters(elements):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("I only accepted list")
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    medium = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return SortCharacters(left) + medium + SortCharacters(right)
print(SortCharacters(["$%&/()", "?'¿", "!#¡-", "-:;+", "[]&%¡"]))

# 12- Escribe un programa que ordene una lista de números en orden descendente.
def DecendedSort(Data):
    if len(Data) <= 1:
        return Data
    if not isinstance(Data, list):
        raise TypeError("I only accept list")
    pivot = Data[len(Data) // 2]
    left = [n for n in Data if n < pivot]
    medium = [n for n in Data if n == pivot]
    right = [n for n in Data if n > pivot]
    return DecendedSort(right) + medium + DecendedSort(left)

nums = [random.randint(1, 500) for x in range(10)]
print(DecendedSort(nums))

# 13- Implementa un algoritmo que ordene una lista de cadenas por su longitud utilizando Quicksort.
def SortlenghtStrings(lenght):
    if len(lenght) <= 1:
        return lenght
    if not isinstance(lenght, list):
        raise TypeError("I only accept list")
    pivot = lenght[len(lenght) // 2]
    left = [aux for aux in lenght if len(aux) < len(pivot)]
    medium = [aux for aux in lenght if len(aux) == len(pivot)]
    right = [aux for aux in lenght if len(aux) > len(pivot)]
    return SortlenghtStrings(left) + medium + SortlenghtStrings(right)

print(SortlenghtStrings(["Eric", "Murcielago", "zebra", "Helen", "carro", "Lavanderia", "Maria", "aux", "all", "carro"]))
    
# 14- Crea un método que ordene una lista de objetos complejos.
class Warhouse:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        
    def __repr__(self):
        return f"Warhouse(product='{self.product}', price={self.price})"
        
def SortComplainObjects(elements):
    if len(elements) <= 1:
        return elements
    if not isinstance(elements, list):
        raise TypeError("I only accept list")
    pivot = elements[len(elements) // 2].product.capitalize()
    left = [aux for aux in elements if aux.product.capitalize() < pivot]
    medium = [aux for aux in elements if aux.product.capitalize() == pivot]
    right = [aux for aux in elements if aux.product.capitalize() > pivot]
    return SortComplainObjects(left) + medium + SortComplainObjects(right)

menu = [Warhouse("Hax", 2500), Warhouse("Knife", 250), Warhouse("Hammer", 290), Warhouse("drill", 25000), Warhouse("Tester", 100), Warhouse("Wellding", 85)]
print(SortComplainObjects(menu))


# Mini Proyectos
# Crea un simulador de un sistema de reservas que utilice Quicksort para organizar reservas.
class Reservation:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.reservations = []
        # nota falta implementarlo con fechas reales
        
    def __repr__(self):
        return f"Reservation(name='{self.name}', date={self.date})"
    
    def sort_reservations(self, reservations=None):
        if reservations is None:
            reservations = self.reservations
        if len(reservations) <= 1:
            return reservations
        pivot = reservations[len(reservations) // 2]["date"]
        left = [x for x in reservations if x["date"] < pivot]
        medium = [x for x in reservations if x["date"] == pivot]
        right = [x for x in reservations if x["date"] > pivot]
        return self.sort_reservations(left) + medium + self.sort_reservations(right)
    
    def add_reservation(self, name, date):
        # guardar y convertir a fecha real
        from datetime import datetime
        if not isinstance(date, str) or not isinstance(name, str):
            raise TypeError("I only accept text")
        date = datetime.strptime(date, "%d-%m-%Y").date()
        self.reservations.append({"name": name.capitalize(), "date": date})
        self.reservations = self.sort_reservations()
       
        
    def Update_reservation(self, old_name, new_date):
        from datetime import datetime
        if not isinstance(old_name, str) or not isinstance(new_date, str):
            raise TypeError("I only accept text")
        new_date = datetime.strptime(new_date, "%d-%m-%Y").date()
        for reservation in self.reservations:
            if reservation["name"] == old_name:
                reservation["date"] = new_date
                return f"Reservation for {old_name} has been updated to {new_date}."
        self.sort_reservations()
        
    def Cancel_reservation(self, name):
        if not isinstance(name, str):
            raise TypeError("I only accept text")
        for reservation in self.reservations:
            if reservation["name"] == name:
                self.reservations.remove(reservation)
                return f"Reservation for {name} has been cancelled."
        self.sort_reservations()
        
    def show_reservations(self):
        if not self.reservations:
            print("No reservations found.")
        for id, reservation in enumerate(self.reservations, start=1):
            print(f"{id}. {reservation['name']} - {reservation['date']}")
            
    def Search_reservation(self, name):
        # Usando busqueda binaria para encontrar la reserva
        if not isinstance(name, str):
            raise TypeError("I only accept text")
        name = name.capitalize()
        left = 0
        right = len(self.reservations) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.reservations[medium]["name"] == name:
                aux = self.reservations[medium]
                return f"Reservation found: {aux['name']} - {aux['date']}"
            elif self.reservations[medium]["name"] < name:
                left = medium + 1
            else:
                right = medium - 1
        return "Reservation not found"
    

res_system = Reservation("Hotel Plaza", "2025-10-30")
res_system.add_reservation("Alice", "25-12-2025")
res_system.add_reservation("Bob", "01-10-2025")
res_system.add_reservation("Charlie", "02-10-2025")
res_system.add_reservation("Diana", "31-10-2025")
res_system.add_reservation("helen", "31-10-2030")
print(res_system.Update_reservation("Alice", "15-11-2025"))
print(res_system.Cancel_reservation("Bob"))
print(res_system.Search_reservation("Charlie"))
res_system.show_reservations()
        
            
        
    
       
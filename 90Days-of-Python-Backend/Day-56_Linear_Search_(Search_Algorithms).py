# 🎉 Búsqueda Lineal: ¡Vamos a Buscar!
# =======================================
# La búsqueda lineal es un algoritmo que busca un elemento en una lista, recorriéndola de principio a fin. ¡Es simple y efectivo,
# especialmente cuando la lista no está ORDENADA!

# 🚀 Características
# - **Complejidad temporal**: O(n), donde n es el número de elementos en la lista.
# - **Complejidad espacial**: O(1), ya que solo usamos unas pocas variables.

# ✅ Clases de Complejidad
# | Notación  | Descripción                      | Ejemplo común                                | Eficiencia  |
# |-----------|----------------------------------|--------------------------------------------- |-------------|
# | O(1)      | Tiempo constante                  | Acceso a un elemento en una lista           | Excelente   |
# | O(log n)  | Tiempo logarítmico               | Búsqueda binaria, se reduce a la mitad       | Muy buena   |
# | O(n)      | Tiempo lineal                    | Recorrer una lista                           | Buena       |
# | O(n log n)| Tiempo casi lineal               | Algoritmos de ordenación como Merge Sort     | Aceptable |
# | O(n²)     | Tiempo cuadrático                | Doble bucle anidado                          | Pobre       |
# | O(2ⁿ)     | Tiempo exponencial               | Algoritmo recursivo de Fibonacci             | Mala        |

# ✅ Notación Big O en Complejidad Espacial
# | Notación  | Descripción                      | Ejemplo común                                | Eficiencia  |
# |-----------|----------------------------------|----------------------------------------------|-------------|
# | O(1)      | Espacio constante                | Variables temporales                         | Excelente   |
# | O(n)      | Espacio lineal                   | Almacenar una lista de n elementos           | Buena       |
# | O(n²)     | Espacio cuadrático               | Matrices bidimensionales                     | Pobre       |

# 💡 Tips para Usar Búsqueda Lineal
# 1. Utiliza la búsqueda lineal en listas pequeñas o desordenadas.
# 2. Asegúrate de manejar correctamente los casos en los que el elemento no se encuentra.

# ✅ Buenas Prácticas
# - Documenta el propósito y la lógica de tu implementación.
# - Realiza pruebas con diferentes entradas para verificar su correcto funcionamiento.

def busqueda_lineal(lista, objetivo):
    """🔍 Algoritmo de búsqueda lineal."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # 🎯 Retorna el índice del elemento encontrado
    return -1  # ❌ Retorna -1 si no se encuentra el elemento

resultado = busqueda_lineal([3, 5, 2, 4, 1], 4)
print("Elemento encontrado en el índice:", resultado)  # Salida: Elemento encontrado en el índice: 3

# Ejercicios

# 1- Implementa la búsqueda lineal en una lista de números enteros.
from random import randint as rd
def linear_search(numbers, aux):
    if not numbers or not aux:
        return "An item is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    elif not isinstance(aux, int):
        raise TypeError("I only accept the object as a number")
    for i in range(len(numbers)):
        if numbers[i] == aux:
            return numbers[i]
    return "I did not find the element"
print(linear_search([1, 89, 5, 45, 2, 3], 1))
        
# 2- Crea un método que busque un carácter en una cadena usando búsqueda lineal.
def search_string(phrase, aux):
    if not phrase or not aux:
        return "An item is empty"
    elif not isinstance(aux, str) or not isinstance(phrase, str):
        raise TypeError("I only accept strings objects")
    for i in phrase:
        if i == aux:
            return i
    return "I did not find the element"   
print(search_string("murcielago", "k"))
        
# 3- Desarrolla un algoritmo que cuente cuántas veces aparece un número en una lista.
def count_occurrences(numbers, aux):
    if not numbers or not aux:
        return "An item is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    elif not isinstance(aux, int):
        raise TypeError("I only accept the object as a number")
    count = 0
    for i in numbers:
        if i == aux:
            count += 1
    return f"The number {aux} appears {count} times in the list."
print(count_occurrences([1, 89, 5, 45, 2, 3, 1], 1))

# 4- Escribe un programa que busque un elemento en una lista de cadenas.
def search_string_list(strings, aux):
    if not strings or not aux:
        return "An item is empty"
    elif not isinstance(strings, list) or not all(isinstance(i, str) for i in strings):
        raise TypeError("I only accept a list with strings")
    elif not isinstance(aux, str):
        raise TypeError("I only accept the object as a string")
    for i in strings:
        if i == aux:
            return i
    return "I did not find the element"
print(search_string_list(["murcielago", "raton", "perro", "gato"], "raton"))

# 5- Implementa un algoritmo que retorne el primer índice de un elemento en una lista.
def first_index(numbers, aux):
    if not numbers:
        return "The list is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    for i in range(len(numbers)):
        if numbers[i] == aux:
            return f"First index of {aux} is {i}"
    return "Element not found"

print(first_index([1, 89, 5, 45, 2, 3], 3))

# 6- Crea un método que verifique si un elemento existe en una lista.
def exists_in_list(numbers, aux):
    if not numbers or not aux:
        return "An item is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    elif not isinstance(aux, int):
        raise TypeError("I only accept the object as a number")
    for i in numbers:
        if i == aux:
            return True
    return False
print(exists_in_list([1, 89, 5, 45, 2, 3], 1))

# 7- Desarrolla un algoritmo que busque el máximo en una lista utilizando búsqueda lineal.
def max_in_list(numbers):
    if not numbers:
        return "An item is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    max_value = numbers[0]
    for i in numbers:
        if i > max_value:
            max_value = i
    return max_value
print(max_in_list([1, 89, 5, 45, 2, 3]))

# 8- Escribe un programa que imprima todos los índices de un elemento en una lista.
def Index(List_1):
    if not List_1:
        return "An item is empty"
    elif not isinstance(List_1, list):
        raise TypeError("I only accept a list")
    for i in range(0, len(List_1)):
        print(f"Index: {i}")
    
Index([1, 89, 5, 45, 2, 3])
    
# 9- Desarrolla un algoritmo que encuentre el menor número en una lista usando búsqueda lineal.
def Min_Num(numbers):
    if not numbers:
        return "The list is empty"
    elif not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        raise TypeError("I only accept a list with numbers")
    aux = numbers[0]
    for i in range(0, len(numbers)):
        if aux > numbers[i]:
            aux = numbers[i]
    return aux
print(Min_Num([100, 89, 0, 5, 45, 2, 3, 1]))

# 10- Escribe un programa que busque un elemento en una lista de tuplas.
def tuples(numbers, obj):
    if not numbers or not obj:
        return "An item is empty"
    elif not isinstance(numbers, tuple):
        raise TypeError("I only accept Tuples")
    for i in range(0, len(numbers)):
        if  numbers[i] == obj:
            return obj
    return "I did not find the object"

print(tuples((8, 2, "eric", 45, "helen"), 45))

# 11- Implementa un algoritmo que retorne el último índice de un elemento en una lista.
def last_Index(list_2):
    if not list_2:
        return "The list is empty"
    elif not isinstance(list_2, list):
        raise TypeError("I only accept list")
    aux, Index = list_2[-1], 0
    for i in list_2:
        if i != aux:
            Index += 1
        else:
            return f"the last index from the listn is: {Index}"
print(last_Index([5, 1, 6, 7, 8, 9, 22]))

# 12- Crea un método que busque un valor en una lista de diccionarios.
def find_in_diccionaries(dicc, aux):
    if not dicc or aux:
        return "An element is empty"
    elif not isinstance(dicc, list):
        raise TypeError("Error type: only list")
    for datas in dicc:
        if not isinstance(datas, dict):
            raise TypeError("Error type: only dictionaries")
        for value in datas.values():
            if aux == value:
                return value
    return "I did not find the value"
data = [
    {"value1": 5},
    {"value2": 55},
    {"value3": 22},
    {"value4": "eric"},
    {"value5": 5.0},
    {"value6": False}
]
print(find_in_diccionaries(data, 22))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de contactos y permita buscar contactos por nombre.
class Contacts():
    def __init__(self):
        self.storage = {}
        self.name = None
        self.number = None
            
    def add_contact(self, name, number):
        if not name or not number:
            raise TypeError("An item is empty")
        elif not isinstance(name, str) or not isinstance(number, int):
            raise TypeError("ERROR: REMENBER THAT I ONLY ACCEPT NAMES AND NON-NEGATIVE NUMBERS")
        self.storage[name.capitalize()] = number
        print("thank you for save your contact")
    
    def delete_contact(self, name):
        if not self.storage:
            return "the storage empty"
        elif not isinstance(name, str):
            raise TypeError("ERROR: REMENBER THAT I ONLY ACCEPT NAMES")
        else:
            if name.capitalize() in self.storage: # no borra correctamente
                self.storage.pop(name.capitalize())
                return "thank you for use my program, the contact was succesfuly delete"
            return "I did find any contact to delete"
    
    def search_contact(self, name):
        if not name:
            return "there is no name(empty)"
        elif not isinstance(name, str):
            raise type("ERROR: I only accept names")
        if name.capitalize() in self.storage:
            aux = self.storage.get(name.capitalize())
            return aux
        return "I did not find the name"
    
    def update_number(self, name, number):
        if not name or not number:
            return "You miss one or two elements"
        elif not isinstance(name, str) or not isinstance(number, int):
            raise TypeError("ERROR: REMENBER THAT I ONLY ACCEPT NAMES AND NON-NEGATIVE NUMBERS")
        elif name.capitalize() not in self.storage:
            return "the name is not in the storage, i cant update"
        self.storage[name.capitalize()] = number
        return "Thank you for the update"
    
    def list_of_contacts(self):
        if not self.storage:
            return "there anything to see"
        id = 0
        for names, nums in self.storage.items():
            id += 1
            print(f"{id}- Contact name: {names}, Contact number: {nums}")


telefone = Contacts()
telefone.add_contact("eric", 85623645)
telefone.add_contact("helen", 89745286)
telefone.add_contact("Damaris", 85623610)
telefone.add_contact("enrique", 85003645)
print(telefone.search_contact("damaris"))
print(telefone.update_number("carlos", 22223032))
print(telefone.update_number("eric", 22223032))
print(telefone.delete_contact("helen"))
telefone.list_of_contacts()
   
# Crea un simulador de un sistema de inventario que utilice búsqueda lineal para encontrar productos.
class Inventary():
    def __init__(self):
        self.warehouse = []
        self.products = {}
        
    def add_products(self, item, amount):
        if not item or not amount:
            return "One or two item are empty"
        elif not isinstance(item, str) or not isinstance(amount, int):
            raise TypeError("I only accept words in item and numbers in amount")
        aux = self.products[item.capitalize()] = amount
        self.warehouse.append(aux)
    
    def find_products(self, prod):
        if not prod:
            return "Write something"
        elif not self.products:
            return "The warehouse is empty"
        elif not isinstance(prod, str):
            raise TypeError("I only accept words to find something")
        for item, values in self.products.items():
            if prod.capitalize() == item:
                return f"I find the product: {prod} and the amount in storage is: {values}"
        return f"I did not find {prod} in the warehouse"
                
    def see_products(self):
        id = 0
        for name, amount in self.products.items():
            id += 1
            print(f"{id}- The product: {name} with amount of {amount} in storage")
        return "There is nothing to see in the warehouse"
            
    def delete_products(self, prod):
        if not self.products:
            return "the warehuose is empty you cant delete."
        elif not isinstance(prod, str):
            raise TypeError("ERROR: ONLY PHRASES")
        else:
            if prod.capitalize() in self.products.keys():
                self.products.pop(prod.capitalize())
            return f"the element {prod} not in the warehouse so I cant deleted it"
        
                
warehouse = Inventary()
warehouse.add_products("fork", 14)
warehouse.add_products("pen", 4)
warehouse.add_products("table", 8)
warehouse.add_products("paint", 10)
warehouse.add_products("mirror", 22)
print(warehouse.find_products("mirror"))
warehouse.delete_products("pen")
warehouse.see_products()

                
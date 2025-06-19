# Día 58: Búsqueda binaria: teoría y ejemplos

# Teoría: La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada. 
# Divide repetidamente el rango de búsqueda a la mitad hasta encontrar el elemento o determinar que no está presente.

# Tips
# Asegúrate de que la lista esté ordenada antes de aplicar la búsqueda binaria.
# Considera los casos en los que el elemento no se encuentra.

# Buenas Prácticas
# Documenta la lógica del algoritmo y los pasos que sigue.
# Realiza pruebas con listas de diferentes tamaños y contenidos.

def busqueda_binaria(lista, objetivo): # nota ver como ordenar la lista
    """Algoritmo de búsqueda binaria."""
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Retorna el índice del elemento encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Retorna -1 si no se encuentra el elemento

resultado = busqueda_binaria([1, 2, 3, 4, 5], 4)
print("Elemento encontrado en el índice:", resultado)

def Binary_search_avance(elements, obj):
    for i in range(0, len(elements)):
        for j in range(0, len(elements) -i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    left, right = 0, len(elements) -1
    while left <= right:
        aux = (left + right) // 2 # cuando divide la lista en 2
        if elements[aux] == obj:
            return aux
        elif elements[aux] < obj:
            left = aux + 1
        else:
            right = aux - 1
    return "I did not find the object"
print(Binary_search_avance([8, 56, 1, 89, 22, 10], 56))

# Ejercicios
# 1- Implementa la búsqueda binaria en una lista de números enteros ordenados.
def Binary_search_1(elements, obj):
    if len(elements) == 0 or obj is None:
        return "One or both space are empty"
    elif not all(isinstance(x, int) for x in elements) and isinstance(elements, list):
        raise TypeError("I only accept a list with only numbers")
    elif not isinstance(obj, int):
        raise TypeError("The object must be a number")
    else:
        for n in range(0, len(elements) - 1):
            if elements[n] > elements[n + 1]:
                for i in range(0, len(elements)):
                    for j in range(0, len(elements) -i -1):
                        if elements[j] > elements[j + 1]:
                            elements[j], elements[j + 1] = elements[j + 1], elements[j]
            left, right = 0, len(elements) - 1
            while left <= right:
                medium = (left + right) // 2
                if elements[medium] == obj:
                    return medium
                elif elements[medium] < obj:
                    left = medium + 1
                else:
                    right = medium - 1
        return "I did not find number"
print(Binary_search_1([47, 89, 56, 1, 22], 1))
                
# 2- Crea un método que busque un carácter en una cadena ordenada usando búsqueda binaria.
def Character_Binary_search(string, character):
    if string is None or character is None:
        return "One or both space are empty"
    elif not isinstance(string, str) or not isinstance(character, str):
        raise TypeError("I only accept strings")
    else: 
        aux = list(string)
        for x in range(0, len(aux) - 1):
            if string[x] > string[x + 1]:
                for i in range(0, len(aux)):
                    for j in range(0, len(aux) -i -1):
                        if aux[j] > aux[j + 1]:
                            aux[j], aux[j + 1] = aux[j + 1], aux[j]
            else:
                left, right = 0, len(aux) - 1
                while left <= right:
                    medium = (left + right) // 2
                    if aux[medium] == character:
                        return character
                    elif aux[medium] < character:
                        left = medium + 1
                    else:
                        right = medium - 1
        return "I did not find the character"
        
print(Character_Binary_search("erci", "y"))
                
# 3- Desarrolla un algoritmo que busque un número en una lista de floats ordenada.
def Float_Binary_search(elements, obj):
    if len(elements) == 0 or obj is None:
        return "One or both space are empty"
    elif not all(isinstance(x, float) for x in elements) and isinstance(elements, list):
        raise TypeError("I only accept a list with only floats")
    elif not isinstance(obj, float):
        raise TypeError("The object must be a float")
    else:
        for n in range(0, len(elements) - 1):
            if elements[n] > elements[n + 1]:
                for i in range(0, len(elements)):
                    for j in range(0, len(elements) -i -1):
                        if elements[j] > elements[j + 1]:
                            elements[j], elements[j + 1] = elements[j + 1], elements[j]
            left, right = 0, len(elements) - 1
            while left <= right:
                medium = (left + right) // 2
                if elements[medium] == obj:
                    return medium
                elif elements[medium] < obj:
                    left = medium + 1
                else:
                    right = medium - 1
        return "I did not find the number"
print(Float_Binary_search([1.5, 2.3, 4.1, 5.0, 3.7], 3.7))

# 4- Escribe un programa que busque un elemento en una lista de cadenas ordenadas.
def String_Binary_search(elements, obj):
    if len(elements) == 0 or obj is None:
        return "One or both space are empty"
    elif not all(isinstance(x, str) for x in elements) and isinstance(elements, list):
        raise TypeError("I only accept a list with only strings")
    elif not isinstance(obj, str):
        raise TypeError("The object must be a string")
    else:
        for n in range(0, len(elements) - 1):
            if elements[n] > elements[n + 1]: # nota no esta verificando bien, hay que ver porque no ordena
                for i in range(0, len(elements)):
                    for j in range(0, len(elements) -i -1): 
                        if elements[j] > elements[j + 1]:
                            elements[j], elements[j + 1] = elements[j + 1], elements[j]
            else:
                left, right = 0, len(elements) - 1
                while left <= right:
                    medium = (left + right) // 2
                    if elements[medium] == obj:
                        return medium
                    elif elements[medium] < obj:
                        left = medium + 1
                    else:
                        right = medium - 1
        return "I did not find the string"
print(String_Binary_search(["cherry", "date", "apple", "banana"], "cherry"))

# 5- Implementa un algoritmo que retorne el primer índice de un elemento en una lista ordenada.
def First_Index(element, obj):
    if len(element) == 0:
        return "the list is empty"
    elif not isinstance(element, list):
        raise TypeError("I only accept a list")
    aux = sorted(element)
    left, right = 0, len(element) - 1
    while left <= right:
        medium = (left + right) // 2
        if element[medium] == obj:
            return element[medium][0]
        elif element[medium] < obj:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the object"
        
print(First_Index(["cherry", "date", "apple", "banana"], "cherry"))
    
# 6- Crea un método que verifique si un elemento existe en una lista ordenada.
def Existing_element(elements, element):
    for i in range(0, len(elements) - 1):
        if elements[i] > elements[i + 1]:
            aux = sorted(elements)
        left, right = 0, len(aux) - 1
        while left <= right:
            medium = (left + right) // 2
            if aux[medium] == element:
                return True
            elif aux[medium] < element:
                left = medium + 1
            else:
                right = medium - 1
        return False
print(Existing_element([78, 45, 63, 45, 10], 22))

# 7- Desarrolla un algoritmo que encuentre el máximo en una lista ordenada usando búsqueda binaria.
def Max_of_list(numbers):
    number = sorted(numbers)
    left, right = 0, len(number) - 1
    while left < right:
        medium = (left + right) // 2
        if number[medium] < number[right]:
            left = medium + 1
        else:
            right = medium
    return number[right]
print(Max_of_list([5, 69, 1000, 23, 47, 1, 100]))

def Min_of_list(numbers):
    numbers.sort()
    left, right = 0, len(numbers) - 1
    while left < right:
        medium = (left + right) // 2 # para que cuando llegue al centro de la lista se detenga
        if numbers[medium] > numbers[right]:
            left = medium + 1
        else:
            right = medium - 1
    return numbers[right]
print(Min_of_list([5, 69, 1000, 23, 47, 1, 0,  100]))
        
# 8- Escribe un programa que busque un elemento en una lista ordenada de objetos.
def Sort_Binary_Search(elements, element):
    elements.sort() 
    left, right = 0, len(elements) -1
    while left <= right: 
        medium = (left + right) // 2
        if elements[medium] == element:
            return element
        elif elements[medium] < element:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the element"
print(Sort_Binary_Search([5, 89, 23, 4], 23))

# 9- Implementa un algoritmo que busque un número en una lista ordenada y retorne el número de comparaciones realizadas.
def Binary_search_3(lists, number):
    count = 1
    lists.sort()
    left, right = 0, len(lists) - 1
    while left <= right:
        count += 1
        medium = (left + right) // 2
        if lists[medium] == number:
            return count
        elif lists[medium] < number:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the number"
print(Binary_search_3([5, 89, 23, 4], 89))

# 10- Crea un método que busque un valor con busqueda binaria en una lista ordenada de diccionarios.
def Binary_search_4(elements, key, value):
    if not isinstance(elements, list) or not all(isinstance(x, dict) for x in elements):
        raise TypeError("I only accept a list of dictionaries")
    if not isinstance(key, str):
        raise TypeError("The key must be a string")
    
    elements.sort(key=lambda x: x.get(key, float('inf')))  # Ordena la lista de diccionarios por el valor de la clave
    left, right = 0, len(elements) - 1
    
    while left <= right:
        medium = (left + right) // 2
        if elements[medium].get(key) == value:
            return elements[medium]  # Retorna el diccionario encontrado
        elif elements[medium].get(key) < value:
            left = medium + 1
        else:
            right = medium - 1
            
    return "I did not find the dictionary"
print(Binary_search_4([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}], "age", 35))

# 11- Desarrolla un algoritmo que encuentre el índice del elemento más cercano a un valor dado en una lista ordenada.
def Near_Index(datas, obj):
    datas.sort()
    left, right = 0, len(datas) - 1
    while left <= right:
        medium = (left + right) // 2
        if datas[medium] == obj:
            return medium - 1, medium + 1     
        elif datas[medium] < obj:
            left = medium + 1
        else:
            right = medium - 1
    return -1
print(Near_Index([89, 45, 1, 22, 96, 2], 45))

# 12- Escribe un programa que busque un número en una lista ordenada y retorne el número de elementos que le preceden.
def Preceding_elements(elements, number):
    if not isinstance(elements, list) or not all(isinstance(x, int) for x in elements):
        raise TypeError("I only accept a list of integers")
    elif not isinstance(number, int):
        raise TypeError("The number must be an integer")
    elements.sort()
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == number:
            return medium  # Retorna el número de elementos que le preceden
        elif elements[medium] < number:
            left = medium + 1
        else:
            right = medium - 1
    return -1  
print(Preceding_elements([5, 89, 23, 4], 89))

# 13- Implementa un algoritmo que busque una subcadena en una lista de cadenas ordenadas.
elements = ["eric", "hernandez", "calvin"]
def Search_substring(elements, substring):
    if len(elements) == 0:
        return "the list is empty"
    elif substring is None:
        return "The user space is empty"
    elif len(substring) > 3:
        return "I only accept the firts three letters from the string"
    elements.sort()
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium][:3] == substring:
            return elements[medium]
        elif elements[medium][:3] < substring:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the string"

print(Search_substring(["eric", "hernandez", "calvin"], "cal"))

# 14- Crea un método que busque un elemento en una lista ordenada y retorne el valor anterior.
def Previuos_Value(elements, Value):
    if  len(elements) == 0:
        return "the list is empty"
    elif Value is None:
        return "Please put a value"
    elements.sort()
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return elements[medium - 1]
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the Value"

print(Previuos_Value([89, 45, 2, 56, 1, 3, 10], 10))

# 15- Desarrolla un algoritmo que busque un elemento en una lista de floats ordenada y retorne su índice o -1.
def Find_Floats(list_Floats, Value):
    if len(list_Floats) == 0:
        return "the list is empty"
    elif not isinstance(list_Floats, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, float) for i in list_Floats):
        raise TypeError("I Only accept floats in the list")
    elif Value is None:
        return "I need a value to find"
    list_Floats.sort()
    left, right = 0, len(list_Floats) - 1
    while left <= right:
        medium = (left + right) // 2
        if list_Floats[medium] == Value:
            return medium
        elif list_Floats[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return -1
print(Find_Floats([2.5, 1.0, 56.2, 10.5, 100.1, 93.2, 23.0], 23.0))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de contactos ordenados y permita buscar contactos por nombre.
class ListContacts:
    def __init__(self):
        self.contacts = []
        
    def Empty(self):
        return len(self.contacts) == 0

    def add_contact(self, name, phone):
        if not isinstance(name, str) or not isinstance(phone, str):
            raise TypeError("Both name and phone must be text")
        elif not name or not phone:
            raise ValueError("Name and phone cannot be empty")
        self.contacts.append({"name": name, "phone": phone})
        self.contacts.sort(key=lambda x: x["name"])  # Ordena por nombre

    def search_contact(self, name):
        if self.Empty():
            return "The contact list is empty"
        left, right = 0, len(self.contacts) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.contacts[medium]["name"] == name:
                return self.contacts[medium] 
            elif self.contacts[medium]["name"] < name:
                left = medium + 1
            else:
                right = medium - 1
        return "Contact not found"
    
    def Erase_contact(self, name):
        if self.Empty():
            return "The contact list is empty"
        elif not isinstance(name, str):
            raise TypeError("The name must be a text")
        elif not name:
            raise ValueError("The name cannot be empty")
        for i in range(len(self.contacts)):
            if self.contacts[i]["name"] == name:
                del self.contacts[i]
                return f"Contact {name} has been deleted"
        return "Contact not found"
    
    def show_contacts(self):
        if self.Empty():
            return "The contact list is empty"
        count = 1
        for contact in self.contacts:
            print(f"Contact {count}: Name: {contact['name']}, Phone: {contact['phone']}")
            count += 1
            
Phonebook = ListContacts()
Phonebook.add_contact("Alice", "123-456-7890")
Phonebook.add_contact("Bob", "987-654-3210")
Phonebook.add_contact("Charlie", "555-555-5555")
print(Phonebook.search_contact("Bob"))

# Crea un simulador de un sistema de búsqueda de productos en una tienda utilizando búsqueda binaria.
class Warhouse:
    def __init__(self):
        self.products = []
        
    def Empty(self):
        return len(self.products) == 0
    
    def add_product(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            raise TypeError("Name must be a string and price must be a number")
        elif not name or price < 0:
            raise ValueError("Name cannot be empty and price must be non-negative")
        self.products.append({"name": name, "price": price})
        self.products.sort(key=lambda x: x["name"])  # Ordena por nombre

    def search_product(self, name):
        if self.Empty():
            return "The product list is empty"
        left, right = 0, len(self.products) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.products[medium]["name"] == name:
                return self.products[medium]
            elif self.products[medium]["name"] < name:
                left = medium + 1
            else:
                right = medium - 1
        return "Product not found"
    
    def show_products(self):
        if self.Empty():
            return "The product list is empty"
        count = 1
        for product in self.products:
            print(f"Product {count}: Name: {product['name']}, Price: {product['price']}")
            count += 1
            
Warehouses = Warhouse()
Warehouses.add_product("Laptop", 999.99)
Warehouses.add_product("Smartphone", 499.99)
Warehouses.add_product("Tablet", 299.99)
print(Warehouses.search_product("Smartphone"))

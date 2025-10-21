# Día 86

# Ejercicio 427: Implementa una función que verifique si un número es un número de Armstrong.
# Conceptos: Matemáticas, funciones.
def Amstrong(numbers):
    aux = [n for n in str(numbers)]
    aux1 = 0
    for n in str(numbers):
        aux1 += int(n) ** len(aux)
    return aux1 == numbers
print(Amstrong(153))
       

# Ejercicio 428: Escribe un programa que genere un archivo de texto con una lista de direcciones de correo electrónico.
# Conceptos: Manejo de archivos.
def generate_email_file(emails, filename="emails.txt"):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')

data = ["Calle bronce 123", "Avenida siempre viva 742", "Calle falsa 123", "Calle luna 456", "Avenida sol 789", "Calle y ruta 32"]
generate_email_file(data)



# Día 87

# Ejercicio 432: Implementa una función que encuentre el número de elementos en una lista que son mayores que un valor dado.
# Conceptos: Listas, funciones.
def Bigger_Than(elements, value):
    if not isinstance(elements, (list, tuple)):
        raise TypeError("I need a list of elements")
    if not all(isinstance(n, (int, float)) for n in elements):
        raise TypeError("All the elements in the list must be integers")
    if not isinstance(value, (int, float)):
        raise TypeError("The value must be a number")
    if len(elements) <= 1:
        return 0
    return sum([1 for n in elements if n > value])
print(Bigger_Than([89, 11, 2, 5, 14.0, 3, 9, 4], 10))

# Ejercicio 433: Escribe un programa que lea un archivo de texto y busque líneas que contengan una frase específica.
# Conceptos: Manejo de archivos.
def search_phrase_in_file(filename, phrase):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            matching_lines = [line.strip() for line in lines if phrase in line]
            return matching_lines
    except FileNotFoundError:
        return f"The file {filename} does not exist."
print(search_phrase_in_file("emails.txt", "Calle"))

# Ejercicio 434: Crea una función que reciba una lista y devuelva la lista de números pares.
# Conceptos: Listas, funciones.
def Even_numbers(elements):
    if not isinstance(elements, (list, tuple)):
        raise TypeError("I need a list of elements")
    if not all(isinstance(n, int) for n in elements):
        raise TypeError("All the elements in the list must be integers")
    if len(elements) <= 1:
        return []
    return [n for n in elements if n % 2 == 0]
print(Even_numbers([89, 11, 2, 5, 14, 3, 9, 4]))


# Día 88

# Ejercicio 437: Implementa una función que verifique si una cadena es un palíndromo.
# Conceptos: Manipulación de strings.
def Palindrome(word):
    import re
    if not word:
        return "The text is empty, please insert a word"
    elif not isinstance(word, str):
        raise TypeError("The word or phrase must be a word only")
    else:
        clean = re.sub(r"[^A-Za-z]", "", word)
        return clean == clean[::-1]
print(Palindrome("amo la páloma8,"))

# Ejercicio 439: Crea una función que reciba una lista de números y devuelva la lista de números negativos.
# Conceptos: Listas, funciones.
def Negative_Nums(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept list")
    else:
        aux = [n for n in elements if n < 1]
        return aux

import random
data = [random.randint(-50, 100) for n in range(10)]
print(Negative_Nums(data))

# Ejercicio 440: Escribe un programa que implemente un sistema de gestión de clientes.
# Conceptos: POO, listas.
class Client:
    def __init__(self):
        self.clients = []
        
    def Sort_clients(self, elements=None):
        if elements is None:
            elements = self.clients
        if len(elements) <= 1:
            return elements
        pivot = elements[len(elements) // 2].capitalize()
        left = [x for x in elements if x.capitalize() < pivot]
        middle = [x for x in elements if x.capitalize() == pivot]
        right = [x for x in elements if x.capitalize() > pivot]
        return self.Sort_clients(left) + middle + self.Sort_clients(right)
        
    def Add_client(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        self.clients.append(name)
        self.clients = self.Sort_clients()
        return f"Client {name} added successfully"
    
    def Remove_client(self, name):
        if name in self.clients:
            self.clients.remove(name)
            self.clients = self.Sort_clients()
            return f"Client {name} removed successfully"
        else:
            return f"Client {name} not found"
        
    def View_clients(self):
        if len(self.clients) == 0:
            return "The client list is empty"
        for id, name in enumerate(self.clients, start=1):
            print(f"{id}. {name}")            
            
client_manager = Client()
print(client_manager.Add_client("Alice"))
print(client_manager.Add_client("Bob"))
client_manager.View_clients()
print(client_manager.Remove_client("Alice"))
client_manager.View_clients()

            
# Día 89

# Ejercicio 442: Implementa una función que calcule la suma de los dígitos de un número.
# Conceptos: Matemáticas, funciones. 
def Sum_of_digits(num):
    if not num:
        return "The element is empty"
    elif not isinstance(num, int):
        raise TypeError("The num must be a number")
    aux = sum([int(n) for n in str(num)])
    return aux
print(Sum_of_digits(12))


# Ejercicio 444: Crea una función que reciba una cadena y devuelva la misma cadena en formato "PascalCase".
# Conceptos: Manipulación de strings. 
def PascalCase(word):
    import re
    aux = ""
    for words in word.split():
        clean = re.sub(r"[^A-Za-z]", "", words.capitalize())
        aux += clean
    return aux
print(PascalCase("product price8,")) 

# Ejercicio 445: Escribe un programa que implemente un sistema de gestión de proyectos.
# Conceptos: POO, listas.
class Project:
    def __init__(self):
        self.projects = []
        
    def Sort_projects(self, pro = None):
        if pro is None:
            pro = self.projects
        if len(pro) <= 1:
            return pro
        pivot = pro[len(pro) // 2].capitalize()
        left = [x for x in pro if x.capitalize() < pivot]
        middle = [x for x in pro if x.capitalize() == pivot]
        right = [x for x in pro if x.capitalize() > pivot]
        sorted_list = self.Sort_projects(left) + middle + self.Sort_projects(right)
        if pro is self.projects:
            self.projects = sorted_list
        return sorted_list
        
    def Add_project(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        self.projects.append(name)
        self.projects = self.Sort_projects()
        return f"Project {name} added successfully"
    
    def Remove_project(self, name):
        if name in self.projects:
            self.projects.remove(name)
            self.projects = self.Sort_projects()
            return f"Project {name} removed successfully"
        else:
            return f"Project {name} not found"
        
    def View_projects(self):
        if len(self.projects) == 0:
            return "The project list is empty"
        for id, name in enumerate(self.projects, start=1):
            print(f"{id}. {name}")
            
project_manager = Project()
print(project_manager.Add_project("Website Redesign"))
print(project_manager.Add_project("Mobile App Development"))
project_manager.View_projects()
print(project_manager.Remove_project("Website Redesign"))
project_manager.View_projects()


# Día 90

# Ejercicio 447: Implementa una función que verifique si un número es un número perfecto.
# Conceptos: Matemáticas, funciones.
def Perfect_number(num):
    if not num:
        return "The num is empty"
    elif not isinstance(num, int):
        raise TypeError("I need a number")
    aux = sum([n for n in range(1, num) if num % n == 0])
    return aux == num
print(Perfect_number(28))

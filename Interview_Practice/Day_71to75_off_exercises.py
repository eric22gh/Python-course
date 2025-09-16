# Día 71

# Ejercicio 351: Crea una clase Cuenta con métodos para depositar y retirar dinero, y un método para mostrar el saldo.
# Conceptos: POO.
class Account:
    def __init__(self):
        self.amount = 0
        
    def AddFunds(self, aux):
        self.amount += aux
        return "You Sucessfuly add funds to your account"
    
    def WithdrawFunds(self, aux):
        if aux > self.amount:
            return f"You dont have the amount of: {aux} is your account"
        self.amount -= aux
        return "You Sucessfuly Withdraw funds in your account"
    
    def Funds(self):
        if self.amount == 0:
            return "You do not have funds in your account"
        return self.amount
    
menu = Account()
menu.AddFunds(50)
menu.AddFunds(500)
menu.AddFunds(5)
menu.AddFunds(35)
print(menu.Funds())
print(menu.WithdrawFunds(100))
print(menu.Funds())

# Ejercicio 352: Implementa una función que encuentre el número de caracteres únicos en una cadena.
# Conceptos: Manipulación de strings.
def UniqueCharacters(element):
    lux = {}
    for letters in element:
        if letters in lux:
            lux[letters] += 1
        else:
            lux[letters] = 1
    
    unique = []
    for key, values in lux.items():
        if values == 1:
            unique.append(key)
    return unique
                 
print(UniqueCharacters("eric e e i"))

# Ejercicio 353: Escribe un programa que lea un archivo de texto y cuente la cantidad de líneas.
# Conceptos: Manejo de archivos.
def CountLines(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        return "The file does not exist"
print(CountLines('test.txt'))

# Ejercicio 354: Crea una función que reciba una lista de números y devuelva la lista de números pares.
# Conceptos: Listas, funciones.
def EvenNumbers(elements):
    aux = [n for n in elements if n % 2 == 0]
    return aux
print(EvenNumbers([22, 10, 56, 2, 11, 16, 100, 32]))

# Ejercicio 355: Escribe un programa que implemente un sistema de gestión de tareas con prioridades.
# Conceptos: POO, listas.
class Task:
    def __init__(self):
        self.tasks = []
        
    def Is_Empty(self):
        if len(self.tasks) == 0:
            return "The task list is empty"
        
    def Add_Task(self, name, priority):
        self.tasks.append((name, priority))
        self.tasks.sort(key=lambda x: x[1]) 
        return "Task added successfully"
    
    def Show_Tasks(self):
        if len(self.tasks) == 0:
            return "The task list is empty"
        for num, task in enumerate(self.tasks, start=1):
            print(f"{num}. Task: {task[0]}, Priority: {task[1]}")
    
    def Remove_Task(self, name):
        for task in self.tasks:
            if task[0] == name:
                self.tasks.remove(task)
                return "Task removed successfully"
        return "Task not found"
menu = Task()
print(menu.Add_Task("Do the laundry", 2))
print(menu.Add_Task("Clean the house", 1))  
print(menu.Add_Task("Pay the bills", 3))
menu.Show_Tasks()
print(menu.Remove_Task("Clean the house"))
menu.Show_Tasks()


# Día 72
# Ejercicio 356: Crea una clase Estudiante con atributos nombre, edad y calificaciones. Agrega un método que calcule el promedio de calificaciones.
# Conceptos: POO.
class Estudiante:
    def __init__(self):
        self.averague = []
        
    def add(self, name, age, notes):
        self.averague.append((name, age, notes))
        
    def avergue_notes(self):
        aux = 0
        sux = []
        for note in self.averague:
            aux += note[2]
            sux.append(note[2]) # por si hay una nota faltante
        return aux/len(sux)
    
menu = Estudiante()
menu.add("eric", 22, 85)
menu.add("helen", 21, 75)
menu.add("carlos", 12, 65)
menu.add("calvin", 28, 95)
print(menu.avergue_notes())

# Ejercicio 357: Implementa una función que verifique si una cadena es un anagrama de otra.
# Conceptos: Manipulación de strings.
def Anagram(word1, word2):
    import re
    aux1 = re.sub(r"[^a-zA-Z]", "", word1)
    aux2 = re.sub(r"[^a-zA-Z]", "", word2)
    return sorted(aux2) == sorted(aux1)
print(Anagram("amor8", "8roma"))

# Ejercicio 358: Escribe un programa que genere un archivo de texto con números aleatorios.
# Conceptos: Manejo de archivos, números aleatorios.
def RandomNumbers(file, n):
    import random
    with open(file, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(1, 100)}\n")
    return "File created successfully"
print(RandomNumbers('random_numbers.txt', 10))

# Ejercicio 359: Crea una función que reciba una lista y devuelva el segundo elemento más grande.
# Conceptos: Listas, funciones.
def Second(elements):
    aux = sorted(elements)
    return aux[::-1][1]
print(Second([56, 10, 56, 1, 89, 100]))



# Día 73
# Ejercicio 361: Crea una clase Juego que tenga métodos para iniciar, jugar y finalizar el juego.
# Conceptos: POO.
class Game:
    def __init__(self):
        self.state = "Not started"
        
    def Start(self):
        self.state = "In progress"
        return "Game started"
    
    def Play(self):
        if self.state != "In progress":
            return "You need to start the game first"
        return "Playing the game..."
    
    def End(self):
        if self.state != "In progress":
            return "You need to start the game first"
        self.state = "Finished"
        return "Game ended"
menu = Game()
print(menu.Start())
print(menu.Play())
print(menu.End())
print(menu.Play())

# Ejercicio 363: Escribe un programa que lea un archivo de texto y busque una palabra específica.
# Conceptos: Manejo de archivos, búsqueda.
def SearchWord(file, word):
    try:
        with open(file, 'r') as f:
            content = f.read()
            if word in content:
                return f"The word '{word}' was found in the file"
            else:
                return f"The word '{word}' was not found in the file"
    except FileNotFoundError:
        return "The file does not exist"
print(SearchWord('test.txt', 'hello'))

# Ejercicio 364: Crea una función que reciba una lista de palabras y devuelva la palabra más corta.
# Conceptos: Listas, funciones.
def ShortestWord(elements):
    aux = sorted(elements, key=len) # el key=len ordena por la longitud de la palabra
    return aux[0]
print(ShortestWord(["elephant", "cats", "hippopotamus", "dogs", "ant"]))


# Día 74

# Ejercicio 367: Implementa una función que verifique si un número es primo.
# Conceptos: Matemáticas, funciones.
def IsPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(IsPrime(29))

# Ejercicio 368: Escribe un programa que genere un reporte en formato CSV a partir de datos ingresados.
# Conceptos: Manejo de archivos, CSV.
def GenerateCSV(file, data):
    import csv
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])  # Header
        writer.writerows(data)
    return "CSV file created successfully"
data = [("Alice", 30, "New York"), ("Bob", 25, "Los Angeles"), ("Charlie", 35, "Chicago")]
print(GenerateCSV('report.csv', data))

# Ejercicio 369: Crea una función que reciba una cadena y devuelva la misma cadena en formato "snake_case".
# Conceptos: Manipulación de strings.
def ToSnakeCase(text):
    import re
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    text = re.sub(r'[^a-z0-9_]', '_', text)  # Reemplaza caracteres no alfanuméricos con guiones bajos
    text = re.sub(r'__+', '_', text)  # Reemplaza múltiples guiones bajos con uno solo
    return text.strip('_')  # Elimina guiones bajos al inicio y al final
print(ToSnakeCase("HelloWorld Example-Test"))


# Día 75

# Ejercicio 372: Implementa una función que calcule la distancia entre dos puntos en un plano.
# Conceptos: Matemáticas, funciones.
def Distance(point1, point2):
    import math
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(Distance((1, 2), (4, 6)))

# Ejercicio 373: Escribe un programa que lea un archivo JSON y lo convierta en un objeto Python.
# Conceptos: Manejo de archivos, JSON.
def ReadJSON(file):
    import json
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return "The file does not exist"
print(ReadJSON('data.json'))

# Ejercicio 374: Crea una función que reciba una lista y devuelva la lista de números impares.
# Conceptos: Listas, funciones.
def OddNumbers(elements):
    aux = [n for n in elements if n % 2 != 0]
    return aux
print(OddNumbers([22, 10, 56, 2, 11, 16, 100, 32, 33, 55, 77]))

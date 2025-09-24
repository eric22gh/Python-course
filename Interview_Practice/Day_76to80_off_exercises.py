# Día 76


# Ejercicio 377: Implementa una función que calcule el área de un trapecio.
# Conceptos: Matemáticas, funciones. # formula (base 1 +  base 2) / 2 x altura
def Trapeze(base1, base2, height):
    try:
        Area =  (base1 + base2) / 2 * height
        return f"The area from the Trapeze is: {Area:.0f}cm"
    except TypeError:
        return "Error: Please, enter only numbers"
    
print(Trapeze(10, 6, 3))

# Ejercicio 378: Escribe un programa que genere un gráfico de líneas a partir de datos ingresados por el usuario.
# Conceptos: Visualización de datos (puedes usar matplotlib).
import matplotlib.pyplot as plt
def Line_Graph(x, y):
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph from User Data')
    plt.grid(True)
    plt.show()
Line_Graph([1, 2, 3, 4, 5], [2, 3, 5, 7, 11])

# Ejercicio 379: Crea una función que reciba una cadena y devuelva la misma cadena en formato "kebab-case".
# Conceptos: Manipulación de strings.
def kebab_case(word):
    import re
    aux = word.strip().replace(" ", "-")
    return re.sub(r"[0-9]", "",aux).lower()
print(kebab_case(" Eri100c Hern0andez Edwards88 "))


# Día 77
# Ejercicio 381: Crea una clase Profesor con atributos nombre y materia. Agrega un método que retorne la información del profesor.
# Conceptos: POO.
class Profesor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
    def Info(self):
        if not isinstance(self.name, str) or not isinstance(self.subject, str):
            raise TypeError("Error: Please, enter only Text")
        return self.name, self.subject
    
menu = Profesor("Carlos Cascante","Math")   
print(menu.Info())

# Ejercicio 382: Implementa una función que encuentre el factorial de un número de forma iterativa.
# Conceptos: Matemáticas, funciones.
def factorial(n):
    if n <= 1:
        return 1
    aux = 1
    for i in range(2, n + 1):
        aux *= i
    return aux
print(factorial(5))

# Ejercicio 384: Crea una función que reciba una lista de números y devuelva la lista de números negativos.
# Conceptos: Listas, funciones.
def NegativeNUms(data):
    return [n for n in data if n < 0]
import random
nums = [random.randint(-50, 50) for x in range(10)]
print(NegativeNUms(nums))

# Ejercicio 385: Escribe un programa que implemente un sistema de gestión de tareas pendientes.
# Conceptos: POO, listas.
class Task:
    def __init__(self):
        self.tasks = []
    
    def Is_Empty(self):
        return len(self.tasks) == 0
    
    def Sort_Tasks(self):
        if self.Is_Empty():
            return "I can't sort an empty list"
        return self.tasks.sort()
    
    
    def Add_Task(self, task):
        self.tasks.append(task)
        self.Sort_Tasks()
        return f"The task '{task}' has been added"
    
    def Remove_Task(self, task):
        if self.Is_Empty():
            return "I can't remove from an empty list"
        if task in self.tasks:
            self.tasks.remove(task)
            return f"The task '{task}' has been removed"
        return f"The task '{task}' is not in the list"
    
    def View_Tasks(self):
        if self.Is_Empty():
            return "The task list is empty"
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
            
    def Search_Task(self, task):
        if self.Is_Empty():
            return "I can't search in an empty list"
       # binary search
        left = 0
        right = len(self.tasks) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.tasks[medium] == task:
                return f"the task '{task}' is in the list"
            elif self.tasks[medium] < task:
                left = medium + 1
            else:
                right = medium - 1
        return f"the task '{task}' is not in the list"
    
menu_task = Task()
print(menu_task.Add_Task("Do the laundry"))
print(menu_task.Add_Task("Clean the house"))
print(menu_task.Add_Task("Buy groceries"))
menu_task.View_Tasks()
print(menu_task.Search_Task("Clean the house"))
print(menu_task.Remove_Task("Buy groceries"))
menu_task.View_Tasks()          


# Día 78

# Ejercicio 387: Implementa una función que verifique si una cadena es un palíndromo ignorando espacios y mayúsculas.
# Conceptos: Manipulación de strings.
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
print(is_palindrome("Amo la paloma"))


# Ejercicio 388: Escribe un programa que genere un archivo de texto con una lista de números aleatorios.
# Conceptos: Manejo de archivos, números aleatorios.
import random
def generate_random_numbers_file(filename, count, lower, upper):
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(lower, upper)
            file.write(f"{number}\n")
    return f"File '{filename}' with {count} random numbers created."
print(generate_random_numbers_file("random_numbers.txt", 10, 1, 100))

# Ejercicio 389: Crea una función que reciba una lista y devuelva la suma de sus elementos.
# Conceptos: Listas, funciones.
def sum_list(data):
    return sum(data)
import random
nums = [random.randint(1, 100) for x in range(10)]
print(sum_list(nums))


# Día 79
# Ejercicio 391: Crea una clase Producto con métodos para calcular el descuento y el precio final.
# Conceptos: POO.
class Product:
    def __init__(self, product, price, discount):
        if not isinstance(product, str):
            raise TypeError("On product I need a text")
        elif not isinstance(price, int):
            raise TypeError("On price I need a numbers")
        elif not isinstance(discount, int):
            raise TypeError("On discount I need a numbers")
        self.product = product
        self.price = price
        self.discount = discount
        
    def Final_Price(self):
        aux = self.price * self.discount / 100
        return self.price - aux
    
prod = Product("Window", 2500, 10)
print(prod.Final_Price())
    

# Ejercicio 392: Implementa una función que calcule la raíz cuadrada de un número.
# Conceptos: Matemáticas, funciones.
def SquareRoot(num):
    import math
    if not isinstance(num, int):
        raise TypeError("I only accept numbers")
    elif num == 1:
        return 1
    elif num < 1:
        return "Error I dont accept negative numbers"
    return math.sqrt(num)
print(SquareRoot(-18))

# Ejercicio 393: Escribe un programa que lea un archivo CSV y lo imprima en formato tabla.
# Conceptos: Manejo de archivos, CSV.
def read_csv_as_table(filename):
    import csv
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
print(read_csv_as_table("data.csv"))


# Día 80
# Ejercicio 396: Crea una clase Empleado con métodos para calcular el salario después de impuestos.
# Conceptos: POO.
class Employee:
    def __init__(self, name, salary, tax_rate):
        if not isinstance(name, str):
            raise TypeError("On name I need a text")
        elif not isinstance(salary, int):
            raise TypeError("On salary I need a numbers")
        elif not isinstance(tax_rate, int):
            raise TypeError("On tax_rate I need a numbers")
        self.name = name
        self.salary = salary
        self.tax_rate = tax_rate
        
    def Salary_After_Tax(self):
        aux = self.salary * self.tax_rate / 100
        return self.salary - aux
emp = Employee("Ana Gomez", 3000, 15)
print(emp.Salary_After_Tax())

# Ejercicio 397: Implementa una función que encuentre el número más grande en una lista.
# Conceptos: Listas, funciones. # nota: intentarlo con busqueda binaria
def max_in_list(data):
    if not data:
        return "Error: The list is empty"
    max_num = data[0]
    for num in data:
        if num > max_num:
            max_num = num
    return max_num
import random
nums = [random.randint(1, 100) for x in range(10)]
print(max_in_list(nums))

# Ejercicio 398: Escribe un programa que genere un archivo de texto con la fecha y hora actual.
# Conceptos: Manejo de archivos, fechas.
def generate_datetime_file(filename):
    from datetime import datetime
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'w') as file:
        file.write(f"Current date and time: {formatted_date}\n")
    return f"File '{filename}' with current date and time created."
print(generate_datetime_file("current_datetime.txt"))

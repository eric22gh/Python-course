# Día 61

# Ejercicio 301: Crea una clase Persona con atributos nombre y edad. Implementa un método que imprima la información de la persona.
# Conceptos: Programación orientada a objetos (POO).
class Person:
    def __init__(self):
       pass
        
    def Information(self, name, age):
        return f"Hello I am {name} and I am {age} years old"
    
data = Person()
print(data.Information("eric", 32))
print(data.Information("ericka", 20))
print(data.Information("Helen", 30))
print(data.Information("carlos", 53))

# Ejercicio 302: Crea una función que reciba una lista de números y devuelva la mediana.
# Conceptos: Estadísticas, listas.
# La mediana de una lista de números es el valor que se encuentra justo en el medio cuando los datos están ordenados de menor a mayor.

def mediumList(elements):
    elements.sort()
    if not elements:
        return -1
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif len(elements) % 2 == 0:
        aux = int(len(elements) / 2)
        aux2 = (aux + 1)
        return (aux + aux2) / 2
    else:
        index = int(len(elements) / 2)
        return(elements[index])

print(mediumList([1, 2, 3, 4]))

# Ejercicio 303: Implementa un decorador que mida el tiempo de ejecución de una función.
# Conceptos: Decoradores.
def time_decorator(func):
    import time
    def wrapper(elements):
        start_time = time.time()
        aux = 0
        for i in elements:
            aux += i # incompleto, ocupo un mini curso de decorasdores
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return func(elements)
    return wrapper

import random
print(time_decorator([random.randint(1, 100) for _ in range(100000)]))

# Ejercicio 304: Crea una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada carácter.
# Conceptos: Manipulación de strings, diccionarios.
def frequency_characters(string):
    if not isinstance(string, str):
        raise TypeError("I need a string")
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(frequency_characters("hello world"))

# Ejercicio 305: Escribe un programa que implemente la búsqueda binaria en una lista ordenada.
# Conceptos: Algoritmos, listas.
def BinarySearch(elements, obj):
    elements.sort()
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == obj:
            return elements[medium]
        elif elements[medium] < obj:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the number"
print(BinarySearch([10, 22, 36, 1, 22, 33], 33))


# Día 62
# Ejercicio 306: Crea una clase Rectángulo con métodos para calcular el área y el perímetro.
# Conceptos: POO, geometría.
class Rectangle:
    def __init__(self, width, height):
        if not width or not height:
            raise ValueError("Width and height must be greater than zero or the space is empty")
        self.width = width
        self.height = height
        
    def area(self):
        if not isinstance(self.width, (int, float)) or not isinstance(self.height, (int, float)):
            raise TypeError("Width and height must be numbers")
        return self.width * self.height
    
    def perimeter(self):
        if not isinstance(self.width, (int, float)) or not isinstance(self.height, (int, float)):
            raise TypeError("Width and height must be numbers")
        return 2 * (self.width + self.height)
    
rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

# Ejercicio 307: Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinarlo.
# Conceptos: Números aleatorios, bucles.
import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            if attempts >= 10:
                print("Has agotado tus intentos. El número era:", number_to_guess)
                break
            guess = int(input("Adivina el número entre 1 y 100: "))
            attempts += 1
            if guess < number_to_guess:
                print("Demasiado bajo. Inténtalo de nuevo.")
            elif guess > number_to_guess:
                print("Demasiado alto. Inténtalo de nuevo.")
            else:
                print(f"¡Correcto! El número era {number_to_guess}. Lo adivinaste en {attempts} intentos.")
                break
        except KeyboardInterrupt:
            print("\nJuego terminado por el usuario.")
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
guess_number()


# Ejercicio 308: Implementa un sistema de gestión de estudiantes utilizando clases.
# Conceptos: POO, listas.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class StudentManagement:
    def __init__(self):
        self.students = []
        
    def Is_empty(self):
        return len(self.students) == 0
    
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("I need a Student object")
        self.students.append(student)
        
    def list_students(self):
        if self.Is_empty():
            print("No hay estudiantes registrados.")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}")
            
    def remove_student(self, name):
        if self.Is_empty():
            print("No hay estudiantes registrados.")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Estudiante {name} eliminado.")
        else:
            print(f"No se encontró al estudiante {name}.")
            
student_management = StudentManagement()
student_management.add_student(Student("Alice", 20))
student_management.add_student(Student("Bob", 22))
student_management.list_students()

# Ejercicio 309: Crea una función que reciba una lista y devuelva una nueva lista con los elementos duplicados eliminados.
# Conceptos: Listas, funciones.
def remove_duplicates(elements):
    if not isinstance(elements, list):
        raise TypeError("I need a list")
    return list(set(elements))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# Ejercicio 310: Escribe un programa que lea un archivo de texto y cuente el número de palabras.
# Conceptos: Manejo de archivos.
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"
print(count_words_in_file('example.txt')) 


# Día 63
# Ejercicio 311: Crea una clase Coche con atributos como marca, modelo y año. Agrega un método que imprima la información del coche.
# Conceptos: POO.
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def Is_empy(self):
        if len(self.año) == 0 or len(self.marca) == 0 or len(self.modelo) == 0:
            return "You miss one ot two elements"
        
    def PrintInformation(self):
        return f"Auto: {self.marca} {self.modelo} del año: {self.año}"
    
    
data = Coche("Toyota", "land cruiser", 2025)
print(data.PrintInformation())
        
# Ejercicio 312: Implementa una función que calcule el factorial de un número de forma recursiva.
# Conceptos: Recursividad.
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    return  n * Factorial(n - 1) 
print(Factorial(6))
        

# Ejercicio 313: Crea una función que verifique si una cadena es un palíndromo.
# Conceptos: Manipulación de strings.
def Palindrome(word):
    if not isinstance(word, str):
        raise TypeError("I only accept text")
    elif not word:
        return "the space is empty"
    clean = word.replace(" ", "").lower()
    return clean == clean[::-1]

print(Palindrome("Amo la paloma"))

# Ejercicio 314: Escribe un programa que implemente un juego de "piedra, papel o tijera" contra la computadora.
# Conceptos: Números aleatorios, condicionales.
import random
def rock_paper_scissors():
    try:
        choices = ["piedra", "papel", "tijera"]
        computer_choice = random.choice(choices)
        user_choice = input("Elige piedra, papel o tijera: ").lower()
        if user_choice not in choices:
            return "Opción no válida. Por favor, elige piedra, papel o tijera."
        print(f"Computadora eligió: {computer_choice}")
        if user_choice == computer_choice:
            return "¡Es un empate!"
        elif (user_choice == "piedra" and computer_choice == "tijera") or \
            (user_choice == "papel" and computer_choice == "piedra") or \
            (user_choice == "tijera" and computer_choice == "papel"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"
    except KeyboardInterrupt:
        return "Juego terminado por el usuario"
    except Exception as e:
        return f" ERROR: {e}"
print(rock_paper_scissors())

# Ejercicio 315: Crea una función que reciba una lista de tuplas y devuelva una lista ordenada por el segundo elemento de cada tupla.
# Conceptos: Tuplas, ordenamiento.
def TupleSort(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    elif  not all(isinstance(tup, tuple) for tup in elements):
        raise Exception("I need tuples in the list")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n -i -1):
            if elements[j][1] > elements[j + 1][1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(TupleSort([("eric", 65, "math"), ("helen", 21, "physics"), ("Carlos", 1, "spanish"), ("maris", 0, "elements")]))


# Día 64
# Ejercicio 316: Crea una clase CuentaBancaria con métodos para depositar y retirar dinero.
# Conceptos: POO, manejo de atributos.
class CuentaBancaria:
    def __init__(self):
        self.Bank = []
        
    def AddAcounts(self, name, funds):
        self.Bank.append([name, funds])
        return f"Thank you for your knew account {name}"
    
    def AddFunds(self, name, funds):
        for data in self.Bank:
            if data[0].lower() == name.lower():
                data[1] += funds
        return f"The adding from your acount {name} was successfuly, the knew amount of your acount is {data[1]}"
        
    def WithdrawFunds(self, name, funds):
        for Money in self.Bank:
            if Money[0].lower() == name.lower():
                if Money[1] < funds:
                    return f"Insufficient funds in the account {name}."
                Money[1] -= funds
                return f"The withdraw from acount {name} was successfuly, the knew amount of the acount is {Money[1]}"
        return f"Account {name} not found."
        
bank = CuentaBancaria()
print(bank.AddAcounts("eric", 2500))
print(bank.AddAcounts("helen", 25000))
print(bank.AddAcounts("carlos", 250))
print(bank.AddAcounts("ericka", 2500000))
print(bank.AddFunds("helen", 25000))
print(bank.WithdrawFunds("helen", 50))

# Ejercicio 317: Escribe un programa que calcule la suma de los primeros n números primos.
# Conceptos: Números primos, bucles.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_of_primes(n):
    if n < 1:
        return "I need a number greater than 0"
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)  
        num += 1
    return sum(primes)
print(sum_of_primes(10))  


# Ejercicio 318: Implementa un algoritmo de ordenamiento (como burbuja o selección).
# Conceptos: Algoritmos.
def bubble_sort(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    n = len(elements)
    for i in range(n):
        aux = False
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                aux = True
        if not aux:
            break
    return elements
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

def selection_sort(elements):
    if not elements:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I need a list")
    n = len(elements)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if elements[j] < elements[min_index]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]
    return elements
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))

# Ejercicio 319: Crea una función que reciba una cadena y devuelva la misma cadena en formato "CamelCase".
# Conceptos: Manipulación de strings.
def camel_case(string):
    if not isinstance(string, str):
        raise TypeError("I need a string")
    elif not string:
        return "the space is empty"
    words = string.split()
    camel_cased = ''.join(word.capitalize() for word in words)
    return camel_cased
print(camel_case("hola mundo desde python")) # HolaMundoDesdePython

# Ejercicio 320: Escribe un programa que convierta un número decimal a binario.
# Conceptos: Matemáticas, manipulación de números.
def decimal_to_binary(num):
    if not isinstance(num, int):
        raise TypeError("I need an integer")
    elif num < 0:
        return "I need a positive number"
    return bin(num).replace("0b", "")
print(decimal_to_binary(10))  


# Día 65
# Ejercicio 321: Crea una clase Libro con atributos título, autor y año. Implementa un método que imprima la información del libro.
# Conceptos: POO.
class Libro:
    def __init__(self, Titulo, autor, año):
        self.Titulo = Titulo
        self.autor = autor
        self.año = año
        
    def PrintInformation(self):
        print(f"El libro: {self.Titulo} del autor: {self.autor}, fue publicado en el año: {self.año}")
        
data = Libro("El cuervo","Gabriel Garcia Marquez", 1889)
data.PrintInformation()
        
# Ejercicio 322: Escribe una función que encuentre el máximo común divisor (MCD) de dos números.
# Conceptos: Matemáticas, funciones.
# (MCD) es el número más grande que divide exactamente a dos o más números sin dejar residuo. Es decir, es el mayor número que tienen en común como divisor.
def MaximunCD(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("I only accept numbers")
    elif not a or not b:
        return "the space is empty"
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a
print(MaximunCD(48, 18))

# Ejercicio 323: Implementa un sistema de gestión de tareas utilizando clases.
# Conceptos: POO, listas.
class Task:
    def __init__(self):
        self.storage = []
        pass
        
class Admin(Task):
    def __init__(self):
        super().__init__()
        
    def Is_empty(self):
        if len(self.storage) == 0:
            return "The storage is empty"
        
    def AddTask(self, Task):
        if not isinstance(Task, str):
            raise TypeError("I only accept Text")
        self.storage.append(Task)
        self.storage.sort()
        
    def DeleteTask(self, task):
        if self.Is_empty():
            return "No tasks to delete."
        elif task not in self.storage:
            return f"There is no task call {task} in the storage, so I can not deleted"
        self.storage.remove(task)
        return "You deleted {task} from The storage, Thank you"
    
    def Show(self):
        if self.Is_empty():
            return "There is anything to see in the storage"
        aux = 1
        for data in self.storage:
            print(f"{aux}- {data}")
            aux += 1
            
    def CheckTask(self, task):
        if self.Is_empty():
            return "No Task to check"
        elif task not in self.storage:
            return "The task not into the storage, choose another"
        for data in self.storage:
            if data == task:
                ind = self.storage.index(data)
                self.storage[ind] = data + "  ready"
        return "Congratulations you finish your task"
    
menu = Admin()
print(menu.AddTask("mow the lawn"))
print(menu.AddTask("Wash the dishes"))
print(menu.AddTask("fix the car"))
print(menu.AddTask("paint the yard"))
print(menu.DeleteTask("fix the car"))
menu.Show()
print(menu.CheckTask("mow the lawn"))
menu.Show()

# Ejercicio 324: Crea una función que reciba una lista de números y devuelva la suma de los cuadrados.
def SumOfSquaresNumbers(numbers):
    if len(numbers) == 0:
        return "the list is empty"
    elif not isinstance(numbers, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("I only accept numbers")
    return sum([n ** 2 for n in numbers])
print(SumOfSquaresNumbers([89, 20.2, 56, 4, 10, 22]))
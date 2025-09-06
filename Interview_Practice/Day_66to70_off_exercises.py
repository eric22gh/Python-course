# Día 66


# Ejercicio 326: Crea una clase Empleado con atributos nombre, salario y departamento. Agrega un método que calcule el aumento de salario.
# Conceptos: POO.
class Empleado:
    def __init__(self, name, salary, appartment):
        self.name = name
        self.salary = salary
        self.appartment = appartment
        
    def SalaryIncrease(self, Increase):
        aux = self.salary * (Increase / 100)
        return f"The amount of salary increse for the employee: {self.name} is {aux:.2f}"
    
data = Empleado("eric", 506000, "Sales")
print(data.SalaryIncrease(10))

# Ejercicio 327: Implementa una función que encuentre el n-ésimo número de Fibonacci.
# Conceptos: Recursividad.
def fibonnaci(n):
    a, b = 0, 1
    fibo = []
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo
print(fibonnaci(10))

def recursive(n):
    if n <= 1:
        return n
    return recursive(n - 1) + recursive(n - 2)
print([recursive(i) for i in range(10)])

# Ejercicio 328: Escribe un programa que lea un archivo CSV y lo convierta en una lista de diccionarios.
# Conceptos: Manejo de archivos, CSV.
def csv_to_dict(file_path):
    try:
        import csv
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except FileNotFoundError:
        return "File not found"
print(csv_to_dict('Interview_Practice/sample.csv'))

# Ejercicio 329: Crea una función que reciba un número y devuelva su representación en formato romano.
# Conceptos: Matemáticas, manipulación de números.
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num
print(int_to_roman(44))

# Ejercicio 330: Escribe un programa que implemente un sistema de votación.
# Conceptos: POO, listas.
class VotingSystem:
    def __init__(self):
        self.votes = {}

    def add_candidate(self, candidate):
        if candidate not in self.votes:
            self.votes[candidate] = 0

    def cast_vote(self, candidate):
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            return "Candidate not found"

    def get_results(self):
        return self.votes
voting = VotingSystem()
voting.add_candidate("Alice")
voting.add_candidate("Bob")
voting.cast_vote("Alice")   
voting.cast_vote("Bob")
voting.cast_vote("Alice")
print(voting.get_results())



# Día 67
# Ejercicio 331: Crea una clase Producto con atributos nombre, precio y cantidad. Agrega métodos para calcular el valor total del inventario.
# Conceptos: POO.
class Producto:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return f"The total value of the inventory for the product: {self.name} is {self.price * self.quantity:.2f}"
product = Producto("Laptop", 1500, 10)
print(product.total_value())

# Ejercicio 332: Implementa una función que verifique si un número es un cuadrado perfecto.
# Conceptos: Matemáticas, funciones.
# NUmero es cuadrado perfecto si la raiz cuadrada del numero es un numero entero
def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num**0.5)
    return root * root == num
print(is_perfect_square(16))
print(is_perfect_square(20))

# Ejercicio 333: Escribe un programa que genere un gráfico de barras a partir de datos ingresados por el usuario.
# Conceptos: Visualización de datos (puedes usar matplotlib).
# import matplotlib.pyplot as plt 
# def bar_chart(data):
#     names = list(data.keys())
#     values = list(data.values())
#     plt.bar(names, values)
#     plt.xlabel("Names")
#     plt.ylabel("Values")
#     plt.title("Graph Bar")
#     plt.show()
    
# data = {"A": 10, "B": 15, "C": 7, "D": 12}
# bar_chart(data)


# Ejercicio 334: Crea una función que reciba una lista de palabras y devuelva la longitud de la palabra más larga.
# Conceptos: Listas, funciones.
def longest_word(words):
    if not words:
        return 0
    elif not isinstance(words, list):
        raise TypeError("I only accept list")
    elif not all(isinstance(i, str) for i in words):
        raise TypeError("I only accept strings in the list")
    length = max(len(word) for word in words)
    return length
print(longest_word(["apple", "banana", "cherry", "date"]))

# Ejercicio 335: Escribe un programa que implemente un sistema de gestión de libros en una biblioteca.
# Conceptos: POO, listas.
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        
    def list_books(self):
        return [(book.title, book.author, book.year) for book in self.books]
library = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library.add_book(book1)
library.add_book(book2)
print(library.list_books())


# Día 68

# Ejercicio 338: Escribe un programa que convierta una lista de números en una lista de cadenas.
# Conceptos: Listas, manipulación de tipos.
def NumbersToSAtrings(elements):
    if len(elements) == 0:
        return "the list is empty"
    elif not isinstance(elements, list):
        raise TypeError("I only accept a list")
    elif not all(isinstance(n, int) for n in elements):
        raise TypeError("I only accept a list of numbers")
    return [str(n) for n in elements]

print(NumbersToSAtrings([89, 56, 23, 0, 236, 22, 100]))

# Ejercicio 340: Escribe un programa que implemente un juego de adivinanza de palabras.
# Conceptos: Números aleatorios, bucles.
import random
def word_guessing_game(word_list):
    word_to_guess = random.choice(word_list)
    attempts = 6
    guessed_letters = set()
    print("Welcome to the Word Guessing Game!")
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            return
    print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")
word_list = ["python", "java", "kotlin", "javascript"]
# word_guessing_game(word_list) 

# Día 69

# Ejercicio 342: Implementa una función que encuentre el mínimo común múltiplo (MCM) de dos números.
# Conceptos: Matemáticas, funciones.
def MCM(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("I only accept positive integers")
    def GCD(x, y):
        while y:
            x, y = y, x % y
        return x
    return (a * b) // GCD(a, b)
print(MCM(4, 5))
print(MCM(15, 20))

# Ejercicio 343: Escribe un programa que lea datos de un archivo JSON y los imprima.
# Conceptos: Manejo de archivos, JSON.
def read_json(file_path):
    try:
        import json
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Error decoding JSON"
print(read_json('Interview_Practice/sample.json'))


# Día 70
# Ejercicio 346: Crea una clase Animal con un método hacer_sonido. Luego, crea clases derivadas como Perro y Gato que implementen este método.
# Conceptos: POO, herencia.
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Subclasses must implement this method")
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"
class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"
dog = Perro()
cat = Gato()
print(dog.hacer_sonido())
print(cat.hacer_sonido())

# Ejercicio 347: Implementa una función que calcule la suma de los dígitos de un número.
# Conceptos: Matemáticas, funciones.
def sum_of_digits(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("I only accept a non-negative integer")
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(12345))

# Ejercicio 350: Escribe un programa que implemente un sistema de gestión de empleados.
# Conceptos: POO, listas.
class Company:
    def __init__(self):
        self.employees = []
        
    def sort_employees(self):
        self.employees.sort(key=lambda x: x['job'])
        
    def add_employee(self, employee, job, place, salary):
        self.employees.append({
            "employee": employee.lower(),
            "job": job.lower(),
            "place": place.lower(),
            "salary": salary
        })
        self.sort_employees()
        return f"Employee {employee} added successfully"
    
    def list_employees(self):
        aux = 0
        for emp in self.employees:
            aux += 1
            print(f"{aux}. Name: {emp['employee']}, Job: {emp['job']}, Place: {emp['place']}, Salary: {emp['salary']}")
            
    def remove_employee(self, employee):
        for emp in self.employees:
            if emp['employee'] == employee.lower():
                self.employees.remove(emp)
                return f"Employee {employee} removed successfully"
        return "Employee not found"
company = Company()
print(company.add_employee("Eric", "Developer", "New York", 60000))
print(company.add_employee("Alice", "Manager", "Los Angeles", 80000))   
print(company.add_employee("Bob", "Designer", "Chicago", 55000))
company.list_employees()

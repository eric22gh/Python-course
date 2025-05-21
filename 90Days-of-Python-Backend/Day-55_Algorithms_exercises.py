# Día 30: Ejercicios prácticos sobre análisis de algoritmos

# Teoría: En este día, se aplicarán todos los conceptos aprendidos sobre algoritmos, complejidad temporal, complejidad espacial y notación Big O a través de ejercicios prácticos.

# Tips
# Revisa todos los conceptos antes de comenzar los ejercicios.
# Trabaja en grupo para discutir y analizar diferentes enfoques a los problemas.

# Buenas Prácticas
# Documenta tus soluciones y analiza su complejidad.
# Comparte tus soluciones con otros para recibir retroalimentación.


def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 1, 0
    for x in range(2, n + 1):
        a, b = b, b + a
        print(b, end=" ")
fibonacci(10)
# Complejidad temporal: O(n) y complejidad espacial O(1)

# Ejercicios

# 1- Analiza un algoritmo de ordenamiento y determina su complejidad temporal y espacial. 
def bubble_sort(numbers):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers) -i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
    # Complejidad temporal: O(n^2) tiempo cuadratico y complejidad espacial O(1) variable temporal

print(bubble_sort([3, 2, 9, 1, 5, 6]))

# 2- Implementa un algoritmo de búsqueda y analiza su complejidad en notación Big O.
def search(data, obj):
    for i in range(0, len(data)):
        if data[i] == obj:
            return data[i]
    else:
        return "I did not find the value in the list"
    # complejidad temporal O(n) tiempo lineal y complejidad espacial O(1) variable temporal

print(search([3, 2, 9, 1, 5, 6], 1))

# 3- Desarrolla un algoritmo que calcule el factorial de un número y evalúa su complejidad.
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    if n < 0:
        return "I do not accept non-negative numbers"
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# la complejidad temporal O(n) tiempo lineal y complejidad espacial O(1)
print(factorial(5))

def factory(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    if n < 0:
        return "I do not accept non-negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factory(n - 1)
print(factory(5))

# 4- Crea un algoritmo que encuentre el máximo en una lista y determina su complejidad.
def Bigger_num(elements):
    if not isinstance(elements, list):
        raise TypeError("i need a list")
    aux = elements[0]
    for i in elements:
        if aux < i:
            aux = i
    return aux
# la complejidad temporal es O(n) tiempo lineal y complejidad espacial O(1) variable temporal
print(Bigger_num([10, 52, 1, 56, 1000, 3]))
            
# 5- Escribe un algoritmo que realice un recorrido en un árbol y analiza su complejidad.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self,node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.add_recursive(node.right, value)

    def see(self):
        return self.algorithm_to_see(self.root)
    
    def algorithm_to_see(self, node):
        if node is not None:
            self.algorithm_to_see(node.left)
            print(node.value)
            self.algorithm_to_see(node.right)
# Complejidad temporal O(n) tiempo lineal y complejidad espacial O(h) donde h es la altura del árbol

data_binary = binarytree(15)
data_binary.add(12)
data_binary.add(17)
data_binary.add(10)
data_binary.add(13)
data_binary.add(16)
data_binary.add(18)
data_binary.see()
    
# 6- Escribe un algoritmo que calcule el MCD de dos números y determina su complejidad.
def MCD(a, b):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("I only accept numbers")
    while b:
        a, b = b, a % b
    return a
# complejidad temporal O(log n), tiempo logaritmico y complejidad espacial O(1) variable temporal
print(MCD(15, 20))

# 7- Desarrolla un algoritmo que busque un elemento en un árbol binario y evalúa su complejidad.
def search_in_tree(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    elif value < node.value:
        return search_in_tree(node.left, value)
    else:
        return search_in_tree(node.right, value)
    # Complejidad temporal O(n) tiempo lineal y complejidad espacial O(h) donde h es la altura del árbol
print(search_in_tree(data_binary.root, 13)) 

# 8- Crea un algoritmo que genere la serie de Fibonacci y analiza su complejidad.
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b, fibo = 0, 1, []
    for i in range(0, n):
        a, b = b, a + b
        fibo.append(b)
    return fibo
# complejidad temporal O(n) tiempo lineal y complejidad especial O(n) espacio lineal
print(fibonacci(5))

# 9- Crea un algoritmo que cuente el número de palabras en un texto y evalúa su complejidad.
def wordsINtext(word):
    if not isinstance(word, str):
        raise TypeError("I need texts")
    import re 
    aux = re.sub(r"[^a-zA-Z\s]+$", "", word)
    return len(aux.split())
# complejidad temporal O(1) tiempo constante y complejidad espacial O(1) espacio constante
print(wordsINtext("eric hernandez   edwards8%"))

# Mini Proyectos
# Desarrolla un programa que gestione una biblioteca y analice la complejidad de las operaciones.
class Book:
    def __init__(self, title, author, year, genre, reserve=False):
        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(year, int) or not isinstance(genre, str):
            raise TypeError("I need a string for title, author and genre and a number for year")
        elif not title or not author or not genre:
            raise ValueError("I need a title, author and genre")
        elif year < 0:
            raise ValueError("I do not accept negative numbers")
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.reserve = reserve
        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        if not isinstance(title, str):
            raise TypeError("I need a text")
        elif not title:
            raise ValueError("I need a title")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"{title} has been removed from the library."
        return f"{title} not found in the library."

    def search_book(self, title):
        if not isinstance(title, str):
            raise TypeError("I need a text to search")
        elif not title:
            raise ValueError("I need a title to search")
        for book in self.books:
            if book.title == title:
                return book
        return f"{title} not found in the library."
    
    def list_books(self):
        if not self.books:
            return "No books in the library."
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Reserved: {book.reserve}")
    
    def check_reserve(self, title):
        if not isinstance(title, str):
            raise TypeError("I only accept text")
        elif not title:
            raise ValueError("the espace is empty")
        for book in self.books:
            if book.reserve == False and book.title == title:
                return f"{title} is available."
            elif book.reserve == True and book.title == title:
                return f"{title} is reserved."
        return f"{title} not found in the library."
    
    def reserve_book(self, title):
        if not isinstance(title, str):
            raise TypeError("I only accept text")
        elif not title:
            raise ValueError("the espace is empty")
        for book in self.books:
            if book.title == title and book.reserve == False:
                book.reserve = True
                return f"{title} has been reserved."
            elif book.title == title and book.reserve == True:
                return f"{title} is already reserved."
        return f"{title} not found in the library."
# Complejidad temporal O(n) tiempo lineal y complejidad espacial O(n) espacio lineal

library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"))
library.add_book(Book("1984", "George Orwell", 1949, "Dystopian"))
library.add_book(Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy"))
library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"))
library.reserve_book("The Great Gatsby")
library.list_books()
    
    
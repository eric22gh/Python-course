# Día 60: Comparación entre búsqueda lineal y binaria

# Teoría
# La comparación entre búsqueda lineal y búsqueda binaria se basa en la eficiencia de cada algoritmo. 
# La búsqueda lineal es más simple pero menos eficiente en listas grandes, 
# mientras que la búsqueda binaria es más rápida pero requiere que la lista esté ordenada.


# Tips
# Analiza el contexto en el que se utilizará cada algoritmo antes de elegir uno.
# Considera el tamaño de la lista y si está ordenada al decidir qué algoritmo usar.

# Buenas Prácticas
# Realiza pruebas de rendimiento con listas de diferentes tamaños y contenidos.
# Documenta las ventajas y desventajas de cada algoritmo.

# Ejemplo de Comparación
import time
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Ejemplo de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Comparación de tiempos
lista = list(range(10000000))  # Lista ordenada
objetivo = 9999999 

# Búsqueda lineal
inicio = time.time()
resultado_lineal = busqueda_lineal(lista, objetivo)
fin = time.time()
print("Búsqueda lineal encontró el elemento en el índice:", resultado_lineal, "en tiempo:", fin - inicio)

# Búsqueda binaria
inicio = time.time()
resultado_binario = busqueda_binaria(lista, objetivo)
fin = time.time()
print("Búsqueda binaria encontró el elemento en el índice:", resultado_binario, "en tiempo:", fin - inicio)
# es mas eficiente la busqueda binaria..

import bisect # el modulo bisect permite realizar búsquedas binarias en listas ordenadas
numeros = [1, 3, 5, 70, 9, 110, 13, 15, 17, 19]
numeros.sort()  
indice = bisect.bisect_left(numeros, 17)
if indice < len(numeros) and numeros[indice] == 17:
    print("Número encontrado en el índice:", indice)
else:
    print("Número no encontrado")

# Ejercicios
# 1- Implementa un programa que permita al usuario elegir entre búsqueda lineal y binaria.
class Searching:
    def __init__(self):
        self.storage = []
        
    def Is_Empty(self):
        return len(self.storage) == 0
    
    def Add(self, number):
        if not number:
            return "There is no number to add"
        elif not isinstance(number, int):
            raise TypeError("I only accept numbers to add")
        self.storage.append(number)
        self.storage.sort()
        
    def LinearSearch(self, Value):
        if self.Is_Empty():
            return "The list is empty"
        elif not isinstance(Value, int):
            return "I only accept numbers to search"
        for i in range(0, len(self.storage) - 1):
            if self.storage[i] == Value:
                return F"I found the Value: {self.storage[i]} \n"
        return "I did not find the value"
        
    def BinarySearch(self, Value):
        if self.Is_Empty():
            return "The list is empty"
        elif not isinstance(Value, int):
            return "I only accept numbers to search"
        left, right = 0, len(self.storage) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.storage[medium] == Value:
                return f"I found the value: {self.storage[medium]} \n" 
            elif self.storage[medium] < Value:
                left = medium + 1
            else:
                right = medium - 1
        return "I did not find the value"
    
    def See(self):
        if self.Is_Empty():
            return "The list is empty"
        return self.storage
            
Menu = Searching() # se tiene que poner afuera de el bucle while, porque de no ser asi el buble en cada iterracion va a crear una lista nueva
while True:
    print("Welcome to my Menu \n"
          "1- Add Number \n"
          "2- Busqueda Lineal \n"
          "3- Binary Search \n"
          "4- See The list \n"
          "5- Finish \n")
    aux = int(input("Select a number: "))
    if not isinstance(aux, int):
        raise TypeError("I only accept numbers")
    if aux == 1:
        sux = int(input("Which number do you want to add?: "))
        Menu.Add(sux)
        print("Thank you for add")
    elif aux == 2: 
        print("welcome to Linear Search")
        sux = int(input("Which number do you want to Search?: "))
        print(Menu.LinearSearch(sux))
        print("Thank you for Search")
    elif aux == 3:
        print("welcome to Binary Search")
        sux = int(input("Which number do you want to Search?: "))
        print(Menu.BinarySearch(sux))
        print("Thank you for Search")
    elif aux == 4:
        print(Menu.See())
        print("Thank you for Whatch")
    elif aux == 5:
        print("Thank you so much for use my program, Bye")
        break
    else:
        print("The Only accept numbers between 1 and 5")
        
        
# 2- Crea un método que imprima las ventajas y desventajas de cada algoritmo.
def AdvantagesAndDisadvantages():
    print("Linear Search \n"
          "Advantages \n"
          "1- Simplicidad: Fácil de implementar \n"
          "2- No requiere orden\n"
          "Disavantages \n"
          "1- Poco eficiente para listas grandes\n"
          "2- Puede requerir revisar todos los elementos\n"
          "3- No escala bien\n"
          "\n"
          "Binary Search \n"
          "Advantages \n"
          "1- Alta eficiencia\n"
          "2- Menor número de comparaciones\n"
          "3- Ideal para grandes volúmenes de datos. \n"
          "Disavantages \n"
          "1- Requiere que los datos estén ordenados\n"
          "2- Implementación más compleja\n"
          "3- Menos eficiente en listas pequeñas"
          )
    
AdvantagesAndDisadvantages()

# 3- Desarrolla un programa que permita al usuario ingresar un número y elija el método de búsqueda.
def SearchingProgram():
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  
    while True:
       print("Select a search method: \n"
             "1- Linear Search \n"
             "2- Binary Search \n"
             "3- Exit")
       choice = input("Enter your choice: ")
       if choice == '1':
           number = int(input("Enter a number to search using Linear Search: "))
           for i in range(len(lista)):
               if lista[i] == number:
                   print(f"Number {number} found at index {i} using Linear Search.")
                   break
           else:
               print(f"Number {number} not found using Linear Search.")
       elif choice == '2':
           number = int(input("Enter a number to search using Binary Search: "))
           left, right = 0, len(lista) - 1
           while left <= right:
               mid = (left + right) // 2
               if lista[mid] == number:
                   print(f"Number {number} found at index {mid} using Binary Search.")
                   break
               elif lista[mid] < number:
                   left = mid + 1
               else:
                   right = mid - 1
           else:
               print(f"Number {number} not found using Binary Search.")
       elif choice == '3':
           print("Exiting search program.")
           break
SearchingProgram()
      
# 4- Crea un método que imprima estadísticas sobre el rendimiento de cada algoritmo.
def performance_statistics():
    print("Estadísticas de rendimiento: \n"
          "Búsqueda Lineal: \n"
          "1. Complejidad temporal: O(n) \n"
          "2. Complejidad espacial: O(1) \n"
          "3. Mejor caso: O(1) (cuando el elemento está al principio) \n"
          "4. Peor caso: O(n) (cuando el elemento está al final o no está presente) \n"
          "\n"
          "Búsqueda Binaria: \n"
          "1. Complejidad temporal: O(log n) \n"
          "2. Complejidad espacial: O(1) \n"
          "3. Mejor caso: O(1) (cuando el elemento está en el medio) \n"
          "4. Peor caso: O(log n) (cuando el elemento no está presente o está al final)"
          )
performance_statistics()

# Mini Proyectos
# Desarrolla un programa que gestione una biblioteca y permita buscar libros usando ambos métodos.
class Library:
    def __init__(self):
        self.bookshelf = []
        
    def Is_Empty(self):
        return len(self.bookshelf) == 0
    
    def Add(self, book):
        if not book:
            return "There is no book to add"
        elif not isinstance(book, str):
            raise TypeError("I only accept text to add")
        self.bookshelf.append(book.capitalize().replace(" ", ""))
        self.bookshelf.sort()
        
    def LinearSearch(self, Value):
        if self.Is_Empty():
            return "The bookshelf is empty"
        elif not isinstance(Value, str):
            return "I only accept text to search"
        for i in range(0, len(self.bookshelf) - 1):
            if self.bookshelf[i] == Value.capitalize().replace(" ", ""):
                return F"I found the Book: {self.bookshelf[i]} \n"
        return "I did not find the book"
        
    def BinarySearch(self, Value):
        if self.Is_Empty():
            return "The bookshelf is empty"
        elif not isinstance(Value, str):
            return "I only accept text to search"
        self.bookshelf.sort()
        left, right = 0, len(self.bookshelf) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.bookshelf[medium] == Value.capitalize().replace(" ", ""):
                return f"I found the book: {self.bookshelf[medium]} \n" 
            elif self.bookshelf[medium] < Value.capitalize():
                left = medium + 1
            else:
                right = medium - 1
        return "I did not find the book"
    
    def See(self):
        if self.Is_Empty():
            return "The bookshelf is empty"
        for i, n in enumerate(self.bookshelf, start=1):
            print(f"{i}- {n}")
            
    def Eliminate(self, book):
        if self.Is_Empty():
            return "The bookshelf is empty"
        elif not isinstance(book, str):
            raise TypeError("I only accept text to eliminate")
        if book.capitalize() in self.bookshelf:
            self.bookshelf.remove(book.capitalize().replace(" ", ""))
            return f"The book '{book}' has been removed from the bookshelf."
        else:
            return f"The book '{book}' is not found in the bookshelf."
            
Menu = Library()
while True:
    print("Welcome to my Library \n"
          "1- Add a Book \n"
          "2- Search a book with linear Search \n"
          "3- Search a book with Binary Search \n"
          "4- See all the bookshelf \n"
          "5- Eliminate \n"
          "6- Finish \n")
    aux = int(input("Select a number: "))
    if not isinstance(aux, int):
        raise TypeError("I only accept numbers")
    if aux == 1:
        def recursive_add():
            sux = str(input("Which book do you want to add?: "))
            Menu.Add(sux)
            print("Thank you for adding")
            lux = str(input("Do you want to continue adding? (yes/no): "))
            if lux.lower() == 'yes':
                recursive_add()
            elif lux.lower() == 'no': 
                print("Thank you for using the add") # volver al menu principal
                return 
            else:
                print("I only accept 'yes' or 'no'")
                recursive_add()
        recursive_add()
    elif aux == 2: 
        print("welcome to Linear Search")
        def recursive_Linear_Search():
            sux = str(input("Which book do you want to Search?: "))
            print(Menu.LinearSearch(sux))
            print("Thank you for Search")
            lux = str(input("Do you want to continue searching with linear Search? (yes/no): "))
            if lux.lower() == 'yes':
                recursive_Linear_Search()
            elif lux.lower() == 'no': 
                print("Thank you for use Linear Search")
                return
            else:
                print("I only accept 'yes' or 'no'")
                recursive_Linear_Search()
        recursive_Linear_Search()
    elif aux == 3:
        print("welcome to Binary Search")
        def recursive_Binary_Search():
            sux = str(input("Which book do you want to Search?: "))
            print(Menu.BinarySearch(sux))
            print("Thank you for Search")
            lux = str(input("Do you want to continue searching with Binary Search? (yes/no): "))
            if lux.lower() == 'yes':
                recursive_Binary_Search()
            elif lux.lower() == 'no': 
                print("Thank you for use Binary Search")
                return
            else:
                print("I only accept 'yes' or 'no'")
                recursive_Binary_Search()
        recursive_Binary_Search()
    elif aux == 4:
        Menu.See()
        print("Thank you for Whatch")
    elif aux == 5:
        print("Welcome to Eliminate")
        def recursive_eliminate():
            sux = str(input("Which book do you want to eliminate?: "))
            print(Menu.Eliminate(sux))
            lux = str(input("Do you want to continue eliminating? (yes/no): "))
            if lux.lower() == 'yes':
                recursive_eliminate()
            elif lux.lower() == 'no': 
                print("Thank you for using the eliminate feature")
                return
            else:
                print("I only accept 'yes' or 'no'")
                recursive_eliminate()
        recursive_eliminate()
    elif aux == 6:
        print("Thank you so much for use my program, Bye")
        break
    else:
        print("The Only accept numbers between 1 and 6")
        
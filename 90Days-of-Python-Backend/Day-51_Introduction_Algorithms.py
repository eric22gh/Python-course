# Día 26: Definición y características de algoritmos

# Teoría
# Un algoritmo es un conjunto de pasos o instrucciones bien definidas que se utilizan para resolver un problema específico. 
# Las características de un algoritmo incluyen:
# Finitud: Debe terminar después de un número finito de pasos.
# Definición: Cada paso debe ser claro y no ambiguo.
# Entrada: Puede tener cero o más entradas.
# Salida: Debe producir al menos una salida.
# Efectividad: Los pasos deben ser realizables.

# Tips
# Asegúrate de que tu algoritmo sea eficiente y fácil de entender.
# Divide problemas complejos en subproblemas más sencillos.

# Buenas Prácticas
# Documenta cada paso del algoritmo para facilitar su comprensión.
# Realiza pruebas de tu algoritmo con diferentes entradas para verificar su funcionalidad.

def suma(a, b):
    """Algoritmo para sumar dos números."""
    return a + b

# Uso del algoritmo
resultado = suma(5, 3)
print("La suma es:", resultado)

# Ejercicios

# 1- Define un algoritmo para calcular la suma de una lista de números.
def Sum_list(list_numbers):
    # algoritmo para verificar si es una list y si esta vacia
    if len(list_numbers) == 0:
        return "The list is empty, I can not sum"
    if not isinstance(list_numbers, list):
        raise TypeError("I only accept list")
    # algoritmo para verificar si todos los elementos en la lista se pueden sumar
    if all(isinstance(i, (int, float))for i in list_numbers):
        return sum(list_numbers)
    raise TypeError("I only accept numbers")

data_2 = [58, 56, 22, 21, 10, 8 ]
print(Sum_list(data_2))

# 2- Crea un algoritmo que encuentre el máximo de una lista de números.
def Max_of_list(list_number):
    # algoritmo para verificar si es una lista
    if not isinstance(list_number, list):
        raise TypeError("I only accept list")
    elif len(list_number) == 0:
        return "The list is empty"
    else:
        if all(isinstance(i, (float, int))for i in list_number):
            aux = max(list_number)
            return f"The maximum number of the list is: {aux}"
        return "All the elements of the list must be integer"
    
import random
data_3 = [random.randint(1, 100) for i in range(8)]
print(Max_of_list(data_3))

# 3- Implementa un algoritmo que verifique si un número es primo.
def prime_number(n):
    # Algoritmo para verificar si es un numero natural y luego si el es un numero primo
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 2:
        return "I need a higher number than 2"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"The number {n} is not a prime number" 
        return f"The number {n} is a prime number"
    
print(prime_number(29))

# 4- Escribe un algoritmo que calcule el factorial de un número.
# El factorial de un numero es el resultado de multiplicar ese nuymero por todos los numeros menores que el.
def factorial(n):
    # Algoritmo para el factorial de un numero
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    # for i in range(1, n):
    #     n *= i
    # return n
print(factorial(6))

# 5- Desarrolla un algoritmo que genere la serie de Fibonacci cierta cantidad de veces.
def Fibonacci(n):
    # Algoritmo para secuencia de fibonacci
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    a, b = 0, 1
    fibo = []
    for i in range(0, n):
        a, b = b, a + b
        fibo.append(a)
    return fibo
print(Fibonacci(10))

# 6- Crea un algoritmo que cuente las vocales en una cadena de texto.
def Vowels(word):
    # Algoritmo para contar cuantas vocales hay en una frase
    if not isinstance(word, str):
        raise Exception("I only accept words")
    v, o = "aeiouAEIOU", 0
    for i in word:
        if i in v:
            o += 1
    return f"The amount of vowels in the text: {word} is {o} vowels"
print(Vowels("murcielago"))

# 7- Implementa un algoritmo que invierta una cadena de texto.
def Invert_text(text):
    # Algoritmo para invertir una palabra
    if not isinstance(text, str):
        raise Exception("ERROR, I need a text or a phrase")
    return text[::-1]
print(Invert_text("Eric"))

# 8- Escribe un algoritmo que elimine duplicados de una lista.
def Eliminate_duplicates_list(list_1):
    if not isinstance(list_1, list):
        raise TypeError("I only accept lists")
    new = list(set(list_1))
    return new
print(Eliminate_duplicates_list([22, 56, 22, 89, 100, 78, 50, 89, "eric", "eric"]))

# 9- Desarrolla un algoritmo que ordene una lista de números.
def Sort_list(list_2):
    # Algoritmo para ordenar una lista
    if not isinstance(list_2, list):
        raise TypeError("I only accept lists")
    elif len(list_2) == 0:
        return "The list is empty"
    else:
        if all(isinstance(i, (int, float))for i in list_2):
            return sorted(list_2)
        return "All the elements of the list must be integer"
    
print(Sort_list([22, 56, 22, 89, 100, 78, 50, 89]))

# 10- Crea un algoritmo que determine si dos cadenas son anagramas.
def Anagram(word_1, word_2):
    # Algoritmo para verificar si 2 palabras son anagramas
    if not isinstance(word_1, str) or not isinstance(word_2, str):
        raise TypeError("I only accept words")
    return sorted(word_1.lower()) == sorted(word_2.lower())
print(Anagram("a mor", "Ro ma"))

# 11- Implementa un algoritmo que encuentre el segundo mayor número en una lista.
def Second_list(numbers):
    # Algoritmo para retornar el segundo numero mas grande de una lista
    if not isinstance(numbers, list):
        raise TypeError("ERROR: THE ELEMENT IS NOT A LIST")
    elif len(numbers) == 0 or len(numbers) == 1:
        return "I need more numbers"
    elif all(isinstance(i, (int, float)) for i in numbers):
        aux = list(numbers)
        return sorted(aux)[-2]
    return "All the elements of the list must be numbers"
print(Second_list([2, 10, 56, 89, 100]))

# 12- Escribe un algoritmo que cuente cuántas veces aparece un carácter en una cadena.
def Count_characters(i, phrase):
    # Algoritmo que cuente cuántas veces aparece un carácter
    if not isinstance(i, str) or not isinstance(phrase, str):
        raise TypeError("ERROR: I only accept text")
    count = 0
    for x in phrase.lower():
        if i.lower() == x:
            count += 1
    return f"I count {count} time the charater {i} in the phrase."
print(Count_characters("a", "marcielago"))

# 13- Desarrolla un algoritmo que convierta grados Celsius a Fahrenheit.
def Celsius_to_Fahrenheit(celsius):
    # Algoritmo para convertir grados Celsius a Fahrenheit
    if not isinstance(celsius, (int, float)):
        raise TypeError("I only accept numbers")
    degress = celsius * 9/5 + 32
    return f"The temperature in Fahrenheit is: {degress} F"
print(Celsius_to_Fahrenheit(30))

# 14- Crea un algoritmo que determine si una cadena es un palíndromo.
def Palindrome(word):
    # Algoritmo para verificar si una palabra es un palíndromo
    if not isinstance(word, str):
        raise TypeError("I only accept words")
    return word == word[::-1]
print(Palindrome("reconocer"))

# 15- Implementa un algoritmo que calcule la suma de los dígitos de un número.
def Sum_digits(num):
    if not isinstance(num, int):
        raise TypeError("I need numbers")
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum
print(Sum_digits(890))

def Digits(n):
    if not isinstance(n, int):
        raise TypeError("I need numbers")
    return sum(int(i) for i in str(n))
print(Digits(890))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas utilizando algoritmos para agregar, eliminar y listar tareas.
class Taskmanager():
    def __init__(self):
        self.manager = []
    # Algoritmo para un administrador de tareas
    def add(self, task):
        if not isinstance(task, str):
            raise TypeError("I only accept text")
        elif task == None:
            return "No task to add"
        self.manager.append(task)
        return "Thank you for add"
    
    def delete(self, task):
        if len(self.manager) == 0:
            return "I did not find anything to delete"
        self.manager.remove(task)
        return f"Thank you for delete the task: {task}"
    
    def see(self,):
        if len(self.manager) == 0:
            return "I did not find anything to see"
        for t, n in enumerate(self.manager, start=1):
            print(f"Task {t}- {n}")

manager = Taskmanager()
manager.add("clean the dishes")
manager.add("go to the drogstore ")
manager.add("whash the car")
manager.add("Go to the supermarket")
manager.delete("clean the dishes")
manager.see()

# Crea un simulador de un sistema de reservas que utilice algoritmos para gestionar las reservas de asientos.
class Reservation():
    def __init__(self):
        self.reservation = {}
    # Algoritmo para un administrador de reservas
    def add(self, name, seat):
        if not isinstance(name, str) or not isinstance(seat, int):
            raise TypeError("I only accept text and numbers")
        elif name == None or seat == None:
            return "No reservation to add"
        self.reservation[name] = seat
        return "Thank you for your reservation"
    
    def search(self, name):
        if name not in self.reservation:
            return "I did not find the reservation"
        return f"Thank you for your reservation: {name} to the seat: {self.reservation[name]} "
    
    def search_seat(self, seat):
        if seat not in self.reservation.values():
            return "I did not find the reservation"
        for name, s in self.reservation.items():
            if s == seat:
                return f"Thank you for your reservation: {name} to the seat: {s}"
    def update(self, name, seat):
        if name not in self.reservation:
            return "I did not find the reservation"
        self.reservation[name] = seat
        return f"Thank you for update the reservation: {name} to the seat: {seat}"
    
    def delete(self, name):
        if len(self.reservation) == 0:
            return "I did not find anything to delete"
        self.reservation.pop(name)
        return f"Thank you for delete your reservation: {name}"
    
    def see(self,):
        if len(self.reservation) == 0:
            return "I did not find anything to see"
        count = 0
        for name, seat in self.reservation.items():
            count += 1
            print(f"Reservation {count} - {name} to the seat: {seat}")
            

reservation = Reservation()
reservation.add("Eric", 1)
reservation.add("helen", 2)
reservation.add("carlos", 3)
reservation.add("vilma", 4)
reservation.add("martha", 5)
reservation.delete("Eric")
reservation.search("martha")
reservation.search_seat(2)
reservation.update("helen", 5)
reservation.see()

    
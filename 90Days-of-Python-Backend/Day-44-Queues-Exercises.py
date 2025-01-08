# Día 44: Ejercicios prácticos de colas

# Teoría:
# Este día se dedicará a la práctica intensiva de los conceptos aprendidos sobre colas. 
# Se realizarán ejercicios que refuercen el conocimiento sobre la implementación y uso de colas en diferentes contextos.

# Ejercicios:
# 1- Crea una cola y realiza una serie de operaciones enqueue y dequeue, mostrando el estado de la cola después de cada operación.
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if self.is_empty():
            return "The queue is empty"
        self.queue.append(item)
        print(f"queue after the enqueue {self.queue}")
        

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        self.queue.pop(0)
        print(f"queue after the dequeue {self.queue}")
    
    def is_empty(self):
        return len(self.queue) == 0
    
adm = Queue()
adm.enqueue(5)
adm.enqueue(10)
adm.enqueue(20)
adm.enqueue(30)
adm.dequeue()

# 2- Implementa una función que simule un sistema de atención al cliente utilizando una cola.
class CustomerService():
    def __init__(self):
        self.queue = []

    def add_customer(self, customer):
        self.queue.append(customer)

    def is_empty(self):
        return len(self.queue) == 0

    def attend_customer(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            print(f"Attending customer: {self.queue.pop(0)}")

    def show_customers(self):
        if self.is_empty():
            print("The queue is empty")
        for i, customer in enumerate(self.queue, start=1):
            print(f"{i}. Customer: {customer}")

cs = CustomerService()
cs.add_customer("Mr. and Mrs. Smith")
cs.add_customer("John Doe")
cs.add_customer("Jane Dork")
cs.add_customer("John Smith")
cs.show_customers()
cs.attend_customer()

# 3- Crea un programa que utilice una cola para gestionar un sistema de impresión.
class Printer():
    def __init__(self):
        self.printers = []

    def is_empty(self):
        return len(self.printers) == 0
    
    def enqueue(self, page):
        self.printers.append(page)

    def dequeue(self):
        if self.is_empty():
            return "there are no pages to print"
        item = self.printers.pop(0)
        print(f"page: {item} print")

    def see_pages(self):
        for i, page in enumerate(self.printers, start=1):
            print(f"{i}- {page}")

machine = Printer()
machine.enqueue("Page 1")
machine.enqueue("Page 2")
machine.enqueue("Page 3")
machine.enqueue("Page 44")
machine.dequeue()
machine.see_pages()

# 4- Escribe un programa que use una cola para evaluar expresiones matemáticas en notación prefija.
class Math():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue.pop(0)

    def evaluate(self, expression):
        for item in expression:
            self.enqueue(item)
        while len(self.queue) > 1:
            operator = self.dequeue()
            operand1 = self.dequeue()
            operand2 = self.dequeue()
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = operand1 / operand2
            self.enqueue(result)
        return self.queue[0]
    
math = Math()
print(math.evaluate(["+", 5, 3]))

# 5- Implementa un sistema de gestión de pedidos utilizando una cola donde los pedidos se pueden agregar y eliminar.
class Order():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_order(self, order):
        self.queue.append(order)

    def remove_order(self):
        if self.is_empty():
            return "There are no orders"
        return self.queue.pop(0)

    def show_orders(self):
        for i, order in enumerate(self.queue, start=1):
            print(f"{i}. Order: {order}")

order = Order()
order.add_order("Order 1")
order.add_order("Order 2")
order.add_order("Order 3")
order.add_order("Order 4")
order.show_orders()
order.remove_order()
order.show_orders()

# 6- Crea un programa que use una cola para rastrear el historial de operaciones en un banco.
class Bank():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_operation(self, operation): # enqueue
        if not isinstance(operation, str):
            return f"this is not a valid operation: {operation}, must be a string"
        self.queue.append(operation)

    def remove_operation(self): # dequeue
        if self.is_empty():
            return "There are no operations"
        return self.queue.pop(0)

    def show_operations(self):
        for i, operation in enumerate(self.queue, start=1):
            print(f"{i}. Operation: {operation}")

    def show_last_operation(self): # peek
        if self.is_empty():
            return "There are no operations"
        return f"The last operation added was: {self.queue[-1]}"
    
bank_operations = Bank()
bank_operations.add_operation("Deposit")
bank_operations.add_operation("Withdrawal")
bank_operations.add_operation("Transfer")
bank_operations.add_operation("Deposit")
bank_operations.add_operation(8)
bank_operations.show_operations()
print(bank_operations.show_last_operation())

# 7- Escribe un programa que utilice una cola para almacenar números y calcule el promedio.
class Average():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_number(self, number): # enqueue
        if not isinstance(number, int):
            return f"this is not a valid number: {number}, must be an integer"
        return self.queue.append(number)

    def remove_number(self): # dequeue
        if self.is_empty():
            return "There are no numbers"
        return self.queue.pop(0)

    def show_numbers(self):
        for i, number in enumerate(self.queue, start=1):
            print(f"{i}. Number: {number}")

    def calculate_average(self):
        # ZeroDivisionError: division by zero
        try:
            if sum(self.queue) and len(self.queue) == 0:
                raise ZeroDivisionError
            else:
                result = sum(self.queue) / len(self.queue)
                return f"The average from the queue is: {result}"
        except ZeroDivisionError:
            return "There are no numbers to calculate the average"
    
average = Average()
average.add_number(10)
average.add_number(25)
average.add_number(30)
average.add_number(400)
print(average.calculate_average())

# 8- Implementa un método que permita clonar una cola.
class CloneQueue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_item(self, item): # enqueue
        self.queue.append(item)

    def remove_item(self): # dequeue
        if self.is_empty():
            return "There are no items"
        return self.queue.pop(0)

    def show_items(self):
        for i, item in enumerate(self.queue, start=1):
            print(f"{i}. Item: {item}")

    def last_item(self): # peek
        if self.is_empty():
            return "There are no items"
        return f"The last item added was: {self.queue[-1]}"

    def clone_queue(self):
        return f"the clone process was succesfuly done: {self.queue.copy()}"
    
clone = CloneQueue()
clone.add_item("Item 1")
clone.add_item("Item 2")
clone.add_item("Item 3")
clone.add_item("Item 4")
print(clone.clone_queue())

# 9- Desarrolla un programa que use una cola para realizar un recorrido en amplitud en un grafo.
# un grafo es una estructura de datos que se utiliza para modelar relaciones entre pares de objetos.
class Graph():
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            return f"Vertex {vertex} not found"

    def breadth_first_search(self, vertex):
        visited = []
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                queue.extend(self.graph[current_vertex]) # extend() agrega los elementos de una lista (o cualquier iterable) al final de la lista actual.
        return visited
    
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
print(graph.breadth_first_search("A"))

# 10- Crea una cola que limite su tamaño y maneje el error de desbordamiento.
class LimitedQueue():
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def add_item(self, item): # enqueue
        if self.is_full():
            return "The queue is full"
        self.queue.append(item)

    def remove_item(self): # dequeue
        if self.is_empty():
            return "There are no items"
        return self.queue.pop(0)

    def show_items(self):
        if self.is_empty():
            return "There are no items"
        elif self.is_full():
            return "The queue is full"
        else:
            for i, item in enumerate(self.queue, start=1):
                print(f"{i}. Item: {item}")

    def last_item(self): # peek
        if self.is_empty():
            return "There are no items"
        return f"The last item added was: {self.queue[-1]}"

limit = LimitedQueue(3)
limit.add_item("Item 1")
limit.add_item("Item 2")
limit.add_item("Item 3")
limit.add_item("Item 4")
print(limit.show_items())

# 11- Escribe un programa que use una cola para implementar un algoritmo de búsqueda en amplitud.
class queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue.pop(0)

    def breadth_first_search(self, graph, start):
        visited = []
        queue = [start]
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                queue.extend(graph[current_vertex])
        return visited
    
graph = {
    "A": ["B", "C"], 
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}

bfs = queue()
print(bfs.breadth_first_search(graph, "A"))

# 12- Crea una cola que almacene cadenas y las imprima en orden alfabético.
class AlphabeticalQueue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_string(self, string): # enqueue
        if not isinstance(string, str):
            return f"this is not a valid string: {string}, must be a string"
        self.queue.append(string)

    def remove_string(self): # dequeue
        if self.is_empty():
            return "There are no strings"
        return self.queue.pop(0)

    def show_strings(self):
        for i, string in enumerate(self.queue, start=1):
            print(f"{i}. String: {string}")

    def sort_strings(self):
        return sorted(self.queue) # self.queue.sort()
    
alphabetical = AlphabeticalQueue()
alphabetical.add_string("Zebra")
alphabetical.add_string("Apple")
alphabetical.add_string("Banana")
alphabetical.add_string("Orange")
alphabetical.remove_string()
print(alphabetical.sort_strings())

# 13- Implementa un método que permita fusionar dos colas en una sola.
class MergeQueue():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def is_empty(self):
        return len(self.queue1) == 0

    def push_queue1(self, item): # enqueue
        self.queue1.append(item)

    def push_queue2(self, item): # enqueue
        self.queue2.append(item)

    def pop_queue1(self): # dequeue
        if self.is_empty():
            return "There are no items"
        return self.queue1.pop(0)

    def pop_queue2(self): # dequeue
        if self.is_empty():
            return "There are no items"
        return self.queue2.pop(0)

    def show_queue1(self):
        for i, item in enumerate(self.queue1, start=1):
            print(f"{i}. Item: {item}")

    def show_queue2(self):
        for i, item in enumerate(self.queue2, start=1):
            print(f"{i}. Item: {item}")

    def merge_queues(self):
        return self.queue1 + self.queue2
    
merge = MergeQueue()
merge.push_queue1("Item 1")
merge.push_queue1("Item 28")
merge.push_queue1("Item 3")
merge.push_queue2("Item 40")
merge.push_queue2("Item 55")
print(merge.merge_queues())

# 14- Desarrolla un programa que use una cola para almacenar mensajes y permita imprimir el primer mensaje enviado.
class Messages():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push_message(self, message): # enqueue
        self.queue.append(message)

    def pop_message(self): # dequeue
        if self.is_empty():
            return "There are no messages"
        return self.queue.pop(0)
    
    def peek_message(self):
        if self.is_empty():
            return "There are no messages"
        return f"the last message added was {self.queue[-1]}"

    def show_messages(self):
        for i, message in enumerate(self.queue, start=1):
            print(f"{i}. Message: {message}")

    def first_message(self): 
        if self.is_empty():
            return "There are no messages"
        return f"The first message sent was: {self.queue[0]}"
    
messages = Messages()
messages.push_message("Message 1")
messages.push_message("Message 2")
messages.push_message("Message 3")
messages.push_message("Message 4")
print(messages.first_message())

# 15- Crea una cola que almacene objetos y permita acceder a sus atributos.
class ObjectsQueue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_object(self, obj): # enqueue
        self.queue.append(obj)

    def remove_object(self): # dequeue
        if self.is_empty():
            return "There are no objects"
        return self.queue.pop(0)

    def show_objects(self):
        for i, obj in enumerate(self.queue, start=1):
            print(f"{i}. Object: {obj}")

    def access_attributes(self, attribute):
        if self.is_empty():
            return "There are no objects"
        return [getattr(obj, attribute) for obj in self.queue] # getattr() devuelve el valor del atributo de un objeto dado su nombre.
    
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 30)
person2 = Person("Jane", 25)
person3 = Person("Doe", 40)
person4 = Person("Smith", 35)

objects = ObjectsQueue()
objects.add_object(person1)
objects.add_object(person2)
objects.add_object(person3)
objects.add_object(person4)
print(objects.access_attributes("name"))
print(objects.access_attributes("age"))

# Mini Proyectos:
# Desarrolla un juego de adivinanza de palabras que utilice una cola para rastrear las letras adivinadas.
class WordGuess():
    def __init__(self, word):
        self.word = word
        self.queue = ["_" for _ in word] # create a list of underscores with the same length as the word

    def is_empty(self):
        return len(self.queue) == 0

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "Please guess one letter at a time."
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.queue[i] = letter # replace the underscore with the letter
        return self.queue

    def show_word(self):
        return "".join(self.queue)
    
word_guess = WordGuess("Python")
print(word_guess.guess_letter("P"))
print(word_guess.guess_letter("y")) 
print(word_guess.guess_letter("z"))

# Crea un programa que simule un juego de cartas utilizando colas para manejar las cartas en juego.
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, cards):
        if not isinstance(cards, str):
            return "the card must be a string"
        self.queue.append(cards)
    
    def pop(self):
        if self.is_empty():
            return "there are no cards"
        return f"the firt card is on the table: {self.queue.pop(0)}"
    
    def remove_card(self, card):
        if self.is_empty():
            return "there are no cards"
        try: 
            self.queue.remove(card) 
            return f"You removed the card from your hand: {card}" 
        except ValueError as a: 
            return f"the card {card} is not in your hand"
    
    def last_card(self):
        if self.is_empty():
            return "there are no cards"
        return self.queue[-1] 
        
    def my_hand(self):
        if self.is_empty():
            return "there are no cards"
        return [f"Card {i} is: {hand}" for i, hand in enumerate(self.queue, start=1)]

cards_hand = Queue()
cards_hand.push("card1")
cards_hand.push("card2")
cards_hand.push("card3")
cards_hand.push("card4")
cards_hand.my_hand()
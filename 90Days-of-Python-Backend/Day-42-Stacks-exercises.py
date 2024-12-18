# Día 42: Ejercicios prácticos de pilas

# Teoría:
# Este día se dedicará a la práctica intensiva de los conceptos aprendidos sobre pilas. 
# Se realizarán ejercicios que refuercen el conocimiento sobre la implementación y uso de pilas en diferentes contextos.

# Ejercicios:
# 1- Crea una pila y realiza una serie de operaciones push y pop, mostrando el estado de la pila después de cada operación.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "The stack is empty"

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "The stack is empty"
        
    def see_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return "The stack is empty"
        
admin = Stack()
admin.push(1)
admin.push(2)
admin.push(3)
print(admin.see_stack())
admin.push(4)
admin.push(5)
print(admin.see_stack())
admin.pop()
print(admin.see_stack())

# 2- Implementa una función que verifique si una palabra es un palíndromo utilizando una pila.
class Stack_palindrome:
    def __init__(self):
        self.palindrome = []

    def push(self, item):
        return self.palindrome.append(item)
    
    def see_stack(self):
        if not self.is_empty():
            return self.palindrome
        return "The stack is empty"
    
    def pop(self):
        if not self.is_empty():
            return self.palindrome.pop()
        return "The stack is empty"
    
    def is_empty(self):
        return len(self.palindrome) == 0
    
word = Stack_palindrome() 
word.push("apipa")
word.push("amo la paloma")
word.push("roma")
def Verify_palindrome(stack):
    import re
    for w in stack:
        clean_word = re.sub(r"[ ,;.:\d]", "",w)
        clean_word2 = clean_word[::-1]
        if clean_word == clean_word2:
            print(f"this word: {w} is a palindrome")
        else:
            print(f"this word: {w} is not a palindrome")
data = word.see_stack()
Verify_palindrome(data)

# 3- Crea un programa que convierta un número decimal a binario utilizando una pila.
class Stack_binary():
    def __init__(self):
        self.binary = []

    def push(self, number):
        self.binary.append(number)
    
    def is_empty(self):
        return len(self.binary) == 0
    
    def pop(self):
        if not self.is_empty():
            self.binary.pop()
        return "the Stack is empty"
    
    def see_stack(self):
        if not self.is_empty():
            return self.binary
        return "the Stack is empty"
        
binary = Stack_binary()
binary.push(5)
binary.push(22)
binary.push(18)
def convert_to_binary(stack):
    convert = [bin(s) for s in stack]
    return convert  
numbers = binary.see_stack()
print(convert_to_binary(numbers))

# 4- Escribe un programa que use una pila para evaluar una expresión matemática en notación posfija.
class Stack_evaluete_expression():
    def __init__(self):
        self.expression = []

    def push(self, item):
        return self.expression.append(item)
    
    def see_stack(self):
        if not self.is_empty():
            return self.expression
        return "the Stack is empty"
    
    def is_empty(self):
        return len(self.expression) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.expression.pop()
        return "the Stack is empty"
    
expression = Stack_evaluete_expression()
expression.push(5)
expression.push("+")
expression.push("-")
def evaluate_expression(stack):
    expression2 = ["+", "-", "*", "/"]
    for e in expression2:
        if e in stack:
            return f"la expresion {e} esta en la pila"
        else:
            return f"la expresion {e} no esta en la pila"
item = expression.see_stack()         
print(evaluate_expression(item))
    
# 5- Implementa un sistema de gestión de tareas utilizando una pila donde las tareas se pueden agregar y eliminar.
class Stack_tasks():
    def __init__(self):
        self.tasks = []

    def push_agregar(self, item):
        return self.tasks.append(item)
    
    def see_stack(self):
        if not self.is_empty():
            return self.tasks
        return "the Stack is empty"
    
    def is_empty(self):
        return len(self.tasks) == 0
    
    def pop_eliminar(self):
        if not self.is_empty():
            return self.tasks.pop()
        return "the Stack is empty"
    
tasks = Stack_tasks()
tasks.push_agregar("tarea 1")
tasks.push_agregar("tarea 2")
tasks.push_agregar("tarea 3")
tasks.push_agregar("tarea 4")
print(tasks.see_stack())
tasks.pop_eliminar()
print(tasks.see_stack())

# 6- Crea un programa que use una pila para rastrear el historial de navegación en un navegador web.
class Stack_history():
    def __init__(self):
        self.history = []

    def push(self, item):
        return self.history.append(item)
    
    def see_stack(self):
        if not self.is_empty():
            return self.history
        return "the Stack is empty"
    
    def is_empty(self):
        return len(self.history) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.history.pop()
        return "the Stack is empty"
    
history = Stack_history()
history.push("pagina 1")
history.push("pagina 2")
history.push("pagina 3")
history.push("pagina 4")
print(history.see_stack())
history.pop()
print(history.see_stack())

# 7- Escribe un programa que utilice una pila para invertir una lista de elementos.
class Stack_invert():
    def __init__(self):
        self.item = []

    def push(self, elemento):
        return self.item.append(elemento)
    
    def is_empty(self):
        return len(self.item) == 0
    
    def pop(self):
        if not self.is_empty:
            return self.item.pop
        return "the stack is empty"
    
    def peek(self):
        if not self.is_empty:
            return self.item[-1]
        return "the stack is empty"
    
    def see_stack(self):
        if not self.is_empty:
            return self.item
        return "the stack is empty"
    
    def invert_stacK(self):
        return self.item[::-1]
            
invert = Stack_invert()
invert.push("papa")
invert.push("coma")   
invert.push("palo")   
invert.push("fruta")   
print(invert.invert_stacK())

# 8- Implementa un método que permita clonar una pila.
class Stack_clone():
    def __init__(self):
        self.item = []

    def push(self, elemento):
        return self.item.append(elemento)
    
    def is_empty(self):    
        return len(self.item) == 0
    
    def pop(self):
        if not self.is_empty:
            return self.item.pop
        return "the stack is empty"
    
    def peek(self):
        if not self.is_empty:
            return self.item[-1]
        return "the stack is empty"
    
    def see_stack(self):
        if not self.is_empty:
            return self.item    
        return "the stack is empty"
    
    def clone_stack(self):
        new_stack = self.item.copy()
        return new_stack
    
clone = Stack_clone()
clone.push("manzana")
clone.push("cerreza")   
clone.push("banana")   
clone.push("fruta")   
print(clone.clone_stack())

# 9- Desarrolla un programa que use una pila para realizar un recorrido en profundidad en un grafo.
# un grafo es una estructura de datos que se utiliza para modelar relaciones entre pares de objetos.
class Stack_graph():
    def __init__(self):
        self.graph = []

    def push_vertice(self, vertice):
        if vertice not in self.graph:
            return self.graph.append(vertice)
        
    def push_arista(self, vertice1, vertice2):
        if vertice1 in self.graph and vertice2 in self.graph:
            self.graph.append((vertice1, vertice2))
            self.graph.append((vertice2, vertice1))

    def recorrer_graph(self):
        for v in self.graph:
            print(f"vertice: {v} aristas: {self.graph.count(v)}")
    
    def is_empty(self):
        return len(self.graph) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.graph.pop()
        return "the Stack is empty"
    
graph = Stack_graph()
graph.push_vertice("A")
graph.push_vertice("B")
graph.push_vertice("C")
graph.push_arista("A", "B")
graph.push_arista("B", "C")
graph.push_arista("C", "A")
graph.recorrer_graph()

# 10- Crea una pila que limite su tamaño y maneje el error de desbordamiento.
class Stack_limit():
    def __init__(self):
        self.stack = []
        self.limit = 5

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            print("La pila esta llena")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("La pila esta vacia")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("La pila esta vacia")

    def is_empty(self):
        return len(self.stack) == 0
    

limit = Stack_limit()
limit.push(1)
limit.push(2)
limit.push(3)
limit.push(4)
limit.push(5)
limit.push(6)

# 11- Escribe un programa que use una pila para implementar un algoritmo de búsqueda en profundidad.
class Stack_search():
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

raiz = Stack_search(12)
raiz.izquierda = Stack_search(5)
raiz.izquierda.izquierda = Stack_search(4)
raiz.izquierda.derecha = Stack_search(7)
raiz.izquierda.izquierda.izquierda = Stack_search(2)
raiz.izquierda.derecha.izquierda = Stack_search(6)
raiz.derecha = Stack_search(20)
raiz.derecha.izquierda = Stack_search(15)
raiz.derecha.derecha = Stack_search(25)
raiz.derecha.derecha.derecha = Stack_search(30)

def busqueda_profundidad(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        busqueda_profundidad(nodo.izquierda)
        busqueda_profundidad(nodo.derecha)

busqueda_profundidad(raiz)

print("\n")
# 12- Crea una pila que almacene cadenas y las imprima en orden alfabético.
class Stack_alphabetic():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def sort_stack(self):
        if self.is_empty():
            return "the stack is empty"
        return sorted(self.stack)
    
stack = Stack_alphabetic()
stack.push("Z")
stack.push("B")
stack.push("A")
stack.push("D")
stack.push("E")
print(stack.sort_stack())

# Mini Proyectos:
# Desarrolla un juego de adivinanza de palabras que utilice una pila para rastrear las letras adivinadas.
class Stack_game():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def search(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack

stack = Stack_game()
win_word = "python"
import re
conteo = 3
while  conteo > 0:
    guess = input("Guess the word: ")
    clean = re.sub(r"[ ,.:;\d]", "", guess.lower())
    if clean == win_word.lower():
        print("you win")
        stack.push(win_word)
        break
    else:
        conteo -= 1
        print(f"Try again {conteo}")
    
# Crea un programa que simule un juego de cartas utilizando pilas para manejar las cartas en juego.
class Stack_cards():
    def __init__(self):
        self.table = []

    def put_card(self, item):
        self.table.append(item)

    def delete_card(self):
        if self.is_empty():
            return "the stack is empty"
        return self.table.pop()

    def select_card(self, item):
        return self.table[item]

    def is_empty(self):
        return len(self.table) == 0
    
    def show_table(self):
        if self.is_empty():
            return "the stack is empty"
        return self.table


stack = Stack_cards()
stack.put_card(1)
stack.put_card(2)   
stack.put_card(3)
stack.put_card(4)
stack.put_card(5)
stack.delete_card()
print(stack.show_table())
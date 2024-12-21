# Día 43: Introducción a colas (implementación y uso)

# Teoría:
# Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out), 
# lo que significa que el primer elemento añadido es el primero en ser retirado. Imagina una fila de personas esperando en una cola: 
# la primera persona en llegar es la primera en ser atendida.

# Las operaciones principales son:
# enqueue: Agregar un elemento al final de la cola. append(1)
# dequeue: Retirar y devolver el elemento al frente de la cola. pop(0)
# peek: Ver el elemento al frente sin retirarlo. elementos[0]
# is_empty: Verificar si la cola está vacía. len(elementos) == 0

# Tips y Buenas Prácticas:
# Asegúrate de manejar el caso de la cola vacía al realizar operaciones dequeue o peek.
# Uso adecuado: Utiliza colas para problemas que requieren un procesamiento en orden, como la gestión de tareas, 
# la impresión en una impresora, o la simulación de colas en supermercados.

# Manejo de excepciones: Asegúrate de manejar el caso de la cola vacía al realizar operaciones dequeue o peek. 
# Puedes usar condicionales para verificar si la cola está vacía antes de realizar estas operaciones, evitando errores.

# Documentación: Incluye comentarios y documentación en tu código para explicar la lógica y las funciones de las operaciones. 
# Esto hace que el código sea más fácil de entender y mantener.

# Testeo: Realiza pruebas exhaustivas para asegurarte de que todas las operaciones funcionen correctamente, 
# especialmente en casos borde como cuando la cola está vacía o llena.

# Implementación de una Cola:
class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if not self.is_empty():
            return self.elementos.pop(0)
        raise IndexError("La cola está vacía")

    def peek(self):
        if not self.is_empty():
            return self.elementos[0]
        raise IndexError("La cola está vacía")

    def is_empty(self):
        return len(self.elementos) == 0
    
    def see_queue(self):
        return self.elementos

# Uso de la cola
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola.see_queue())
print("Elemento al frente:", cola.peek())
print("Elemento retirado:", cola.dequeue())
print(cola.see_queue())

class Queue:
    def __init__(self):
        self.cola = []

    def enqueue(self, item):
        self.cola.append(item)
        print(f"Item enqueue: {item}")

    def dequeue(self):
        if not self.is_empty():
            elemento = self.cola.pop(0)
            print(f"Item dequeue: {elemento}")
            return elemento
        return "the queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.cola[0]
        return "the queue is empty"

    def is_empty(self):
        return len(self.cola) == 0

    def see_queue(self):
        return self.cola

# Ejemplo de uso de la cola
mi_cola = Queue()
mi_cola.enqueue(1)  
mi_cola.enqueue(2)  
mi_cola.enqueue(3) 
print(mi_cola.peek()) # see the first element from the queue
mi_cola.dequeue()  # remove the first element from the queue
print(mi_cola.peek())  # see the new first element from the queue
print(mi_cola.see_queue())  # see the new whole queue


# Ejercicios:
# 1- Implementa una cola y realiza operaciones enqueue y dequeue.
class New_Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return "Item enqueue"
    
    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        elemento = self.queue.pop(0)
        return f"The element. {elemento} is remove from the queue"
    
    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        element = self.queue[0]
        return f"This is the firt element from the queue: {element}"

    def is_empty(self):
        return len(self.queue) == 0
    
admin = New_Queue()
admin.enqueue("eric")
admin.enqueue("helen")
admin.enqueue("alvarado")
admin.enqueue("pera")
admin.enqueue("pais")
print(admin.dequeue())
print(admin.peek())

# 2- Crea un programa que simule una línea de espera en una tienda utilizando una cola.
class People_Queue():
    def __init__(self):
        self.line = []

    def enqueue(self, people):
        self.line.append(people)
        return f"this person: {people} in the line"
    
    def dequeue(self):
        if self.is_empty():
            return "the line from the Store is empty"
        process = self.line.pop(0)
        return f"We sucessfuly process the order for this person: {process}"
    
    def is_empty(self):
        return len(self.line) == 0
    
store = People_Queue()
print(store.dequeue())
store.enqueue("eric")
store.enqueue("marta")
store.enqueue("helen")
store.enqueue("damaris")
print(store.dequeue())

# 3- Implementa un método peek en tu clase de cola.
print("\n")
class People_Queue():
    def __init__(self):
        self.line = []

    def enqueue(self, people):
        add = self.line.append(people)
        return f"this person: {add} in the line"
    
    def dequeue(self):
        if self.is_empty():
            return "the line from the Store is empty"
        process = self.line.pop(0)
        return f"We sucessfuly process the order for this person: {process}"
    
    def peek(self):
        if self.is_empty():
            return "the line from the Store is empty"
        person = self.line[0]
        return f" this is the firt person from the line: {person}"
    
    def is_empty(self):
        return len(self.line) == 0
    
store = People_Queue()
print(store.dequeue())
store.enqueue("eric")
store.enqueue("marta")
store.enqueue("helen")
store.enqueue("damaris")
print(store.dequeue())
print(f"Now {store.peek()}")

# 4- Crea un programa que gestione una cola de tareas y las procese en orden.
class Task_Stack():
    def __init__(self):
        self.task = []

    def queue(self, item):
        add = self.task.append(item)
        return f" the task: {item} is added"
    
    def is_empty(self):
        return len(self.task) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There are no task to process"
        process = self.task.pop(0)
        return f"The task: {process} was sucessfuly process"
    
    def see_task(self):
        if self.is_empty():
            return "There is not any task"
        return self.task
    
manage = Task_Stack()
manage.queue("paint")
manage.queue("supermarket")
manage.queue("Wash the dishes")
manage.queue("Wash the car")
print(manage.see_task())
manage.dequeue()
print(manage.see_task())
manage.dequeue()
print(manage.see_task())
manage.dequeue()
print(manage.see_task())

# 5- Implementa una cola que almacene números y calcule la suma de todos los elementos al final. 
class Sum_Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        add = self.queue.append(item)
        return f" the number: {item} is added"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any number to process"
        process = self.queue.pop(0)
        return f"The number: {process} was sucessfuly delete"
    
    def sum(self):
        total = 0
        for x in self.queue:
            total += x
        return f"The sum of all the numbers is: {total}"
    
sum = Sum_Queue()
sum.enqueue(1)
sum.enqueue(2)
sum.enqueue(3)
sum.enqueue(4)
sum.enqueue(8)
sum.enqueue(9)
sum.enqueue(10)
print(sum.sum())

# 6- Escribe un programa que simule un sistema de impresión utilizando una cola.
class Print_Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        add = self.queue.append(item)
        return f" the document: {item} is added"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any document to process"
        process = self.queue.pop(0)
        return f"The document: {process} was sucessfuly print"
    
    def see_documents(self):
        if self.is_empty():
            return "There is not any document"
        return self.queue
    
print_queue = Print_Queue()
print_queue.enqueue("document1")
print_queue.enqueue("document2")
print_queue.enqueue("document3")
print_queue.dequeue()
print_queue.dequeue()
print(print_queue.see_documents())


# 7- Crea una cola que almacene nombres y los imprima en el orden en que fueron añadidos.
class Queue_names():
    def __init__(self):
        self.name = []

    def enqueue(self, names):
        self.name.append(names)
        return f"the name: {names} is saved"
    
    def is_empty(self):
        return len(self.name) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There are no names to print"
        item = self.name.pop(0)
        return f"the name: {item} successfuly print"
    
    def see_printer(self):
        if self.is_empty():
            return "There is not any name to print"
        return self.name

printer = Queue_names()
printer.enqueue("alex")
printer.enqueue("maria")
printer.enqueue("carlos")
print(printer.see_printer())
printer.dequeue()
printer.enqueue("ronald")
printer.dequeue()
print(printer.see_printer())

# 8- Implementa un método is_empty en tu clase de cola.
class Queue_names():
    def __init__(self):
        self.name = []

    def enqueue(self, names):
        self.name.append(names)
        return f"the name: {names} is saved"
    
    def is_empty(self):
        return len(self.name) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any name to print"
        item = self.name.pop(0)
        return f"the name: {item} successfuly print"
    
    def see_printer(self):
        if self.is_empty():
            return "There is not any name to print"
        return self.name

printer = Queue_names()
printer.enqueue("marta")
printer.enqueue("carlos")
printer.enqueue("jermy")
print(printer.see_printer())

# 9- Escribe un programa que use una cola para gestionar el historial de navegación en un navegador web.
class Browser_History():
    def __init__(self):
        self.history = []

    def enqueue(self, url):
        self.history.append(url)
        return f"the url: {url} is saved"
    
    def is_empty(self):
        return len(self.history) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any url to show"
        item = self.history.pop(0)
        return f"the url: {item} successfuly show"
    
    def see_history(self):
        if self.is_empty():
            return "There is not any url to show"
        return self.history
    
    def peek(self):
        if self.is_empty():
            return "There is not any url to show"
        return self.history[0]
    
browser = Browser_History()
browser.enqueue("google.com")
browser.enqueue("facebook.com")
browser.enqueue("instagram.com")
print(browser.see_history())
browser.dequeue()
print(browser.see_history())

# 10- Crea un programa que implemente un algoritmo de búsqueda en amplitud utilizando una cola.
class Breadth_First_Search():
    def __init__(self):
        # Inicializar el grafo como un diccionario vacío
        self.graph = {}

    def add_node(self, node, neighbors_node):
        # Agregar un nodo y sus vecinos al grafo
        self.graph[node] = neighbors_node
        return f"the node: {node} is added"
    
    def bfs(self, start_node):
        # Lista de nodos visitados
        visited = []
        # Cola de nodos a visitar, comenzando por el nodo inicial
        queue = [start_node]
        while queue:
            # Sacar el primer nodo de la cola
            node = queue.pop(0)
            # Si el nodo no ha sido visitado
            if node not in visited:
                # Marcar el nodo como visitado
                visited.append(node)
                # Obtener los vecinos del nodo
                neighbors_node = self.graph[node]
                for neighbor in neighbors_node:
                    # Agregar los vecinos a la cola
                    queue.append(neighbor)
        # Retornar la lista de nodos visitados
        return visited
    
    def see_graph(self):
        return self.graph
    
bfs = Breadth_First_Search()
bfs.add_node("A", ["B", "C"])
bfs.add_node("B", ["A", "D", "E"])
bfs.add_node("C", ["A", "F"])
bfs.add_node("D", ["B"])
print(bfs.see_graph())

# 11- Implementa una cola que limite su tamaño y maneje el error de desbordamiento.
class Queue_limit():
    def __init__(self):
        self.queue = []
        self.limit = 6

    def enqueue(self, item):
        if len(self.queue) >= self.limit:
            raise OverflowError("The Queue is Overflow, you can not add more items")
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "the queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "the queue is empty"
        return self.queue[0]
    
    def see_queue(self):
        if self.is_empty():
            return "the queue is empty"
        return self.queue
    
admin = Queue_limit()
try:
    admin.enqueue(5)
    admin.enqueue(8)
    admin.enqueue(7)
    admin.enqueue(6)
    admin.enqueue(10)
    admin.enqueue(22)
    admin.enqueue(20)
except OverflowError as a:
    print(a)

# 12- Crea una cola que almacene objetos y permita acceder a sus atributos.
class Queue_objects():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return f"the object: {item} is saved"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any object to show"
        item = self.queue.pop(0)
        return f"the object: {item} successfuly show"
    
    def see_queue(self):
        if self.is_empty():
            return "There is not any object to show"
        return self.queue
    
    def peek(self):
        if self.is_empty():
            return "There is not any object to show"
        return self.queue[0]
    
    def see_attributes(self, index):
        if self.is_empty():
            return "There is not any object to show"
        return self.queue[index]

admin = Queue_objects()
admin.enqueue({"name": "eric", "age": 20})
admin.enqueue({"name": "marta", "age": 25})
admin.enqueue({"name": "carlos", "age": 30})
print(admin.see_attributes(1))

# 13- Escribe un programa que use una cola para almacenar mensajes y permita imprimir el primer mensaje enviado.
class Queue_message():
    def __init__(self):
        self.message = []

    def enqueue(self, messages):
        self.message.append(messages)
        print(f"Message: {messages} added")

    def dequeue(self):
        if self.is_empty():
            print("There is not any message to send")
        item = self.message.pop(0)
        print(f"The message: {item} was sucessfuly send")

    def is_empty(self):
        return len(self.message) == 0
    
Msg = Queue_message()
Msg.enqueue("Message 1")
Msg.enqueue("Message 2")
Msg.enqueue("Message 3")
Msg.enqueue("Message 4")
Msg.dequeue()

# 14- Crea un programa que utilice una cola para gestionar eventos en un sistema de notificaciones.
class Queue_notification():
    def __init__(self):
        self.notification = []

    def enqueue(self, event):
        self.notification.append(event)
        print(f"Event: {event} added")

    def dequeue(self):
        if self.is_empty():
            print("There is not any event to show")
        item = self.notification.pop(0)
        print(f"The event: {item} was sucessfuly show")

    def is_empty(self):
        return len(self.notification) == 0
    
event = Queue_notification()
event.enqueue("Event 1")
event.enqueue("Event 2")
event.enqueue("Event 3")
event.enqueue("Event 4")
event.dequeue()

# 15- Desarrolla un programa que use una cola para realizar un recorrido en amplitud en un árbol.
# busqueda en profundidad
class Queue_tree():
    def __init__(self, Value):
        self.Value = Value
        self.left = None
        self.Right = None
bfs_queue = Queue_tree(15)
bfs_queue.left = Queue_tree(10)
bfs_queue.Right = Queue_tree(18)
bfs_queue.left.left = Queue_tree(7)
bfs_queue.left.Right = Queue_tree(13)
bfs_queue.Right.Right = Queue_tree(20)
bfs_queue.Right.left = Queue_tree(16)

def search_bfs(node):
    if node:
        print(node.Value, end=" ")
        search_bfs(node.left)
        search_bfs(node.Right)

search_bfs(bfs_queue)

# busqueda en amplitud
class Queue_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_queue(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# árbol
bfs_root = Queue_tree(15)
bfs_root.left = Queue_tree(10)
bfs_root.right = Queue_tree(18)
bfs_root.left.left = Queue_tree(7)
bfs_root.left.right = Queue_tree(13)
bfs_root.right.right = Queue_tree(20)
bfs_root.right.left = Queue_tree(16)
bfs_queue(bfs_root)

# Mini Proyectos:
# Desarrolla una aplicación de gestión de tareas que permita agregar, eliminar y ver tareas utilizando una cola.
class Task_Queue():
    def __init__(self):
        self.task = []

    def enqueue(self, item):
        self.task.append(item)
        return f"the task: {item} is added"
    
    def is_empty(self):
        return len(self.task) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any task to process"
        process = self.task.pop(0)
        return f"The task: {process} was sucessfuly process"
    
    def see_task(self):
        if self.is_empty():
            return "There is not any task"
        return self.task
    def peek(self):
        if self.is_empty():
            return "There is not any task"
        return self.task[0]
    
manage = Task_Queue()
manage.enqueue("paint")
manage.enqueue("supermarket")
manage.enqueue("Wash the dishes")
manage.enqueue("Wash the garage")
manage.dequeue()
print(manage.see_task())

# Crea un simulador de atención al cliente que utilice colas para gestionar las solicitudes.
class Queue_customer():
    def __init__(self):
        self.customer = []

    def enqueue(self, item):
        self.customer.append(item)
        return f"the customer: {item} is added"
    
    def is_empty(self):
        return len(self.customer) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is not any customer to process"
        process = self.customer.pop(0)
        return f"The customer: {process} was sucessfuly process"
    
    def see_customer(self):
        if self.is_empty():
            return "There is not any customer"
        return self.customer
    
    def peek(self):
        if self.is_empty():
            return "There is not any customer"
        return self.customer[0]
    
customers = Queue_customer()
customers.enqueue("eric")
customers.enqueue("marta")
customers.enqueue("carlos")
customers.enqueue("jermy")
customers.dequeue()
customers.dequeue()
print(customers.see_customer())
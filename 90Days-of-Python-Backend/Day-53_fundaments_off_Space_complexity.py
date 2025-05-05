# Día 28: Complejidad espacial: conceptos básicos

# 🧠 Teoría
# La complejidad espacial se refiere a la cantidad de memoria que un algoritmo utiliza en función del tamaño de la entrada.
# Esto incluye variables y estructuras de datos.

# 📏 Evaluación de la Complejidad Espacial
# Al igual que la complejidad temporal, es importante evaluar la complejidad espacial de tus algoritmos.

# ✅ Notación Big O en Complejidad Espacial
# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Espacio constante                | Variables temporales             | Excelente   |
# | O(n)      | Espacio lineal                   | Almacenar una lista de n elementos| Buena       |
# | O(n²)     | Espacio cuadrático               | Matrices bidimensionales         | Pobre       |

# ✅ Buenas Prácticas
# 1. Documenta el uso de memoria.
# 2. Realiza pruebas de uso de memoria.
# 3. Optimiza el uso de memoria.

# Sumar elementos de una lista
def suma_lista(lista):
    """Algoritmo para sumar los elementos de una lista."""
    suma = 0  # O(1) espacio
    for num in lista:
        suma += num  # O(1) espacio, variable temporal
    return suma
print(suma_lista([1, 2, 3, 4]))
# Complejidad espacial: O(1)

# Ejemplo de Código con Espacio Lineal
def duplicar_lista(lista):
    """Devuelve una nueva lista con los elementos duplicados."""
    nueva_lista = []  # O(1) espacio
    for num in lista:
        nueva_lista.append(num)  # O(n) espacio total
    return nueva_lista
print(duplicar_lista([1, 2, 3]))  # Devuelve [1, 2, 3]
# Complejidad temporal: O(n)

# Ejemplo de Código con Espacio Cuadrático
def crear_matriz(n, m):
    """Crea una matriz de n x m."""
    matriz = []  # O(1) espacio
    for i in range(n):  # O(n) espacio
        fila = []  # O(1) espacio
        for j in range(m):  # O(m) espacio
            fila.append(0)  # O(1) espacio
        matriz.append(fila)  # O(n*m) espacio total
    return matriz
print(crear_matriz(3, 4))  # Devuelve una matriz de 3x4

# complejidad espacial
def complejidad_espacial_temporal(numbers):
    suma = 0
    for i in range(len(numbers)): 
        suma += numbers[i] ** 2
    return suma  
print(complejidad_espacial_temporal([89, 56, 2, 45]))
# Complejidad espacial: O(1) porque solo uso una variable temporal para almacenar el resultado 
# complejidad temporal: O(n) porque recorro la lista una vez.
    
# 1- Analiza la complejidad espacial del algoritmo de suma de una lista.
def sum_list(numbers):
    if not numbers:
        return 0
    if not isinstance(numbers, list) or not all(isinstance(i, (int, float))for i in numbers): 
        raise TypeError("I need a list with only numbers")
    aux = 0
    for i in numbers:
        aux += i
    return aux
# the space complexity is o(1) because we use temporary variable, constant space 
data = [8, 56, 22, 21]
print(sum_list(data))

# 2- Evalúa la complejidad espacial de un algoritmo de búsqueda binaria.
def binary_search(list_item, object):
    try:
        list_item.sort()  # Ordenar la lista para la búsqueda binaria
        if not isinstance(list_item, list) or not isinstance(object, int):
            raise TypeError("I need a list and an object as number")
        elif not all(isinstance(i, int)for i in list_item):
            raise TypeError("I only accept numbers in the list ")
        start = 0
        end = len(list_item) - 1
        while start <= end:
            aux = (start + end) // 2
            if list_item[aux] == object:
                return aux
            elif list_item[aux] < object:
                start = aux + 1
            else:
                end = aux - 1
        return f"Value: {object} not found"
    except Exception as e:
        return f"ERROR: {e}"

# the space complexity is o(1) because we use temporary variable, constant space 
print(binary_search([89, 5, 4, 22, 4, 2, 7, 10, 54], 40))

# 3- Implementa un algoritmo que genere la serie de Fibonacci y determina su complejidad espacial.
def fibonacci(i):
    if not isinstance(i, (int, float)):
        raise TypeError("I only accept numbers")
    a, b = 0, 1
    for aux in range(i):
        a, b = b, b + a
        print(a, end=" ")
# the space complexity is O(1) because we use a temporary variable, constant space
fibonacci(10)

# 4- Escribe un algoritmo que elimine duplicados de una lista y evalúa su complejidad espacial.
def remove_duplicates(numbers):
        if not isinstance(numbers, list):
            raise TypeError("I only accept lists")
        elif not all(isinstance(i, (int, float))for i in numbers):
            raise TypeError("I only accept numbers in the list")
        return list(set(numbers))  # the space complexity is O(n) because we use a set to store unique elements
data = [8, 56, 22, 21, 8, 56]
print(remove_duplicates(data))

# 5- Desarrolla un algoritmo que calcule el factorial de un número y analiza su complejidad espacial.
def factorial(num):
    if num == 1:
        return 1
    result = 1
    for var in range(1, num + 1):
        result *= var
    return num
# the space complexity is O(1), constant space
print(factorial(5))

# 6- Crea un algoritmo que invierta una cadena y determina su complejidad espacial.
def inverted(string):
    if not string:
        return None
    elif not isinstance(string, str):
        raise TypeError("I only accept words")
    return string[::-1]
    # the space complexity is O(1) constant space
print(inverted("eric"))

# 7- Implementa un algoritmo que encuentre el máximo en una lista y evalúa su complejidad espacial.
def Max_list(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("I need a list")
        elif not all(isinstance(i, (int, float))for i in numbers):
            raise TypeError("All the elements in the list must be numbers")
        aux = 0
        for i in numbers:
            if i > aux:
                aux = i
        return aux 
    except Exception as e:
        return F"ERROR: {e}"
    # the space complexity is O(1),  constant space
data = [2, 1, 56, 10, 101, 50, 3]
print(Max_list(data))

# 8- Escribe un algoritmo que realice un recorrido en profundidad en un árbol y analiza su complejidad espacial.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def depth_first_search(self):
        return self._depth_first_search_recursive(self.root)

    def _depth_first_search_recursive(self, node):
        if node is None:
            return []
        return [node.value] + self._depth_first_search_recursive(node.left) + self._depth_first_search_recursive(node.right)
    
node = BinaryTree()
node.insert(10)
node.insert(5)
node.insert(15)
node.insert(3)
node.insert(7)
node.insert(12)
print(node.depth_first_search())  # Devuelve [10, 5, 3, 7, 15, 12]
# Complejidad espacial: O(n) porque se utiliza espacio adicional para la pila de recursión.

# 9- Desarrolla un algoritmo que genere todas las combinaciones de una lista y determina su complejidad espacial.
def combinations(lst):
    if len(lst) == 0:
        return [[]]
    first = lst[0]
    rest = lst[1:]
    without_first = combinations(rest)
    with_first = [[first] + comb for comb in without_first]
    return with_first + without_first
    # the space complexity is O(2^n) because we generate all combinations of the list
data = [1, 2, 3, 4]
print(combinations(data)) 

# 10- Crea un algoritmo que encuentre la intersección de dos listas y evalúa su complejidad espacial.
def intersection(list1, list2):
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("I need two lists")
        elif not all(isinstance(i, (int, float))for i in list1) or not all(isinstance(i, (int, float))for i in list2):
            raise TypeError("I only accept numbers in the lists")
        return list(set(list1) & set(list2))  # the space complexity is O(n) because we use a set to store elements
    except Exception as e:
        return f"ERROR: {e}"
data1 = [1, 2, 3, 4, 5]
data2 = [4, 5, 6, 7, 8]
print(intersection(data1, data2)) 

# 11- Implementa un algoritmo que calcule la suma de los dígitos de un número y analiza su complejidad espacial.
def sum_digits(number):
    try:
        if not number:
            return 0
        elif not isinstance(number, (int, float)):
            raise TypeError("I need a number")
        cont = 0
        for i in str(number):
            cont += int(i)
        return cont
    except Exception as e:
        return f"ERROR: {e}"
    # the space complexity is o(1) because we use temporary varaible, constant space

print(sum_digits(288))

# 12- Escribe un programa que encuentre el número de formas de hacer cambio para una cantidad dada y evalúa su complejidad espacial.
def change_ways(coins, amount):
    dp = [0] * (amount + 1)  # O(n) espacio
    dp[0] = 1  # Hay una forma de hacer cambio para 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]  # O(1) espacio
    return dp[amount]  # O(1) espacio
# Complejidad espacial: O(n) porque se utiliza un array de tamaño n+1 para almacenar las combinaciones.

print(change_ways([1, 2, 5], 5))  
# 13- Desarrolla un algoritmo que busque un elemento en un árbol binario y determina su complejidad espacial.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

node = BinaryTree()
node.insert(10)
node.insert(5)
node.insert(15)
node.insert(3)
node.insert(7)
node.insert(12)
print(node.search(7))  # Devuelve el nodo con valor 7
# Complejidad espacial: O(h) donde h es la altura del árbol, debido a la pila de recursión.
# 14- Crea un algoritmo que implemente el algoritmo de Dijkstra y evalúa su complejidad espacial.
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    visited = set()
    while visited != set(graph.keys()):
        current_node = min((node for node in graph if node not in visited), key=lambda node: shortest_paths[node])
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = shortest_paths[current_node] + weight
                if new_distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = new_distance
    return shortest_paths
# Complejidad espacial: O(n) porque se utiliza un diccionario para almacenar las distancias más cortas.
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'C'))  # Devuelve las distancias más cortas desde el nodo A

# 15- Implementa un algoritmo que ordene una lista y analiza su complejidad espacial.
def order_list(list_nums):
    n = len(list_nums)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if list_nums[j] > list_nums[j + 1]: # si el primero es mayor al que le sigue, se cambian los valores
                list_nums[j], list_nums[j + 1] = list_nums[j + 1], list_nums[j]
    return list_nums
# the space complexity 0(n2), quadratic space
data = [22, 1, 56, 10, 3]
print(order_list(data))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de contactos y analice la complejidad espacial de las operaciones.
class Contact:
    def __init__(self):
        self.phone = []

    def add_contact(self, name, phone):
        if not isinstance(name, str) or not isinstance(phone, str):
            raise TypeError("I need a string")
        self.phone.append({"name": name, "phone": phone})
        return F"Contact {name} added with phone {phone}"
    
    def remove_contact(self, name):
        for contact in self.phone:
            if contact["name"] == name:
                self.phone.remove(contact)
                return F"Contact {name} removed"
        return F"Contact {name} not found"
    
    def search_contact(self, name):
        for contact in self.phone:
            if contact["name"] == name:
                return contact
        return F"Contact {name} not found"
    
    def see_all_contacts(self):
        if not self.phone:
            return "No contacts found"
        for contact in self.phone:
            num = 0
            print(f"Contact {num}: {contact['name']}: {contact['phone']}")
            num += 1
        return "All contacts displayed"
    # the space complexity is O(n) because we use a list to store contacts

telephone = Contact()
telephone.add_contact("Eric", "123456789")
telephone.add_contact("John", "987654321")
telephone.add_contact("Jane", "456789123")  
telephone.add_contact("Doe", "321654987")
telephone.see_all_contacts() 

# Crea un simulador de un sistema de gestión de reservas que utilice algoritmos y evalúe su uso de memoria.
class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, name, date):
        if not isinstance(name, str) or not isinstance(date, str):
            raise TypeError("I need a string")
        self.reservations.append({"name": name, "date": date})
        return f"Reservation for {name} on {date} added."
    
    def remove_reservation(self, name):
        for reservation in self.reservations:
            if reservation["name"] == name:
                self.reservations.remove(reservation)
                return f"Reservation for {name} removed."
        return f"Reservation for {name} not found."
    
    def view_reservations(self):
        if not self.reservations:
            return "No reservations found."
        for reservation in self.reservations:
            print(f"Reservation: {reservation['name']} on {reservation['date']}")
        return "All reservations displayed."
    # the space complexity is O(n) because we use a list to store reservations
reservation = ReservationSystem()
reservation.add_reservation("Eric", "2023-10-01")
reservation.add_reservation("John", "2023-10-02")   
reservation.add_reservation("Jane", "2023-10-03")
reservation.add_reservation("Doe", "2023-10-04")
reservation.view_reservations()
print(reservation.remove_reservation("John"))
reservation.view_reservations()

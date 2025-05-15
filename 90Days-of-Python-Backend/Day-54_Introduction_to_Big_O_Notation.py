# 🧠 Teoría
# La notación Big O es una forma de describir la complejidad temporal y espacial de un algoritmo en términos de su comportamiento asintótico.
# que significa comportamiento asintótico, se refiere a cómo se comporta un algoritmo a medida que el tamaño de la entrada se aproxima al infinito.

# Esto significa que se centra en cómo el tiempo de ejecución o el uso de memoria crece a medida que aumenta el tamaño de la entrada. 
# La notación Big O se utiliza para clasificar algoritmos según su rendimiento y eficiencia.

# ✅ Clases de Complejidad
# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Tiempo constante                  | Acceso a un elemento en una lista| Excelente   |
# | O(log n)  | Tiempo logarítmico               | Búsqueda binaria, se reduce a la mitad | Muy buena   |
# | O(n)      | Tiempo lineal                    | Recorrer una lista                | Buena       |
# | O(n log n)| Tiempo casi lineal               | Algoritmos de ordenación como Merge Sort | Aceptable |
# | O(n²)     | Tiempo cuadrático                | Doble bucle anidado              | Pobre       |
# | O(2ⁿ)     | Tiempo exponencial               | Algoritmo recursivo de Fibonacci  | Mala        |

# ✅ Notación Big O en Complejidad Espacial
# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Espacio constante                | Variables temporales             | Excelente   |
# | O(n)      | Espacio lineal                   | Almacenar una lista de n elementos| Buena       |
# | O(n²)     | Espacio cuadrático               | Matrices bidimensionales         | Pobre       |

# ✅ Tips
# 1. Familiarízate con las diferentes clases de complejidad.
# 2. Utiliza la notación Big O para comunicar la eficiencia de tus algoritmos.

# ✅ Buenas Prácticas
# - Siempre que analices un algoritmo, intenta expresarlo en notación Big O.
# - Realiza comparaciones entre diferentes algoritmos utilizando la notación Big O.

# Explicación
# La búsqueda binaria divide repetidamente la lista en mitades, lo que resulta en una complejidad temporal logarítmica O(log n). 
# Esto significa que el tiempo de ejecución crece lentamente en comparación con el tamaño de la lista.

# Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    """Algoritmo de búsqueda binaria."""
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
# Complejidad temporal: O(log n)

def Binary_search(numbers, obj):
    numbers = sorted(numbers)
    left, right = 0, len(numbers) - 1
    while left <= right:
        aux = (left + right) // 2
        if numbers[aux] == obj: # si es igual
            return aux
        elif numbers[aux] < obj: # si es menor
            left = aux + 1
        else:
            right = aux - 1
    return -1

# Pruebas
if __name__ == "__main__":
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(busqueda_binaria(datos, 7))  # Devuelve 6
    print(Binary_search(datos, 22 ))

# Ejercicios

# 1- Expresa la complejidad temporal del algoritmo de suma de una lista en notación Big O.
def sum_of_list(numbers):
    if not isinstance(numbers, list) or not all(isinstance(i, (int, float)) for i in numbers):
        raise TypeError("I need a list with only numbers")
    cont = 0
    for i in numbers:
        cont += i
    return cont
from random import randint as rd
data = [rd(1, 100)for i in range(8)]
print(sum_of_list(data))
# the time complexity is O(n), linear time

# 2- Analiza un algoritmo de ordenamiento y determina su complejidad en notación Big O.
def bubbles_sort(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
    # the time complexity is O(n2), cuadratic time and the space complexity is O(n), linear time
data1 = [rd(1, 100)for i in range(8)]
print(bubbles_sort(data1))

def better_bubbles(numbers):
    i = 0
    control = True
    while i <= len(numbers) - 2 and control:
        control = False
        for j in range(0, len(numbers) - i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                control = True
        i += 1
    return numbers
    # usamos una variable bool como control, ella nos va adeterminar si ordenamos la lista o no, 
    # por si fuera el caso de que la lista ya este ordenada
print(better_bubbles(data))

# 3- Escribe un algoritmo que implemente la búsqueda lineal y expresa su complejidad.
def linear_search(nums, aux):
    for i in range(len(nums)):
        if nums[i] == aux:
            return aux 
    return f"I did not find: {aux} in the list"
data2 = [8, 10, 22, 56, 7, 8, 89, 21]
print(linear_search(data2, 21))
# the time complexity is o(n) linear time

# 4- Desarrolla un algoritmo que encuentre el máximo en una lista y expresa su complejidad en notación Big O.
def max_list(numbers):
    aux = numbers[0]
    for i in numbers:
        if i > aux:
            aux = i
    return aux
# the time complexity is O(n) linear time and the space complexity is O(1), constant space
data3 = [52, 1000, 56, 500, 2, 10, 1]
print(max_list(data3))

# 5- Crea un algoritmo que realice un recorrido en un árbol y determina su complejidad en notación Big O.
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
    # the complexity is O(2n) recursive algorithm

data_binary = binarytree(15)
data_binary.add(12)
data_binary.add(17)
data_binary.add(10)
data_binary.add(13)
data_binary.add(16)
data_binary.add(18)
data_binary.see()

# 6- Implementa un algoritmo que genere combinaciones y analiza su complejidad en notación Big O.
def generate_combinations(elements, r):
    if r == 0:
        return [[]]
    if len(elements) < r:
        return []
    combinations = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[i + 1:]
        for combination in generate_combinations(remaining, r - 1):
            combinations.append([current] + combination)
    return combinations
# the complexity is O(n) bedause we have to go through all the elements in the list
data4 = [1, 2, 3, 4]
print(generate_combinations(data4, 2))

# 7- Desarrolla un algoritmo que implemente el algoritmo de Dijkstra y determina su complejidad en notación Big O.
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda node: shortest_paths[node])
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = shortest_paths[current_node] + weight
                if new_distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = new_distance

    return shortest_paths

# the complexity is O(n2) because we have to go through all the nodes in the graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
print(dijkstra(graph, start_node)) 
# 9- Crea un algoritmo que encuentre la intersección de dos listas y expresa su complejidad.
def intersection(list1, list2):
    return list(set(list1) & set(list2))
# the complexity is O(n) because we have to go through all the elements in the list
data5 = [1, 2, 3, 4, 5]
data6 = [4, 5, 6, 7, 8]
print(intersection(data5, data6)) 

# 8- Implementa un algoritmo que calcule el MCD de dos números y analiza su complejidad en notación Big O.
# El MCD (Máximo Común Divisor) es el mayor número que divide a dos números sin dejar residuo.
def gcd(a, b):
    while b:
        a, b = b, a % b # El algoritmo de Euclides, que es eficiente para calcular el MCD.
        # Complejidad O(log n) en el peor de los casos.
    return a

print(gcd(48, 18))  # Devuelve 6

# 10- Escribe un algoritmo que busque un elemento en un árbol binario y expresa su complejidad.
def search_in_tree(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search_in_tree(node.left, value) or search_in_tree(node.right, value)
# Complejidad O(n) en el peor de los casos, donde n es el número de nodos en el árbol.

print(search_in_tree(data_binary.root, 13))  

# 11- Desarrolla un algoritmo que genere la serie de Fibonacci y expresa su complejidad en notación Big O.
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for x in range(2, n + 1):
        a, b = b, b + a
        print(b, end=" ")
# Complejidad O(n) y O(1)
fibonacci(10)  

# 12- Escribe un programa que encuentre el número de formas de hacer cambio para una cantidad dada y expresa su complejidad.
def count_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]
# Complejidad O(n * m) donde n es la cantidad y m es el número de monedas.  

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y analice la complejidad de las operaciones en notación Big O.
# Crea un simulador de un sistema de recomendaciones que utilice algoritmos y evalúe su complejidad en notación Big O.

class recommendation_system:
    def __init__(self):
        self.users = {}
        self.items = {}

    def add_user(self, user_id):
        self.users[user_id] = []

    def add_item(self, item_id):
        self.items[item_id] = []

    def recommend(self, user_id):
        return self.users[user_id]

    def add_recommendation(self, user_id, item_id):
        if user_id in self.users and item_id in self.items:
            self.users[user_id].append(item_id)
            self.items[item_id].append(user_id)
        else:
            raise ValueError("User or item not found in the system")
        
    # Complejidad O(n) para agregar recomendaciones y O(m) para recomendar, donde n es el número de usuarios y m es el número de elementos.
    # La complejidad total es O(n + m) para agregar y recomendar.

# Ejemplo de uso
rec_sys = recommendation_system()
rec_sys.add_user("user1")
rec_sys.add_item("item1")   
rec_sys.add_item("item2")
rec_sys.add_recommendation("user1", "item1")
rec_sys.add_recommendation("user1", "item2")    
print(rec_sys.recommend("user1"))  
# 🧠 Día 27: Complejidad Temporal – Conceptos Básicos

# 🎓 Teoría
# La complejidad temporal de un algoritmo mide cuánto tiempo tarda en ejecutarse en función del tamaño de la entrada, 
# usualmente representado como n.
# No se trata de tiempo en segundos, sino del número de operaciones que el algoritmo realiza conforme n crece.

# 📏 ¿Por qué es importante?
# Ayuda a comparar algoritmos sin necesidad de implementarlos.
# Nos permite anticipar si un algoritmo es escalable.
# Es crucial cuando tratamos con grandes volúmenes de datos.

# ✅ ¿La complejidad temporal depende del número exacto de operaciones?
# No exactamente. La complejidad temporal no se mide en número exacto de operaciones en un caso específico, 
# sino en cómo crece ese número de operaciones cuando aumenta el tamaño de la entrada (n).

# 🔢 Notación Big O o tiempo lineal O(n)
# La notación Big O (O(...)) o lista[i] describe el comportamiento del algoritmo en el peor de los casos.
# Notación Big O - Complejidad Temporal
# | Notación  | Nombre                      | Ejemplo común                     | Eficiencia  |
# |-----------|-----------------------------|-----------------------------------|-------------|
# | O(1)      | Tiempo constante            | Acceso a lista[i]                 | Excelente   |
# | O(log n)  | Tiempo logarítmico          | Búsqueda binaria                  | Muy buena   |
# | O(n)      | Tiempo lineal               | Recorrer lista                    | Buena       |
# | O(n log n)| Tiempo casi lineal          | Merge sort, Quick sort (mejor caso) | Aceptable |
# | O(n²)     | Tiempo cuadrático           | Doble bucle for                   | Pobre       |
# | O(2ⁿ)     | Tiempo exponencial          | Fibonacci recursivo               | Mala        |

# ✅ Tips
# Analiza la complejidad antes de escribir el código.
# Considera tanto el mejor caso, el caso promedio y el peor caso.
# Prefiere algoritmos más eficientes cuando n puede ser grande.

# 👨‍💻 Buenas Prácticas
# Usa notación Big O en comentarios cuando compartas tu código.
# Haz pruebas de rendimiento usando time o timeit en Python.
# Compara diferentes soluciones para el mismo problema según su complejidad.

# Ejemplo de algoritmo de búsqueda Lineal Big O
def busqueda_lineal(lista, objetivo):
    """Algoritmo de búsqueda lineal."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

datos = [4, 2, 7, 1, 9, 3]
print(busqueda_lineal(datos, 9))  # Devuelve 4
# Complejidad temporal: O(n)
# 🧠 Explicación: En el peor caso, el algoritmo tiene que revisar todos los elementos.
# Por eso, la complejidad es O(n): crece linealmente con el tamaño de la lista.

#Ejemplo de Código 2: Acceso directo(Tiempo constante), siempre va a ser 1
def obtener_elemento(lista, indice):
    """Devuelve el elemento en la posición indicada."""
    return lista[indice]

valores = [10, 20, 30, 40]
print(obtener_elemento(valores, 2))  # Devuelve 30
# Complejidad temporal: O(1)
# 🧠 Explicación:El acceso por índice o O(1) en listas es instantáneo, sin importar cuántos elementos haya.
#Por eso se dice que tiene complejidad constante O(1).

# Ejercicios
# 1- Analiza la complejidad temporal del algoritmo de suma de una lista.
def time_complexity_sum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("I only accept list")
    elif all(isinstance(i, (int, float)) for i in numbers):
        count = 0
        for i in range(len(numbers)):
            count += numbers[i]
        return f"The totaly sum of the list is: {count}, I the time complexity is {i}"
    raise TypeError("All the elements must be numbers")
datos = [59, 56, 89, 78] # hace 3 operaciones o crece 3 veces para resolver el resultado, O(n)
print(time_complexity_sum(datos)) # sum(numbers), sum tambien itera sobre la lista asi que no puede ser o(1)

# 2- Evalúa la complejidad temporal de un algoritmo de búsqueda binaria.
# La complejidad temporal es O(log n) porque con cada iteración se reduce el tamaño del problema a la mitad.
def Algorithm_binary_search(list_1, aux):
    left = 0
    right = len(list_1) - 1
    while left <= right:
        medio = (left + right) // 2
        if list_1[medio] == aux:
            return medio
        elif list_1[medio] < aux:
            left = medio + 1
        else:
            right = medio - 1
    return -1
datos = [59, 56, 89, 78]
print(Algorithm_binary_search(datos, 89))

# 3- Implementa un algoritmo de ordenamiento y determina su complejidad temporal.
def bubble_sort(list_2):
    n = len(list_2)
    #En cada pasada, el mayor elemento "flota" al final
    if n == 0:
        return list_2
    for i in range(0, (n - 1)):
        for j in range(0, n - i - 1):
            if list_2[j] > list_2[j + 1]:
                # Intercambiar si están en el orden incorrecto
                list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]
    return f"The result is {list_2}"
data = [5, 3, 100, 8, 4, 78]
print(bubble_sort(data))

# 4- Escribe un algoritmo que encuentre el elemento más pequeño en una lista y analiza su complejidad.
def Smallest_number(aux):
    if not aux:
        return None
    smallest = aux[0] # -2
    for num in aux: # 5, 100, 4, 1, 89, -2, 22
        if num < smallest:
            smallest = num
    return smallest
data = [5, 100, 4, 1, 89, -2, 22]
print(Smallest_number(data))
# # Complejidad temporal: O(n)
def bigger_number(aux): 
    if not aux:
        return None
    bigger = aux[0] # 100
    for i in aux:
        if i > bigger:
            bigger = i
    return bigger
data = [5, 100, 4, 1, 89, -2, 22, 1000]
print(bigger_number(data))

# 5- Desarrolla un algoritmo que cuente los elementos en una lista y evalúa su complejidad.
def count_elements(list):
        if not list:
            return 0
        return len(list)
print(count_elements(data))

# 6- Crea un algoritmo que verifique si una lista está ordenada y determina su complejidad.
# complejidad temporal O(n) porque tiene que iterar
def verify_order(aux):
    if not aux:
        return None
    for i in range(len(aux) - 2): # -2 es para asegurar que el bucle no acceda a un indice que no existe
        if aux[i] > aux[i + 1]: # si el primer elemento de la lista es mayor que el segundo return false
            return False
    return True
data = [1, 2, 33, 4, 5]
print(verify_order(data))

# 7- Implementa un algoritmo de búsqueda en profundidad en un grafo y analiza su complejidad.
def DFS(grafo, nodo, visitados):
    if nodo not in visitados:
        visitados.append(nodo)
        print(nodo)

    for aux in grafo[nodo]:
        DFS(grafo, aux, visitados)
def START_DFS(grafo, nodo_1):
    visitados = []
    DFS(grafo, nodo_1, visitados)
    return visitados
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(START_DFS(grafo, 'A')) 
# Complejidad temporal: O(V + E) donde V es el número de vértices y E es el número de aristas.

# 8- Escribe un algoritmo que calcule la suma de los cuadrados de los números en una lista y evalúa su complejidad.
def Sum_square(list_num):
    if not list_num:
        return 0
    count = 0
    for i in range(len(list_num)):
        count += list_num[i] ** 2
    return count

data = [2, 3, 5]
print(Sum_square(data))

# 9- Desarrolla un algoritmo que encuentre la longitud de la cadena más larga en una lista de cadenas y analiza su complejidad.
def largest_string(strings):
    if not strings:
        return None
    if not all(isinstance(i, str) for i in strings) or not isinstance(strings, list):
        raise TypeError("All the elements must be strings and a list")
    aux = strings[0]
    for i in strings:
        if len(i) > len(aux):
            aux = i
    return aux
data_words = ["mar","hdvbkhbkhshdb", "sol", "eric", "murcielago", "cielo"]
print(largest_string(data_words))

# 10- Crea un algoritmo que realice la multiplicación de matrices y determina su complejidad.
# una matriz es una estructura de números en filas y columnas, se conocen como elementos de la matriz. 
# Las matrices se utilizan para representar sistemas de ecuaciones lineales.
def multiply_matrices(A, B):
    if len(A[0]) != len(B): #
        raise ValueError("Las matrices no se pueden multiplicar.")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])): # 
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiply_matrices(A, B)) # [[19, 22], [43, 50]]
# Complejidad temporal: O(n³) porque hay tres bucles anidados.

# 11- Implementa un algoritmo que encuentre la intersección de dos listas y evalúa su complejidad.
def intersection(list_1, list_2):
    if not list_1 and not list_2:
        return None
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        raise TypeError("I only accept lists")
    return list(set(list_1) & set(list_2))
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
print(intersection(list_1, list_2)) # [4, 5]
# Complejidad temporal: O(n) porque se utiliza un conjunto para almacenar los elementos únicos de ambas listas.

# 12- Escribe un algoritmo que calcule el máximo común divisor (MCD) de dos números y analiza su complejidad.
def MCD(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("I only accept integers")
    while b: # mientras b no sea 0
        a, b = b, a % b # se asigna a b el valor de a y a a el residuo de la división entre a y b
    # el residuo de la división entre a y b
    return a
print(MCD(56, 98)) # 14
# Complejidad temporal: O(log n) porque el algoritmo de Euclides reduce el problema a la mitad en cada iteración.

# 13- Desarrolla un algoritmo que genere todas las permutaciones de una cadena y determina su complejidad.
# las permutaciones son todas las combinaciones posibles de los elementos de una lista o cadena.
from itertools import permutations
def generate_permutations(string):
    if not isinstance(string, str):
        raise TypeError("I only accept strings")
    return [''.join(p) for p in permutations(string)]
string = "abc"
print(generate_permutations(string)) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Complejidad temporal: O(n!) porque el número de permutaciones de una cadena de longitud n es n!.

# generar todas las combinaciones posibles de una lista sin modulos
def generate_combinations(lst):
    if not isinstance(lst, list):
        raise TypeError("I only accept lists")
    result = []
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            result.append(lst[i:j])
    return result
data = [1, 2, 3]
print(generate_combinations(data)) # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
# Complejidad temporal: O(n²) porque hay dos bucles anidados.

# 14- Crea un algoritmo que encuentre el número de formas de dar cambio para una cantidad dada y evalúa su complejidad.
def coin_change(coins, amount):
    if not coins or not amount:
        return 0
    if not isinstance(coins, list) or not isinstance(amount, int):
        raise TypeError("I only accept lists and integers")
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
coins = [1, 2, 5,]
amount = 5
print(coin_change(coins, amount)) # 4
# Complejidad temporal: O(n * m) donde n es la cantidad y m es el número de monedas.

# 15- Implementa un algoritmo que busque un elemento en un árbol binario y analiza su complejidad.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_tree(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    elif target < node.value:
        return search_tree(node.left, target)
    else:
        return search_tree(node.right, target)
def insert_tree(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert_tree(node.left, value)
    else:
        node.right = insert_tree(node.right, value)
    return node

root = Node(10)
insert_tree(root, 5)
insert_tree(root, 15)
insert_tree(root, 3)
insert_tree(root, 7)
insert_tree(root, 12)
insert_tree(root, 18)
print(search_tree(root, 7)) # True
# Complejidad temporal: O(h) donde h es la altura del árbol. En el peor caso, puede ser O(n) si el árbol es degenerado.

# Mini Proyectos
# Desarrolla un programa que simule un sistema de gestión de inventarios y analice la complejidad temporal de las operaciones.
def inventory_management(inventory, operation, item=None):
    if operation == "add":
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    elif operation == "remove":
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    elif operation == "check":
        return inventory.get(item, 0)
    return inventory
inventory = {}
inventory = inventory_management(inventory, "add", "apple")
inventory = inventory_management(inventory, "add", "banana")
inventory = inventory_management(inventory, "add", "apple")
inventory = inventory_management(inventory, "remove", "apple")
print(inventory) # {'apple': 1, 'banana': 1}
# Complejidad temporal: O(1) para agregar, eliminar y verificar elementos en un diccionario.

# Crea un simulador de un sistema de recomendaciones que utilice algoritmos de búsqueda y ordenamiento, evaluando su complejidad.
def recommendation_system(user_preferences, items):
    recommended_items = []
    for item in items:
        if item not in user_preferences:
            recommended_items.append(item)
    return sorted(recommended_items)
user_preferences = ["apple", "banana"]
items = ["banana", "orange", "grape", "apple"]
print(recommendation_system(user_preferences, items)) # ['grape', 'orange']
# Complejidad temporal: O(n log n) para ordenar la lista de elementos recomendados.


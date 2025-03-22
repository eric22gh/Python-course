# Día 24: Árboles binarios: definición y propiedades
# Teoría
# Un árbol binario es un tipo de árbol donde cada nodo tiene como máximo dos hijos. Las propiedades incluyen la altura y el número de nodos.

# Tips
# Mantén el árbol balanceado para optimizar el rendimiento.
# Utiliza árboles binarios para representar expresiones matemáticas y algoritmos de búsqueda.

# Buenas Prácticas
# Documenta cada método para facilitar su comprensión y mantenimiento.
# Realiza pruebas para verificar la correcta implementación de los métodos.

class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self, valor):
        self.raiz = NodoBinario(valor)

    def agregar(self, valor):
        self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None: 
                nodo.izquierdo = NodoBinario(valor)
            else:
                self._agregar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoBinario(valor)
            else:
                self._agregar_recursivo(nodo.derecho, valor)

    def imprimir(self):
        self._imprimir_recursivo(self.raiz)

    def _imprimir_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_recursivo(nodo.izquierdo)
            print(nodo.valor)
            self._imprimir_recursivo(nodo.derecho)

    def is_empty(self):
        return self.raiz is None
    
# Uso del árbol binario, los menores van a la izquierda y los mayores a la derecha
arbol_binario = ArbolBinario(10)
arbol_binario.agregar(5)
arbol_binario.agregar(15)
arbol_binario.agregar(4)
arbol_binario.agregar(6)
arbol_binario.agregar(14)
arbol_binario.imprimir()

# Ejercicios
# 1- Implementa un árbol binario y agrega nodos.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def print_tree(self):
        self.print_recursive(self.root)

    def print_recursive(self, node):
        if node is not None:
            self.print_recursive(node.left)
            print(node.value)
            self.print_recursive(node.right)

BinaryTree_1 = BinaryTree(22)
BinaryTree_1.add(5)
BinaryTree_1.add(6)
BinaryTree_1.add(50)
BinaryTree_1.add(51)
BinaryTree_1.print_tree()

# 2- Crea un método para imprimir el árbol en orden (in-order traversal).
# orden tradicional: izquierda, raiz, derecha, se recorre el arbol de forma ascendente
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binarytree_traversal:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def in_order_traversal(self):
        self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value, end=" ")
            self.in_order_traversal(node.right)

BinaryTree_2 = Binarytree_traversal(200)
BinaryTree_2.add(100)
BinaryTree_2.add(300)
BinaryTree_2.add(50)
BinaryTree_2.add(150)
BinaryTree_2.in_order_traversal(BinaryTree_2.root) # hay que poner el nodo raiz o arbol para que el lo recorra

# 3- Desarrolla un método que cuente el número de nodos en un árbol binario.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_count:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def count_nodes(self):
        count = self.count_recursive(self.root)
        return F"the amount of nodes is {count}"
    
    def count_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.count_recursive(node.left) + self.count_recursive(node.right)
    
BinaryTree_3 = BinaryTree_count(200)
BinaryTree_3.add(100)
BinaryTree_3.add(300)
BinaryTree_3.add(50)
print(BinaryTree_3.count_nodes())

# 4- Implementa un método para encontrar un nodo en un árbol binario.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_find:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def find_node(self, value):
        return self.find_recursive(self.root, value)
    
    def find_recursive(self, node, value):
        if node is None:
            return "the node is not in the tree"
        if node.value == value:
            return "the node is in the tree"
        if value < node.value:
            return self.find_recursive(node.left, value)
        else:
            return self.find_recursive(node.right, value)
        
BinaryTree_4 = BinaryTree_find(200)
BinaryTree_4.add(100)
BinaryTree_4.add(300)
BinaryTree_4.add(50)    
print(BinaryTree_4.find_node(5))
        
# 5- Escribe un programa que calcule la altura de un árbol binario.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_height:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def height(self):
        height = self.height_recursive(self.root)
        return F"the height of the tree is {height}"
    
    def height_recursive(self, node):
        if node is None:
            return 0
        left_height = self.height_recursive(node.left)
        right_height = self.height_recursive(node.right)
        return 1 + max(left_height, right_height)
    
BinaryTree_5 = BinaryTree_height(200)
BinaryTree_5.add(100)   
BinaryTree_5.add(300)
BinaryTree_5.add(50)
BinaryTree_5.add(150)
BinaryTree_5.add(355)
print(BinaryTree_5.height())

# 6- Crea un método que devuelva el nodo más pequeño.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_min:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def min_node(self):
        return self.min_recursive(self.root)
    
    def min_recursive(self, node):
        if node.left is None:
            return node.value
        return self.min_recursive(node.left)
    
BinaryTree_6 = BinaryTree_min(200)
BinaryTree_6.add(10)
BinaryTree_6.add(300)
BinaryTree_6.add(50)
BinaryTree_6.add(150)
BinaryTree_6.add(5)
BinaryTree_6.add(4)
print(BinaryTree_6.min_node())

# 7- Implementa un método que devuelva el nodo más grande.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_max:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def max_node(self):
        return self.max_recursive(self.root)
    
    def max_recursive(self, node):
        if node.right is None:
            return node.value
        return self.max_recursive(node.right)
    
BinaryTree_7 = BinaryTree_max(200)
BinaryTree_7.add(10)
BinaryTree_7.add(300)
BinaryTree_7.add(50)
BinaryTree_7.add(150)
BinaryTree_7.add(4)
print(BinaryTree_7.max_node())

# 8- Desarrolla un método que imprima el árbol en preorden.
# preorden: raiz, izquierda, derecha, se recorre el arbol de forma descendente
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_preorder:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def pre_order_traversal(self):
        self.pre_order_traversal(self.root)

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

BinaryTree_8 = BinaryTree_preorder(200)
BinaryTree_8.add(100)
BinaryTree_8.add(300)
BinaryTree_8.add(50)
BinaryTree_8.add(150)
BinaryTree_8.pre_order_traversal(BinaryTree_8.root)

# 9- Crea un método que imprima el árbol en postorden.
# postorden: izquierda, derecha, raiz, se recorre el arbol de forma descendente
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_postorder:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def post_order_traversal(self):
        self.post_order_traversal(self.root)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=" ")

BinaryTree_9 = BinaryTree_postorder(200)
BinaryTree_9.add(100)
BinaryTree_9.add(300)
BinaryTree_9.add(50)
BinaryTree_9.add(150)
BinaryTree_9.post_order_traversal(BinaryTree_9.root)

# 10- Escribe un programa que verifique si un árbol es un árbol binario de búsqueda.
# Un árbol binario de búsqueda (ABB) es un tipo especial de árbol binario que sigue estas reglas claves:
# Nodo raíz: Todo valor en el subárbol izquierdo es menor al valor del nodo actual (o raíz).
# Subárbol derecho: Todo valor en el subárbol derecho es mayor al valor del nodo actual.
# Subárboles recursivos: Ambos subárboles (izquierdo y derecho) también deben ser árboles binarios de búsqueda.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_search:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def is_binary_search_tree(self):
        return self.is_binary_search_tree_recursive(self.root, float("-inf"), float("inf"))
    
    def is_binary_search_tree_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value <= min_value or node.value >= max_value:
            return False
        return self.is_binary_search_tree_recursive(node.left, min_value, node.value) and self.is_binary_search_tree_recursive(node.right, node.value, max_value)
    
BinaryTree_10 = BinaryTree_search(200)
BinaryTree_10.add(100)
BinaryTree_10.add(300)
BinaryTree_10.add(50)   
BinaryTree_10.add(150)
print(BinaryTree_10.is_binary_search_tree()) 

# 11- Implementa un método que elimine un nodo de un árbol binario.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_delete:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def delete_node(self, value):
        self.delete_recursive(self.root, value)

    def delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self.delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self.delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self.min_recursive(node.right)
            node.right = self.delete_recursive(node.right, node.value)
        return node
    
    def min_recursive(self, node):
        if node.left is None:
            return node.value
        return self.min_recursive(node)
    
    def min_recursive(self, node):
        if node.left is None:
            return node.value
        return self.min_recursive(node.left)
    
    def print_tree(self):
        self.print_recursive(self.root)

    def print_recursive(self, node):
        if node is not None:
            self.print_recursive(node.left)
            print(node.value)
            self.print_recursive(node.right)

BinaryTree_11 = BinaryTree_delete(20)
BinaryTree_11.add(10)
BinaryTree_11.add(30)
BinaryTree_11.add(5)
BinaryTree_11.add(15)
BinaryTree_11.delete_node(15)
BinaryTree_11.print_tree()

# 12- Crea un método que imprima el nivel de cada nodo.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_level:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def print_level(self):
        self.print_recursive(self.root, 0)

    def print_recursive(self, node, level):
        if node is not None:
            self.print_recursive(node.left, level + 1)
            print(node.value, level)
            self.print_recursive(node.right, level + 1)

BinaryTree_12 = BinaryTree_level(200)
BinaryTree_12.add(100)
BinaryTree_12.add(300)
BinaryTree_12.add(50)
BinaryTree_12.add(150)
BinaryTree_12.print_level() 

# 13- Desarrolla un método que verifique si un árbol es balanceado.
# Un árbol binario está equilibrado si la diferencia de altura entre sus subárboles izquierdo y derecho es de 1 o menos.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_balanced:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def is_balanced(self):
        return self.is_balanced_recursive(self.root) != -1
    
    def is_balanced_recursive(self, node):
        if node is None:
            return 0
        left_height = self.is_balanced_recursive(node.left)
        right_height = self.is_balanced_recursive(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
    
BinaryTree_13 = BinaryTree_balanced(200)
BinaryTree_13.add(100)
#BinaryTree_13.add(300)
BinaryTree_13.add(50)
BinaryTree_13.add(150)
print(BinaryTree_13.is_balanced())

# 14- Crea un método que retorne el padre de un nodo dado.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_parent:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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

    def parent_node(self, value):
        return self.parent_recursive(self.root, value)
    
    def parent_recursive(self, node, value):
        if node is None:
            return None
        if node.left is not None and node.left.value == value:
            return node
        if node.right is not None and node.right.value == value:
            return node
        if value < node.value:
            return self.parent_recursive(node.left, value)
        else:
            return self.parent_recursive(node.right, value)
        
BinaryTree_14 = BinaryTree_parent(200)
BinaryTree_14.add(100)
BinaryTree_14.add(300)
BinaryTree_14.add(50)
BinaryTree_14.add(150)
print(BinaryTree_14.parent_node(150).value)

# 15- Implementa un método que imprima todos los nodos en un nivel dado.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree_level_nodes:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
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
    
    def print_level_nodes(self, level):
        self.print_recursive(self.root, level, 0)

    def print_recursive(self, node, level, current_level):
        if node is not None:
            if level == current_level:
                print(node.value)
            self.print_recursive(node.left, level, current_level + 1)
            self.print_recursive(node.right, level, current_level + 1)

BinaryTree_15 = BinaryTree_level_nodes(200)
BinaryTree_15.add(100)
BinaryTree_15.add(300)
BinaryTree_15.add(50)
BinaryTree_15.add(150)
BinaryTree_15.print_level_nodes(2)

# Mini Proyectos
# Desarrolla un programa que implemente un sistema de gestión de inventario utilizando árboles binarios.
class Node:
    def __init__(self, Article):
        self.Article = Article
        self.left = None
        self.right = None

class Inventory:
    def __init__(self, Article):
        self.root = Node(Article)
    
    def add(self, Article):
        self.add_recursive(self.root, Article)
    def add_recursive(self, node, Article):
        if Article < node.Article:
            if node.left is None:
                node.left = Node(Article)
            else:
                self.add_recursive(node.left, Article)
        else:
            if node.right is None:
                node.right = Node(Article)
            else:
                self.add_recursive(node.right, Article)

    def print_tree(self):
        self.print_recursive(self.root)

    def print_recursive(self, node):
        if node is not None:
            print(node.Article)
            self.print_recursive(node.left)
            self.print_recursive(node.right)

Inventory_1 = Inventory("Warehouse")
Inventory_1.add("Article 1")
Inventory_1.add("Article 2")
Inventory_1.add("Article 3")
Inventory_1.add("Article 4")
Inventory_1.add("Article 5")
Inventory_1.print_tree()

# Crea un simulador de un sistema de búsqueda de palabras en un diccionario utilizando árboles binarios.
class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class Dictionary:
    def __init__(self, word):
        self.root = Node(word)

    def add(self, word):
        self.add_recursive(self.root, word)

    def add_recursive(self, node, word):
        if word < node.word:
            if node.left is None:
                node.left = Node(word)
            else:
                self.add_recursive(node.left, word)
        else:
            if node.right is None:
                node.right = Node(word)
            else:
                self.add_recursive(node.right, word)

    def search(self, word):
        return self.search_recursive(self.root, word)
    
    def search_recursive(self, node, word):
        if node is None:
            return False
        if node.word == word:
            return True 
        if word < node.word:
            return self.search_recursive(node.left, word)
        else:
            return self.search_recursive(node.right, word)
        
Dictionary_1 = Dictionary("A")
Dictionary_1.add("B")
Dictionary_1.add("C")
Dictionary_1.add("D")
Dictionary_1.add("E")
print(Dictionary_1.search("D")) # True
print(Dictionary_1.search("F")) # False
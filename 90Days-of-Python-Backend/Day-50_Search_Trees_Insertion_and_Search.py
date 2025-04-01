# Día 25: Árboles de búsqueda: inserción y búsqueda

# Teoría
# Un árbol de búsqueda binaria (BST) es un árbol binario donde cada nodo tiene un valor mayor que todos los nodos en su subárbol izquierdo 
# y menor que los nodos en su subárbol derecho.

# Tips
# Mantén el árbol balanceado para asegurar un rendimiento óptimo.
# Implementa métodos de rotación si es necesario para mantener el equilibrio.

# Buenas Prácticas
# Documenta cada método para facilitar su comprensión y mantenimiento.
# Realiza pruebas para verificar la correcta implementación de los métodos.

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the BST while maintaining its properties."""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                self._insert_recursive(node.right, value) # lo valida por cada nivel de el arbol

    def search(self, value):
        """Searches for a value in the BST and returns the node if found."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def in_order(self):
        """Returns the values of the tree in ascending order."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

bst = BinarySearchTree()
values = [10, 5, 15, 2, 7, 12, 20]
for v in values:
    bst.insert(v)

# Searching for a node
found = bst.search(70)
print("Node found:", found.value if found else "Not found")

# Print the tree values in order
print("Tree in-order:", bst.in_order())

###############################

# Ejercicios

# 1- Implementa un árbol de búsqueda binaria y realiza inserciones.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST_1:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recursive_insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.recursive_insert(node.right, value)

    def see(self):
        aux = []
        self.recursive_see(self.root, aux)
        return aux
    
    def recursive_see(self, node, aux):
        if node:
            self.recursive_see(node.left, aux)
            aux.append(node.value)
            self.recursive_see(node.right, aux)

BST_one = BST_1()
data = [15, 19, 10, 7, 12, 17, 21]
for x in data:
    BST_one.Insert(x)
print(BST_one.see())

# 2- Crea un método para buscar un valor en el árbol de búsqueda.
class Node_1:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST_Search:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_1(value)
        self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:  # valor de el nodo
            if node.left is None:
                node.left = Node_1(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_1(value)
            else:
                self.insert_recursive(node.right, value)

    def see(self):
        aux = []
        self.see_recursive(self.root, aux)
        return aux
    
    def see_recursive(self, node, aux):
        if node:
            self.see_recursive(node.left, aux)
            aux.append(node.value)
            self.see_recursive(node.right, aux)

    def search(self, value):
        aux = self.search_recursive(self.root, value)
        if aux is None:
            return "I did not find the node"
        return aux
    
    def search_recursive(self, node, value):
        if node is None:  # Si no hay más nodos, el valor no se encuentra
            return None
        elif node.value == value:
            return node
        elif value < node.value:
            return self.search_recursive(node.left, value)
        return self.search_recursive(node.right, value)

BST_two = BST_Search()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_two.insert(i)
result = BST_two.search(21)
if result == "I did not find the node":
    print(result)
else:
    print("I found the node:", result.value)

# 3- Desarrolla un método para eliminar un nodo en el árbol de búsqueda.
class Node_2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Delete:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_2(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_2(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_2(value)
            else:
                self.insert_recursive(node.right, value)

    def see(self):
        aux = []
        self.recursive_see(self.root, aux)
        return aux
    
    def recursive_see(self, node, aux):
        if node:
            self.recursive_see(node.left, aux)
            aux.append(node.value)
            self.recursive_see(node.right, aux)

    def Delete(self, value):
        self.root = self.Delete_recursive(self.root, value)

    def Delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.Delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self.Delete_recursive(node.right, value)
        else:
            # Caso 1: Nodo sin hijos
            if node.left is None and node.right is None:
                return None
            # Caso 2: Nodo con un solo hijo
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Caso 3: Nodo con dos hijos
            else:
                min_larger_node = self.get_min(node.right)
                node.value = min_larger_node.value
                node.right = self.Delete_recursive(node.right, min_larger_node.value)
        return node

    def get_min(self, node):
        """Encuentra el nodo con el valor más bajo en un subárbol."""
        while node.left is not None:
            node = node.left
        return node
        
BST_three = BST_Delete()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_three.insert(i)
print(BST_three.see())
BST_three.Delete(21)
print(BST_three.see())

# 4- Implementa un recorrido en preorden, inorden y postorden.
class Node_3:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Order:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_3(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_3(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_3(value)
            else:
                self.insert_recursive(node.right, value)

    def inoerder(self):
        aux = []
        self.inorder_recursive(self.root, aux)
        return aux
    
    def inorder_recursive(self, node, aux):
        if node:
            self.inorder_recursive(node.left, aux)
            aux.append(node.value)
            self.inorder_recursive(node.right, aux)

    def preorder(self):
        aux = []
        self.preorder_recursive(self.root, aux)
        return aux
    
    def preorder_recursive(self, node, aux):
        if node:
            aux.append(node.value)
            self.preorder_recursive(node.left, aux)
            self.preorder_recursive(node.right, aux)

    def postorder(self):
        aux = []
        self.postorder_recursive(self.root, aux)
        return aux
    
    def postorder_recursive(self, node, aux):
        if node:
            self.postorder_recursive(node.left, aux)
            self.postorder_recursive(node.right, aux)
            aux.append(node.value)

BST_four = BST_Order()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_four.insert(i)

print(BST_four.inoerder())
print(BST_four.preorder())
print(BST_four.postorder())

# 5- Escribe un programa que verifique si un árbol es un árbol de búsqueda binaria.
class Node_4:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Check:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_4(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_4(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_4(value)
            else:
                self.insert_recursive(node.right, value)

    def check(self):
        return self.check_recursive(self.root, float("-inf"), float("inf"))
    
    def check_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value <= min_value or node.value >= max_value:
            return False
        return self.check_recursive(node.left, min_value, node.value) and self.check_recursive(node.right, node.value, max_value)
    
BST_five = BST_Check()
data = [15, 14, 10]
for i in data:
    BST_five.insert(i)
print(BST_five.check())

# 6- Crea un método que devuelva el nodo más pequeño en el árbol de búsqueda.
class Node_5:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Smallest:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_5(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_5(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_5(value)
            else:
                self.insert_recursive(node.right, value)

    def smallest(self):
        return self.smallest_recursive(self.root)
    
    def smallest_recursive(self, node):
        if node.left is None:
            return node
        return self.smallest_recursive(node.left)
    
BST_six = BST_Smallest()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_six.insert(i)
print(BST_six.smallest().value)

# 7- Implementa un método que devuelva el nodo más grande en el árbol de búsqueda.
class Node_6:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_MIN:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_6(value)
        else:
            self.insert_rescursive(self.root, value)

    def insert_rescursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_6(value)
            else:
                self.insert_rescursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_6(value)
            else:
                self.insert_rescursive(node.right, value)

    def largest(self):
        return self.largest_recursive(self.root)
    
    def largest_recursive(self, node):
        if node.right is None:
            return node
        return self.largest_recursive(node.right)
    
BST_seven = BST_MIN()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_seven.insert(i)
print(BST_seven.largest().value)
        
# 8- Desarrolla un método que imprima el árbol de búsqueda.
class Node_7:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Print:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_7(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_7(value)
            else:
                self.insert_recursive(node.left, value)

        else:
            if node.right is None:
                node.right = Node_7(value)
            else:
                self.insert_recursive(node.right, value)

    def print_tree(self):
        self.print_recursive(self.root)

    def print_recursive(self, node, level=0):
        if node:
            self.print_recursive(node.right, level + 2)
            print(" " * 4 * level + "->", node.value)
            self.print_recursive(node.left, level + 2)

BST_eight = BST_Print()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_eight.insert(i)
BST_eight.print_tree()

# 9- Crea un método que cuente el número de nodos en el árbol de búsqueda.
class Node_8:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Count:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_8(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_8(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_8(value)
            else:
                self.insert_recursive(node.right, value)

    def count(self):
        return self.count_recursive(self.root)
    
    def count_recursive(self, node):
        if node is None:
            return 0
        count = 1
        count += self.count_recursive(node.left)
        count += self.count_recursive(node.right)
        return count
    
BST_nine = BST_Count()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_nine.insert(i)
print(BST_nine.count())

# 10- Implementa un método que retorne el padre de un nodo dado.
class Node_9:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Parent:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_9(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_9(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_9(value)
            else:
                self.insert_recursive(node.right, value)

    def parent(self, value):
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
        return self.parent_recursive(node.right, value)
    
BST_ten = BST_Parent()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_ten.insert(i)
aux = BST_ten.parent(1)
if aux:
    print(aux.value)
else:
    print("The value is not in the tree")

# 11- Escribe un programa que imprima todos los nodos en un nivel dado.
class Node_10:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Level:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_10(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_10(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_10(value)
            else:
                self.insert_recursive(node.right, value)

    def level(self, level):
        return self.level_recursive(self.root, level)
    
    def level_recursive(self, node, level):
        if node is None:
            return
        if level == 0:
            print(node.value, end=" ")
        else:
            self.level_recursive(node.left, level - 1)
            self.level_recursive(node.right, level - 1)

BST_eleven = BST_Level()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_eleven.insert(i)
BST_eleven.level(0)

# 12- Crea un método que elimine duplicados en el árbol de búsqueda.
class Node_11:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Duplicates:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_11(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_11(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_11(value)
            else:
                self.insert_recursive(node.right, value)

    def remove_duplicates(self):
        self.remove_duplicates_recursive(self.root)

    def remove_duplicates_recursive(self, node):
        if node is None:
            return
        self.remove_duplicates_recursive(node.left)
        self.remove_duplicates_recursive(node.right)
        self.remove(node)

    def remove(self, node):
        if node is None:
            return
        if node.left is not None and node.value == node.left.value:
            node.left = None
        if node.right is not None and node.value == node.right.value:
            node.right = None

    def see(self):
        aux = []
        self.see_recursive(self.root, aux)
        return aux
    
    def see_recursive(self, node, aux):
        if node:
            self.see_recursive(node.left, aux)
            aux.append(node.value)
            self.see_recursive(node.right, aux)

BST_twelve = BST_Duplicates()
data = [15, 19, 10, 7, 12, 17, 21, 21, 12]
for i in data:
    BST_twelve.insert(i)
BST_twelve.remove_duplicates()
print(BST_twelve.see())

# 13- Implementa un método que verifique si un árbol de búsqueda es balanceado.
class Node_12:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Balance:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_12(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_12(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_12(value)
            else:
                self.insert_recursive(node.right, value)

    def is_balanced(self):
        return self.is_balanced_recursive(self.root) != -1
    
    def is_balanced_recursive(self, node):
        if node is None:
            return 0
        left = self.is_balanced_recursive(node.left)
        right = self.is_balanced_recursive(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
BST_thirteen = BST_Balance()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_thirteen.insert(i)
print(BST_thirteen.is_balanced())

# 14- Crea un método que retorne el nivel de un nodo dado en el árbol de búsqueda.
class Node_13:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_Level_Node:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node_13(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node_13(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node_13(value)
            else:
                self.insert_recursive(node.right, value)

    def level(self, value):
        return self.level_recursive(self.root, value, 0)
    
    def level_recursive(self, node, value, level):
        if node is None:
            return -1
        if node.value == value:
            return level
        left = self.level_recursive(node.left, value, level + 1)
        right = self.level_recursive(node.right, value, level + 1)
        return max(left, right)
    
BST_fourteen = BST_Level_Node()
data = [15, 19, 10, 7, 12, 17, 21]
for i in data:
    BST_fourteen.insert(i)
print(BST_fourteen.level(15))

# Mini Proyectos
# Desarrolla un programa que implemente un sistema de gestión de contactos utilizando árboles de búsqueda.
class Node_14:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class BST_Contacts:
    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        if self.root is None:
            self.root = Node_14(name, phone)
        else:
            self.insert_recursive(self.root, name, phone)

    def insert_recursive(self, node, name, phone):
        if name < node.name:
            if node.left is None:
                node.left = Node_14(name, phone)
            else:
                self.insert_recursive(node.left, name, phone)
        else:
            if node.right is None:
                node.right = Node_14(name, phone)
            else:
                self.insert_recursive(node.right, name, phone)

    def see(self):
        aux = []
        self.see_recursive(self.root, aux)
        return aux
    
    def see_recursive(self, node, aux):
        if node:
            self.see_recursive(node.left, aux)
            aux.append((node.name, node.phone))
            self.see_recursive(node.right, aux)

Bst_cont = BST_Contacts()
data = [("Eric", 123456), ("Helen", 654321), ("Edwards", 987654)]
for i, j in data:
    Bst_cont.insert(i, j)
print(Bst_cont.see())

# Crea un simulador de un sistema de recomendaciones de productos basado en un árbol de búsqueda.
class Node_15:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class BST_Recommendations:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = Node_15(product)

        else:
            self.insert_recursive(self.root, product)

    def insert_recursive(self, node, product):
        if product < node.product:
            if node.left is None:
                node.left = Node_15(product)
            else:
                self.insert_recursive(node.left, product)
        else:
            if node.right is None:
                node.right = Node_15(product)
            else:
                self.insert_recursive(node.right, product)

    def see(self):
        aux = []
        self.see_recursive(self.root, aux)
        return aux
    
    def see_recursive(self, node, aux):
        if node:
            self.see_recursive(node.left, aux)
            aux.append(node.product)
            self.see_recursive(node.right, aux)

Bst_recom = BST_Recommendations()
data = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
for i in data:
    Bst_recom.insert(i)
print(Bst_recom.see())
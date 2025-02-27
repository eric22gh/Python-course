# Introducción a Árboles
# Un árbol es una estructura de datos que se organiza de manera jerárquica. Imagina un árbol real: 
# tiene un tronco (la raíz) y ramas que se extienden hacia afuera (los nodos hijos). 

# En programación, los árboles se utilizan para representar relaciones jerárquicas, como:
# 1- Estructuras de carpetas en un sistema operativo.
# 2- Jerarquías organizacionales en una empresa.
# 3- Árboles de decisión en inteligencia artificial.

# Conceptos Básicos
# Nodo(value): Es la unidad básica de un árbol. Cada nodo puede contener un valor y puede tener cero o más nodos hijos.
# Raíz(es el primero que se agrega): Es el nodo superior del árbol. No tiene padres.
# Hijos(despues del nodo padre o raiz): Son los nodos que están directamente conectados a otro nodo que se llama padre.
# Hoja(ultimo nodo): Es un nodo que no tiene hijos. Es el final de una rama.
# Altura(conteo de nodos): La altura de un árbol es la longitud del camino más largo desde la raíz hasta una hoja.

# Tipos de Árboles
# Árbol Binario: Cada nodo tiene como máximo dos hijos (izquierdo y derecho).
# Árbol N-ario: Cada nodo puede tener hasta N hijos.
# Árbol de Búsqueda Binaria (ABB): Un tipo especial de árbol binario donde los nodos a la izquierda son menores y los nodos a la derecha son mayores que el nodo padre.

# Ejemplo: 
class Node_tree:
    def __init__(self, value):
        """Inicializa un nodo con un valor y una lista de hijos."""
        self.value = value
        self.sons = []

class Tree: # arbol
    def __init__(self, value):
        """Inicializa el árbol con una raíz."""
        self.root = Node_tree(value) # Nodo padre o raiz

    def add_son(self, father_node, value): # hijos 
        """Agrega un nuevo hijo al nodo padre especificado."""
        new_song = Node_tree(value)
        father_node.sons.append(new_song)

    def see_tree(self, node=None, level=0):
        """Muestra el árbol de forma jerárquica."""
        if node is None:
            node = self.root
        print(' ' * level * 3 + str(node.value))
        for son in node.sons:
            self.see_tree(son, level + 1)

    def is_empty(self):
        """Verifica si el árbol esta vacio."""
        return self.root is None
    
    def get_root(self):
        """Devuelve la raíz del árbol."""
        return f"La raiz del arbol es: {self.root.value}"
    
    def get_nodes(self):
        """Devuelve la cantidad de nodos del árbol."""
        return f"La cantidad de nodos del arbol es: {len(self.root.sons)}"
    
    def delete_node(self, node):
        """Elimina un nodo del árbol."""
        self.root.sons.remove(node)

# Uso del árbol
arbol = Tree(1)  # Creamos un árbol con raíz 1
arbol.add_son(arbol.root, 2)  # Agregamos un hijo 2 a la raíz
arbol.add_son(arbol.root, 3)  # Agregamos un hijo 3 a la raíz
arbol.add_son(arbol.root.sons[0], 4)  # Agregamos un hijo que es 4, al nodo 2, la posicion en la que esta 2 en la lista es 0
arbol.add_son(arbol.root.sons[0], 6)
arbol.add_son(arbol.root.sons[1], 5)  # Agregamos un hijo que es 5, al nodo 3, la posicion en la que esta 3 en la lista es 1
arbol.add_son(arbol.root.sons[1], 10)
arbol.see_tree()

# Ejercicios
# 1- Implementa un árbol y agrega nodos.
class Node_1:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree:
    def __init__(self, value):
        self.root = Node_1(value)

    def is_empty(self):
        return self.root == None
    
    def add_son(self, father_node, value):
        new_node = Node_1(value)
        father_node.sons.append(new_node)

    def see_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux_sons in node.sons:
            self.see_tree(aux_sons, level + 1)

    def delete_node(self, node_to_delete, parent=None):
        if parent is None:
            parent = self.root
        for child in parent.sons:
            if child == node_to_delete:
                parent.sons.remove(child)
                return True
            if self.delete_node(node_to_delete, child):
                return True
        return False
        
B_tree = tree(8)
B_tree.add_son(B_tree.root, 7)
B_tree.add_son(B_tree.root, 6)
B_tree.add_son(B_tree.root, 5)
B_tree.add_son(B_tree.root.sons[0], 20)
B_tree.add_son(B_tree.root.sons[1], 21)
B_tree.add_son(B_tree.root.sons[2], 22)
B_tree.add_son(B_tree.root.sons[2], 23)
B_tree.delete_node(22, B_tree.root) # borra los hijos, no puede solo borrar el hijo(hoja, ultimo nodo)
B_tree.see_tree()

# 2- Crea un método para imprimir todos los nodos de un árbol.
class Node_2:
    # we create the node, with the value that will be the first node
    def __init__(self, value):
        self.value = value
        self.list_sons = []

class tree_2:
    # we create the tree, with the value that will be the root
    def __init__(self, value):
        self.root = Node_2(value)

    def is_empty(self):
        return self.root == None
    
    def add_son(self, father_node, value):
        new_node = Node_2(value)
        father_node.list_sons.append(new_node)

    def see_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux_sons in node.list_sons:
            self.see_tree(aux_sons, level + 1)

C_tree = tree_2(8)
C_tree.add_son(C_tree.root, 20)
C_tree.add_son(C_tree.root, 30)
C_tree.add_son(C_tree.root.list_sons[0], 21)
C_tree.add_son(C_tree.root.list_sons[0], 22)
C_tree.add_son(C_tree.root.list_sons[1], 31)
C_tree.add_son(C_tree.root.list_sons[1], 32)
C_tree.see_tree()

# 3- Desarrolla un método que cuente el número de hojas en un árbol.
class Node_3:
    def __init__(self, value):
        self.value = value
        self.list_sons = []

class tree_3:
    def __init__(self, value):
        self.root = Node_3(value)

    def is_empty(self):
        return self.root == None
    
    def add_son(self, father_node, value):
        new_node = Node_3(value)
        father_node.list_sons.append(new_node)

    def see_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux_sons in node.list_sons:
            self.see_tree(aux_sons, level + 1)

    def count_leaves(self, node=None):
        if node is None:
            node = self.root
        if node.list_sons == []:
            return 1
        count = 0
        for aux_sons in node.list_sons:
            count += self.count_leaves(aux_sons)
        return count

D_tree = tree_3(22)
D_tree.add_son(D_tree.root, 40)
D_tree.add_son(D_tree.root, 50)
D_tree.add_son(D_tree.root, 60)
D_tree.add_son(D_tree.root.list_sons[0], 41)
D_tree.add_son(D_tree.root.list_sons[0], 51)
print(f"The number of leaves is: {D_tree.count_leaves()}")

# 4- Implementa un método para encontrar la altura de un árbol.
class Node_4:
    def __init__(self, value):
        self.value = value
        self.list_sons = []

class tree_4:
    def __init__(self, value):
        self.root = Node_4(value)
        # se agrega un valor a la raiz

    def Is_empty(self):
        return self.root is None
    
    def add_son(self, father, value):
        new_node = Node_4(value)
        father.list_sons.append(new_node)

    def see_tree(self, node=None, level = 0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.list_sons:
            self.see_tree(aux, level + 1)

    def height_of_tree(self, node=None):
        if node is None:
            node = self.root
        if not node.list_sons:
            return 1
        else:
            var = [self.height_of_tree(aux) for aux in node.list_sons]
            return 1 + max(var)
    
f_tree = tree_4(5)
f_tree.add_son(f_tree.root, 100)
f_tree.add_son(f_tree.root, 200)
f_tree.add_son(f_tree.root.list_sons[0], 10)
f_tree.add_son(f_tree.root.list_sons[1], 200)
print(f"The height of the tree is: {f_tree.height_of_tree(f_tree.root)}")

# 5- Escribe un programa que verifique si un árbol está vacío.
class Node_5:
    def __init__(self, value):
        self.value = value
        self.list_sons = []

class tree_5:
    def __init__(self, value):
        self.root = Node_5(value)

    def is_empty(self):
        return self.root is None
    
    def add_son(self, father, value):
        try:
            aux = Node_5(value)
            father.list_sons.append(value)
        except Exception as E:
            return f"An Error Happend: {E}"

h_tree = tree_5(100)  
h_tree.add_son(h_tree.root, 9)   
h_tree.add_son(h_tree.root, 19)
h_tree.add_son(h_tree.root.list_sons[0], 10)   
h_tree.add_son(h_tree.root.list_sons[1], 20)  
print(h_tree.is_empty()) 
        
# 6- Crea un método que encuentre el nodo raíz.
class Node_6:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_6:
    def __init__(self, value):
        self.root = Node_6(value)
    
    def is_empty(self):
        self.root is None

    def add(self, father, value):
        aux = Node_6(value)
        father.sons.append(aux)

    def found_root(self):
        return self.root.value
    
    def see_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.see_tree(aux, level + 1)
    
h_tree = tree_6(22)
h_tree.add(h_tree.root, 25)
h_tree.add(h_tree.root, 55)
h_tree.add(h_tree.root.sons[0], 26)
print(f"The root node from the tree is: {h_tree.found_root()}")

# 7- Implementa un método que retorne el número de nodos en un árbol.
class Node_7:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_7:
    def __init__(self, value):
        self.root = Node_7(value)
    
    def is_empty(self):
        return self.root is None

    def add(self, father, value):
        aux = Node_7(value)
        father.sons.append(aux)

    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        if not node.sons:
            return 1
        else:
            var = [self.count_nodes(aux) for aux in node.sons]
            return 1 + sum(var)
        
    def see_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.see_tree(aux, level + 1)

g_tree = tree_7(3)
g_tree.add(g_tree.root, 4)
g_tree.add(g_tree.root, 5)
g_tree.add(g_tree.root, 6)
print(f"The number of nodes in the tree is: {g_tree.count_nodes()}")

# 8- Desarrolla un método que imprima los hijos de un nodo dado.
class Node_8:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_8:
    def __init__(self, value):
        self.root = Node_8(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_8(value)
        return father.sons.append(aux)
    
    def print_sons(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.print_sons(aux, level + 1)
j_tree = Tree_8(700)
j_tree.add(j_tree.root, 7)
j_tree.add(j_tree.root, 77)
j_tree.add(j_tree.root, 37)
j_tree.add(j_tree.root.sons[0],21)
j_tree.add(j_tree.root.sons[1],87)
j_tree.add(j_tree.root.sons[2],47)
j_tree.print_sons()

# 9- Crea un método que busque un valor en el árbol.
class Node_9:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_9:
    def __init__(self, value):
        self.root = Node_9(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_9(value)
        return father.sons.append(aux)
    
    def search(self, node=None, value=None):
        if node is None:
            node = self.root
        if node.value == value:
            return node.value
        for aux in node.sons:
            result = self.search(aux, value)
            if result is not None:
                return f"You found the value: {result} in the tree"
        return None

j_tree = Tree_9(00)
j_tree.add(j_tree.root, 10)
j_tree.add(j_tree.root, 27)
j_tree.add(j_tree.root, 57)
j_tree.add(j_tree.root.sons[0],201)
j_tree.add(j_tree.root.sons[1],807)
j_tree.add(j_tree.root.sons[2],407)
print(j_tree.search(j_tree.root, 10))

# 10- Implementa un método que devuelva el padre de un nodo dado.
class Node_10:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_10:
    def __init__(self, value):
        self.root = Node_10(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_10(value)
        return father.sons.append(aux)
    
    def return_father(self, node=None, value=None):
        if node is None:
            node = self.root
        if node.value == value:
            return node.value
        for aux in node.sons:
            result = self.return_father(aux, value)
            if result is not None:
                return f"You found the value: {result} in the tree"
        return None

j_tree = Tree_10(00)
j_tree.add(j_tree.root, 10)
j_tree.add(j_tree.root, 27) 
j_tree.add(j_tree.root, 57)
j_tree.add(j_tree.root.sons[0],201)
j_tree.add(j_tree.root.sons[1],807)                                    
j_tree.add(j_tree.root.sons[2],407)
print(j_tree.return_father(j_tree.root, 27))   

# 11- Escribe un programa que imprima el camino desde la raíz hasta una hoja.
class Node_11:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_11:
    def __init__(self, value):
        self.root = Node_11(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_11(value)
        return father.sons.append(aux)
    
    def print_path(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.print_path(aux, level + 1)
j_tree = Tree_11(100)
j_tree.add(j_tree.root, 71)
j_tree.add(j_tree.root, 700)
j_tree.add(j_tree.root, 300)
j_tree.add(j_tree.root.sons[0], 21)
j_tree.add(j_tree.root.sons[1],  87)
j_tree.print_path()

# 12- Crea un método que elimine un nodo de un árbol.
class Node_12:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_12:
    def __init__(self, value):
        self.root = Node_12(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_12(value)
        return father.sons.append(aux)
    
    def delete_node(self, parent=None, node=None, value=None): # función eliminar_nodo(padre, nodo, valor)
        if node is None: # si nodo es nulo
            node = self.root # nodo ← raíz del árbol(valor)
        if node.value == value: # si nodo.valor es igual a valor
            if parent is not None: # si padre no es nulo
                parent.sons.remove(node) # eliminar nodo de la lista de hijos de padre
            return node.value # retornar nodo.valor
        for aux in node.sons: # para cada hijo en nodo.hijos
            result = self.delete_node(node, aux, value) # resultado ← eliminar_nodo(nodo, hijo, valor)
            if result is not None: # si resultado no es nulo
                return f"Valor eliminado: {result}" # retornar "Valor eliminado: " + resultado
        return None # retornar nulo
    
    def see(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for son in node.sons:
            self.see(son, level + 1)

j_tree = Tree_12(200)
j_tree.add(j_tree.root, 71)
j_tree.add(j_tree.root, 700)
j_tree.add(j_tree.root, 300)
j_tree.add(j_tree.root.sons[0], 21)
j_tree.add(j_tree.root.sons[1],  87)
j_tree.delete_node(None, j_tree.root, 700) # si se borra un nodo con hijos, ellos se borran tambien
j_tree.see()
        
# 13- Implementa un método que devuelva el nivel de un nodo dado.
class Node_13:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_13:
    def __init__(self, value):
        self.root = Node_13(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_13(value)
        return father.sons.append(aux)
    
    def found_level(self, node=None, value=None, level=0):
        if node is None:
            return -1
        if node.value == value:
            return level
        for aux in node.sons:
            song_level = self.found_level(aux, value, level + 1)
            if song_level != -1:
                return song_level
        return -1
    
    def see(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for son in node.sons:
            self.see(son, level + 1)

j_tree = tree_13(200)
j_tree.add(j_tree.root, 71)
j_tree.add(j_tree.root, 11)
j_tree.add(j_tree.root, 300)
j_tree.add(j_tree.root.sons[0], 21)
j_tree.add(j_tree.root.sons[1],  87)
level = j_tree.found_level(j_tree.root, 87, 0)
if level != -1:
    print(f"the level is: {level}")
else:
    print("the level is not found")


# 14- Desarrolla un método que imprima el árbol en formato de lista.
class Node_14:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_14:
    def __init__(self, value):
        self.root = Node_14(value)
    
    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_14(value)
        return father.sons.append(aux)
    
    def print_tree(self, node=None, list_tree = None):
        if list_tree is None:
            list_tree = []   
        if node is None:
            return list_tree
        list_tree.append(node.value)
        for aux in node.sons:
            self.print_tree(aux, list_tree)
        return list_tree
    
k_tree = tree_14(1)
k_tree.add(k_tree.root, 2)
k_tree.add(k_tree.root, 3)
k_tree.add(k_tree.root, 4)
k_tree.add(k_tree.root.sons[0], 5)
k_tree.add(k_tree.root.sons[1], 6)
k_tree.add(k_tree.root.sons[2], 7)
print(k_tree.print_tree(k_tree.root))

# 15- Crea un método que verifique si un árbol es completo.
# arbol lleno: es un árbol binario donde todos los nodos no hojas tienen exactamente dos hijos y todas las hojas están en el mismo nivel.
# Un árbol completo es un tipo de árbol binario en el que todos los niveles, excepto posiblemente el último, están completamente llenos, 
# y todos los nodos del último nivel están tan a la izquierda como sea posible.
class Node_15:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_15:
    def __init__(self, value):
        self.root = Node_15(value)
    
    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_15(value)
        return father.sons.append(aux)
    
    def is_full(self, node=None):
        if node is None:
            return True
        if len(node.sons) == 0:
            return True
        if len(node.sons) == 2:
            return self.is_full(node.sons[0]) and self.is_full(node.sons[1])
        return False
    
l_tree = tree_15(1)
l_tree.add(l_tree.root, 2)
l_tree.add(l_tree.root, 3)
l_tree.add(l_tree.root.sons[0], 5)
l_tree.add(l_tree.root.sons[0], 6)
l_tree.add(l_tree.root.sons[1], 8)
l_tree.add(l_tree.root.sons[1], 7)
print(l_tree.is_full(l_tree.root))

# Mini Proyectos
# Desarrolla un programa que gestione una estructura de carpetas utilizando árboles.
class Node_folder:
    def __init__(self, value):
        self.value = value
        self.sons = []

class tree_folder:
    def __init__(self, value):
        self.root = Node_folder(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_folder(value)
        return father.sons.append(aux)
    
    def see(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.see(aux, level + 1)

m_tree = tree_folder("C:")
m_tree.add(m_tree.root, "Users")
m_tree.add(m_tree.root, "Program Files")
m_tree.add(m_tree.root, "Windows")
m_tree.add(m_tree.root.sons[0], "User1")
m_tree.add(m_tree.root.sons[0], "User2")
m_tree.add(m_tree.root.sons[1], "Python")
m_tree.add(m_tree.root.sons[1], "Java")
m_tree.see()
   
# Crea un simulador de un sistema de organización jerárquica de empleados.
class Node_employee:
    def __init__(self, value):
        self.value = value
        self.sons = []

class Tree_employee:
    def __init__(self, value):
        self.root = Node_employee(value)

    def is_empty(self):
        return self.root is None
    
    def add(self, father, value):
        aux = Node_employee(value)
        return father.sons.append(aux)
    
    def see(self, node=None, level = 0):
        if node is None:
            node = self.root
        print(" " * level * 3 + str(node.value))
        for aux in node.sons:
            self.see(aux, level + 1)

n_tree = Tree_employee("CEO")
n_tree.add(n_tree.root, "Manager")
n_tree.add(n_tree.root, "Manager 2")
n_tree.add(n_tree.root.sons[0], "Supervisor")
n_tree.add(n_tree.root.sons[0], "Supervisor 2")
n_tree.add(n_tree.root.sons[1], "Supervisor 3")
n_tree.add(n_tree.root.sons[1], "Supervisor 4")
n_tree.see()
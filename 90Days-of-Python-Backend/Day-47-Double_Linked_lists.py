# Día 22: Listas enlazadas dobles
# Teoría: Las listas enlazadas dobles permiten la navegación en ambas direcciones, ya que cada nodo tiene referencias tanto al siguiente como al anterior.

# Imagina que tienes una cadena de bloques, pero esta vez, cada bloque tiene dos cuerdas:
# Una cuerda que lo conecta con el siguiente bloque (como en la lista enlazada simple) y Otra cuerda que lo conecta con el bloque anterior.
# Esto significa que puedes ir hacia adelante y hacia atrás en la cadena. ¡Es como tener un camino en ambas direcciones!

# Tips
# 1- Asegúrate de actualizar ambos punteros al agregar o eliminar nodos.
# 2- Considera el uso de listas dobles para aplicaciones que requieren navegación bidireccional.
# 3- Cuidado con las cuerdas: Cuando agregues o quites bloques, asegúrate de que ambas cuerdas (punteros) estén bien conectadas. 
# Si no, ¡puedes perderte en la cadena!
# 4- Usa listas dobles cuando necesites ir en dos direcciones: Si tu aplicación necesita moverse hacia adelante y hacia atrás, 
# las listas enlazadas dobles son una buena opción.

# Buenas Prácticas
# Realiza pruebas exhaustivas para garantizar que ambas direcciones de la lista funcionen correctamente.
# Documenta cada método para facilitar el mantenimiento.

# Lista doblemente enlazada: Cada bloque apunta al siguiente bloque y al bloque anterior.
# Ejemplo: Ninguno ← Bloque 1 ↔ Bloque 2 ↔ Bloque 3 → Ninguno
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first == None # si el first de la lista(var) es nada, returna true
    
    def last_add(self, data):
        if self.is_empty():
            self.first = self.last = Node(data) # si la lista esta vacia, el first va a ser igual al last
        else:
            aux = self.last # aux va a tener el last valor de la lista
            self.last = aux.next = Node(data) # el last valor de la lista va a ser igual al siguiente valor de aux
            self.last.prev = aux # el valor anterior del last valor de la lista va a ser igual a aux
        self.size += 1 # aumentar el tamaño de la lista

    def inicial_add(self, data):
        if self.is_empty():
            self.first = self.last = Node(data) # si la lista esta vacia, el first va a ser igual al last
        else:
            aux = Node(data)
            aux.next = self.first # el siguiente valor de aux va a ser igual al first de la lista
            self.first.prev = None # el valor anterior del first de la lista va a ser igual a aux
            self.first = aux # el first de la lista va a ser igual a aux
        self.size += 1 # aumentar el tamaño de la lista

    def inicial_see(self):
        aux = self.first # aux va a tener el primer valor de la lista
        while aux != None: # mientras que aux no tenga valor
            print(aux.data, end=" -- ") # imprimir el valor de aux
            aux = aux.next # moverse al siguiente valor de la lista

    def final_see(self):
        aux = self.last # aux va a tener el last valor de la lista
        while aux != None: # mientras que aux no tenga valor
            print(aux.data, end=" -- ") # imprimir el valor de aux
            aux = aux.prev # moverse al valor anterior de la lista

    def size(self):
        return self.size # retornar el tamaño de la lista
    
    def inicial_delete(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
            self.size = 0
        else:
            self.first = self.first.next
            self.first.prev = None
            self.size -= 1

    def final_delete(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
            self.size = 0
        else:
            self.last = self.last.prev
            self.last.next = None
            self.size -= 1

double_linked_list = DoubleLinkedList()
double_linked_list.last_add(1)
double_linked_list.last_add(2)
double_linked_list.last_add(3)
double_linked_list.last_add(0)
double_linked_list.inicial_see()
print("\n")

# Ejercicios

# 1- Implementa una lista enlazada doble y realiza operaciones para agregar elementos.
class Node_1:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_1(value)
        else:
            aux = Node_1(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is anything to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

list_1 = DoubleList()
list_1.add(5)
list_1.add(21)
list_1.add(56)
list_1.add(1)
list_1.see()

# 2- Crea un método para eliminar un nodo específico de la lista doble.
print("\n")
class Node_2:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleList_2:
    def __init__(self):
        self.first = None
        self.last = None
    
    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_2(value)
        else:
            aux = Node_2(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete_node(self, value):
        if self.is_empty():
            return "There is nothing to delete."
        aux = self.first
        while aux:
            if aux.value == value:
                if aux.prev:
                    aux.prev.next = aux.next
                else:
                    self.first = aux.next
                if aux.next:
                    aux.next.prev = aux.prev
                else:
                    self.last = aux.prev 
                return f"Node with value {value} has been deleted."
            aux = aux.next
        return "The value is not in the list"
    
    def see(self):
        if self.is_empty():
            return "There is anything to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

list_2 = DoubleList_2()
list_2.add(25)
list_2.add(121)
list_2.add(6)
list_2.add(11)
print(list_2.delete_node(6))
list_2.see()

# 3- Escribe un método para buscar un valor en la lista doble.
class Node_3:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleList_3:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_3(value)
        else:
            aux = Node_3(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux 

    def search(self, value):
        if self.is_empty():
            return "There is nothing to search."
        aux = self.first
        while aux:
            if aux.value == value:
                return f"You found the Value {value} in the list."
            aux = aux.next
        return f"the Value: {value} is not in the list."
    
    def see(self):
        if self.is_empty():
            return "There is anything to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def delete(self):
        if self.is_empty():
            return "there is nothing to delete."
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def final_delete(self):
        if self.is_empty():
            return "there is nothing to delete."
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None

list_3 = DoubleList_3()
list_3.add(5)
list_3.add(2)
list_3.add(6)
list_3.add(10)
print(list_3.search(6))
list_3.delete()
list_3.final_delete()
print(list_3.see())

# 4- Implementa un método para insertar un nodo en una posición específica en la lista doble.
class node_4:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doublelist_4:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = node_4(value)
        else:
            aux = node_4(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def final_delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None

    def insert(self, value, position):
        aux = self.first
        cont = 0
        while aux != None:
            cont += 1
            if cont == position:
                aux.value = value
            aux = aux.next

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> " )
            aux = aux.next

list_4 = doublelist_4()
list_4.add(4)
list_4.add(8)
list_4.add(3)
list_4.add(7)
list_4.insert(5, 3)
print(list_4.see())

# 5- Desarrolla un método que recorra la lista en reversa.
class Node_5:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class Reverse_list:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_5(value)
        else:
            aux = Node_5(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see_reverse(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.last
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.prev

list_5 = Reverse_list()
list_5.add(11)
list_5.add(110)
list_5.add(16)
list_5.add(18)
print(list_5.see_reverse())

# 6- Crea un método que cuente el número de nodos en la lista doble.
class Node_6:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class count_list:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_6(value)
        else:
            aux = Node_6(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.next

    def count_nodes(self):
        if self.is_empty():
            return "there is nothing to count in the list"
        aux = self.first
        cont = 0
        while aux != None:
            cont += 1
            aux = aux.next
        return f"The Number of nodes in the list is: {cont}"

list_5 = count_list()
list_5.add(11)
list_5.add(110)
list_5.add(16)
list_5.add(18)
print(list_5.count_nodes())

# 7- Implementa un método que devuelva el primer nodo de la lista.
class Node_7:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class first_node:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_6(value)
        else:
            aux = Node_6(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.next

    def first_node(self):
        if self.is_empty():
            return "The list is empty"
        aux = self.first
        return f"the first node from the list is: {aux._value}"

list_6 = first_node()
list_6.add(16)
list_6.add(116)
list_6.add(162)
list_6.add(8)
print(list_6.first_node())

# 8- Escribe un programa que combine dos listas dobles.
class Node_8:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class combine_list:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_8(value)
        else:
            aux = Node_8(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.next

    def combine(self, list_1, list_2):
        aux = list_1.first
        while aux.next != None:
            aux = aux.next
        aux.next = list_2.first
        list_2.first.prev = aux
        return list_1
    
list_7 = combine_list()
list_7.add(16) 
list_7.add(116)
list_7.add(162)
list_7.add(8)
list_8 = combine_list()
list_8.add(56)
list_8.add(156)
list_8.add(165)
list_8.add(18)
print(list_8.combine(list_7, list_8).see())

# 9- Crea un método que elimine duplicados en la lista doble.
class Node_9:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class delete_duplicates:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_9(value)
        else:
            aux = Node_9(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.next

    def delete_duplicates(self):
        if self.is_empty():
            return "There is nothing to delete in the list"
        aux = self.first
        while aux != None:
            aux_2 = aux.next
            while aux_2 != None:
                if aux._value == aux_2._value:
                    aux_2.prev.next = aux_2.next
                    if aux_2.next:
                        aux_2.next.prev = aux_2.prev
                aux_2 = aux_2.next
            aux = aux.next
        return self
    

list_9 = delete_duplicates()
list_9.add(16)
list_9.add(16)
list_9.add(162)
print(list_9.delete_duplicates().see())

# 10- Implementa un método que verifique si la lista doble está vacía.
class Node_10:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

class empty_list:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_10(value)
        else:
            aux = Node_10(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is nothing to see in the list"
        aux = self.first
        while aux != None:
            print(aux._value, end=" <-> ")
            aux = aux.next

    def empty(self):
        if self.is_empty():
            return "The list is empty"
        return "The list is not empty"
    
list_10 = empty_list()
print(list_10.empty())
list_10.add(16)
list_10.add(116)
list_10.add(162)
print(list_10.empty())

# 11- Desarrolla un método que retorne el último nodo de la lista doble.
class Node_11:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinked:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_11(value)
        else:
            aux = Node_11(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def last_node(self):
        if self.is_empty():
            return "There is no node in the list"
        aux = self.last
        return f"the last node from the list is: {aux.value}"
    
list_11 = DoubleLinked()
list_11.add("Eric")
list_11.add("Edwards")
list_11.add("Brenes")
list_11.add("Calvin")
list_11.see()
print(list_11.last_node())

# 12- Crea un método que imprima los nodos de la lista en orden inverso.
class Node_12:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinked_revert:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_11(value)
        else:
            aux = Node_11(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def reverted(self):
        if self.is_empty():
            return "There is nothing to revert"
        aux = self.last
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.prev

list_12 = DoubleLinked_revert()
list_12.add(1.2)
list_12.add("helen")
list_12.add(2.100)
list_12.add(True)
print(list_12.reverted())

# 13- Escribe un programa que cuente cuántas veces aparece un valor en la lista doble.
class Node_13:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinked_count:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_11(value)
        else:
            aux = Node_11(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def count_value(self, item):
        if self.is_empty():
            return "There is no value to count in the list"
        else:
            aux = self.first
            cont = 0
            while aux != None:
                if aux.value == item:
                    cont += 1
                aux = aux.next
            return f"You count: {cont} indentics values of {item} in the list"
list_13 = DoubleLinked_count()
list_13.add("eric")
list_13.add("25")
list_13.add("eric")
list_13.add("eric")
list_13.add("1.2")
print(list_13.count_value("eric"))

# 14- Implementa un método que devuelva el nodo anterior a un valor dado.
class Node_14:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinked_before:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_11(value)
        else:
            aux = Node_11(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def node_before(self, item):
        if self.is_empty():
            return "There is no node to return in the list"
        aux = self.first
        while aux.next and aux.next.value != item:
            aux = aux.next
        if aux.next:
            return f"the node before: {item} is: {aux.value}"
        return None
list_14 = DoubleLinked_before()
list_14.add(78)
list_14.add(8)
list_14.add(28)
list_14.add(98)
print(list_14.node_before(78))

# 15- Crea un método que retorne la posición de un valor dado en la lista doble.
class Node_15:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinked_position:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_11(value)
        else:
            aux = Node_11(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.value, end=" <-> ")
            aux = aux.next

    def return_position(self, node):
        if self.is_empty():
            return "The list is empty"
        aux = self.first
        position = 0
        while aux != None:
            position += 1
            if aux.value == node:
                return f"the position in the list of the node: {aux.value} is {position}"
            aux = aux.next
        return f"the node: {node} is not in the list"

list_15 = DoubleLinked_position()
list_15.add(8)
list_15.add(7)
list_15.add(1)
list_15.add(87)
print(list_15.see())
print(list_15.return_position(8))

# Mini Proyectos
# Desarrolla un gestor de contactos donde cada contacto se almacene en una lista doble.
class Node_16:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None
        self.prev = None

class DoubleLinked_contacts:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, name, phone):
        if self.is_empty():
            self.first = self.last = Node_16(name, phone)
        else:
            aux = Node_16(name, phone)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.name, aux.phone, end=" <-> ")
            aux = aux.next

    def search(self, name):
        if self.is_empty():
            return "There is nothing to search"
        aux = self.first
        while aux != None:
            if aux.name == name:
                return f"the contact {name} is in the list"
            aux = aux.next
        return f"the contact {name} is not in the list"
    
    def delete_contact(self, name):
        if self.is_empty():
            return "There is nothing to delete"
        aux = self.first
        while aux != None:
            if aux.name == name:
                if aux.prev:
                    aux.prev.next = aux.next
                else:
                    self.first = aux.next
                if aux.next:
                    aux.next.prev = aux.prev
                else:
                    self.last = aux.prev
                return f"the contact {name} has been deleted"
            aux = aux.next
        return f"the contact {name} is not in the list"
    
    def update_contact(self, name, phone):
        if self.is_empty():
            return "There is nothing to update"
        aux = self.first
        while aux != None:
            if aux.name == name:
                aux.phone = phone
                return f"the contact {name} has been updated"
            aux = aux.next
        return f"the contact {name} is not in the list"
    
    def count_contacts(self):
        if self.is_empty():
            return "There is nothing to count"
        aux = self.first
        cont = 0
        while aux != None:
            cont += 1
            aux = aux.next
        return f"the number of contacts in the list is: {cont}"
    
list_16 = DoubleLinked_contacts()
list_16.add("Eric", 123456789)
list_16.add("Erick", 123456789)
list_16.add("Ericka", 123456789)
list_16.add("Ericko", 123456789)
print(list_16.see())
print(list_16.search("Erick"))
print(list_16.delete_contact("Ericko"))
print(list_16.see())

# Crea un programa que simule un sistema de navegación entre páginas web utilizando listas dobles.
class Node_17:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class DoubleLinked_web:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def web_add(self, url):
        if self.is_empty():
            self.first = self.last = Node_17(url)
        else:
            aux = Node_17(url)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def web_delete(self):
        if self.is_empty():
            return "There is nothing to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None

    def see_web(self):
        if self.is_empty():
            return "There is nothing to see"
        aux = self.first
        while aux != None:
            print(aux.url, end=" <-> ")
            aux = aux.next

list_17 = DoubleLinked_web()
list_17.web_add("www.google.com")
list_17.web_add("www.facebook.com")
list_17.web_add("www.twitter.com")
list_17.web_add("www.instagram.com")
print(list_17.see_web())
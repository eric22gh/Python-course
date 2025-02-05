# Día 21: Aprendiendo sobre Listas Enlazadas Simples
# Teoría: Las listas enlazadas simples son estructuras de datos donde cada nodo contiene un valor y una referencia al siguiente nodo. 
# Esto permite una inserción y eliminación eficiente de elementos.
# Imagina que tienes una cadena de bloques de colores. Cada bloque tiene un color (que sería el valor) y una cuerda que lo conecta con el siguiente bloque 
# (eso es la referencia al siguiente nodo).

# Bloque = Nodo
# Color del bloque = Valor del nodo # value
# Cuerda = Referencia al siguiente nodo #next
# Esto nos ayuda a agregar o quitar bloques fácilmente sin tener que mover todos los demás.

# Tips
# Maneja correctamente los punteros al agregar o eliminar nodos.
# Realiza pruebas para verificar la integridad de la lista después de cada operación. 
# Cuidado con las cuerdas: Cuando agregas o quitas bloques, asegúrate de que las cuerdas (punteros) estén bien conectadas. Si no, ¡la cadena se puede romper!
# Prueba tu cadena: Después de agregar o quitar bloques, revisa que todos estén conectados correctamente. Asegúrate de que no haya bloques perdidos.

# Buenas Prácticas
# Asegúrate de liberar la memoria adecuadamente para evitar fugas, por ejemplo, al eliminar un nodo, asegúrate de que no haya referencias a él.
# Documenta cada función para facilitar su comprensión.
# Limpieza: Cuando ya no necesites un bloque, asegúrate de soltarlo para que no ocupe espacio innecesario. (Esto se llama liberar memoria).
# Escribe notas: Es importante dejar notas (documentación) sobre cómo funciona cada parte de tu cadena para que tú o alguien más pueda entenderlo más tarde.

# Resumen
# Listas enlazadas son como cadenas de bloques donde cada bloque sabe quién es su siguiente.
# Puedes agregar y quitar bloques fácilmente.
# Siempre verifica que tus bloques estén bien conectados y limpia después de ti.

class Node_1:
    def __init__(self, value):
        self.value = value
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_1(value)
        else:
            aux = Node_1(value)
            aux.next = self.first
            self.first = aux

    def remove(self):
        if self.is_empty():
            return "The list is empty"
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "There is anything to see in the list"
        else:
            aux = self.first
            while aux != None:
                print(aux.value)
                aux = aux.next

list_1 = SimpleLinkedList()
list_1.is_empty()
list_1.add(23)
list_1.add(13)
list_1.add(253)
list_1.add(273)
list_1.remove()
list_1.see()

# Ejercicios
# 1- Implementa una lista enlazada simple y realiza operaciones para agregar elementos.
class Node_2:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.Last = None

    def is_empty(self):
        return self.first == None
    
    def add_elements(self, value):
        if self.is_empty():
            self.first = self.Last = Node_2(value)
        else:
            aux = Node_2(value)
            aux.next = self.first
            self.first = aux

    def see_elements(self):
        if self.is_empty():
            return "there is anything to see in the list"
        else:
            aux = self.first
            while aux != None:
                print(aux.value, end=" - ")
                aux = aux.next

list_2 = LinkedList()
list_2.add_elements(78)
list_2.add_elements(8)
list_2.add_elements(798)
list_2.see_elements()
   
# 2- Crea un método para eliminar un nodo específico de la lista.
class Node_3:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist2:
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
            self.first = aux

    def remove(self, node):
        if self.is_empty():
            return "there is anything to remove in the list"
        if self.first.value == node:
            self.first = self.first.next
            return
        aux = self.first
        while aux.next:
            if aux.next.value == node:
                aux.next = aux.next.next
                return
            aux = aux.next
                    
    def see(self):
        if self.is_empty():
            return "there is anything to see in the list"
        else:
            aux = self.first
            while aux:
                if aux.value is not None:
                    print(aux.value, end=", ")
                aux = aux.next
            
list_3 = Linkedlist2()
list_3.add("eric")
list_3.add("Hernandez")
list_3.add("edwards")
list_3.remove("Hernandez")
list_3.see()

# 3- Escribe un método para buscar un valor en la lista enlazada.
class Node_4:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist3:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        self.first =  None

    def add(self, value):
        if self.is_empty():
            self.first = self.last == Node_4(value)
        aux = Node_4(value)
        aux.next = self.first
        self.first = aux

    def found(self, value):
        aux = self.first
        while aux != None:
            if aux.value == value:
                return f"the node in the list is: {value}"
            aux.next
        return "NO node found"
           
list_4 = Linkedlist3()
list_4.add(78)
list_4.add(8)
list_4.add(785)
list_4.add(71)
print(list_4.found(71))

# 4- Implementa un método para insertar un nodo en una posición específica.
class Node_5:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist4:
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
            self.first = aux

    def insert(self, value, position):
        aux = self.first
        count = 0
        while aux != None:
            count += 1
            if count == position:
                aux.value = value
            aux = aux.next

    def see(self):
        if self.is_empty():
            return "there is anything to see in the list"
        else:
            aux = self.first
            while aux != None:
                print(aux.value, end=", ")
                aux = aux.next

list_5 = Linkedlist4()
list_5.add(7)
list_5.add(81)
list_5.add(85)
list_5.add(41)
list_5.insert(3, 2)
list_5.see()

# 5- Desarrolla un método que cuente el número de nodos en la lista.
class Node_6:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist5:
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
            return "there is anything in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" --")
            aux = aux.next
    
    def count(self):
        if self.is_empty():
            return "there is anything in the list"
        aux = self.first
        cont = 0
        while aux != None:
            cont += 1
            aux = aux.next
        return f"the number of nodes in the list is: {cont}."
    
list_6 = Linkedlist5()
list_6.add("eric")
list_6.add("helen")
list_6.add("maria")
print(list_6.count())

# 6- Crea un método para invertir la lista enlazada.
class Node_7:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist6:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_7(value)
        else:
            aux = Node_7(value)
            aux.next = self.first
            self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "there is anything in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" --")
            aux = aux.next

    def reverse(self):
        aux = self.first
        list = []
        while aux != None:
            list.append(aux.value)
            aux = aux.next
        return list[::-1]
        
list_7 = Linkedlist6()
list_7.add("helen")
list_7.add("martinez")
print(list_7.reverse())

# 7- Implementa un método que devuelva el valor en la posición n.
class Node_8:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist7:
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
            #self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "there is anything in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" --")
            aux = aux.next

    def value(self, position):
        aux = self.first
        count = 0
        while aux != None:
            count += 1
            if count == position:
                return aux.value
            aux = aux.next
        return "there is not value in the position"
    
list_8 = Linkedlist7()
list_8.add("helen")
list_8.add("martinez")
list_8.add("eric")
list_8.add("hernandez")
print(list_8.value(3))

# 8- Escribe un programa que combine dos listas enlazadas.
class Node_9:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist8:
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
            #self.first.prev = aux
            self.first = aux

    def see(self):
        if self.is_empty():
            return "there is anything in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" --")
            aux = aux.next

    def combine(self, list):
        aux = self.first
        while aux.next != None:
            aux = aux.next
        aux.next = list.first # para que se combine las dos listas
        return self.see()
    
list_9 = Linkedlist8()
list_9.add("martinez")
list_9.add("hernandez")
list_10 = Linkedlist8()
list_10.add("89")
list_10.add("87")
list_9.combine(list_10)

# 9- Crea un método que elimine duplicados en la lista.
print("\n")
class Node_10:
    def __init__(self, value):
        self.value = value
        self.next = None

class Duplicade:
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
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is anything to see in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end=" ~> ")
            aux = aux.next

    def duplicades(self):
        aux = self.first
        while aux != None:
            aux2 = aux
            while aux2.next != None:
                if aux2.next.value == aux.value:
                    aux2.next = aux2.next.next
                else:
                    aux2 = aux2.next
            aux = aux.next

list_11 = Duplicade()
list_11.add(21)
list_11.add(21)
list_11.add(1)
list_11.add(221)
list_11.duplicades()
list_11.see()

# 10- Implementa un método que devuelva el último nodo de la lista.
print("\n")
class Node_11:
    def __init__(self, value):
       self.value = value
       self.next = None

class Linked:
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
            self.first = aux

    def see(self):
        if self.is_empty():
            return "There is anything to see in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end= "--")
            aux = aux.next

    def last_node(self):
        if self.is_empty():
            return "There is any node in the list"
        else:
            aux = self.first
            while aux.next != None: 
                aux = aux.next
            return f"The last node in the list is: {aux.value}" 
        # el va a seguir avanzando hasta que el siguiente sea NOne y ahi se va a detener y va a retornar el valor de ese nodo

list_12 = Linked()
list_12.add(56)
list_12.add(566)
list_12.add(6)
print(list_12.last_node())

# 11- Desarrolla un método para encontrar el nodo anterior a un valor dado.
class Node_12:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linked2: 
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_12(value)
        else:
            aux = Node_12(value)
            aux.next = self.first
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "there is not anything to delete"
        elif self.first == self.last:
            self.first = self.last = None # si el primero y el ultimo son iguales su valor va a ser none 
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "there is anything to see in the list"
        aux = self.first
        while aux != None:
            print(aux.value, end="-- ")
            aux = aux.next

    def the_node_before(self, value):
        if self.is_empty():
            return "there is any value to return"
        else:
            aux = self.first
            while aux.next and aux.next.value != value:
                aux = aux.next
            if aux.next:
                return f"the node before {aux.value}"
            return None
              
list_13 = Linked2()
list_13.add(5)
list_13.add(1)
list_13.add(6)
list_13.add(3)
print(list_13.the_node_before(6))

# 12- Crea un método que imprima la lista en reversa.
print("\n")
class Node_13:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked3:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_13(value)
        else:
            aux = Node_13(value)
            aux.next = self.first
            self.first = aux

    def see(self):
        if self.is_empty():
            return "there is not anything to see"
        aux = self.first
        while aux != None:
            print(aux.value, end="-- ")
            aux = aux.next

    def reverse(self):
        aux = self.first
        list = []
        while aux != None:
            list.append(aux.value)
            aux = aux.next
        return list[::-1]
    
list_14 = Linked3()
list_14.add(52)
list_14.add(10)
list_14.add(67)
list_14.add("eric")
print(list_14.reverse())
# 13- Implementa un método que verifique si la lista está vacía.
class Node_14:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked4:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_14(value)
        else:
            aux = Node_14(value)
            aux.next = self.first
            self.first = aux

    def delete_first(self):
        if self.is_empty():
            return "there is anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next 

    def delete_last(self):
        if self.is_empty():
            return "there is anything to delete"
        else:
            aux = self.first
            while aux.next != self.last:
                aux = aux.next
            aux.next = None
            self.last = aux

    def see(self):
        if self.is_empty():
            return "there is anything to see in the list"
        else:
            aux = self.first
            while aux != None:
                print(aux.value, end=" ~>")
                aux = aux.next

list_16 = linked4()
list_16.add("ericka")
list_16.add("vargas")
list_16.add("perez")
list_16.add(88) 
list_16.delete_first()
list_16.delete_last()
list_16.see()
print(list_16.is_empty())

# 14- Escribe un programa que cuente cuántas veces aparece un valor en la lista.
class Node_15:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist22:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_15(value)
        else:
            aux = Node_15(value)
            aux.next = self.first
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "there is anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "there is anything to see"
        else:
            aux = self.first
            while aux != None:
                print(aux.value, end="->")
                aux = aux.next

    def count(self, values):
        if self.is_empty():
            return "there is anything to count"
        else:
            aux = self.first
            cont = 0
            while aux != None:
                if aux.value == values:
                    cont += 1
                aux = aux.next
            return f"You count: {cont} times the value: {values} in the list"
                
list_17 = linkedlist22()
list_17.add(2)
list_17.add(1)
list_17.add(2)
list_17.add(2)
print(list_17.count(2))

# 15- Crea un método que retorne la posición de un valor dado en la lista.
class Node_16:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist23:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, value):
        if self.is_empty():
            self.first = self.last = Node_16(value)
        else:
            aux = Node_16(value)
            aux.next = self.first
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "there is anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "there is anything to see"
        else:
            aux = self.first
            while aux != None:
                print(aux.value, end="->")
                aux = aux.next

    def position(self, value):
        if self.is_empty():
            return "there is not anything to see"
        else:
            aux = self.first
            count = 0
            while aux != None:
                count += 1
                if aux.value == value:
                    return f"the position of the value {value} is: {count}"
                aux = aux.next
            return "there is not value in the list"
        
list_18 = linkedlist23()
list_18.add(25)
list_18.add(1)
list_18.add(29)
list_18.add(2)
print(list_18.position(2))

# Mini Proyectos
# Desarrolla un gestor de tareas donde las tareas se almacenen en una lista enlazada.
class Node_17:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskManager:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, task):
        if self.is_empty():
            self.first = self.last = Node_17(task)
        else:
            aux = Node_17(task)
            aux.next = self.first
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "there is not anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "there is not anything to see"
        else:
            aux = self.first
            while aux != None:
                print(aux.task, end=" -> ")
                aux = aux.next

    def delete_task(self, task):
        if self.is_empty():
            return "there is not anything to delete"
        else:
            aux = self.first
            while aux.next and aux.next.task != task:
                aux = aux.next
            if aux.next:
                aux.next = aux.next.next
            return f"the task {task} has been deleted"
        
list_19 = TaskManager()
list_19.add("clean the house")
list_19.add("wash the dishes")
list_19.add("do the homework")
list_19.add("go to the gym")
list_19.delete_task("go to the gym")
list_19.see()

# Crea un programa que simule un playlist de canciones utilizando listas enlazadas.
class Node_18:
    def __init__(self, song):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, song):
        if self.is_empty():
            self.first = self.last = Node_18(song)
        else:
            aux = Node_18(song)
            aux.next = self.first
            self.first = aux

    def delete(self):
        if self.is_empty():
            return "there is not anything to delete"
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next

    def see(self):
        if self.is_empty():
            return "there is not anything to see"
        else:
            aux = self.first
            while aux != None:
                print(aux.song, end=" -> ")
                aux = aux.next

    def delete_song(self, song):
        if self.is_empty():
            return "there is not anything to delete"
        else:
            aux = self.first
            while aux.next and aux.next.song != song:
                aux = aux.next
            if aux.next:
                aux.next = aux.next.next
            return f"the song {song} has been deleted"
        
    def play(self, song):
        if self.is_empty():
            return "there is not anything to play"
        else:
            aux = self.first
            while aux != None:
                if aux.song == song:
                    return f"playing the song: {song}"
                aux = aux.next
            return "the song is not in the playlist"

    def stop(self, song):
        if self.is_empty():
            return "there is not anything to stop"
        else:
            aux = self.first
            while aux != None:
                if aux.song == song:
                    return f"stop the song: {song}"
                aux = aux.next
            return "the song is not in the playlist"
        
list_20 = Playlist()
list_20.add("song 1")
list_20.add("song 2")
list_20.add("song 3")
list_20.add("song 4")
print(list_20.play("song 3"))
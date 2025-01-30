# Día 20: Introducción a listas enlazadas

# Teoría:
# Una lista enlazada es una estructura de datos que consiste en nodos o bloques, donde cada nodo o bloque contiene un valor y una referencia al siguiente nodo o bloque. 
# Esto permite una inserción y eliminación eficiente de elementos en cualquier parte de la lista.
# Imagina que tienes una cadena de bloques de juguete. Cada bloque tiene un número y una cuerda que lo conecta al siguiente bloque. 
# Esto es lo que llamamos una lista enlazada. Cada bloque es un nodo, y cada nodo tiene un valor (el número) y una referencia (la cuerda) al siguiente nodo.
# 
# tipos de listas enlazadas:
# Lista enlazada simple: Cada bloque o nodo apunta solo al siguiente bloque o nodo.
# Ejemplo: Bloque 1 → Bloque 2 → Bloque 3 → Ninguno

# Lista doblemente enlazada: Cada bloque o nodo apunta al siguiente bloque y al bloque anterior.
# Ejemplo: Ninguno ← Bloque 1 ↔ Bloque 2 ↔ Bloque 3 → Ninguno

# Lista circular: El último bloque o nodo apunta de nuevo al primer bloque.
# Ejemplo: Bloque 1 → Bloque 2 → Bloque 3 → Bloque 1

# Tips y Buenas Prácticas:
# Utiliza listas enlazadas cuando necesites una estructura de datos dinámica que permita inserciones y eliminaciones frecuentes.
# Recuerda que las listas enlazadas no permiten acceso aleatorio como las listas estándar.
# Usa listas enlazadas cuando necesites agregar o quitar bloques con frecuencia.
# Recuerda que no puedes saltar a un bloque cualquiera como lo harías con una lista normal. Tienes que empezar desde el primer bloque y seguir la cuerda.
# Al eliminar un nodo Se ajustan las referencias del nodo anterior y del siguiente para que se salten el nodo que se está eliminando.

# nota: como hacer inserciones y eliminaciones en una lista enlazada

# Lista enlazada simple:
# Cada bloque apunta solo al siguiente bloque, Bloque 1 → Bloque 2 → Bloque 3 → Ninguno
class Nodo_1:
    def __init__(self, value):
        self.value = value
        self.next = None

class listasimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        # en si no se hace una lista, se hace como bloques
    def vacias(self):
        return self.primero == None # cabeza
    
    def agregar_ultimo(self, value):
        if self.vacias():
            self.primero = self.ultimo = Nodo_1(value) # el primero va a ser igual al ultimo
        else:
            aux = self.ultimo # la var aux va a guardar el ultimo valor de la lista
            self.ultimo = aux.next = Nodo_1(value) # self.ultimo va a tener el mismo valor que aux pero avanzando una posicion(next)
    
    def agregar_inicio(self, value):
        if self.vacias():
            self.primero = self.ultimo = Nodo_1(value) # el primero va a ser igual al ultimo
        else:
            aux = Nodo_1(value)
            aux.next = self.primero # se hace una copia de el primer valor y esa copia va a ser el segundo valor de la lista
            self.primero = aux
    
    def eliminar_ultimo(self):
        aux = self.primero
        while aux.next != self.ultimo: # mientras que aux sea distinto de el ultimo valor de la lista, 
        #aux se va a mover al siguiente valor de la lista
            aux = aux.next
        # si aux llega a el ultimo valor y ese es none(no tiene valor), el ultimo valor de lista pasa a ser aux que seria none
        aux.next = None
        self.ultimo = aux 

    def eliminar_inicio(self):
        self.primero = self.primero.next # el primer valor de la lista va a ser el segundo

    def recorrido(self): # se hace con while para que vaya aumentando
        aux = self.primero # aux guarda el primer valor de la lista
        while aux != None: #mientras que aux tenga valor
            print(aux.value) # imprimir el valor almacenado de aux
            aux = aux.next # moverse al siguiente valor de la lista(aumentar)
           
# menu para la lista enlazada anterior
try:
    if __name__ == '__main__':
        lista = listasimple()
        while True:
            print("Menu de lista enlazada")
            print("1. Agregar ultimo")
            print("2. Agregar al inicio")
            print("3. Eliminar ultimo")
            print("4. Eliminar al inicio")
            print("5. Recorrer")
            print("6. Salir")
            op = int(input("Opcion: "))
            if op == 1:
                lista.agregar_ultimo(int(input("Valor: ")))
            elif op == 2:
                lista.agregar_inicio(int(input("Valor: ")))
            elif op == 3:
                print("Lista antes de eliminar el ultimo")
                lista.recorrido()
                lista.eliminar_ultimo()
                print("se elimino con exito")
            elif op == 4:
                print("Lista antes de eliminar el primero")
                lista.recorrido()
                lista.eliminar_inicio()
                print("se elimino con exito")
            elif op == 5:
                lista.recorrido()
            elif op == 6:
                break
            else:
                print("Opcion no valida")
except Exception as e:
    print(e)

# Lista doblemente enlazada: Cada bloque apunta al siguiente bloque y al bloque anterior.
# Ejemplo: Ninguno ← Bloque 1 ↔ Bloque 2 ↔ Bloque 3 → Ninguno
class Nodo_2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class listadoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacias(self):
        return self.primero == None # si el primero de la lista(var) es nada, returna true
    
    def agregar_ultimo(self, data):
        if self.vacias():
            self.primero = self.ultimo = Nodo_2(data) # si la lista esta vacia, el primero va a ser igual al ultimo
        else:
            aux = self.ultimo # aux va a tener el ultimo valor de la lista
            self.ultimo = aux.next = Nodo_2(data) # el ultimo valor de la lista va a ser igual al siguiente valor de aux
            self.ultimo.prev = aux # el valor anterior del ultimo valor de la lista va a ser igual a aux
        self.size += 1 # aumentar el tamaño de la lista

    def agregar_inicio(self, data):
        if self.vacias():
            self.primero = self.ultimo = Nodo_2(data) # si la lista esta vacia, el primero va a ser igual al ultimo
        else:
            aux = Nodo_2(data)
            aux.next = self.primero # el siguiente valor de aux va a ser igual al primero de la lista
            self.primero.prev = None # el valor anterior del primero de la lista va a ser igual a aux
            self.primero = aux # el primero de la lista va a ser igual a aux
        self.size += 1 # aumentar el tamaño de la lista

    def recorrer_inicio(self):
        aux = self.primero # aux va a tener el primer valor de la lista
        while aux != None: # mientras que aux no tenga valor
            print(aux.data) # imprimir el valor de aux
            aux = aux.next # moverse al siguiente valor de la lista

    def recorrer_final(self):
        aux = self.ultimo # aux va a tener el ultimo valor de la lista
        while aux != None: # mientras que aux no tenga valor
            print(aux.data) # imprimir el valor de aux
            aux = aux.prev # moverse al valor anterior de la lista

    def size(self):
        return self.size # retornar el tamaño de la lista
    
    def eliminar_inicio(self):
        if self.vacias():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.next
            self.primero.prev = None
            self.size -= 1

    def eliminar_final(self):
        if self.vacias():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.prev
            self.ultimo.next = None
            self.size -= 1

# menu para la lista doblemente enlazada
try:
    if __name__ == '__main__':
        lista = listadoble()
        while True:
            print("Menu de lista doblemente enlazada")
            print("1. Agregar ultimo")
            print("2. Agregar al inicio")
            print("3. Eliminar ultimo")
            print("4. Eliminar al inicio")
            print("5. Recorrer inicio")
            print("6. Recorrer final")
            print("7. Tamaño de la lista")
            print("8. Salir")
            op = int(input("Opcion: "))
            if op == 1:
                lista.agregar_ultimo(int(input("Valor: ")))
            elif op == 2:
                lista.agregar_inicio(int(input("Valor: ")))
            elif op == 3:
                print("Lista antes de eliminar el ultimo")
                lista.recorrer_inicio()
                lista.eliminar_final()
                print("se elimino con exito")
            elif op == 4:
                print("Lista antes de eliminar el primero")
                lista.recorrer_inicio()
                lista.eliminar_inicio()
                print("se elimino con exito")
            elif op == 5:
                lista.recorrer_inicio()
            elif op == 6:
                lista.recorrer_final()
            elif op == 7:
                print("Tamaño de la lista: ", lista.size())
            elif op == 8:
                print("Gracias por usar el programa...Saliendo")
                break
            else:
                print("Opcion no valida")
except Exception as e:
    print(e)

# Lista circular: El último bloque apunta de nuevo al primer bloque.
# Ejemplo: Bloque 1 → Bloque 2 → Bloque 3 → Bloque 1
class Nodo_3:
    def __init__(self, data):
        self.data = data
        self.next = None

class listacircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacias(self):
        return self.primero == None # si el primero de la lista(var) es nada, returna true
    
    def agregar_inicio(self, data):
        if self.vacias():
            self.primero = self.ultimo = Nodo_3(data) # si mi lista esta vacia, se agrega un dato al principio
        else:
            aux = Nodo_3(data)
            aux.next = self.primero # el siguiente valor de aux va a ser igual al primero de la lista
            self.primero = aux
            self.ultimo.next = self.primero # el ultimo valor de la lista va a ser igual al primero de la lista)osea enlazado)

    def agregar_final(self, data):
        if self.vacias():
            self.primero = self.ultimo = Nodo_3(data) # si mi lista esta vacia, se agrega un dato al final
            self.primero.next = self.primero # 

        else:
            aux = self.ultimo
            self.ultimo = aux.next = Nodo_3(data) # el ultimo valor de la lista va a ser igual al siguiente valor de aux
            self.ultimo.next = self.primero # el dato que sigue despues de el ultimo va a apuntar al primero

    def recorrer(self):
        aux = self.primero
        while aux != None:
            print(aux.data)
            aux = aux.next # moverse al siguiente valor de la lista
            if aux == self.primero: # si aux es igual al primero de la lista, se rompe el ciclo
                break

    def eliminar_inicio(self):
        if self.vacias():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.next
            self.ultimo.next = self.primero

    def eliminar_final(self):
        if self.vacias():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.next != self.ultimo:
                aux = aux.next
            aux.next = self.primero
            self.ultimo = aux
# menu para la lista doblemente enlazada
try:
    if __name__ == '__main__':
        lista = listacircular()
        while True:
            print("Menu de lista doblemente enlazada")
            print("1. Agregar al inicio")
            print("2. Agregar al final")
            print("3. Recorrer")
            print("4. Eliminar al inicio")
            print("5. Eliminar al ultimo")
            print("6. Salir")
            op = int(input("Opcion: "))
            if op == 1:
                lista.agregar_inicio(int(input("Valor: ")))
            elif op == 2:
                lista.agregar_final(int(input("Valor: ")))
            elif op == 3:
                lista.recorrer()
            elif op == 4:
                print("Lista antes de eliminar el primero")
                lista.recorrer()
                lista.eliminar_inicio()
                print("se elimino con exito")
            elif op == 5:
                print("Lista antes de eliminar al ultimo")
                lista.recorrer()
                lista.eliminar_final()
            elif op == 6:
                print("Gracias por usar el programa...Saliendo")
                break
            else:
                print("Opcion no valida")
except Exception as e:
    print(e)

# lista circular doblemente enlazada: el ultimo bloque apunta al primer bloque y el primer bloque al ultimo
# ejemplo: Bloque 1 ↔ Bloque 2 ↔ Bloque 3 ↔ Bloque 1
class Nodo:  # Clase Nodo
    def __init__(self, valor):  # Función Inicializar(valor)
        self.valor = valor  # Este.valor = valor
        self.siguiente = None  # Este.siguiente = Ninguno
        self.anterior = None  # Este.anterior = Ninguno

class ListaCircularDoblementeEnlazada: 
    def __init__(self): 
        self.primero = None
        self.ultimo = None

    def vacia(self): 
        return self.primero == None
    
    def __unir_nodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def agregar_inicio(self, valor): 
        if self.vacia(): 
            self.primero = self.ultimo = Nodo(valor) 
        else: 
            aux = Nodo(valor)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self, valor): 
        if self.vacia(): 
            self.primero = self.ultimo = Nodo(valor) 
        else: 
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(valor)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def recorrer_inicio_a_fin(self):
        aux = self.primero
        while aux:
            print(aux.valor)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_a_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.valor)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos()

    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unir_nodos()

    def buscar(self, valor):
        aux = self.primero
        while aux:
            if aux.valor == valor:
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
                
    def eliminar_cualquiera(self, valor):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.valor == valor:
            self.eliminar_inicio()
        elif self.ultimo.valor == valor:
            self.eliminar_final()
        else:
            aux = self.primero
            while aux:
                if aux.valor == valor:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                    break
                aux = aux.siguiente
                if aux == self.primero:
                    print("Valor no encontrado")
                    break
        self.__unir_nodos()

# menu para la lista circular doblemente enlazada
try:
    if __name__ == '__main__':
        lista = ListaCircularDoblementeEnlazada()
        while True:
            print("Menu de lista circular doblemente enlazada")
            print("1. Agregar al inicio")
            print("2. Agregar al final")
            print("3. Recorrer inicio a fin")
            print("4. Recorrer fin a inicio")
            print("5. Eliminar al inicio")
            print("6. Eliminar al final")
            print("7. Buscar")
            print("8. Eliminar cualquier valor")
            print("9. Salir")
            op = int(input("Opcion: "))
            if op == 1:
                lista.agregar_inicio(int(input("Valor: ")))
            elif op == 2:
                lista.agregar_final(int(input("Valor: ")))
            elif op == 3:
                lista.recorrer_inicio_a_fin()
            elif op == 4:
                lista.recorrer_fin_a_inicio()
            elif op == 5:
                print("Lista antes de eliminar el primero")
                lista.recorrer_inicio_a_fin()
                lista.eliminar_inicio()
                print("se elimino con exito")
            elif op == 6:
                print("Lista antes de eliminar al ultimo")
                lista.recorrer_inicio_a_fin()
                lista.eliminar_final()
                print("se elimino con exito")

            elif op == 7:
                valor = int(input("Valor a buscar: "))
                if lista.buscar(valor):
                    print("Valor encontrado")
                else:
                    print("Valor no encontrado")
            elif op == 8:
                valor = int(input("Valor a eliminar: "))
                lista.eliminar_cualquiera(valor)
            elif op == 9:
                print("Gracias por usar el programa...Saliendo")
                break
            else:
                print("Opcion no valida")
except Exception as e:
    print(e)

# Ejercicios:
# 1- Implementa una lista enlazada simple y realiza operaciones para agregar elementos.
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linked_list():
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add_item(self, value):
        if self.is_empty():
            self.first = self.last = Node(value)
        var = Node(value)
        var.next = self.first
        self.first = var

    def recorrer(self):
        var = self.first
        while var != None:
            print(var.data)
            var = var.next
lista_1 = linked_list()
lista_1.add_item(8)
lista_1.add_item(80)
lista_1.add_item(71)
lista_1.recorrer()
print("\n")
# 2- Crea un método para eliminar un nodo específico de la lista enlazada.
class node_eliminar:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_1:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None

    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_eliminar(data) 
        aux = node_eliminar(data)
        aux.next = self.first
        self.first = aux

    def recorrido(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next # incompleto 
            # no lo esta recorriendo bien, soolo un valor, arreglar eso

    def eliminar(self):
        self.first = self.first.next# el primer elemento ya no va tener el valor que tenia si no que
        # va a tener el segundo valor, por lo tanto el anterior se elimina
list_2 = linked_list_1()
list_2.add(22)
list_2.add(45)
list_2.add(43)
list_2.recorrido()
print("\n")
# 3- Escribe un método para buscar un valor en la lista enlazada y devolver su posición.
class node_buscar:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_2:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_buscar(data)
        aux = node_buscar(data)
        aux.next = self.first
        self.first = aux

    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next

    def buscar_posicion(self, valor):
        aux = self.first
        cont = 0
        while aux != None:
            if aux.data == valor:
                return f"El valor {valor} se encuentra en la posicion {cont}"
            else:
                cont += 1
                aux = aux.next
list_3 = linked_list_2()
list_3.add(20)
list_3.add(46)
list_3.add(43)
list_3.add(90)
print(list_3.buscar_posicion(46))

# 4- Implementa un método para insertar un nodo en una posición específica de la lista.
class node_insert:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_3:
    def __init__(self):
        self.first = None
        self.last = None
    
    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_insert(data)
        aux = node_insert(data)
        aux.next = self.first
        self.first = aux

    def insertar(self, valor, posicion):
        aux = self.first
        cont = 0
        while aux != None:
            if cont == posicion:
                var = node_insert(valor)
                var.next = aux.next
                aux.next = var
                break
            else:
                cont += 1
                aux = aux.next

    def see(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next

list_4 = linked_list_3()
list_4.add(2)
list_4.add(6)
list_4.add(4)
list_4.insertar(8, 1)
list_4.see()
# 5- Crea un programa que imprima todos los elementos de la lista enlazada en orden.
class node_imprimir:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_4:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_imprimir(data)
        aux = node_imprimir(data)
        aux.next = self.first
        self.first = aux

    def imprimir_orden(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next

list_5 = linked_list_4()
list_5.add(2)
list_5.add(6)
list_5.add(4)
list_5.imprimir_orden()

# 6- Desarrolla un método que cuente el número de nodos en la lista enlazada.
class node_contar:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_5:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_contar(data)

        aux = node_contar(data)
        aux.next = self.first
        self.first = aux

    def contar(self):
        aux = self.first
        cont = 0
        while aux != None:
            cont += 1
            aux = aux.next
        return f"La lista tiene {cont} elementos"
    
list_6 = linked_list_5()
list_6.add(2)
list_6.add(6)
list_6.add(4)
print(list_6.contar())

# 7- Crea un método para invertir la lista enlazada.
class node_invertir:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_6:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_invertir(data)
        aux = node_invertir(data)
        aux.next = self.first
        self.first = aux

    def invert(self):
        aux = self.first
        var = None
        while aux:
            next = aux.next
            aux.next = var
            var = aux 
            aux = next
        self.first = var
        #return self.first # incompleto, no retorna el valor alrevez

    def print_list(self):
        aux = self.first
        while aux:
            print(aux.data, end=" ")
            aux = aux.next
        print()

list_7 = linked_list_6()
list_7.add(1)
list_7.add(6)
list_7.add(4)
list_7.invert()
list_7.print_list()

# 8- Implementa una lista doblemente enlazada y realiza operaciones de inserción y eliminación.
class node_doble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linked_list_7:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_doble(data)
        aux = node_doble(data)
        aux.next = self.first
        self.first.prev = aux # el valor anterior del primero de la lista va a ser igual a aux
        self.first = aux

    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next

    def eliminar_inicio(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next # el primer valor de la lista va a ser el segundo, eliminando su primer valor
            self.first.prev = None # el valor anterior que tenia self.first va a ser none

    def eliminar_final(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last = self.last.prev # el ultimo valor va a cambiar y ser el valor anterior a el
            self.last.next = None # el valor despues de el ultimo va a ser none

    def see(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next

list_8 = linked_list_7()
list_8.add(78)
list_8.add(45)
list_8.add(90)
list_8.add(23)
list_8.add(12)
list_8.eliminar_inicio()
list_8.eliminar_final()
list_8.see()
print("\n")
# 9- Escribe un programa que convierta una lista enlazada en una lista estándar (o viceversa).
class node_convertir:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_8:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_convertir(data)
        aux = node_convertir(data)
        aux.next = self.first
        self.first = aux

    def convertir_to_list(self):
        aux = self.first
        lista = []
        while aux != None:
            lista.append(aux.data)
            aux = aux.next
        return lista
    
    def convertir_to_linked(self, lista):
        for i in lista:
            self.add(i)
        return self.first
    
    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next

list_9 = linked_list_8()
list_9.add(78)
list_9.add(45)
list_9.add(90)
list_9.add(23)
list_9.add(12)
print(list_9.convertir_to_list())
# 10- Desarrolla un método que elimine duplicados de una lista enlazada.
class node_duplicados:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_9:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_duplicados(data)
        aux = node_duplicados(data)
        aux.next = self.first
        self.first = aux

    def eliminar_duplicados(self):
        aux = self.first
        while aux != None:
            aux_2 = aux
            while aux_2.next != None:
                if aux_2.next.data == aux.data:
                    aux_2.next = aux_2.next.next
                else:
                    aux_2 = aux_2.next
            aux = aux.next

    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next

list_10 = linked_list_9()
list_10.add(78)
list_10.add(45)
list_10.add(45)
list_10.add(90)
list_10.add(23)
list_10.eliminar_duplicados()
list_10.recorrer()

# 11- Crea un método para obtener el último nodo de la lista enlazada.
class last_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list_10:
    def __init__(self):
        self.first = None
        self.last_ = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last_ = last_node(data)
        aux = last_node(data)
        aux.next = self.first
        self.first = aux

    def last(self):
        aux = self.first
        while aux.next != None:
            aux = aux.next
        return aux.data

    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next

list_11 = linked_list_10()
list_11.add(80)
list_11.add(45)
list_11.add(90)
list_11.add(23)
list_11.last()

# 12- Implementa una lista circular y realiza operaciones de inserción y eliminación.
class node_circular:
    def __init__(self, data):
        self.data = data
        self.next = None    

class linked_list_11:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, data):
        if self.is_empty():
            self.first = self.last = node_circular(data)
            self.last.next = self.first
        else:
            aux = node_circular(data)
            aux.next = self.first
            self.last.next = aux
            self.last = aux

    def recorrer(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.next
            if aux == self.first: # para romper el ciclo porque si no va a seguir ya que el ultimo esta unido con el primero
                break

    def eliminar_inicio(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.last.next = self.first

    def eliminar_final(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            aux = self.first
            while aux.next != self.last:
                aux = aux.next
            aux.next = self.first
            self.last = aux

list_12 = linked_list_11()
list_12.add(80)
list_12.add(45)
list_12.add(90)
list_12.add(23)
list_12.eliminar_inicio()
list_12.eliminar_final()
list_12.recorrer()
print("\n")

# 13- Escribe un método que recorra la lista enlazada y devuelva una lista de sus valores.
class Nodo_8:
    def __init__(self, data):
        self.data = data
        self.next = None

class lista_enlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None
    
    def add(self, data):
        if self.vacia():
            self.primero = self.ultimo = Nodo_8(data)
        aux = Nodo_8(data)
        aux.next = self.primero
        self.primero = aux

    def list_values(self):
        aux = self.primero
        lista = []
        while aux != None:
            lista.append(aux.data)
            aux = aux.next
        return lista
    
    def values(self):
        aux = self.primero
        while aux != None:
            print(aux.data)
            aux = aux.next

list_13 = lista_enlazada()
list_13.add(80)
list_13.add(45)
list_13.add(90)
list_13.add(23)
print(list_13.list_values())

# 14- Crea un programa que use una lista enlazada para implementar una cola.
class Nodo_9:
    def __init__(self, data):
        self.data = data
        self.next = None

class cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def is_empty(self):
        return self.primero == None
    
    def enqueue(self, data):
        if self.is_empty():
            self.primero = self.ultimo = Nodo_9(data)
        else:
            aux = Nodo_9(data)
            self.ultimo.next = aux
            self.ultimo = aux

    def dequeue(self):
        if self.is_empty():
            print("Cola vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.next

    def see(self):
        aux = self.primero
        while aux != None:
            print(aux.data)
            aux = aux.next

    def peek(self):
        return self.primero.data
    
cola_1 = cola()
cola_1.enqueue(80)
cola_1.enqueue(46)
cola_1.enqueue(90)
cola_1.enqueue(23)
cola_1.dequeue()
print(cola_1.peek())

# 15- Desarrolla un programa que use una lista enlazada para implementar una pila.
class Node_10:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack_1:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def is_empty(self):
        return self.primero == None
    
    def push(self, data):
        if self.is_empty():
            self.primero = self.ultimo = Node_10(data)
        aux = self.ultimo
        aux.next = Node_10(data)
        self.ultimo = aux.next 

    def pop(self):
        if self.is_empty():
            print("Pila vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.next != self.ultimo:
                aux = aux.next
            aux.next = None
            self.ultimo = aux

    def see(self):
        if self.is_empty():
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                print(aux.data)
                aux = aux.next

stack = stack_1()
stack.push(83)
stack.push(41)
stack.push(91)
stack.push(24)
stack.pop()
stack.pop()
stack.see() 

# Mini Proyectos:
# Desarrolla un programa que gestione una lista de contactos utilizando una lista enlazada.
class Node_contats:
    def __init__(self, contact):
        self.contact = contact
        self.next = None
class list_simple:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None
    
    def add(self, contact):
        if self.is_empty():
            self.first = self.last = Node_contats(contact)
        else:
            aux = Node_contats(contact)
            aux.next = self.first
            self.first = aux

    def remove(self):
        if self.is_empty():
            print("Lista vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next

    def see_contact(self):
        aux = self.first
        while aux != None:
            print(aux.contact)
            aux = aux.next

    def search_contact(self, contact):
        aux = self.first
        while aux != None:
            if aux.contact == contact:
                return f"El contacto {contact} se encuentra en la lista"
            aux = aux.next
        return "Contacto no encontrado"
    
list_contact = list_simple()
list_contact.add("Juan")
list_contact.add("Pedro")
list_contact.add("Maria")
list_contact.add("Ana")
print(list_contact.search_contact("Pedro"))

# Crea un simulador de un sistema de reservas donde los asientos se gestionen mediante una lista enlazada.
class Node_reservas:
    def __init__(self, asiento):
        self.asiento = asiento
        self.next = None

class list_reservas:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def is_empty(self):
        return self.primero == None
    
    def add(self, asiento):
        if self.is_empty():
            self.primero = self.ultimo = Node_reservas(asiento)
        else:
            aux = Node_reservas(asiento)
            aux.next = self.primero
            self.primero = aux

    def remove(self):
        if self.is_empty():
            print("Todos los asientos estan disponibles, no hay nada que eliminar")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.next

    def see_reservas(self):
        aux = self.primero
        while aux != None:
            print(aux.asiento)
            aux = aux.next

    def verificar_asiendo(self, Asiento):
        aux = self.primero
        while aux != None:
            if aux.asiento == Asiento:
                return "Asiento ocupado"
            aux = aux.next
        return "Asiento disponible"
    
reservas = list_reservas()
reservas.add("A1")
reservas.add("A2")
reservas.add("A3")
reservas.add("A4")
print(reservas.verificar_asiendo("A10"))

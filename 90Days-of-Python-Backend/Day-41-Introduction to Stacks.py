# Día 41: Introducción a pilas (implementación y uso)

# Teoría:
# Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out), 
# lo que significa que el último elemento añadido es el primero en ser retirado. 
# 
# Las operaciones principales son:
# push: Agregar un elemento a la parte superior de la pila.
# pop: Retirar y devolver el elemento en la parte superior de la pila.
# peek: Ver el elemento en la parte superior sin retirarlo.
# is_empty: Verificar si la pila está vacía.

# Tips y Buenas Prácticas:
# Utiliza pilas para problemas que requieren un seguimiento de operaciones, como deshacer acciones en aplicaciones.
# Asegúrate de manejar el caso de la pila vacía al realizar operaciones pop o peek.
# Uso de Pilas: Son útiles para problemas como el seguimiento de operaciones (por ejemplo, deshacer acciones en aplicaciones), evaluación de expresiones matemáticas, y recorrido de estructuras de datos como árboles.
# Manejo de Errores: Asegúrate de manejar el caso de la pila vacía al realizar operaciones pop o peek. Esto previene errores en tiempo de ejecución.
# Implementación: Aunque las listas en Python son una forma simple de implementar pilas, considera usar collections.deque para un rendimiento mejorado en operaciones de apilamiento y desapilado.

# Implementación de una Pila:
# class Pila:
#     def __init__(self):
#         self.elementos = []

#     def push(self, elemento):
#         self.elementos.append(elemento)

#     def pop(self):
#         if not self.is_empty():
#             return self.elementos.pop()
#         raise IndexError("La pila está vacía")

#     def peek(self):
#         if not self.is_empty():
#             return self.elementos[-1]
#         raise IndexError("La pila está vacía")

#     def is_empty(self):
#         return len(self.elementos) == 0

# # Uso de la pila
# pila = Pila()
# pila.push(1)
# pila.push(2)
# print("Elemento en la parte superior:", pila.peek())
# print("Elemento retirado:", pila.pop())

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        """Agrega un elemento a la parte superior de la pila."""
        self.elementos.append(elemento)

    def pop(self):
        """Retira y devuelve el elemento en la parte superior de la pila."""
        if self.is_empty():
            raise IndexError("Pop desde una pila vacía.")
        return self.elementos.pop()

    def peek(self):
        """Devuelve el elemento en la parte superior sin retirarlo."""
        if self.is_empty():
            raise IndexError("Peek en una pila vacía.")
        return self.elementos[-1]

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

    def size(self):
        """Devuelve el tamaño de la pila."""
        return len(self.elementos)

# Uso de la pila
if __name__ == "__main__": #para ejecutar todos
    pila = Pila()
    pila.push(10)
    pila.push(20)
    pila.push(30)
    pila.push(40)

    print("Elemento en la parte superior:", pila.peek())  # Salida: 40
    print("Retirando elemento:", pila.pop())              # Salida: 40
    print("¿Está vacía la pila?", pila.is_empty())       # Salida: False
    print("Tamaño de la pila:", pila.size())              # Salida: 3


# Ejercicios:
# 1. Implementa una pila y realiza operaciones push y pop.
class Stack:
    def __init__(self):
        self.warhouse = []
    
    def push(self, item):
        self.warhouse.append(item)
        return "Elemento agregado"
    
    def peek(self):
        if not self.is_empty():
            return self.warhouse[-1] # devuelve el elemento de arriba
        raise IndexError("La pila esta vacia")
    
    def pop(self): # retira el elemento de arriba de la pila
        if not self.is_empty():
            return self.warhouse.pop()
        raise IndexError("La pila esta vacia")
    def is_empty(self):
        return len(self.warhouse) == 0
    
    def size(self):
        return len(self.warhouse)

Stacks = Stack()
Stacks.push(10)
Stacks.push(50)
Stacks.push(100)
Stacks.push(150)
print(f"El elemento  de arriba de la pila que se retira es: {Stacks.pop()}")

# 2- Crea un programa que verifique si una cadena de paréntesis está balanceada utilizando una pila.
def verificar(cadena):
    stack = Stack()
    for exp in cadena:
        if exp == "(":
            stack.push(exp)
        elif exp == ")" :
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
print(verificar("(a + b) * (c + d)"))

# 3- Implementa un método peek2 en tu clase de pila.
def peek2(self, lista): # Esto no es una buena practica
    return lista[-1]
Pila.peek2 = peek2
print(pila.peek2([1, 5, 3, 89]))

# 4- Crea un programa que invierta una cadena utilizando una pila.
def pila_reverse(cadena):
    stac = Pila()
    for x in cadena:
        stac.push(x)

    alrevez = ""
    while not stac.is_empty(): # cuando la pila esta vacia el bucle se detiene
        alrevez += stac.pop() # ir quitando de arriba de la pila y iz guardandolo en la variable

    return alrevez
print(pila_reverse(" l carro"))

# 5- Implementa una pila que almacene números y calcule la suma de todos los elementos al final.
class Pila_2:
    def __init__(self):
        self.guardar = []
        self.sum = 0

    def push(self, dato):
        self.guardar.append(dato)
        self.sum += dato
    
    def suma_total(self):
        return self.sum
    
stack2 = Pila_2()
for x in range(1, 10):
    suma = stack2.push(x)
print(stack2.suma_total())

# 6- Escribe un programa que simule una calculadora básica utilizando una pila.
class Pila_Matematica():
    def __init__(self):
        self.calculo = []

    def push(self, dato):
        self.calculo.append(dato)

    def suma_pila(self):
        suma = sum(self.calculo)
        return f"La suma de los elementos de la pila es: {suma}"
    
    def resta_pila(self):
        if len(self.calculo) < 2:
            return "Error deben de haber 2 numeros para restar"
        resta = self.calculo[-1] - self.calculo[-2]
        return f"La resta de los elementos de la pila es: {resta}"
    
    def multi_pila(self):
        if len(self.calculo) < 2:
            return "Error deben de haber 2 numeros para multiplicar"
        b = self.calculo.pop()
        a = self.calculo.pop()
        multi = a * b
        return f"La multiplicacion de los elementos de la pila es: {multi}"
    def divi_pila(self):
        if len(self.calculo) < 2:
            return "Error deben de haber 2 numeros para dividir"
        elif self.calculo[-2] == 0:
            return "Error un numero no puede ser divisible entre 0"
        else:
            divi = self.calculo[-1] / self.calculo[-2]
            return f"La division de los elementos de la pila es: {divi}"
    
dato = Pila_Matematica()
dato.push(5)
dato.push(6)
print(dato.divi_pila()) 

# 7- Crea una pila que almacene nombres y los imprima en orden inverso.
class Pila_nombres():
    def __init__(self):
        self.name = []
    def push(self, dato):
        self.name.append(dato)

    def is_empty(self):
        return len(self.name) == 0
    def pop(self):
        if not self.is_empty():
            return self.name.pop()
        return IndexError("La pila esta vacia")
    
    def imprimir_pila(self):
        return self.name[::-1]
    
    def imprimir_pila_2(self):
        if self.is_empty():
            print("La pila está vacía.")
        else:
            print("Nombres en orden inverso:")
            for nombre in reversed(self.name):
                print(nombre)

Names = Pila_nombres()
Names.push("eric")
Names.push("helen")
Names.push("calvin")
Names.push("edwards")
print(Names.imprimir_pila())


# 8- Implementa un método is_empty en tu clase de pila.
def is_empty(self, stack):
    return len(stack) == 0
Pila_Matematica.is_empty = is_empty
print(dato.is_empty([2, 5, 89]))

# 9- Escribe un programa que use una pila para deshacer acciones (simulando un editor de texto).
class P_editor:
    def __init__(self):
        self.editor = []
        self.deshacer_pila = []

    def is_empty(self):
        return len(self.editor) == 0
    
    def is_empty_deshacer_pila(self):
        return len(self.deshacer_pila) == 0

    def push(self, dato):
        self.editor.append(dato)
        self.deshacer_pila = []
        return "Agregado correctamente"
    
    def deshacer(self):
        if not self.is_empty():
            dato = self.editor.pop()
            self.deshacer_pila.append(dato)
            return "El elemento se deshizo"
        raise IndexError ("La pila deshacer esta vacia")
    
    def rehacer(self):
        if not self.is_empty_deshacer_pila():
            dato = self.deshacer_pila.pop()
            self.editor.append(dato)
        raise IndexError("La pila deshacer esta vacia")
    
    def ver_editor(self):
        if not self.is_empty():
            return self.editor
        raise IndexError ("La pila deshacer esta vacia")
    
admin = P_editor()
admin.push(8)
admin.push(9)
admin.push(5)
admin.push(1)
admin.deshacer()
print(admin.ver_editor())

# 10- Crea un programa que convierta una expresión infija a posfija utilizando una pila.
# Una expresión infija y una expresión posfija son dos maneras diferentes de escribir expresiones aritméticas, infija = (5 + 2) * 2 / posfija 52+2* , no se necesitan parentesis
def infija_a_posfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pila = []
    salida = []
    for char in expresion:
        if char.isalnum():  # Si el carácter es un operando (número o letra)
            salida.append(char)
        elif char == '(':
            pila.append(char)
        elif char == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        else:  # Si el carácter es un operador
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia[char]:
                salida.append(pila.pop())
            pila.append(char)

    while pila:
        salida.append(pila.pop())
    return ''.join(salida)
expresion = "(A+B)*C"
print(infija_a_posfija(expresion)) 

# 11- Implementa una pila que limite su tamaño y maneje el error de desbordamiento.
# un desbordamiento de pila ocurre cuando se intenta agregar un elemento a una pila que ya está llena. Este escenario es más común en pilas de tamaño fijo.
class Limite_pila:
    def __init__(self, limite):
        self.pila = []
        self.limite = limite
    
    def push(self, dato):
        if len(self.pila) >= self.limite:
            raise OverflowError("La pila esta llena(desbordamiento), libere espacio")
        self.pila.append(dato)

    def ver_pila(self):
        return self.pila

    def pop(self):
        return self.pila.pop() 
ad = Limite_pila(3)
ad.push(7)
ad.push(4)
ad.push(6)
try: 
    ad.push(3)
except OverflowError as e:
    print(e)

# 12- Crea un programa que use una pila para evaluar expresiones aritméticas.
class Pila_aritmetica():
    def __init__(self):
        self.Pila_a = []
        self.expresiones = ["+", "-", "*", "**", "/"]

    def push(self, dato):
        self.Pila_a.append(dato)

    def push_expresiones(self, expresion):
        self.expresiones.append(expresion)

    def peek(self):
        if self.is_empty():
            raise IndexError ("La pila esta vacia")
        return self.Pila_a[-1]
    
    def pop(self):
        if self.is_empty():
            raise IndexError ("La pila esta vacia")
        return self.Pila_a.pop()

    def is_empty(self):
        return len(self.Pila_a) == 0
    
    def evaluar(self):
        for char in self.expresiones:
            if char in self.Pila_a:
                print(f"La expresion: {char}, esta adentro de la pila")
            else:
                print(f"La expresion {char}, no esta en la pila")
am = Pila_aritmetica()
am.push(8)
am.push("*")
am.push("/")
am.push(80)
print(am.evaluar())

# 13- Implementa un método que devuelva el tamaño de la pila.
def size(self, lista):
    return f"El tamaño de la pila es: {len(lista)}"
Pila_Matematica.size = size
print(dato.size([2, 5]))

# 14- Crea una pila que almacene objetos y permita acceder a sus atributos.
class Pila_objetos():
    def __init__(self):
        self.objetos = []
    
    def push(self, obj):
        self.objetos.append(obj)

    def peek(self):
        if not self.is_empty():
            return self.objetos[-1]
        raise IndexError("La pila esta vacia")
    
    def pop(self):
        if not self.is_empty():
            return self.objetos.pop()
        raise IndexError("La pila esta vacia")
    
    def atributos(self):
        return self.objetos
    
    def is_empty(self):
        return len(self.objetos) == 0
    
obj = Pila_objetos()
obj.push(5)
obj.push(1)
obj.push(7)
obj.push(3)
print(obj.atributos())

# 15- Desarrolla un programa que use una pila para realizar un recorrido en profundidad en un árbol.
class Pila_nodo():
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
# árbol binario de búsqueda (BST)
dato = Pila_nodo(8) #arbol raiz
dato.izquierda = Pila_nodo(6) # todos los numeros menores que el nodo raiz van a la izquierda
dato.izquierda.izquierda = Pila_nodo(4) # todos lo menores que 8 van a la izquierda
dato.izquierda.derecha = Pila_nodo(7) # todoos los mayores que 6 pero menores que 8(nodo raiz) van a la derecha de el segundo hijo
dato.izquierda.izquierda.izquierda = Pila_nodo(2)
dato.derecha = Pila_nodo(15) # tdos los mayores que el nodo raiz van a la derecha
dato.derecha.derecha = Pila_nodo(17)
dato.derecha.izquierda = Pila_nodo(13)
dato.derecha.derecha.derecha = Pila_nodo(20)

#         8
#        / \
#       6   15
#      / \  / \
#     4   7 13 17
#    /           \
#   2             20

def recorrer(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        recorrer(nodo.izquierda)
        recorrer(nodo.derecha)
recorrer(dato)

# Mini Proyectos:
# Desarrolla una aplicación de notas que permita agregar, eliminar y ver notas utilizando una pila.
class Pila_notas():
    def __init__(self):
        self.notas = []

    def agregar_push(self, nota):
        self.notas.append(nota)
        return "Nota agregada"
    
    def eliminar_pop(self):
        if not self.is_empty():
            return self.notas.pop()
        raise IndexError("La pila esta vacia")
    
    def ver_notas(self):
        if not self.is_empty():
            return self.notas
        raise IndexError("La pila esta vacia")
    
    def is_empty(self):
        return len(self.notas) == 0
    
note = Pila_notas()
note.agregar_push("luz")
note.agregar_push("agua")
note.agregar_push("Internet")
print(note.ver_notas())

# Crea un simulador de deshacer/rehacer para un editor de texto utilizando pilas.
class Pila_editor:
    def __init__(self):
        self.deshacer_pila = []
        self.rehacer_pila = []
    
    def rehacer_push(self, texto): # metodo patra subirlo a la pila
        self.deshacer_pila.append(texto)
        # Limpiar la pila de rehacer cuando se agrega un nuevo elemento
        self.rehacer_pila = []
        print(f"Texto '{texto}' agregado.")
    
    def deshacer_pop(self): # metodo pata sacarlo de la pila
        if not self.is_empty():
            # Mover el último elemento de deshacer_pila a rehacer_pila
            elemento = self.deshacer_pila.pop()
            self.rehacer_pila.append(elemento)
            print(f"Deshacer: '{elemento}'")
            return elemento
        raise IndexError("La pila de deshacer está vacía.")
    
    def rehacer(self): # metodo para volver a ponerlo en la pila
        if not self.rehacer_is_empty():
            # Mover el último elemento de rehacer_pila a deshacer_pila
            elemento = self.rehacer_pila.pop()
            self.deshacer_pila.append(elemento)
            print(f"Rehacer: '{elemento}'")
            return elemento
        raise IndexError("La pila de rehacer está vacía.")
    
    def ver_editor(self):
        if not self.is_empty():
            return self.deshacer_pila
        raise IndexError("La pila de deshacer está vacía.")
    
    def is_empty(self):
        return len(self.deshacer_pila) == 0
    
    def rehacer_is_empty(self):
        return len(self.rehacer_pila) == 0

editor = Pila_editor()
editor.rehacer_push("Primera línea")
editor.rehacer_push("Segunda línea")
editor.rehacer_push("Tercera línea")
print(editor.ver_editor())
print("------------------")
editor.deshacer_pop()
editor.deshacer_pop()
print(editor.ver_editor())
print("------------------")
editor.rehacer()
editor.rehacer()
print(editor.ver_editor())
print("------------------")

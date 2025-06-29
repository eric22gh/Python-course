# Día 59: Ejercicios de búsqueda binaria
# En este día, se practicarán diversas implementaciones y variaciones de la búsqueda binaria para reforzar el aprendizaje.

# Teoría
# La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada.
# Requiere que la lista esté ordenada y funciona dividiendo el espacio de búsqueda a la mitad en cada iteración.
# La complejidad temporal de la búsqueda binaria es O(log n), lo que la hace muy eficiente para listas grandes.


# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.
# Utiliza comentarios en tu código para explicar cada paso del algoritmo.


# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.
# Utiliza nombres descriptivos para funciones y variables.
# Mantén tu código limpio y organizado, siguiendo las convenciones de estilo de Python.


# Ejercicios
# 1- Implementa un algoritmo de búsqueda binaria que devuelva -1 si el elemento no se encuentra.
def BinarySearch(elements, Value):
    if not elements:
        return "the List is empty"
    elif not Value:
        return "The value is empty"
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return Value
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return -1
print(BinarySearch([1, 2, 3, 4, 5, 6, 10, 22, 56], 21))

# 2- Crea un método que busque un valor en una lista de enteros ordenados y retorne verdadero o falso.
def SearchFalseTrue(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return True
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return False
print(SearchFalseTrue([1, 2, 3, 4, 5, 6, 10, 22, 56], 22))

# 3- Desarrolla un algoritmo que encuentre el primer y último índice de un elemento en una lista ordenada.
def FirstAndLastIndex(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    first_index = -1
    last_index = -1
    left, right = 0, len(elements) - 1
    
    # Buscar el primer índice
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            first_index = medium
            right = medium - 1  # Seguir buscando a la izquierda
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    
    left, right = 0, len(elements) - 1
    
    # Buscar el último índice
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            last_index = medium
            left = medium + 1  # Seguir buscando a la derecha
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    
    return first_index, last_index
print(FirstAndLastIndex([1, 2, 3, 4, 5, 6, 10, 22, 22, 22, 56], 22))

# 4- Escribe un programa que imprima todos los elementos que coinciden con un valor dado en una lista ordenada.
def PrintALLtheSAmeElements(elements, value):
    if not elements:
        return "the list is empty"
    elif not value:
        return "the value is empty"
    left, right = 0, len(elements) - 1
    aux = []
    # Buscar la primera ocurrencia
    firt_Index = -1
    while left <= right:
        medium = (left +  right) // 2
        if elements[medium] == value:
            firt_Index = medium # va aguardar el primer indice
            right = medium - 1 # Buscar derecha a Izquierda
        elif elements[medium] < value:
            left = medium + 1
        else:
            right = medium - 1
    # Desde la primera ocurrencia, ir hacia la derecha y agregar mientras coincidan
    if firt_Index == -1:
        return "I did not find the value"
    sux = firt_Index
    while sux < len(elements) and elements[sux] == value: # si 7(el primer indice donde coinciden) es mayor a la cantidad de elementos en la lista y
        # y a la vez el  elemento 7 de lista es igual al valor buscado, se agrega a aux
        aux.append(value)
        sux += 1 # se sube el contador y se avanza a siguiente elemento de la lista
    print(aux)
PrintALLtheSAmeElements([1, 2, 3, 4, 5, 6, 10, 21, 21, 21, 56], 21)
        
# 5- Implementa un algoritmo que busque un número en una lista ordenada y retorne el número de comparaciones realizadas.
def Comparisons(elements, Values):
    if not elements:
        return "the list is empty"
    elif not Values:
        return "the value is empty"
    lux = 0
    left, right = 0, len(elements) - 1
    while left <= right:
        lux += 1
        medium = (left + right) // 2
        if elements[medium] == Values: # incompleto no cuenta bien
            return lux 
        elif elements[medium] < Values:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(Comparisons([1, 2, 3, 4, 5, 6, 10, 21, 24, 28, 56], 56))

# 6- Crea un método que busque un valor en una lista de diccionarios ordenados y retorne el diccionario completo.
def SearchInDict(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium]['value'] == Value:  # Asumiendo que el diccionario tiene una clave 'value'
            return elements[medium]
        elif elements[medium]['value'] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(SearchInDict([{'value': 1}, {'value': 2}, {'value': 3}, {'value': 4}, {'value': 5}], 3))

# 7- Desarrolla un algoritmo que encuentre el índice del elemento más cercano a un valor dado en una lista ordenada.
def ClosestElement(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    closest_index = -1
    closest_diff = float('inf')  # Inicializar con infinito
    
    while left <= right:
        medium = (left + right) // 2
        diff = abs(elements[medium] - Value) # que hace abs: # devuelve el valor absoluto de la diferencia entre el elemento y el valor buscado
        
        if diff < closest_diff:
            closest_diff = diff
            closest_index = medium
        
        if elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    
    return closest_index
print(ClosestElement([1, 2, 3, 4, 5, 6, 10, 21, 24, 28, 56], 23))

# 8- Escribe un programa que busque un número en una lista ordenada y retorne el número de elementos que le preceden.
def SearchElements(list, value):
    if not list:
        return "the list is empty"
    elif not value:
        return "the value is empty"
    previous = 0
    left, right = 0, len(list) - 1
    while left <= right:
        medium = (left + right) // 2
        previous = medium
        if list[medium] == value:
            return previous
        elif list[medium] < value:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the element"

print(SearchElements([1, 2, 3, 4, 10], 10))

# 9- Implementa un algoritmo que busque un elemento en una lista de objetos basándose en un atributo.
# Atributo: Es una propiedad o característica de un objeto. En POO, los atributos son variables que pertenecen a una clase y describen el estado o las propiedades del objeto.
def SearchInObjects(elements, attribute):
    if not elements:
        return "the list is empty"
    elif not attribute:
        return "the value is empty"
    elif len(attribute) > 3 or len(attribute) < 3:
        return "the attribute must be 3 characters long"
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium][:3] == attribute:  
            return elements[medium]
        elif elements[medium][:3] < attribute:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(SearchInObjects(['apple','banana', 'cherry', "dulce", "uva"], 'dul'))
    

# 10- Crea un método que busque un valor en una lista de cadenas ordenadas y retorne la cadena completa.
def SearchInStrings(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return elements[medium]
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(SearchInStrings(["apple", "banana", "cherry", "date", "fig"], "cherry"))

# 11- Desarrolla un algoritmo que busque un número en una lista ordenada y retorne el índice o -1.
def IndexReturn(elements, Value):
    if not elements:
        return "The list is empty"
    elif not Value:
        return "The value is empty"
    left, right = 0, len(elements) -1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return medium
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return -1
print(IndexReturn(["apple", "banana", "cherry", "date", "fig"], "cherry"))

# 12- Escribe un programa que busque un elemento en una lista de floats ordenados y retorne su índice.
def SearchInFloats(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return medium
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(SearchInFloats([1.1, 2.2, 3.3, 4.4, 5.5], 3.3))

# 13- Implementa un algoritmo que busque un número en una lista ordenada y retorne el valor anterior.
def PreviousValue(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    previous = None
    
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            return previous if previous is not None else "No previous value found"
        elif elements[medium] < Value:
            previous = elements[medium]
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
print(PreviousValue([1, 2, 3, 4, 5, 6, 10, 22, 56], 22))
# 14- Crea un método que busque un número en una lista de enteros ordenados y retorne el índice del siguiente mayor.
def NextGreaterIndex(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    next_index = -1
    
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] > Value:
            next_index = medium
            right = medium - 1  # Buscar a la izquierda para encontrar el menor índice
        else:
            left = medium + 1
    
    return next_index if next_index != -1 else "No greater element found"
print(NextGreaterIndex([1, 2, 3, 4, 5, 6, 10, 22, 56], 22))

# 15- Desarrolla un algoritmo que busque un número en una lista ordenada y determine si es un número primo.
def IsPrime(elements, Value):
    if not elements:
        return "the list is empty"
    elif not Value:
        return "the value is empty"
    
    left, right = 0, len(elements) - 1
    
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == Value:
            # Verificar si el número es primo
            if Value < 2:
                return False
            for i in range(2, int(Value**0.5) + 1):
                if Value % i == 0:
                    return False
            return True
        elif elements[medium] < Value:
            left = medium + 1
        else:
            right = medium - 1
    
    return "I did not find the value"
print(IsPrime([2, 3, 5, 7, 11, 13, 17, 19], 13))


# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas ordenadas y permita buscar tareas por nombre.
class TaskManager:
    def __init__(self):
        self.storague = []
        
    def Is_Empty(self):
        return len(self.storague) == 0
        
    def add_task(self, Task):
        if not isinstance(Task, str):
            raise TypeError("I  only accept words")
        self.storague.append(Task.capitalize())
        self.storague.sort()
        
    def SearchTask(self, Task):
        if self.Is_Empty():
            return "The list is empty"
        elif not isinstance(Task, str):
            raise TypeError("I only accept words")
        left, right = 0, len(self.storague) - 1
        while left <= right:
            medium = (left +  right) // 2
            if self.storague[medium] == Task.capitalize():
                return f"I found the Task: {self.storague[medium]}"
            elif self.storague[medium] < Task.capitalize():
                left = medium + 1
            else:
                right = medium - 1
        return "I did not find the Task"
    
    def EraseTask(self, Task):
        if self.Is_Empty():
            return "The list is empty I can not erase anything"
        elif not isinstance(Task, str):
            raise("The task must be a text to eliminate")
        elif Task.capitalize() not in self.storague:
            return f"The task {Task} does not exist in the list so I can not erase it"
        self.storague.remove(Task.capitalize())
        return f"The {Task} Sucessfuly eliminate"
    
    def ViewTask(self):
        if self.Is_Empty():
            return "The list is empty"
        count = 1
        for tasks in self.storague:
            print(f"Task: {count}- {tasks}")
            count += 1
    
Manager = TaskManager()
Manager.add_task("Paint")
Manager.add_task("Whash the dishes")
Manager.add_task("Mow the lawn")
Manager.add_task("mop the floor")
Manager.add_task("hang the picture")
print(Manager.EraseTask("Whash the dishes"))
Manager.ViewTask()
print(Manager.SearchTask("mow the lawn"))

# Crea un simulador de un sistema de gestión de reservas que utilice búsqueda binaria para encontrar asientos disponibles.
class Reservation:
    def __init__(self):
        self.seats = []
        
    def Is_Empty(self):
        return len(self.seats) == 0
    
    def AddSeat(self, seat):
        if not isinstance(seat, int):
            raise TypeError("I only accept numbers")
        self.seats.append(seat)
        self.seats.sort()
        
    def SearchSeat(self, seat):
        if self.Is_Empty():
            return "The list is empty"
        elif not isinstance(seat, int):
            raise TypeError("I only accept numbers")
        left, right = 0, len(self.seats) - 1
        while left <= right:
            medium = (left + right) // 2
            if self.seats[medium] == seat:
                return f"I found the Seat: {self.seats[medium]}"
            elif self.seats[medium] < seat:
                left = medium + 1
            else:
                right = medium - 1
        return "I did not find the Seat"
    
    def EraseSeat(self, seat):
        if self.Is_Empty():
            return "The list is empty I can not erase anything"
        elif not isinstance(seat, int):
            raise TypeError("The seat must be a number to eliminate")
        elif seat not in self.seats:
            return f"The seat {seat} does not exist in the list so I can not erase it"
        self.seats.remove(seat)
        return f"The {seat} Sucessfuly eliminate"
    
    def ViewSeats(self):
        if self.Is_Empty():
            return "The list is empty"
        count = 1
        for seats in self.seats:
            print(f"Seat: {count}- {seats}")
            count += 1
            
            
Manager = Reservation()
Manager.AddSeat(1)
Manager.AddSeat(6)
Manager.AddSeat(3)
Manager.AddSeat(5)
Manager.AddSeat(7)
Manager.ViewSeats()
print(Manager.EraseSeat(2))
print(Manager.SearchSeat(3))
# Día 32: Ejercicios de búsqueda lineal
# Teoría: En este día, se practicarán diversas implementaciones y variaciones de la búsqueda lineal para reforzar el aprendizaje.

# Tips
# Asegúrate de entender cada ejercicio antes de implementarlo.
# Comparte tus soluciones con compañeros para recibir retroalimentación.

# Buenas Prácticas
# Documenta cada solución y analiza su eficiencia.
# Realiza pruebas exhaustivas con diferentes entradas.


# Ejercicios

# 1- Implementa un algoritmo de búsqueda lineal que devuelva -1 si el elemento no se encuentra.
def linear_search(elements, obj):
    if len(elements) == 0 and obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    elif not isinstance(obj, (str, int)):
        raise TypeError("I only accept strings or integer elements")
    for i in range(0, len(elements)):
        if elements[i] == obj:
            return i
        return -1
print(linear_search([8, 22, "eric", 5], "helen"))

# 2- Crea un método que busque un valor en una lista de enteros y retorne verdadero o falso.
def Integer_list(Integers, obj):
    if len(Integers) == 0 and obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(Integers, list):
        raise TypeError("Error: elements must be a list")
    elif not isinstance(obj, (str, int)):
        raise TypeError("I only accept strings or integer elements")
    for i in range(0, len(Integers)):
        if Integers[i] == obj:
            return True
        return False
    
print(Integer_list([8, 22, "eric", 5], 1))

# 3- Desarrolla un algoritmo que encuentre el primer y último índice de un elemento en una lista.
def Index_of_elements(elements, obj):
    if len(elements) == 0 and obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    elif not isinstance(obj, str):
        raise TypeError("Error: The object is not a string")
    for i in range(0, len(elements)):
        if elements[i] == obj:
            return str(obj[0]) + " and " + str(obj[-1])
print(Index_of_elements(["carlos", "helen", "eric", "paris"], "helen"))

# 4- Escribe un programa que imprima todos los elementos que coinciden con un valor dado en una lista.
def Coincidence(elements, value):
    if len(elements) == 0 and value == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    for i in range(0, len(elements)):
        if elements[i][0].lower() == value.lower():
            print(elements[i])
    print("I did not find any coincidence in the list with value")
            
Coincidence(["carlos", "helen", "eric", "paris", "Erika"], "e")

# 5- Implementa un algoritmo que busque un elemento en una lista de cadenas ignorando mayúsculas y minúsculas.
def Ignore_case_search(elements, obj):
    if len(elements) == 0 and obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    elif not isinstance(obj, str):
        raise TypeError("Error: The object is not a string")
    for i in range(0, len(elements)):
        if elements[i].lower() == obj.lower():
            return "I found the object"
    return -1

print(Ignore_case_search(["carlos", "helen", "eric", "paris"], "HELEN"))
# 6- Desarrolla un algoritmo que busque un número en una lista y retorne el número de comparaciones realizadas.
def Comparisons(elements, obj):
    if len(elements) == 0 and obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    count = 0
    for i in range(0, len(elements)):
        count += 1
        if elements[i].lower() == obj.lower():
            return count
    return "I did not find the item"
print(Comparisons(["carlos", "helen", "eric", "paris"], "HELEN"))

# 7- Escribe un programa que busque un elemento en una lista y retorne una lista de todos los índices donde se encuentra.
def Find_index(elements, obj):
    if len(elements) == 0 or obj == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    Index_list = []
    for i in range(0, len(elements)):
        if isinstance(obj, str) and isinstance(elements[i], str):
            if elements[i].lower() == obj.lower():
                Index_list.append(i) 
        elif isinstance(obj, int) and isinstance(elements[i], int):
            if elements[i] == obj:
                Index_list.append(i)  
    return Index_list if Index_list else "I did not find the items"  
    
print(Find_index(["carlos", "helen", "eric", 0, "paris", "HELEN", 0], "HeLeN"))
print(Find_index(["carlos", "helen", "eric", 0, "paris", "HELEN", 0], 0))

# 8- Implementa un algoritmo que busque un elemento en una lista de objetos basándose en un atributo.
def Find_object(Objects, attribute):
    if len(Objects) == 0 or attribute == None:
        return "One or both of the fields are empty"
    elif not isinstance(Objects, list):
        raise TypeError("Error: elements must be a list")
    for i in range(0, len(Objects)):
        if isinstance(Objects[i], dict) and "name" in Objects[i]:
            if Objects[i]["name"].lower() == attribute.lower():
                return Objects[i]
    return "I did not find the object with that name"

print(Find_object([{"name": "carlos"}, {"name": "helen"}, {"name": "eric"}], "helen"))
 

# 9- Desarrolla un algoritmo que encuentre el índice del elemento más cercano a un valor dado en una lista.
def Nearest_Index(elements, value):
    if len(elements) == 0 and value == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    for i in range(0, len(elements)):
        if elements[i] == value:
            return str(i-1) + " and " + str(i+1)
    return "I did not find a value in the list with that name"
print(Nearest_Index(["carlos", "helen", "eric", 0, "paris", "HELEN"], "paris"))
    
# 10- Escribe un programa que busque un número en una lista y retorne el número de elementos que le preceden.
def Count_elements(elements, number):
    if len(elements) == 0 and number == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    count = 0
    for i in range(0, len(elements)):
        count += 1
        if elements[i] == number:
            return f"The amount of elements before {number} is: {count - 1}"
    return "I did not find the value in the list"
print(Count_elements([1, 89, 63, 5, 45, 22, 6], 22))

    
# 11- Implementa un algoritmo que busque una subcadena en una lista de cadenas.
def Sub_string(elements, sub_string):
    if len(elements) == 0 and sub_string == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    for i in range(0, len(elements)):
        if isinstance(elements[i], str) and sub_string in elements[i]:
            if elements[i][:3].lower() == sub_string.lower():
                return f"I found the substring {sub_string} in the string {elements[i]}"
    return "I did not find the substring in the list"
print(Sub_string(["HELEN", "carlos", "helen", "eric", "paris"], "hel"))

# 12- Crea un método que busque un elemento en una lista y retorne el valor anterior.
def Previous_value(elements, value):
    if len(elements) == 0 and value == None:
        return "One or both of the fields are empty"
    elif not isinstance(elements, list):
        raise TypeError("Error: elements must be a list")
    for i in range(0, len(elements)):
        if elements[i] == value:
            if i > 0:
                return f"The previous value of {value} is {elements[i-1]}"
            else:
                return f"There is no previous value for {value}"
    return "I did not find the value in the list"
print(Previous_value([1, 89, 63, 5, 45, 22, 6], 22))

# Mini Proyectos
# Desarrolla un programa que gestione una lista de tareas y permita buscar tareas por nombre.
def Task_manager(tasks, task_name):
    if len(tasks) == 0 and task_name == None:
        return "One or both of the fields are empty"
    elif not isinstance(tasks, list):
        raise TypeError("Error: tasks must be a list")
    for i in range(0, len(tasks)):
        if isinstance(tasks[i], dict) and "task" in tasks[i]:
            if tasks[i]["task"].lower() == task_name.lower():
                return f"I found the task: {tasks[i]}"
    return "I did not find the task in the list"

print(Task_manager([{"task": "Buy groceries"}, {"task": "Clean the house"}, {"task": "Walk the dog"}], "clean the house"))
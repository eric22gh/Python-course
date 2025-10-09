# Día 81

# Ejercicio 402: Implementa una función que verifique si un año es bisiesto.
# Conceptos: Matemáticas, funciones.
def LeapYear(year):
    if not isinstance(year, int):
        return "Input must be an integer"
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
print(LeapYear(2020))  
print(LeapYear(1900))  

# Ejercicio 403: Escribe un programa que lea un archivo de texto y busque líneas que contengan una palabra específica.
# Conceptos: Manejo de archivos.
def search_word_in_file(file_path, word):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matching_lines = [line.strip() for line in lines if word in line]
            return matching_lines
    except FileNotFoundError:
        return "File not found"
print(search_word_in_file('example.txt', 'specific'))



# Día 82

# Ejercicio 407: Implementa una función que calcule la distancia entre dos puntos en el espacio tridimensional.
# Conceptos: Matemáticas, funciones.
import math
def distance_3d(point1, point2):
    if len(point1) != 3 or len(point2) != 3:
        return "Both points must have three coordinates"
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
print(distance_3d((1, 2, 3), (4, 5, 6)))



# Día 83 

# Ejercicio 412: Implementa una función que encuentre el índice de un elemento en una lista.
# Conceptos: Listas, funciones.
def find_index(elements, aux):
    try:
        return elements.index(aux)
    except ValueError:
        return -1
print(find_index([10, 20, 30, 40], 30))
    

# Ejercicio 413: Escribe un programa que lea un archivo JSON y lo imprima en formato legible.
# Conceptos: Manejo de archivos, JSON.
import json
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return json.dumps(data, indent=4)
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Error decoding JSON"
print(read_json_file('example.json'))

# Ejercicio 414: Crea una función que reciba una lista de números y devuelva el promedio.
# Conceptos: Listas, funciones.
def AverageOflist(elements):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    elif not all(isinstance(n, int) for n in elements):
        raise TypeError("All the elements must be numbers")
    return sum(elements)/len(elements)
import random
numbers = [random.randint(1, 100) for _ in range(8)]
print(AverageOflist(numbers))



# Día 84

# Ejercicio 417: Implementa una función que verifique si una cadena es un anagrama de otra.
# Conceptos: Manipulación de strings.
def Anagram(word1, word2):
    import re
    aux1 = re.sub(r"[^a-zA-Z]", "", word1)
    aux2 = re.sub(r"[^a-zA-Z]", "", word2)
    return sorted(aux1), sorted(aux2)
print(Anagram(".-r oma8", "amo+r, "))
    

# Ejercicio 418: Escribe un programa que genere un archivo de texto con una lista de nombres aleatorios.
# Conceptos: Manejo de archivos, números aleatorios.
def generate_random_names(file_path, count):
    import random
    import string
    names = []
    for _ in range(count):
        name_length = random.randint(4, 8)
        name = ''.join(random.choices(string.ascii_letters, k=name_length))
        names.append(name)
    with open(file_path, 'w') as file:
        for name in names:
            file.write(name + '\n')
generate_random_names('random_names.txt', 10)


# Ejercicio 419: Crea una función que reciba una lista y devuelva la lista de números enteros.
# Conceptos: Listas, funciones.
def filter_integers(elements):
    if not isinstance(elements, list):
        raise TypeError("The element must be a list")
    return [n for n in elements if isinstance(n, int)]
print(filter_integers([1, 'two', 3.0, 4, 'five', 6]))


# Día 85

# Ejercicio 422: Implementa una función que calcule el área de un círculo dado su radio.
# Conceptos: Matemáticas, funciones.
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("The radius must be a number")
    elif radius < 0:
        raise ValueError("The radius cannot be negative")
    import math
    return math.pi * radius ** 2
print(circle_area(5))


# Ejercicio 423: Escribe un programa que lea un archivo de texto y cuente la cantidad de caracteres.
# Conceptos: Manejo de archivos.
def count_characters_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return "File not found"
print(count_characters_in_file('example.txt'))

# Ejercicio 424: Crea una función que reciba una lista de palabras y devuelva la palabra más repetida.
# Conceptos: Listas, funciones.
def most_frequent_word(words):
    if not isinstance(words, list):
        raise TypeError("The element must be a list")
    elif not all(isinstance(word, str) for word in words):
        raise TypeError("All the elements must be strings")
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]
print(most_frequent_word(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))
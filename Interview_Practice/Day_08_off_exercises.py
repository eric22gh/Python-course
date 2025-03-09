# Día 8

# Ejercicio 36: Crea una función que reciba un número y devuelva True si es par, False si es impar.
# Conceptos: Funciones, condicionales.
def even_odd_numbers(num):
    if not isinstance(num, (int, float)):
        raise TypeError("I only accept numbers")
    return num % 2 == 0
        
print(even_odd_numbers(53))

# Ejercicio 37: Escribe un programa que imprima el reverso de una cadena.
# Conceptos: Manipulación de strings, bucles.
def reversed_string(aux):
    if not isinstance(aux, str):
        raise TypeError("I only accept strings")
    elif not aux:
        return "the string is empty"
    return aux[::-1]
print(reversed_string("Eric"))

# Ejercicio 38: Crea una lista de palabras y encuentra la más larga.
# Conceptos: Listas, funciones.
def largest_word(list_words):
    if not isinstance(list_words, list):
        raise TypeError("We only accept list of words")
    elif len(list_words) == 0:
        return "The list is empty"
    else:
        if not all(isinstance(aux, str) for aux in list_words ):
            raise TypeError("The list must contain only strings")
        return max(list_words, key=len) 
    
new = ["eric", "muercielago", "Helen"]
print(largest_word(new))

# Ejercicio 39: Escribe un programa que cuente cuántos números son mayores que 10 en una lista.
# Conceptos: Listas, bucles.
def bigger_than_ten(list_numbers):
    if not isinstance(list_numbers, list):
        raise TypeError("We need a list")
    elif len(list_numbers) == 0:
        return "the list is empty"
    else:
        if not all(isinstance(x, int) for x in list_numbers):
            raise TypeError("All the elements in the list must be numbers")
        else:
            cont = 0
            for n in list_numbers:
                if n > 10:
                    cont += 1
            return f"the amount off numbers bigger than 10 is {cont}"
nums_list = [52, 1, 6, 22, 3, 45]
print(bigger_than_ten(nums_list))

# Ejercicio 40: Crea una función que reciba dos listas y devuelva la intersección.
# Conceptos: Listas, funciones.
def intersection_off_lists(list_1, list_2):
    if not isinstance((list_1 and list_2), list):
        raise TypeError("we only accept lists")
    elif len(list_1) == 0 or len(list_2) == 0:
        return "One of the list or both of them are empty"
    else:
        set_1 = set(list_1)
        set_2 = set(list_2)
        result = list(set_1.intersection(set_2))
        return result

list_one = ["eric", 22, "helen", 21, "noviembre"]
list_two = ["edwards", 31, "calvin", 42,"noviembre"]
print(intersection_off_lists(list_one, list_two))

# Día 15
# Ejercicio 71: Crea una función que encuentre la longitud de una lista.
# Conceptos: Listas, funciones.
def length_of_list(aux):
        if not isinstance(aux, list):
            raise TypeError("I need a list")
        else:
            return 0 if not aux  else len(aux)
    
data = [8, 89, 56, 89, 25]
print(length_of_list(data))

# Ejercicio 72: Escribe un programa que convierta un número decimal a binario.
# Conceptos: Matemáticas, funciones.
def dec_bin(n):
        if not isinstance(n, (int, float)):
            raise TypeError("I need decimals")
        return 0 if not n else bin(int(n))
print(dec_bin(10.0))

# Ejercicio 73: Crea una función que encuentre el número más pequeño en una lista.
# Conceptos: Listas, funciones.
def smallest_num(numbers):
    if not isinstance(numbers, list):
        raise TypeError("I only accept lists")
    elif not numbers:
        return None
    elif not all(isinstance(n, (int, float))for n in numbers):
        raise TypeError("I only accept numbers in the list")
    aux = numbers[0]
    for i in numbers:
        if i < aux:
            aux = i
    return aux
data = [20, 56, 8, 59, 1]
print(smallest_num(data))
        
# Ejercicio 74: Escribe un programa que imprima los elementos de una lista en orden inverso.
# Conceptos: Listas, bucles.
def reverse(elements):
    if not isinstance(elements, list):
        raise TypeError("I only accept lists")
    if not all(isinstance(n, (int, float))for n in elements):
        raise TypeError("I only accept numbers in the list")
    return [] if not elements else elements[::-1]
print(reverse([85, 25, 66]))

# Ejercicio 75: Crea una función que reciba una cadena y devuelva el número de vocales.
# Conceptos: Manipulación de strings, funciones.
def vowels(aux):
    data = "AEIOUaeiou"
    results = {}
    if not isinstance(aux, str):
        raise TypeError("I only accept words")
    if not aux:
        return None
    for i in aux:
        if i in data:
            results[i] = results.get(i, 0) + 1
    return results
print(vowels("murcielagoo"))
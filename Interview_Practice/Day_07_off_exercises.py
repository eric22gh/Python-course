# Día 7
# Ejercicio 31: Escribe un programa que imprima los números de 1 a 100, pero solo los múltiplos de 7.
# Conceptos: Bucles, condicionales.
def Seven_Multiplies():
    for aux in range(1, 101):
        if aux % 7 == 0:
            print(f"the number: {aux} is multiplie from 7")

Seven_Multiplies()

# Ejercicio 32: Crea una función que reciba un string y devuelva el número de palabras.
# Conceptos: Manipulación de strings, funciones.
def Count_words(aux):
    if not isinstance(aux, str):
        raise TypeError("You need a string")
    count = len(aux.split())
    return f"the amount of words in the string is: {count}"
print(Count_words("eric hernandez de la  Edwards "))

# Ejercicio 33: Escribe un programa que encuentre el segundo número más grande en una lista.
# Conceptos: Listas, bucles.
import random
def The_Second(aux):
    if not isinstance(aux, list):
        raise TypeError("You need a list with numbers")
    elif len(aux) == 0:
        return "the list is empty"
    else:
        # Verificar que todos los elementos sean números
        if not all(isinstance(x, int) for x in aux):
            raise TypeError("The list must contain only numbers")
        aux_2 = list(set(aux)) # eliminar duplicados
        aux_2.sort()
        return f"the second biggest number in the list: {aux_2} is: {aux_2[-2]}"
    
list_number = [random.randint(1, 100) for aux in range(8)]
print(The_Second(list_number))

# Ejercicio 34: Crea un programa que genere una lista de 10 números aleatorios y calcule su media.
# Conceptos: Listas, funciones integradas.
def Average(aux):
    if not isinstance(aux, list):
        raise TypeError("we need a list")
    elif len(aux) == 0:
        return "the list is empty"
    else:
        if not all(isinstance(x, (int, float)) for x in aux):
            raise TypeError("The list must contain only numbers")
        numbers = sum(aux)
        amount = len(aux)
        total = numbers / amount
        return f"The averague from the list is: {total}"

new_list = [random.randint(1, 200) for aux in range(10)]
print(Average(new_list))

# Ejercicio 35: Escribe un programa que imprima una pirámide de números.
# Conceptos: Bucles, impresión.
def piramid(n):
    if not isinstance(n, int):
        raise TypeError("we only accept numbers")
    for i in range(1, (n + 1)):
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end=" ")
        print()

piramid(5)
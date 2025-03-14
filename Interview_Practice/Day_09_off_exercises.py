# Día 9

# Ejercicio 41: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz".
# Conceptos: Bucles, condicionales.
for aux in range(1, 101):
    if aux % 3 == 0 and aux % 5 == 0:
        print("FizzBuzz")
    elif aux % 3 == 0:
        print("Fizz")
    elif aux % 5 == 0:
        print("Buzz")
    print(aux)


# Ejercicio 42: Crea una función que reciba una lista y devuelva el elemento más pequeño.
# Conceptos: Listas, funciones.
def minimun_element_of_list(list_elements):
    if not isinstance(list_elements, list):
        raise TypeError("I only accept list")
    elif len(list_elements) == 0:
        return "The list is empty"
    return min(list_elements)

var = [5, 500, 1, 22]
print(minimun_element_of_list(var))

# Ejercicio 43: Escribe un programa que imprima el factorial de un número dado.
# Conceptos: Bucles, recursividad.
def factorial(aux):
    if aux < 0:
        raise ValueError("El número debe ser no negativo")
    elif aux == 0:
        return 1
    return aux * factorial(aux - 1)
print(factorial(5))
    
# Ejercicio 44: Crea un programa que imprima los números del 1 al 50 y solo los múltiplos de 3.
# Conceptos: Bucles, condicionales.
def multply_of_3():
    for aux in range(1, 51):
        if aux % 3 == 0:
            print(aux, end=", ")
multply_of_3()

# Ejercicio 45: Escribe un programa que encuentre la suma de los cuadrados de los números del 1 al 10.
# Conceptos: Bucles, matemáticas.
def sum_of_square_numbers():
    count = 0
    for aux in range(1, 11):
        numbers = aux ** 2
        count += numbers
    return f"the sum of the square numbers is: {count}"
print(sum_of_square_numbers())
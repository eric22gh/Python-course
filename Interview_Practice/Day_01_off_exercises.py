# Día 1

# Ejercicio 1: Escribe un programa que imprima "Hola, Mundo".
# Conceptos: Salida básica.
print("Hola, Mundo")

# Ejercicio 2: Crea una función que sume dos números.
# Conceptos: Funciones, parámetros.
def sum_of_numbers():
    try:
        num_1 = float(input("Introduce the first number: "))
        num_2 = float(input("Introduce the second number: "))
        result = num_1 + num_2
        return f"The result of the sum is: {result}"
    except ValueError:
        return "Invalid input. Please enter valid numbers."

print(sum_of_numbers())

# Ejercicio 3: Escribe un programa que determine si un número es par o impar.
# Conceptos: Condicionales, operadores.
def even_or_odd():
    try:
        num = int(input("Introduce a number: "))
        if num % 2 == 0:
            return f"The number {num} is even."
        else:
            return f"The number {num} is odd."
    except ValueError:
        return "Invalid input. Please enter a valid integer."

print(even_or_odd())

# Ejercicio 4: Crea una lista y calcula su longitud.
# Conceptos: Listas, funciones integradas.
def length_of_list(my_list):
    if not isinstance(my_list, list):
        return "Invalid input. Expected a list."
    return f"The length of the list is: {len(my_list)}"

print(length_of_list([1, "eric", 1.5, True]))

# Ejercicio 5: Escribe un programa que invierta una cadena.
# Conceptos: Manipulación de strings.
def invert_string(aux):
    if not isinstance(aux, str):
        return "Invalid input. Expected a string."
    return aux[::-1]

print(invert_string("eric"))

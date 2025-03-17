# Día 10

# Ejercicio 46: Crea una función que reciba una cadena y devuelva la misma cadena sin espacios.
# Conceptos: Manipulación de strings, funciones.
def without_space(string):
    if not isinstance(string, str):
        raise TypeError("I only accept strings")
    elif not string:
        return "the string is empty"
    new = string.replace(" ", "")
    return new
print(without_space("Eric Hernandez Calvin 12 "))

# Ejercicio 47: Escribe un programa que imprima los números primos del 1 al 100.
# Conceptos: Bucles, condicionales.
def prime_numbers():
    for i in range(1, 101):
        p = int(i**0.5) + 1 # formula para numero primo
        if i % p == 0:
            print(i, end=", ")
prime_numbers()

# def prime_numbers():
#     for i in range(2, 101):  
#         is_prime = True
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i, end=", ")

def prime_num(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 2:
        return "I need a higher number than 0"
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return "the number is a prime num"
        return "the number is not a prime num"
        
print(prime_num(72))

# Ejercicio 48: Crea una lista de 10 números y encuentra su producto.
# Conceptos: Listas, funciones.
def numbers_product():
    import random
    list_nums = [random.randint(1, 100) for n in range(10)]
    product = 1
    for i in list_nums:
        product *= i
    print(f"The product of the numbers is: {product}")
numbers_product()

# Ejercicio 49: Escribe un programa que imprima un triángulo de asteriscos.
# Conceptos: Bucles, impresión.
def asterisk_triangle(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n < 4:
        return "I only accept numbers bigger than 4"
    for i in range(1, (n + 1)):
        for j in range (0, (n - i)):
            print(" ", end="")
        for k in range(0, (2 * i - 1)):
            print("*", end="")
        print()
asterisk_triangle(5)

# Ejercicio 50: Crea una función que reciba un número y devuelva la suma de sus dígitos.
# Conceptos: Funciones, manipulación de strings.
def sum_of_digits(n):
    if not isinstance(n, int):
        raise TypeError("I only accept numbers")
    elif n == 0:
        return "the number 0 is not valid"
    new = str(n)
    count = 0
    for i in new:
        nums = int(i)
        count += nums
    return count
print(sum_of_digits(58 ))
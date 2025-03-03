# Día 6

# Ejercicio 26: Crea una función que reciba una lista y devuelva la lista sin duplicados.
# Conceptos: Listas, funciones.
# def erase_duplicate(list_elements):
#     if not isinstance(list_elements, list):
#         raise TypeError("the element is not a list")
#     new_list = set(list_elements)
#     return list(new_list)
# list_user = []
# while True:
#     print("Menu \n"
#           "1- Add numbers\n"
#           "2- See the list\n"
#           "3- Exit\n"
#           )
#     menu = int(input("Select a numer: "))
#     if menu == 1:
#         print("Add a number")
#         num = int(input("Introduce a number: "))
#         list_user.append(num)
#         print("Thanks for add")
#     elif menu == 2:
#         print(list_user)
#     elif menu == 3:
#         break
#     elif menu > 3:
#         print("The number is no valid")
# print(erase_duplicate(list_user))

# Ejercicio 27: Escribe un programa que imprima los primeros 10 números de la serie de Fibonacci.
# Conceptos: Bucles, recursividad.
def first_10_fibonacci_numbers():
    list_fibo = []
    a = 0
    b = 1
    while len(list_fibo) < 10:
        a, b = b , a + b
        list_fibo.append(b)
    return list_fibo
print(first_10_fibonacci_numbers())

# Ejercicio 28: Crea un programa que cuente cuántas veces aparece una letra en una cadena.
# Conceptos: Manipulación de strings, bucles.
def count_leters(variable):
    if not isinstance(variable, str):
        raise TypeError("You need a string caracter")
    count = {}
    for aux in variable.lower().replace(" ",""):
        if aux not in count:
            count[aux] = 1
        else:
            count[aux] += 1 
    return count
print(count_leters("Hernandez z"))
                             
# Ejercicio 29: Escribe un programa que imprima la suma de los números del 1 al 100.
# Conceptos: Bucles, suma.
def sum_100():
    count = 0
    for aux in range(1, 101):
        count += aux
    return count
print(sum_100())

# Ejercicio 30: Crea una función que reciba un número y devuelva su cuadrado.
# Conceptos: Funciones, matemáticas.
def elevede_number(num):
    if not isinstance(num, (int, float)):
        raise TypeError("we only accepte numbers")
    return num ** 2
print(elevede_number(5))
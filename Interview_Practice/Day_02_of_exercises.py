# Día 2

# Ejercicio 6: Crea una función que convierta grados Celsius a Fahrenheit.
# Conceptos: Funciones, conversión de unidades, f = c * 9/5 + 32
def Celsius_To_Fahrenheit():
    try:
        Degrees = int(input("Indroduce the Celsius Degrees: "))
        formula = Degrees * 9/5 + 32
        return f" The Degrees celsius: {Degrees} in Fahrenheit is: {formula} Degrees"
    except ValueError:
        return "Introduce a valid number"

print(Celsius_To_Fahrenheit())

# Ejercicio 7: Escribe un programa que cuente cuántas vocales hay en una cadena.
# Conceptos: Manipulación de strings, bucles.
def count_vowels():
    try:
        vowels = "aeiouáéíóú"
        count = 0
        string = input("Introduce a phrase: ").lower()
        for aux in string:
            if aux in vowels:
                count += 1
        return f"the amount of vowels in the string: {string} is: {count}."
    except Exception as e:
        return e 
print(count_vowels())

# Ejercicio 8: Crea una lista de números y encuentra el número máximo.
# Conceptos: Listas, funciones integradas.
def max_list(list):
    try:
        if not list:
            return "the list is empty"
        return max(list)
    except TypeError:
        return "there are values that are not numeric"
print(max_list([2, 80, 10, 22, 1]))            

# Ejercicio 9: Escribe un programa que imprima los números del 1 al 10.
# Conceptos: Bucles, impresión.
number = [num for num in range(1, 11)]
print(number)

# Ejercicio 10: Crea un programa que pida al usuario su nombre y lo salude.
# Conceptos: Entrada de datos, impresión.
def welcome():
    try:
        name = input("Introduce your name: ").strip() # elimina msj en blanco
        if not name:
            raise ValueError
        return f"Hello {name.capitalize()}, Welcome to Python coding practices"
    except Exception as e:
        return e 
print(welcome())

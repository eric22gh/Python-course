# Día 15: Manejo de Errores y Excepciones

# El manejo de errores y excepciones en Python permite controlar y gestionar situaciones excepcionales que pueden ocurrir durante la ejecución de un programa. 
# Esto es esencial para mantener la estabilidad del programa y proporcionar retroalimentación útil al usuario.

# Tips del Tema 
# Excepciones: Son eventos que ocurren durante la ejecución de un programa que interrumpen su flujo normal. 
# Python tiene una serie de excepciones predefinidas, como ZeroDivisionError, ValueError, TypeError, entre otras.

# ValueError: Ocurre cuando se pasa un argumento que tiene el tipo correcto pero un valor inapropiado.
# TypeError: Ocurre cuando se opera con tipos de datos incompatibles.
# IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista.
# KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
# FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
# IOError: Intentar abrir un archivo que no existe, leer o escribir en un archivo sin los permisos adecuados, operar en un archivo que ha sido cerrado.

# Bloques try y except: Se utilizan para capturar y manejar excepciones. El bloque try contiene el código que puede generar una excepción, 
# mientras que el bloque except maneja la excepción si se produce.

# Levantar excepciones: Se pueden lanzar excepciones manualmente utilizando la palabra clave raise, lo que permite a los desarrolladores indicar situaciones 
# excepcionales que deben ser tratadas.

########### ejemplo #######

try:
    resultado = 10 / 0  # Intentar dividir por cero
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero.")  # Manejo de la excepción
finally:
    print("Esta línea siempre se ejecuta.")  # Se ejecuta independientemente de si hubo una excepción

try:
    result = 100 / 0
except ZeroDivisionError as w: 
    print("la operacion no se puede hacer")

########### Levantar Excepciones

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")  # Levanta una excepción si b es cero
    return a / b

try:
    dividir(10, 0)  # Intentar dividir por cero
except ValueError as e:
    print(e)  # Salida: El divisor no puede ser cero.

# Manejo de Múltiples Excepciones
# Puedes manejar múltiples excepciones en un solo bloque except:

try:
    # Alguna operación que puede generar múltiples excepciones
    resultado = int("texto")  # Intentar convertir texto a entero
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Uso del bloque else
# El bloque else puede ser utilizado después de los bloques try y except. Se ejecuta si el bloque try no genera ninguna excepción:

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"Resultado: {resultado}")  # Se ejecuta si no hay excepción

# Uso de Excepciones Personalizadas
# Puedes crear tus propias excepciones personalizadas extendiendo la clase base Exception:

class MiExcepcion(Exception):
    pass

def verificar_numero(num):
    if num < 0:
        raise MiExcepcion("El número no puede ser negativo.")
    else:
        print(num * 2)

try:
    verificar_numero(5)
except MiExcepcion as e:
    print(e)  # Salida: El número no puede ser negativo.


################### Ejercicios

# Ejercicio 1: Escribe un programa que intente abrir un archivo inexistente y maneje la excepción FileNotFoundError.
try:
    with open("file.txt", "r") as archivo:
        leer = archivo.read()
        print(leer)
except FileNotFoundError:
    print("El archivo no se puede abrir")

# Ejercicio 2: Define una función que intente convertir una cadena a entero y maneje la excepción ValueError.
def covertir(numero1):
    try:
        numero = (int(numero1))
        print(f"este dato {numero1} de tipo : {type(numero1).__name__} fue convertido a un numero: {numero} pero tipo: {type(numero).__name__}")

    except ValueError:
        print(f"este dato {numero1} de tipo cadena no puede convertirse en un entero")

covertir(numero1 = (str(input("ingrese el numero: "))))

# Ejercicio 3: Define una función que tome dos números y devuelva su división, manejando la excepción ZeroDivisionError.
def division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print(F"este numero no puede dividirse entre 0")

total = division(10, 0)
print(f"el resultado de la division es: {total}")

# Ejercicio 4: Escribe un programa que intente acceder a un índice fuera del rango de una lista y maneje la excepción IndexError.
try:
    lista = ["pera", "manzanas", "banana", "sandia"]
    indice = int(input("ingrese el indice: "))
    print(lista[indice])

except IndexError:
    print("este indice no esta en la lista")
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")

# Ejercicio 5: Define una función que intente acceder a una clave inexistente en un diccionario y maneje la excepción KeyError.
def obtener(key):
    try:
        diccionario = {
            "NOMBRE" : "ERIC",
            "age" : 30,
            "surname" : "edwards"
        }
        print(diccionario[key])
    except KeyError:
        print(f"esta clave {key} no esta en este diccionario")
obtener(key = str(input("ingrese la key:")))

# Ejercicio 6: Escribe un programa que intente abrir y leer un archivo, y maneje las excepciones FileNotFoundError y IOError.
try:
    with open("text.txt", "r") as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print("El archivo no se encuentra.")
except IOError:
    print("No es posible abrir este archivo debido a un error de E/S.")

# Ejercicio 7: Define una función que tome un número como argumento y levante una excepción ValueError si el número es negativo.
def number(a):
    if a < 0:
        raise ValueError(f"{a} es un numero negativo")
    else:
        print(f"{a} es un numero positivo")
    try:
        number(a = int(input("ingrese el numero positivo o negativo: ")))
    except ValueError as e:
        print(e)

# Ejercicio 8: Escribe un programa que use un bloque try para intentar convertir una cadena a entero y maneje cualquier excepción que pueda ocurrir.
try:
    a = str(input("ingrese el numero en la cadena: "))
    p = int(a)
    print(f"la cadena: {a} de tipo: {type(a)} se a convertido a un {p} de tipo {type(p)}")
except (ValueError, TypeError):
    print(f"{a} no es un numero escrito en cadena, vuelva a ingresar el numero en una cadena")

# Ejercicio 9 (Teoría): ¿Qué es una excepción y cómo difiere de un error de sintaxis?
# una excepcion se usa para manejar el error en una operacion en python, ya sea abrir un archivo que no existe o una division a 0,
# a diferencia de un error de sintaxis que ocurre cuando falta algun dato como numero, alguna coma, parentesis o variables no declarada en el codigo.

# Ejercicio 10 (Práctica): Escribe un programa que defina una función calcular_promedio que tome una lista de números y devuelva su promedio. 
# La función debe manejar la excepción ZeroDivisionError si la lista está vacía y levantar una excepción TypeError si algún elemento de la lista no es un número.
def calcular_promedio(lista):
    for types in lista:
        if isinstance (types, (str, bool, float)): 
            raise TypeError("Hay un dato incorrecto") 
    else:
        try:
            sumas = sum(lista) 
            promedio = sumas / len(lista) 
            print(promedio)
        except ZeroDivisionError:
            print("esta lista esta vacia")

calcular_promedio(lista = [100, 55, 23, 5, 1000])
calcular_promedio(lista = [100, 55, 23, 5, "hola"])




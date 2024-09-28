# Día 15: Manejo de Errores y Excepciones

# El manejo de errores y excepciones en Python permite controlar y gestionar situaciones excepcionales que pueden ocurrir durante la ejecución de un programa. 
# Esto es esencial para mantener la estabilidad del programa y proporcionar retroalimentación útil al usuario.

# Tips del Tema 
# Excepciones: Son eventos que ocurren durante la ejecución de un programa que interrumpen su flujo normal. 
# Python tiene una serie de excepciones predefinidas, como ZeroDivisionError, ValueError, TypeError, entre otras.

# ValueError: Ocurre cuando se pasa un argumento que tiene el tipo correcto pero un valor inapropiado.
# ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.
# NameError: Ocurre cuando se intenta acceder a una variable que no existe.
# TypeError: Ocurre cuando se opera con tipos de datos incompatibles.
# IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista.
# KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
# FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
# ImportError: Ocurre cuando se intenta importar un módulo que no se encuentra instalado.
# AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
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
        raise ValueError("El divisor no puede ser cero.")  
    return a / b

try:
    dividir(10, 0) 
except ValueError as e:
    print(e)  # El divisor no puede ser cero.

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

# Ejercicio 11: Escribe un programa que intente abrir un archivo inexistente y maneje la excepción FileNotFoundError.
try:
    with open("open.txt", "r") as read:
        dato = read.read()
        print(dato)
except (FileNotFoundError, IOError, PermissionError):
    print("Este archivo no existe o no tienes permisos para abrir el archivo")
else:
    print("Archivo leído correctamente.")


# Ejercicio 12: Define una función que intente convertir una cadena a entero y maneje la excepción ValueError.
def string_int(dato3):
    try:
        if isinstance(dato3, (bool)):
            raise ValueError("No se puede convertir un valor booleano a entero.")

        dato1 = int(dato3)
        return f"{dato1} este dato a sido cambiado a: {type(dato1)}" 
        
    except (ValueError, TypeError):
        return "no se pudo cambiar el tipo"

dato3 = string_int(1.5)
print(dato3)

# Ejercicio 13: Define una función que tome dos números y devuelva su división, manejando la excepción ZeroDivisionError.
def division(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "No se puede dividir entre 0"
    
nums = division(5, 0)
print(nums)

# Ejercicio 14: Escribe un programa que intente acceder a un índice fuera del rango de una lista y maneje la excepción IndexError.
lista = ["alex", "pop", "brasil", "carlos"]
try:
    n = 8
    print(lista[n])
    print("indice de la lista")
except IndexError:
    print(F"El indice: {n} no existe en la lista")

# Ejercicio 15: Define una función que intente acceder a una clave inexistente en un diccionario y maneje la excepción KeyError.
def key_dic(key):
    dicc = {
        "name" : "eric hernandez",
        "age" : 25,
        "Pais" : "brasil",
        "lenguaje" : "python"
    }
    try:
        return dicc[key]

    except KeyError:
        return"La clave del diccionario no existe"
    
llave = key_dic("n")
print(llave)

# Ejercicio 16: Escribe un programa que intente abrir y leer un archivo, y maneje las excepciones FileNotFoundError y IOError.
try:
    with open("eric.txt", "r") as file:
        archivo = file.read()
        print("archivo leido")

except FileNotFoundError:
    print("El archivo no fue encontrado.")
except IOError:
    print("Hubo un error al leer el archivo.")
# Separar las excepciones permite proporcionar un mensaje más específico y útil para cada tipo de error, 
# ayudando a identificar la causa del problema de manera más clara.

# Ejercicio 17: Define una función que tome un número como argumento y levante una excepción ValueError si el número es negativo.
def negative(a):
    if a < 0:
        raise ValueError(f"este numero: {a} no puede ser negativo")
    else:
        return f"{a} es un numero positivo"
    
a = negative(1)
print(a)

# Ejercicio 18: Escribe un programa que use un bloque try para intentar convertir una cadena a entero y maneje cualquier excepción que pueda ocurrir.
cadena = "22"
if isinstance(cadena, bool):
    raise ValueError("Valor incorrecto: no se puede convertir un booleano a entero")
else:
    try:
        numero = int(cadena)
        print(f"Esta variable: {cadena} se ha convertido en un int: {type(numero)}")
    except ValueError:
        print("No se puede convertir la cadena a un número entero")

# Ejercicio 19: Define una función que tome una lista de números y devuelva su promedio, manejando ZeroDivisionError si la lista está vacía.
def lista_promedio(list):
    try:
        suma = sum(list)
        promedio = suma / len(list)
        return F"El promedio de la lista es: {promedio}"

    except ZeroDivisionError:
        return "esta lista esta vacia"
dato = lista_promedio([12, 56, 5, 62, 30])
print(dato)

# Ejercicio 20: Escribe un programa que intente dividir un número por una cadena y maneje las excepciones TypeError y ValueError.
number = 8
string = "5"
try:
    if not isinstance(string, (int, float)):
        raise TypeError("No se puede dividir un número por una cadena")

    dividir = number / string
    print(f"El resultado de la división es: {dividir}")

except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Ejercicio 21: Escribe un programa que lea un número desde el teclado e intente convertirlo a float. 
# Maneja las excepciones ValueError si el usuario introduce un valor que no puede convertirse.
nu = "NBn"
try:
    numero = float(nu)
    print(f"El numero {numero} ahora es un: {type(numero)}")
except ValueError:
    print(f"El tipo: {nu} es incorrecto")

# Ejercicio 22: Crea una función que tome una lista de números y devuelva la suma de los elementos. 
# Levanta una excepción TypeError si algún elemento no es un número.
def sum_list(numeros):
    for num in numeros:
        if not isinstance(num, (int, float)): # si no es un int o bool 
            raise TypeError(f"Hay un elemento equivocado: {num}")
    return f"La suma de todos los números es: {sum(numeros)}"

datos = sum_list([5, 48, 56, 2, 10, "hbhj"])
print(datos)

# Ejercicio 23: Escribe un programa que intente acceder a un atributo inexistente de un objeto y maneje la excepción AttributeError.
if hasattr(dato, 'aumento'): # Puedes comprobar si un atributo existe usando hasattr() antes de intentar acceder a él.
    print(dato.aumento(0.050)) 
else:
    print("El atributo no existe")

# Ejercicio 24: Define una función que intente importar un módulo y maneje la excepción ImportError si el módulo no está disponible.
import importlib #importlib.import_module() se usa para verificar si un modulo existe
def import_module(modulo):
    try:
        importlib.import_module(modulo)
        return "Módulo importado"
    except ImportError:
        return f"Este módulo no existe"

dato = import_module("mat")
print(dato)

# Ejercicio 25: Escribe un programa que intente abrir un archivo de escritura sin permisos y maneje la excepción PermissionError.
try:
    with open("tda.txt","r") as file:
        read = file.read()
        print(read)

except PermissionError:
    print("No tienes permisos para abrir este archivo")

# Ejercicio 26: Crea una función que intente convertir una lista de cadenas a enteros. 
# Si alguna conversión falla, maneja las excepciones y devuelve una lista con solo los valores convertidos correctamente.
def lista_strings(numeros_):
    if isinstance(numeros_, (bool)):
        raise TypeError("Hay un error de tipo en la lista")
    else:
        new_list = []
        for x in numeros_:
            try:
                new_list.append(int(x))
            except ValueError:
                continue  # se salta el valor que no se puede convertir
        return new_list

data = lista_strings(["2", "56", "3", "True", "abc"])
print(data)

# Ejercicio 27: Define una función que tome una lista de diccionarios y maneje la excepción KeyError si una clave especificada no está en todos los diccionarios.
productos = { 
    "pala": {"nombre": "pala", "precio": 20000},
    "tornillo": {"nombre": "tornillo", "precio": 200},
    "martillo": {"nombre": "martillo", "precio": 2000},
    "cinta": {"nombre": "cinta", "precio": 2500}
}
def key_dics(k):
    try:
        key = productos[k]
        return key
    
    except KeyError as a:
        return f"la clave: {a} no existe" 
    
dato = key_dics("pal")
print(dato)

# Ejercicio 28: Crea una función que intente dividir el valor total de un diccionario por el número de claves. 
# Maneja la excepción ZeroDivisionError si el diccionario está vacío.
def valor_diccio(mi_diccionario):
    total = sum(mi_diccionario.values())
    num_claves = len(mi_diccionario.keys()) # tiene que ser len, porque sum no suma strings
    try:
        resultado = total / num_claves
        return f"el resultado de la division es: {resultado:.2f}"
    except ZeroDivisionError as o:
        return "no se puede dividir un numero entre zero"
    
dato_dic = valor_diccio({
    "manzanas": 10,
    "peras": 5,
    "plátanos": 8
})
print(dato_dic)

# Ejercicio 29: Escribe un programa que intente ejecutar una operación matemática compleja y maneje cualquier tipo de excepción que pueda ocurrir, 
# mostrando un mensaje de error general.
numero1 = 4
numero2 = 8
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
simbolo = str(input("Ingrese su operador (suma/resta/multi/divi): "))

try:
    if simbolo.lower() == "suma":
        print(f"Este es el resultado de la suma: {suma}")
    elif simbolo.lower() == "resta":
        print(f"Este es el resultado de la resta: {resta}")
    elif simbolo.lower() == "multi":
        print(f"Este es el resultado de la multiplicación: {multi}")
    elif simbolo.lower() == "divi":
        print(f"Este es el resultado de la división: {divi}")
    else:
        print("Operador no válido. Intente con suma, resta, multi o divi.")
except Exception as e: # exception para depurar algun tipo de error
    print(f"Ocurrió un error: {e}")

# Ejercicio 30: Define una clase personalizada de excepción llamada `OperacionInvalidaException` y úsala en una función que lance esta excepción 
# si se intenta realizar una operación matemática no permitida (por ejemplo, raíz cuadrada de un número negativo).
class OperacionInvalidaException:
    def __init__(self):
        pass
    
    def nuevo_metodo(self):
        return "OperacionInvalidaException"
data = OperacionInvalidaException()
exeption_new = data.nuevo_metodo()
import math
def func_new(num1):
    if num1 < 0:
        return exeption_new
    else:
        return math.sqrt(num1)
datas = func_new(-5)
print(datas)

########## o ##############

class OperacionInvalidaException(Exception):
    def __init__(self, mensaje="Operación matemática no permitida."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def func_new(num1):
    if num1 < 0:
        raise OperacionInvalidaException("No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        return math.sqrt(num1)

try:
    datas = func_new(-5)
    print(datas)
except OperacionInvalidaException as e:
    print(e)

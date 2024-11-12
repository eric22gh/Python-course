# Día 28: Estructura de datos(Listas y operaciones básicas)
# Las listas en Python son colecciones ordenadas y mutables. Permiten realizar operaciones como agregar, eliminar y acceder a elementos mediante índices.
# También puedes usar métodos como .append(), .remove(), .sort(), .reverse(), .count(), y más.

# Gestión de Inventarios:
inventario = ['manzanas', 'bananas', 'naranjas']

# Agregar un nuevo producto
inventario.append('peras')
print("Inventario después de agregar peras:", inventario)

# Eliminar un producto
inventario.remove('bananas')
print("Inventario después de eliminar bananas:", inventario)

# Ordenar el inventario
inventario.sort()
print("Inventario ordenado:", inventario)

# Contar un elemento en la lista
cantidad_naranjas = inventario.count('naranjas')
print(f'Cantidad de naranjas: {cantidad_naranjas}')

# Invertir el inventario
inventario.reverse()
print("Inventario invertido:", inventario)

# Copiar el inventario
inventario_copia = inventario.copy()
print("Inventario copiado:", inventario_copia)

# Buscar un producto
producto_buscar = 'manzanas'
print(producto_buscar in inventario)

# Longitud del inventario
longitud_inventario = len(inventario)
print("Longitud del inventario:", longitud_inventario)

# Agregar elementos duplicados
inventario.extend(['peras', 'peras', 'peras'])

# Eliminar duplicados
inventario_sin_duplicados = list(set(inventario))
print("Inventario sin duplicados:", inventario_sin_duplicados)

# Agregar un elemento en una posición especifica
inventario.insert(1, 'maracuya')
print("Inventario luego de agregar maracuya:", inventario)

# Buscar el índice de un elemento
inventario.index('maracuya')

# Eliminar un elemento en una posición especifica
del inventario[2]

# Limpiar el inventario
# inventario.clear()
# print("Inventario limpio:", inventario)

# Eliminar el ultimo elemento
print(inventario.pop())

# Análisis de Datos en listas:
temperaturas = [30, 32, 31, 29, 35, 33, 34]

promedio = sum(temperaturas) / len(temperaturas)
print(f'Temperatura promedio: {promedio}')

max_temp = max(temperaturas)
min_temp = min(temperaturas)
print(f'Temperatura máxima: {max_temp}, Temperatura mínima: {min_temp}')

# Tips y Buenas Prácticas:
# Utiliza listas para almacenar colecciones de datos que necesiten ser ordenadas o indexadas.
# Prefiere listas en lugar de arrays si no necesitas operaciones matemáticas avanzadas.
# Ten cuidado al modificar listas mientras las recorres; considera crear una copia si es necesario.

# Ejercicios:
# 1- Crea una lista de números del 1 al 10 y muéstrala.
numeros = [n for n in range(1, 11)]
print(numeros)

# 2- Añade un elemento a la lista y elimínalo.
numeros.append(22)
numeros.pop()

# 3- Ordena una lista de nombres y muéstrala.
nombre = ["sandra", "eric", "helen", "maria", "carlos", "arelis"]
nombre.sort()
print(nombre)

# 4- Escribe un programa que imprima los elementos de una lista en orden inverso.
inverso = [i for i in nombre]
inverso.reverse()
print(inverso)

# nombre.reverse()
# for inverso in nombre:
#     print(inverso)

# 5- Crea una lista de cuadrados de los números del 1 al 10.
cuadrados = [n**2 for n in range(1, 11)]
print(cuadrados)

# 6- Escribe un programa que encuentre el número máximo y mínimo en una lista.
numeros = [22, 89, 56, 3, 56, 1005, -2, 23, -54]
print(f"El numero maximo de la lista es: {max(numeros)}")
print(f"El numero minimo de la lista es: {min(numeros)}")

# 7- Crea una lista de palabras y cuenta cuántas letras tiene cada palabra.
nombre = ["sandra", "eric", "helen", "maria", "carlos", "arelis"]
for letra in nombre:
    conteo = len(letra)
    print(f"La palabra: {letra} tiene: {conteo} letras")

# 8- Escribe un programa que mezcle dos listas.
mezcla = cuadrados + numeros
print(mezcla)

# 9- Crea una lista de estudiantes y verifica si un nombre está presente.
estudiantes = ["alex", "maria", "helen", "sofia", "carlos", "antony"]
print("luis" in estudiantes)

# 10- Escribe un programa que elimine duplicados de una lista.
duplicados = ["tomates", "papaya", "manzanas", "tomates", "kiwi", "fresas", "papaya"]
nueva = list(set(duplicados))
print(nueva)

# 11- Crea una lista de números y calcula su suma.
calculo = sum([n for n in range(1001)])
print(f"la suma total de la lista es: {calculo}")

# 12- Escribe un programa que imprima los números impares de una lista.
impares = [i for i in range(1, 60) if i % 2 != 0]
print(impares)

# 13- Crea una lista de temperaturas y convierte cada temperatura de Celsius a Fahrenheit.
# celsius a fahrenheit = (celsius * 9/5) + 32
tempeture = [22, 45, 32, 5, 10, 89]
for Celsius in tempeture:
    formula = (Celsius * 9/5) + 32
    print(f"Esta temperatura pasa de: {Celsius} grados celsius a: {formula} grados farenheit")

# 14- Escribe un programa que imprima los elementos de una lista que son mayores que un número dado.
numero_dado = 25
num = [n for n in impares if n > numero_dado]
print(num)

# 15- Crea un programa que imprima los primeros 10 números de la serie Fibonacci.
def fibonacci(n):
    a = 0
    b = 1
    lista = []
    for _ in range(10):
        lista.append(a)
        a, b = b, b + a
    return lista
# anagrama: 2 palabras son anagramas cuando tienen diferente significado, sin embargo tienen las mismas letras
def anagramas(frase1, frase2):
    frase1 = frase1.replace(" ","").lower()
    frase2 = frase2.replace(" ","").lower()
    frase1 = list(frase1)
    frase2 = list(frase2)
    frase1.sort()
    frase2.sort()
    if frase1 == frase2:
        print("Las 2 frases si son anagramas")
    else:
        print("Las 2 frases no son anagramas")
frases = anagramas("iman", "mani")
# palindromo: Una frase o palabra es palindromo cuando al derecho y al revez tienen el mismo significado.
def palindromo(frase):
    frase_1 = frase.replace(" ", "").lower()
    alrevez = frase_1[::-1]
    if frase_1 == alrevez:
        print("La frase si es un palindromo")
    else:
        print("La frase no es un palindromo")
dato = palindromo("amo la paloma")

# Mini Proyectos:
# Desarrolla un programa que gestione una lista de tareas pendientes.
class Tareas:
    def __init__(self, lista):
        self.lista = []
        pass

    def agregar_tareas(self, tarea):
        try:
            self.lista.append(tarea.capitalize())
            return "Tarea agregada"
        except TypeError:
            return "Solo se agrega texto"
    
    def eliminar_tarea(self, tarea):
       try:
           self.lista.remove(tarea.capitalize())
           return "Tarea eliminada"
       except ValueError:
           return "Tarea no encontrada"
       
    def mostrar_tareas(self):
        if not self.lista:
            return "No hay tareas pendientes"
        return "\n".join([f"{i}- {tareas}"for i, tareas in enumerate(self.lista, start=1)]) # se acomulan las tareas 
        
admin = Tareas([])
while True:
    print("\n Bienvenido al menu de tareas \n"
          "1- agregar tareas\n"
          "2- eliminar tareas\n"
          "3- mostrar tareas \n"
          "4- salir\n"
    )
    try:
        number = int(input("Ingrese un numero: "))
    except ValueError:
        print("Ingrese un numero valido")
        continue

    if number == 1:
        Task = input("agrega la tarea que deseas agregar: ")
        admin.agregar_tareas(Task)
        print("Tarea agregada")
        
    elif number == 2:
        Task = input("agrega la tarea que deseas eliminar: ")
        admin.eliminar_tarea(Task)
        print("Tarea eliminada")
        
    elif number == 3:
        print(admin.mostrar_tareas())

    elif number == 4:
        print("Gracias por usar el programa")
        break
        
    else:
        print("Ingrese un numero valido")

# Crea un programa que simule un juego de adivinanza de números utilizando una lista.
import random
def juego_adivinanza():
    nume = [random.randint(1, 20) for _ in range(5)]
    print("He generado 5 números aleatorios entre 1 y 20 con 3 intentos, tienes que adivinar uno de ellos.")
    
    intentos = 3  
    while intentos > 0:
        try:
            adivinanza = int(input("Adivina el número ganador (entre 1 y 20): "))
            
            if adivinanza < 1 or adivinanza > 20:
                print("Por favor, elige un número entre 1 y 20.")
                continue
            
            if adivinanza in nume:
                print(f"¡Correcto! El número ganador es: {adivinanza}")
                break
            else:
                intentos -= 1
                print(f"Incorrecto. Te quedan {intentos} intentos.")
                
            if intentos == 0:
                print(f"Lo siento, has agotado tus intentos. Los números ganadores eran: {nume}")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")

juego_adivinanza()


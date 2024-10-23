# Día 21: Iteradores y Generadores

# Iteradores y generadores en Python, herramientas poderosas para manejar secuencias de datos de manera eficiente.

# 1. Iteradores:
#    - Un iterador es un objeto que implementa los métodos `__iter__()` y `__next__()`.
#    - Puedes obtener un iterador de cualquier objeto iterable (como listas, tuplas, diccionarios, etc.) usando la función `iter()`.
#    - El método `next()` se usa para obtener el siguiente elemento del iterador, y lanza una excepción `StopIteration` cuando no hay más elementos.
#    - Son objetos que permiten recorrer todos los elementos de una colección, como listas o tuplas.
#    - Se obtienen llamando a la función `iter()` sobre una colección.
#    - La función `next()` se usa para obtener el siguiente elemento del iterador.

# 2. Generadores:
#    - Los generadores son funciones que devuelven un objeto iterador con una secuencia de valores.
#    - En lugar de `return`, usan la palabra clave `yield` para producir un valor y pausar la ejecución de la función, manteniendo su estado para la siguiente llamada.
#    - Los generadores son más eficientes en términos de memoria que las listas, especialmente para grandes secuencias de datos, ya que producen los elementos sobre la marcha.
#    - Son una forma especial de iterador que se define con una función y la palabra clave `yield`, permitiendo producir una secuencia de valores sobre la marcha.
#    - Son útiles para trabajar con grandes secuencias de datos sin necesidad de almacenarlos en memoria.

# 3. Generadores de Expresión:
#    - Son una forma concisa de crear generadores usando una sintaxis similar a las listas de comprensión, pero con paréntesis en lugar de corchetes.
#    - Al igual que las funciones generadoras, producen elementos uno a uno según se necesiten.

# Crear y Usar Iteradores
numeros = [1, 2, 3, 4, 5]

# Obtener un iterador de la lista
iterador = iter(numeros)
# print(iterador) no da el dato

# Usar next() para obtener elementos del iterador
print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3
print(next(iterador))  # Salida: 4
print(next(iterador))  # Salida: 5
# print(next(iterador)) # Si tratamos de obtener otro elemento, se lanzará una excepción StopIteration
# por que la lista llega hasta 5 por eso el error

# Crear y Usar Generadores
def contador(max):
    n = 1
    while n <= max:
        yield n
        n += 1
contador(10)

# Usar el generador
for numero in contador(5):
    print(numero)

# Generadores de Expresión
gen_exp = (x*x for x in range(5)) # gen_exp tiene varios rerultados por el bucle for, entoces hay que iterarlo 

# Usar el generador de expresión
for cuadrado in gen_exp:
    print(cuadrado)
    # Salida:
    # 0
    # 1
    # 4
    # 9
    # 16


# Ejercicios Avanzados

# Generador de Números Primos:
def generador_primos():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

primos = generador_primos()
for _ in range(10):
    print(next(primos))
    # Salida: los primeros 10 números primos

# Generador de Fibonacci:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
    # Salida: los primeros 10 números de la secuencia de Fibonacci

# Generador de Líneas de un Archivo:
def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()

# for linea in leer_lineas('archivo.txt'): lee cada linea del archivo
#     print(linea)

######### ejercicios
# Ejercicio 1: Crea un iterador para una lista de cadenas de texto y usa next() para mostrar los dos primeros elementos.
lista = ["edwards", "alajuela" ,"hernandez", "costarica", "arhenas"]
texto = iter(lista)
print(next(texto))
print(next(texto))
    
# Ejercicio 2: Escribe una función que tome una lista y devuelva un iterador para recorrer la lista.
def recorrer(lista):
    tex = iter(lista)
    for i in tex:
        print(i) 
recorrer(lista = ["alajuela", "costarica", "arhenas"])

# Ejercicio 3: Define un generador que produzca los primeros n números pares.
def generador_pares(n):
    for i in range(n):
        yield i * 2
n = 10 # numero de veces o vueltas
for par in generador_pares(n):
    print(par)

# Ejercicio 4: Define un generador que produzca los primeros n números impares.
def generador_impares(n):
    for i in range(n):
        yield i * 2 + 1

n = 10 
for impar in generador_impares(n):
    print(impar)

# Ejercicio 5: Escribe una función que tome un número n y devuelva un generador que produzca los números de Fibonacci hasta n.
n = 10
a = 0
b = 1
suma = 0 # para iniciar
print(a,b, end=" ")
while True:
    suma = a + b 
    a = b # se calcula el valor
    b = suma # se calcula el valor
    if suma < n: # hasta el numero n
        print(suma, end=" ")
    else:
        break
# formula de fibonaci f0 = f1 + f2

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Uso del generador
n = 15
for num in fibonacci(n):
    print(num, end=" ")


# Ejercicio 6: Define un generador de expresión que produzca los cubos de los números del 1 al 10.
al_cubo = (x ** 3 for x in range(0, 11))
for cubo in al_cubo:
    print(cubo)

# Ejercicio 7: Escribe una función que use un generador para producir los números primos menores a n.
n = 15
def gen_primos(n):
    for i in range(2, n):
        es_primo = True  # Suponemos que i es primo
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:  
                es_primo = False  
                break
        if es_primo:
            yield i  # Genera el número primo

for primo in gen_primos(15):
    print(f"numero: {primo} es un numero primo")

# Ejercicio 8: Escribe una función que use un generador para producir los cuadrados de los números de una lista.
def cuadrado_num(lista):
    for i in lista:
        yield i ** 2
for cuadrado in cuadrado_num([5, 8, 9, 4, 3]):
    print(cuadrado)

# Ejercicio 9 (Teoría): ¿Qué es un iterador y un generador en Python y cuáles son las diferencias entre ellos?
# los itineradores y generadores son excelentes herramientas para manejar una secuencia de datos en python, con el iterador puedes 
# datos o objetos de cualquier iterable (como listas, tuplas, diccionarios, etc.) en cambio los generadores tiene funciones como 
# yield permite que la función continúe su ejecución en una llamada futura.

# Ejercicio 10 (Práctica): Escribe un programa que use un generador para producir los primeros n números 
# de la secuencia de Fibonacci y los almacene en una lista.
lista_vacia = []
n = 20
a = 0
b = 1
suma = 0
while True:
    suma = a + b
    a = b
    b = suma
    if suma < n:
        lista_vacia.append(suma)
    else:
        print(lista_vacia)
        break
########## o
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

lista_v = list(fibonacci_gen(15)) # hacer fibo 15 veces
print(lista_v)

# Ejercicio 11: Generador de permutaciones
# Las permutaciones se refieren a las diferentes maneras en que se pueden ordenar o reordenar un conjunto de elementos
import itertools
def permutaciones(dato):
    #permutacioness = set(itertools.permutations(dato)) permutations garantiza que no haya repeticiones, por lo que no es necesario convertirlo a set()
    permutacioness = set(itertools.permutations(dato))
    conteo = len(list(permutacioness))
    return F"El numero de permutaciones es: {conteo} y son las siguientes: {permutacioness}"

conjunto = permutaciones(("a", "b", "c"))
print(conjunto)

# Ejercicio 12: Generador de combinaciones
# Las combinaciones son las distintas formas en que puedes seleccionar un conjunto de elementos de un grupo más grande, sin importar el orden.
def combinations(set_1, r):
    combinaciones = set(itertools.combinations(set_1, r)) 
    contar = len(list(combinaciones)) #  itertools.combinations garantiza que no haya repeticiones
    return F"El numero de combinaciones en un grupo de {r} es: {contar} y son las siguiente: {combinaciones}"

dato = combinations(("er", "gh", "op", "yu", "ol"),(2))
print(dato)

# Ejercicio 13: Generador de subconjuntos
conjunto_1 = {12, 56, 89, 78, 56}
lista_subconjuntos = []
for x in range(len(conjunto_1) + 1): # va a ir aumentando el numero de combinacion cuando termine la primera vuelta de el bucle
    for com in itertools.combinations(conjunto_1, x): # define el grupo de combinaciones
        lista_subconjuntos.append(set(com)) # añade el conjunto de combinaciones a una lista
print(lista_subconjuntos)

# Ejercicio 14: Generador de productos cartesianos
# productos cartesianos: tomas cada elemento del primer conjunto y lo emparejas con cada elemento del segundo conjunto.
def prod_cartesianos(con_1, con_2):
    return list(itertools.product(con_1, con_2))

datos = prod_cartesianos((1, 2),(10, 56, 23, 5))
print(datos)

# Ejercicio 15: Generador de números aleatorios únicos
import random
def generador_numeros(start, end):
    numeros_aleatorios = [random.randint(int(start), int(end)) for x in range(8)]
    return f"los numeros aleatorios entre {start} y {end} son: {numeros_aleatorios}"
dato = generador_numeros(5,500)
print(dato)

# Ejercicio 16: Generador de números primos (Criba de Eratóstenes)
# La Criba de Eratóstenes es un método antiguo y eficiente para encontrar todos los números primos hasta un límite determinado.
def gen_numeros_primos(limite):
    numeros = [n for n in range(1, int(limite)) if n % 2 == 0]
    return numeros

datos = gen_numeros_primos(30)
print(datos)

# Ejercicio 17: Generador de árboles binarios (simplificado)
# Un árbol binario es una estructura de datos en la informática que se utiliza para organizar información jerárquicamente.
# cada nodo tiene como máximo dos hijos, llamados hijo izquierdo e hijo derecho. El nodo superior se conoce como raíz.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo_actual, dato):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(dato)
            else:
                self._agregar_recursivo(nodo_actual.izquierda, dato)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(dato)
            else:
                self._agregar_recursivo(nodo_actual.derecha, dato)

    def imprimir_en_orden(self):
        self._imprimir_en_orden_recursivo(self.raiz)

    def _imprimir_en_orden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._imprimir_en_orden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.dato)
            self._imprimir_en_orden_recursivo(nodo_actual.derecha)

def generar_arbol(n, rango):
    arbol = ArbolBinario()
    for _ in range(n):
        dato = random.randint(*rango)
        arbol.agregar(dato)
    return arbol

n = 10  #nodos en el árbol
rango = (0, 100)  # valores para los nodos
arbol_generado = generar_arbol(n, rango)
arbol_generado.imprimir_en_orden()

# Ejercicio 18: Generador de expresiones regulares (simplificado)
import re
def generar_expresion_regular(patron, texto):
    if patron.lower() == "correo":
        patron_correo = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        correos = re.findall(patron_correo, texto)
        for correo in correos:
            return f"Correo encontrado: {correo}"
        
    elif patron.lower() == "numero":
        patron_numero = r'\d+'
        numeros = re.findall(patron_numero, texto)
        for numero in numeros:
            return f"Número encontrado: {numero}"

    elif patron.lower() == "palabra":
        patron_palabra = r'\b\w+\b'
        palabras = re.findall(patron_palabra, texto)
        for palabra in palabras:
            return f"Palabra encontrada: {palabra}"
    
    else:
        return None

texto = "Contacta a alguien@dominio.com o llama al 123456. Más información en http://pagina.com y ferali@gmail.com"
patron_correo = generar_expresion_regular("Correo", texto)
patron_numero = generar_expresion_regular("numero", texto)
patron_palabra = generar_expresion_regular("palabra", texto)
print(patron_correo)
print(patron_numero)
print(patron_palabra)

# Ejercicio 19: Generador de soluciones a un Sudoku (simplificado)
def es_valido(tablero, fila, columna, numero):
    # Ve si un número no está repetido en la fila, columna y o en el 3x3
    for i in range(9):
        if tablero[fila][i] == numero or tablero[i][columna] == numero:
            return False
    sub_fila = (fila // 3) * 3
    sub_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[sub_fila + i][sub_columna + j] == numero:
                return False
    return True

def resolver_sudoku(tablero): #metodo backtraking
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:  # Encuentra la celda vacía
                for numero in range(1, 10):
                    if es_valido(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][columna] = 0
                return False
    return True

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) for num in fila))
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if resolver_sudoku(tablero):
    imprimir_tablero(tablero)
else:
    print("No se pudo resolver el Sudoku.")

# Ejercicio 20: Generador de movimientos en un juego (ejemplo: ajedrez)
class Pieza:
    def __init__(self, color):
        self.color = color

class Rey(Pieza):
    def movimientos_posibles(self, posicion):
        x, y = posicion
        movimientos = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:  # en el tablero
                movimientos.append((nx, ny)) # append solo acepta un argumento
        return movimientos

class Tablero:
    def __init__(self):
        self.tablero = [[None for _ in range(8)] for _ in range(8)]
    
    def colocar_pieza(self, pieza, posicion):
        x, y = posicion
        self.tablero[x][y] = pieza
    
    def movimientos_posibles(self, posicion):
        x, y = posicion
        pieza = self.tablero[x][y]
        if pieza:
            return pieza.movimientos_posibles(posicion)
        return []

tablero = Tablero()
rey_blanco = Rey('blanco')
tablero.colocar_pieza(rey_blanco, (0, 4))
movimientos = tablero.movimientos_posibles((0, 4))
print(movimientos)
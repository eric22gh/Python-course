# Día 72: Análisis de complejidad de algoritmos

# Teoría: El análisis de complejidad se refiere a la evaluación del tiempo y espacio que un algoritmo requiere 
# en función del tamaño de su entrada. 

# Se clasifica en:

# ✅ # Complejidad temporal: Número de operaciones que el algoritmo realiza conforme n(la entrada) crece.
# conocido como Notación Big O o tiempo lineal O(n)
# La notación Big O (O(...)) o lista[i] describe el comportamiento del algoritmo en el peor de los casos.

# Complejidad Temporal
# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Tiempo constante                  | Acceso a un elemento en una lista| Excelente   |
# | O(log n)  | Tiempo logarítmico               | Búsqueda binaria, se reduce a la mitad | Muy buena   |
# | O(n)      | Tiempo lineal                    | Recorrer una lista                | Buena       |
# | O(n log n)| Tiempo casi lineal               | Algoritmos de ordenación como Merge Sort y Quicksort | Aceptable |
# | O(n²)     | Tiempo cuadrático                | Doble bucle anidado              | Pobre       |
# | O(2ⁿ)     | Tiempo exponencial               | Algoritmo recursivo de Fibonacci  | Mala        |


# ✅ Complejidad Espacial: cantidad de memoria que utiliza conforme n(la entrada) crece
# Esto incluye variables y estructuras de datos.

# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Espacio constante                | Variables temporales             | Excelente   |
# | O(n)      | Espacio lineal                   | Almacenar una lista de n elementos| Buena       |
# | O(n²)     | Espacio cuadrático               | Matrices bidimensionales         | Pobre       |
# | O(2ⁿ)     | Espacio exponencial              | Algoritmos recursivos con muchas llamadas | Mala |
#

# ✅ Notación Big O: Se centra en cómo el tiempo de ejecución o el uso de memoria crece a medida que aumenta el tamaño de la entrada. 
# La notación Big O se utiliza para clasificar algoritmos según su rendimiento y eficiencia.

# Notaciones de complejidad
# 1- Big O (O) - Cota Superior: Describe el peor caso o límite superior del tiempo de ejecución.
# 2- Big Θ (Theta) - Cota Ajustada: Describe el caso promedio cuando el límite superior e inferior coinciden.
# 3- Big Ω (Omega) - Cota Inferior: Describe el mejor caso o límite inferior del tiempo de ejecución.


# Tips
# Familiarízate con las notaciones Big O, Big Θ y Big Ω para describir la complejidad.
# Aprende a identificar el caso mejor, promedio y peor.

# Buenas Prácticas
# Siempre analiza la complejidad de tus algoritmos antes de implementarlos.
# Compara diferentes algoritmos para resolver el mismo problema en términos de complejidad.

def ejemplo_complejidad(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]  # O(n) variable temporal y acceso a un elemento de la lista
    return suma  # Complejidad temporal: O(n)

# Ejercicios
# 1- Define la complejidad temporal y espacial de la ordenación por burbuja.
def BubleSort(elements):
    n = len(elements)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements
# complejidad temporal:  O(n²) tiempo cuadratico porque tiene 2 bucles anidados
# complejidad espacial:  O(1) espacio constante porque no se utiliza espacio adicional, solo intercambia elementos en la lista.
print(BubleSort([55, 65, 4, 1, 89, 10, 2]))

# 2- Analiza la complejidad de un algoritmo de búsqueda lineal.
def LinearSearch(elements, obj):
    for i in range(0, len(elements)):
        if obj == elements[i]:
            return obj
    return "Element was not found"
# complejidad temporal: O(n) tiempo lineal porque tiene que recorrer toda la lista
# complejidad espacial: O(1) espacio Constante porque solo se utilizan variables adicionales para los índices.
print(LinearSearch([55, 65, 4, 1, 89, 10, 2], 10))
        
# 3- Investiga la complejidad de un algoritmo de búsqueda binaria.
def BinarySearch(elements, obj):
    left, right = 0, len(elements) - 1
    while left <= right:
        medium = (left + right) // 2
        if elements[medium] == obj:
            return elements[medium]
        elif elements[medium] < obj:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not find the value"
# complejidad temporal O(log n): tiempo logaritmico: se reduce a la mitad la busqueda
# complejidad espacial  O(n): ESpacio lineal: crece con forme n crece

print(BinarySearch([55, 65, 4, 1, 89, 10, 2], 1))
    
# 4- Escribe un breve resumen sobre la notación Big O.
# la notación Big O Es usada para clasificar a los distintos tipos de algoritmos segun su rendimiento y eficiencia en situaciones como:
# en el mejor de los casos Big Ω (Omega) - Cota Inferior, en el caso promedio Big Θ (Theta) - Cota Ajustada y en el peor de los casos Big O (O).
# tambien se evalua su uso de memoria y espacio para crear un programa altamente eficiente.

# 5- Compara la complejidad de diferentes algoritmos de ordenación.
def InsertionSort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements
print(InsertionSort([55, 65, 4, 1, 89, 10, 2]))
# complejidad temporal: O(n²) tiempo cuadratico porque tiene 2 bucles
# complejidad espacial: O(n) espacio lineal porque almacena una lista de n elementos

def SelectionSort(elements):
    for i in range(len(elements)):
        min_idx = i
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min_idx]:
                min_idx = j
        elements[i], elements[min_idx] = elements[min_idx], elements[i]
    return elements
print(SelectionSort([55, 65, 4, 1, 89, 10, 2]))
# complejidad temporal: O(n²) tiempo cuadratico porque tiene 2 bucles anidados
# complejidad espacial: O(n) espacio lineal porque almacena una lista de n elementos

def QuickSort(elements):
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    middle = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)
print(QuickSort([55, 65, 4, 1, 89, 10, 2]))
# complejidad temporal: O(n log n) tiempo casi lineal en el mejor y promedio de los casos.
# complejidad espacial: O(n) espacio lineal porque almacena una lista de n elementos

def MergeSort(elements):
    if len(elements) <= 1:
        return elements
    medium = len(elements) // 2
    left = elements[:medium]
    right = elements[medium:]
    left = MergeSort(left)
    right = MergeSort(right)
    return merge(left, right)
def merge(left, right):
    aux = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1
    aux.extend(left[i:])
    aux.extend(right[j:])
    return aux
print(MergeSort([55, 65, 4, 1, 89, 10, 2]))
# complejidad temporal: O(n log n) tiempo casi lineal en el mejor y promedio de los casos.
# complejidad espacial: O(n) espacio lineal porque almacena una lista de n elementos

def BubbleSort(elements):
    n = len(elements)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements
print(BubbleSort([55, 65, 4, 1, 89, 10, 2]))
# complejidad temporal: O(n²) tiempo cuadratico porque tiene 2 bucles
# complejidad espacial: O(n) espacio lineal porque almacena una lista de n elementos

# 6- Investiga sobre la complejidad de algoritmos recursivos.
# la complejidad en los algoritmos recursivos se determina analizando cómo se descompone el problema en subproblemas 
# y cómo se combinan sus soluciones, En una función recursiva(llamadas repetitivas) se usa una ecuación de recurrencia, que describe el tiempo de ejecución 
# en función del tamaño del problema:

# - Ejemplo: Fibonacci recursiva:
# T(n)=T(n-1)+T(n-2)+O(1)- Es de complejidad exponencial O(2^n), porque se hacen muchas llamadas repetidas.

# - Ejemplo eficiente: Búsqueda binaria:
# T(n)=T(n/2)+O(1)- Su complejidad es logarítmica O(\log n), ya que divide el problema a la mitad en cada paso por lo tanto es menor trabajo el que hace.

# 7- Analiza la complejidad de un algoritmo de Fibonacci recursivo.
def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
# La complejidad temporal de este algoritmo es O(2^n) tiempo exponencial, porque cada llamada a Fibonacci genera dos llamadas adicionales y esas llamadas son repetitivas,
# lo que resulta en un crecimiento exponencial del número de llamadas a medida que n aumenta.
# La complejidad espacial es O(2^n) espacio exponencial debido a la profundidad de la pila de llamadas recursivas, que puede llegar hasta n en el peor de los casos.
print(Fibonacci(5))

# fibonnaci con variables temporales para mejorar la eficiencia
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(Fibonacci(5))
# La complejidad temporal de este algoritmo es O(n) tiempo lineal porque utiliza un bucle que itera(recorre) n veces.
# La complejidad espacial es O(1) espacio constante porque solo utiliza un número fijo de variables temporales independientemente del tamaño de n.

# 8- Escribe un programa que calcule la complejidad de un algoritmo dado.
def calcular_complejidad(algoritmo):
    import re
    cleaned_algoritmo = re.sub(r'[^a-zA-Z]', '', algoritmo)
    if cleaned_algoritmo == "BubbleSort":
        return "Complejidad Temporal: O(n²) tiempo cuadratico: porque tiene 2 bucles anidados, Complejidad Espacial: O(n) espacio lineal: almacena una lista de n elementos"
    elif cleaned_algoritmo == "BinarySearch":
        return "Complejidad Temporal: O(log n) tiempo logaritmico: se reduce a la mitad la busqueda, Complejidad Espacial: O(n) espacio lineal: crecee con forme a la lista"
    elif cleaned_algoritmo == "FibonacciRecursivo":
        return "Complejidad Temporal: O(2^n) tiempo exponencial: muchas llamadas repetitivas, Complejidad Espacial: O(2^n) espacio exponencial: profundidad de la pila de llamadas recursivas"
    elif cleaned_algoritmo == "FibonacciIterativo":
        return "Complejidad Temporal: O(n) tiempo lineal: utiliza un bucle que itera n veces, Complejidad Espacial: O(1) espacio constante: utiliza un número fijo de variables temporales"
    elif cleaned_algoritmo == "QuickSort":
        return "Complejidad Temporal: O(n log n) tiempo casi lineal en el mejor y promedio de los casos, Complejidad Espacial: O(n) espacio lineal porque almacena una lista de n elementos"
    elif cleaned_algoritmo == "MergeSort":
        return "Complejidad Temporal: O(n log n) tiempo casi lineal en el mejor y promedio de los casos, Complejidad Espacial: O(n) espacio lineal porque almacena una lista de n elementos"
    elif cleaned_algoritmo == "InsertionSort":
        return "Complejidad Temporal: O(n²) tiempo cuadratico porque tiene 2 bucles, Complejidad Espacial: O(n) espacio lineal porque almacena una lista de n elementos"
    elif cleaned_algoritmo == "SelectionSort":
        return "Complejidad Temporal: O(n²) tiempo cuadratico porque tiene 2 bucles anidados, Complejidad Espacial: O(n) espacio lineal porque almacena una lista de n elementos"
    elif cleaned_algoritmo == "LinearSearch":
        return "Complejidad Temporal: O(n) tiempo lineal porque tiene que recorrer toda la lista, Complejidad Espacial: O(n) espacio lineal porque crecee conforme a la lista"
    else:
        return "Algoritmo no reconocido"
print(calcular_complejidad("BubbleSort"))


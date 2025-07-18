# Día 61: Introducción a algoritmos de ordenación

# Teoría
# Los algoritmos de ordenación son procedimientos utilizados para reorganizar una colección de elementos 
# en un orden específico, ya sea ascendente o descendente. 
# La ordenación es fundamental en la programación y se utiliza en diversas aplicaciones.

# Tips
# Comprende la importancia de la complejidad temporal y espacial de cada algoritmo de ordenación.
# Familiarízate con los diferentes tipos de algoritmos de ordenación, como los estables y los inestables.

# Buenas Prácticas
# Siempre documenta el propósito y la lógica detrás de cada algoritmo.
# Realiza pruebas con diferentes tipos de datos para evaluar la eficacia de cada algoritmo.

def mostrar_lista(lista):
    print("Lista:", lista)

# Uso del ejemplo
lista = [5, 3, 8, 1, 2]
mostrar_lista(lista)


# Ejercicios
# 1- Investiga y escribe sobre la importancia de la ordenación en la programación.
# 🧠✨ El orden en la programación es crucial, En una danza: si los pasos no están coordinados, todo se descoordina.
# 🔁 1. Orden de ejecución
# - Los programas se ejecutan línea por línea, de arriba hacia abajo (salvo que se indique lo contrario con bucles, condiciones o funciones).
# - Un error de orden puede hacer que una variable se use antes de ser definida, causando errores como NameError en Python.
# 🧩 2. Lógica del algoritmo
# - La estructura lógica depende del flujo correcto: si pones una validación después de usar los datos, podrías procesar información inválida.
# - Ejemplo: primero debes verificar si un archivo existe antes de intentar abrirlo.
# 🧱 3. Modularidad y legibilidad
# - Colocar funciones, clases o comentarios en un orden intuitivo ayuda a entender el código más rápido.
# - Un código bien ordenado es más fácil de mantener, depurar y mejorar.
# 🧠 4. Eficiencia computacional
# - A veces el orden también afecta la eficiencia: por ejemplo, aplicar filtros antes de ordenar una lista puede ahorrar recursos.

# 2- Compara la complejidad temporal de diferentes algoritmos de ordenación.
# 📊 Comparación de algoritmos de ordenación

# | Algoritmo           | Mejor caso     | Promedio         | Peor caso         | Estable | Notas rápidas                                      |
# |---------------------|----------------|------------------|-------------------|---------|----------------------------------------------------|
# | Bubble Sort         | O(n)           | O(n²)            | O(n²)             | Sí      | Simple, pero ineficiente en listas grandes         |
# | Insertion Sort      | O(n)           | O(n²)            | O(n²)             | Sí      | Muy eficiente si la lista ya está casi ordenada    |
# | Selection Sort      | O(n²)          | O(n²)            | O(n²)             | No      | No mejora aunque los datos estén ordenados         |
# | Merge Sort          | O(n log n)     | O(n log n)       | O(n log n)        | Sí      | Rápido y estable, pero usa espacio adicional       |
# | Quick Sort          | O(n log n)     | O(n log n)       | O(n²)             | No      | Muy rápido si el pivote se elige bien              |
# | Heap Sort           | O(n log n)     | O(n log n)       | O(n log n)        | No      | No usa memoria extra, pero no es estable           |
# | Tim Sort (Python)   | O(n)           | O(n log n)       | O(n log n)        | Sí      | Algoritmo híbrido que usa sorted() en Python       |

# 3- Escribe un breve resumen de los algoritmos de ordenación más comunes.
# 🔄 Bubble Sort
# - Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto.
# - Simple, pero muy ineficiente para listas grandes.
# 🧱 Insertion Sort
# - Inserta cada elemento en su posición correcta dentro de una sublista ya ordenada.
# - Rápido para listas pequeñas o casi ordenadas.
# 📦 Selection Sort
# - Encuentra el mínimo (o máximo) y lo coloca en su posición correcta.
# - Siempre recorre la lista completa; no mejora con listas ordenadas.
# 🧬 Merge Sort
# - Divide la lista en mitades, ordena cada mitad recursivamente y luego las une.
# - Muy eficiente y estable, aunque usa memoria adicional.
# ⚡ Quick Sort
# - Elige un pivote y divide la lista en sublistas menores y mayores que el pivote.
# - Muy rápido, pero puede degradarse si el pivote no se elige bien.
# ⛰️ Heap Sort
# - Convierte la lista en un heap (montículo), y extrae elementos en orden.
# - Eficiente sin usar memoria extra, pero no es estable.
# 🧠 Tim Sort
# - Mezcla Merge Sort e Insertion Sort, usado en la función sorted() de Python.
# - Altamente optimizado para datos reales.

# ✅ Estabilidad:
# - Estables: Bubble, Insertion, Merge, Tim
# - No estables: Selection, Quick, Heap

# 4- Investiga sobre la estabilidad de los algoritmos de ordenación y escribe tus conclusiones.
# 🔎 ¿Qué es la estabilidad?
# Un algoritmo de ordenación se considera **estable** si mantiene el orden original 
# de los elementos con claves iguales. Es decir, si dos elementos tienen el mismo valor, 
# su posición relativa no cambia después de ordenar.

# 🧪 Ejemplo práctico:
# Lista original: [("Ana", 90), ("Luis", 90), ("Pedro", 85)]
# Ordenando por nota de mayor a menor (estable):
# Resultado: [("Ana", 90), ("Luis", 90), ("Pedro", 85)]
# En un algoritmo **no estable**, Ana y Luis podrían intercambiarse.

# ✅ Recomendación:
# Usa algoritmos estables como Merge Sort o Tim Sort si necesitas preservar
# la posición de elementos iguales. Si la estabilidad no es crítica y buscas velocidad,
# Quick Sort puede ser más rápido en la práctica.

# 5- Investiga y presenta ejemplos de aplicaciones prácticas de algoritmos de ordenación.
# 🔍 1. Motores de búsqueda (Google, Bing)
# - Ordenan miles de millones de páginas web por relevancia.
# - Algoritmos como Quick Sort y variantes personalizadas ayudan a clasificar resultados rápidamente.

# 🛒 2. Comercio electrónico (Amazon, eBay)
# - Ordenan productos por precio, popularidad, calificación, etc.
# - Tim Sort (usado en Python) es ideal por su eficiencia y estabilidad.

# 🧠 3. Aprendizaje automático (Machine Learning)
# - Se usa para preparar datos, detectar valores atípicos y calcular estadísticas.
# - Ejemplo: ordenar datos para encontrar la mediana o aplicar k-NN (k vecinos más cercanos).

# 🗃️ 4. Bases de datos
# - Ordenan registros para mejorar el rendimiento de consultas.
# - Merge Sort es útil por su estabilidad y rendimiento predecible.

# 📈 5. Análisis financiero y científico
# - Ordenan datos para detectar tendencias, calcular percentiles o limpiar datos.
# - Heap Sort puede ser útil cuando se requiere eficiencia sin memoria adicional.

# 🧬 6. Bioinformática
# - Ordenan secuencias genéticas para comparaciones y alineamientos.
# - Algoritmos eficientes como Quick Sort o Radix Sort se usan en grandes volúmenes de datos.

# 📦 7. Logística y planificación de tareas
# - Ordenan tareas por prioridad, tiempo de entrega o recursos disponibles.
# - Se combinan con estructuras como colas de prioridad (heaps).

# 🧑‍🏫 8. Educación en línea
# - Ordenan entregas de estudiantes, calificaciones y progreso.
# - Selection Sort o Insertion Sort pueden usarse en sistemas simples.

# 🧮 9. Estadísticas y visualización de datos
# - Ordenar datos permite crear histogramas, boxplots y detectar valores extremos.
# - Sorting es paso previo a muchos análisis estadísticos.

# 🧠 CONCLUSIÓN: Elegir el algoritmo correcto depende del contexto: tamaño de los datos, necesidad de estabilidad,
# uso de memoria y velocidad requerida.

# 6- Crea un método que determine si una lista está ordenada.
def VerifyOrder(List1):
    if not isinstance(List1, list):
        raise TypeError("I only accept lists")
    elif not all(isinstance(i, int) for i in List1):
        raise TypeError("I only accept Integer numbers in the list")
    aux = List1[0]
    for i in List1:
        if aux > i:
            return "the list is not in order"
        aux = i
    return "The list is in order"
print(VerifyOrder([1, 11, 20, 5, 10]))

# 7- Desarrolla un programa que clasifique una lista de cadenas por longitud.
def OrderStrings(list2):
    for string in list2:
        if len(string) == 0:
            print("there is no lenght")
        elif len(string) > 0 and len(string) < 10:
            print("the lenght is to short")
        elif len(string) > 10 and len(string) < 20:
            print("the lenght is medium")
        elif len(string) > 20 and len(string) < 30:
            print("the lenght is medium long")
        else:
            print("the lenght is very long")
OrderStrings(["jhgjhvjg", "hvjgchgchcfcukyvkh", "jhvjlhcljgcjlhclhjvhkjvjhvjh", "mhvj,hcjglcjlgcljhclgjclguclhcljhcljgc"])
       
            
# 8- Investiga sobre la ordenación por mezcla (merge sort) y escribe un resumen.
# 🔍 Merge Sort: es un algoritmo de ordenación basado en el paradigma "divide y vencerás".
# Divide recursivamente una lista en mitades, ordena cada mitad y luego las fusiona en orden.

# 🧠 ¿Cómo funciona?
# 1. Divide: Separa la lista en dos mitades.
# 2. Conquista: Ordena cada mitad recursivamente.
# 3. Fusiona: Une las mitades ordenadas en una sola lista ordenada.

# 🧪 Ejemplo:
# Lista original: [38, 27, 43, 10]
# Paso 1: Divide → [38, 27] y [43, 10]
# Paso 2: Divide más → [38], [27], [43], [10]
# Paso 3: Fusiona → [27, 38], [10, 43]
# Paso 4: Fusiona final → [10, 27, 38, 43]

# ⏱️ Complejidad temporal:
# - Mejor caso: O(n log n)
# - Promedio: O(n log n)
# - Peor caso: O(n log n)

# 📦 Complejidad espacial:
# - O(n) → requiere espacio adicional para fusionar sublistas.

# ✅ Ventajas:
# - Estable: conserva el orden de elementos iguales.
# - Rendimiento consistente en todos los casos.
# - Ideal para listas enlazadas y grandes volúmenes de datos.

# ⚠️ Desventajas:
# - No es in-place (usa memoria extra).
# - Más lento que Quick Sort en listas pequeñas.

# 🧠 Conclusión:
# Merge Sort es excelente para datos grandes y cuando se necesita estabilidad.
# Es ampliamente usado en bibliotecas estándar como `sorted()` en Python (TimSort es una variante).

# 9- Crea una lista de objetos y escribe un programa que la ordene por un atributo.
def OrderByAge(list3):
    # De las 2 formas con bubble sort o tim sort
    n = len(list3)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list3[j][1] > list3[j + 1][1]:
                list3[j], list3[j + 1] = list3[j + 1], list3[j]
    # return sorted(list3, key= lambda x: x[1])
    return list3
print(OrderByAge([("Ana", 25), ("Luis", 30), ("Juan", 22)]))


# Mini Proyectos
# Desarrolla un programa que gestione una lista de contactos y permita ordenarlos por nombre.
def OrderByname(contacs):
    return sorted(contacs, key= lambda x: x[0])
print(OrderByname([("eric", 869532310), ("helen", 89754623), ("Ariel", 456321023), ("rosa", 89562310)]))
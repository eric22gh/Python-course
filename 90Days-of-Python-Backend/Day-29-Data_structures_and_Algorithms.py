# Día 29: Diccionarios y conjuntos
# Teoría:

# Los diccionarios son colecciones desordenadas de pares clave-valor, ideales para almacenar datos relacionados. 
# caractéricas: Mutabilidad: Los diccionarios son mutables, lo que significa que puedes agregar, modificar o eliminar elementos.
# Acceso por Clave: Los diccionarios se acceden mediante sus claves, que deben ser unicas.
# Operaciones: Los diccionarios ofrecen operaciones como get(), keys(), values(), items(), update(), pop(), popitem(), clear(), copy(), y setdefault().

# Los conjuntos son colecciones no ordenadas de elementos únicos, útiles para eliminar duplicados y realizar operaciones matemáticas.
# Características: Mutabilidad: Los conjuntos son mutables, lo que significa que puedes agregar o eliminar elementos.
# Operaciones: Los conjuntos ofrecen operaciones como union(), intersection(), difference(), y symmetric_difference().

# Ejemplos de diccionarios:
# Almacenamiento de Datos de Clientes en un Diccionario:
clientes = {
    '001': {'nombre': 'Alice', 'edad': 30, 'correo': 'alice@example.com'},
    '002': {'nombre': 'Bob', 'edad': 25, 'correo': 'bob@example.com'}
}
personas = {
    "nombre": "Eric",
    "edad": 30,
    "correo": "eric@example.com",
    "ciudad": "limon"
}

# Acceder a información de un cliente
print(clientes['001']['nombre'])  # clave es 001 y esa clave tiene un diccionario con nombre, edad y correo
print(clientes['002']['correo'])
print(personas['ciudad'])
print(personas.get("correo"))

# Agregar un nuevo cliente
clientes['003'] = {'nombre': 'Charlie', 'edad': 35, 'correo': 'charlie@example.com'}
clientes.setdefault('004', {'nombre': 'David', 'edad': 40, 'correo': 'david@example.com'})
personas["lenguaje"] = "python"
personas.setdefault("idioma", "ingles")
print(clientes)
print(personas)

# Actualizar información de un cliente
clientes['001']['edad'] = 31
clientes.update({'002': {'edad': 26}})
personas["edad"] = 31
personas.update({"correo": "eric@example.com"})
print(clientes)
print(personas)

# Eliminar un cliente
del clientes['002']
del personas["lenguaje"]
personas.pop("correo")
clientes.popitem()  # elimina el ultimo
print(clientes)

# ejemplo de Conjuntos:
frutas = {'manzana', 'banana', 'naranja'}
verduras = {'zanahoria', 'lechuga', 'tomate'}

# Unir conjuntos
alimentos = frutas.union(verduras)
print(f'Alimentos: {alimentos}')

# Intersección de conjuntos, valores comunes en los 2 conjuntos
frutas_tropicales = {'mango', 'banana', 'piña'}
frutas_comunes = frutas.intersection(frutas_tropicales)
print(f'Frutas comunes: {frutas_comunes}')

# Diferencia entre conjuntos, elementos exclusivos de un conjunto
frutas_diferentes = frutas.difference(verduras)
print(f'Frutas diferentes: {frutas_diferentes}')

# Diferencia simetrica entre conjuntos, elementos comunes a ambos conjuntos
frutas_simetrica = frutas.symmetric_difference(verduras)
print(f'Frutas simétricas: {frutas_simetrica}')

# Copiar conjuntos
frutas_copia = frutas.copy()
print(f'Frutas copia: {frutas_copia}')

# Limpiar conjuntos
frutas.clear()
print(f'Frutas limpias: {frutas}')

# Verificar si un elemento esta en un conjunto
print('manzana' in frutas)

# Contar elementos en un conjunto
print(f'Cantidad de frutas: {len(frutas)}')

# Recorrer conjuntos
for fruta in frutas:
    print(f'Fruta: {fruta}')

# Agregar elementos a un conjunto
frutas.add("kiwi")

# Eliminar elementos de un conjunto
frutas.remove("kiwi")

# Ordenar conjuntos
frutas = {'manzana', 'banana', 'naranja'}
frutas_ordenados = sorted(frutas)
print(frutas_ordenados)

# Buscar elementos en un conjunto
frutas = {'manzana', 'banana', 'naranja'}
print('manzana' in frutas)

# Descartar elementos de un conjunto
frutas.discard('banana')

frutas.update({'kiwi', 'pera'})

frutas.pop() # elimina el ultimo

frutas.isdisjoint(verduras) # devuelve true si no tienen elementos en comun

frutas.issubset(verduras) # devuelve true si todos los elementos de frutas estan en verduras

frutas.issuperset(verduras) # devuelve true si todos los elementos de verduras estan en frutas

# Contar Frecuencia de Palabras:
texto = "El rápido zorro marrón salta sobre el perro perezoso"
palabras = texto.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(f'Frecuencia de palabras: {frecuencia}')

# Tips y Buenas Prácticas:
# Utiliza diccionarios para almacenar datos que necesitan ser accedidos por una clave específica.
# Asegúrate de que las claves sean únicas para evitar sobrescribir datos.
# Los conjuntos son útiles para operaciones de comparación y pueden mejorar la eficiencia en la búsqueda de elementos.

# Ejercicios:
# 1- Crea un diccionario que almacene información sobre un libro (título, autor, año).
# 2- Accede a un valor en el diccionario y modifícalo.
# 3- Crea un conjunto de colores y añade un nuevo color.
# 4- Escribe un programa que imprima todas las claves de un diccionario.
# 5- Crea un conjunto a partir de una lista con duplicados.
# 6- Escribe un programa que cuente la frecuencia de letras en una cadena utilizando un diccionario.
# 7- Crea un diccionario de estudiantes con sus notas y calcula el promedio.
# 8- Escribe un programa que encuentre la clave más larga en un diccionario.
# 9- Crea un conjunto de números y verifica si un número está presente en el conjunto.
# 10- Escribe un programa que imprima todos los valores de un diccionario.
# 11- Crea un diccionario que almacene información sobre varios países y sus capitales.
# 12- Escribe un programa que combine dos diccionarios.
# 13- Crea un conjunto a partir de las claves de un diccionario.
# 14- Escribe un programa que imprima la longitud de cada clave en un diccionario.
# 15- Crea un programa que determine si dos conjuntos son disjuntos.

# Mini Proyectos:
# Desarrolla un programa que gestione una lista de contactos utilizando diccionarios.
# Crea un programa que cuente la frecuencia de palabras en un texto utilizando un diccionario.
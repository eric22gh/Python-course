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
libro = {
    "titulo" : "El cuervo",
    "autor" : "gabriel",
    "año" : 1993
}

# 2- Accede a un valor en el diccionario y modifícalo.
libro['año'] = 1992
libro.update({"autor" : "Eric"})
print(libro)

# 3- Crea un conjunto de colores y añade un nuevo color.
colores = {"verde", "rojo", "negro", "blando"}
colores.add("Turqueza")
print(colores)

# 4- Escribe un programa que imprima todas las claves de un diccionario.
for i, claves in enumerate(libro.keys(), start=1):
    print(f"{i}- {claves}")

# 5- Crea un conjunto a partir de una lista con duplicados.
lista = [1, 55, 1, 32, 58, 10, 22, 85, 58]
conjunto = set(lista)
print(conjunto)

# 6- Escribe un programa que cuente la frecuencia de letras en una cadena utilizando un diccionario.
from collections import Counter
cadena = "Hola, Soy Eric Hernandez Edwards Ingeniero Informatico"
fre = Counter(cadena)
for letra, cant in fre.items():
    print(f"Esta letra: {letra} aparece: {cant} en la frase")

############### otra forma
import re 
contar = {}
for frase in re.sub(r"[ ,.:;\d]", "", cadena.lower()):
    if frase in contar:
        contar[frase] += 1
    else:
        contar[frase] = 1 
for letra, cantidad in contar.items():
    print(f"{letra}: {cantidad}")

# 7- Crea un diccionario de estudiantes con sus notas y calcula el promedio.
estudiantes = {
    "eric" : {"ciencias": 85, "español": 75, "ingles" : 95},
    "luis" : {"ciencias": 75, "español": 95, "ingles" : 55},
    "helen" : {"ciencias": 45, "español": 65, "ingles" : 85},
    "carlos" : {"ciencias": 95, "español": 85, "ingles" : 90}
}
for claves, valor in estudiantes.items():
    promedio = sum(valor.values()) / len(valor.values())
    print(f"El promedio del estudiante: {claves} es de: {promedio}")

# 8- Escribe un programa que encuentre la clave más larga en un diccionario.
info = {
    "eric" : "hernandez",
    "alexander" : "gomez",
    "Helen" : "calvin",
    "sofia" : "perez"
}
clave_mas_larga = max(info.keys(), key=len)
longitud = len(clave_mas_larga)
print(f"La clave más larga es: '{clave_mas_larga}' con {longitud} letras.")

# 9- Crea un conjunto de números y verifica si un número está presente en el conjunto.
numeros = {1, 22, 56, 1, 54, 10}
print(23 in numeros)

# 10- Escribe un programa que imprima todos los valores de un diccionario.
for i, valores in enumerate(info.values(), start=1):
    print(f"{i}- {valores}")
    
# 11- Crea un diccionario que almacene información sobre varios países y sus capitales.
paises = {
    "Costa Rica" : "San jose",
    "Grecia" : "Athenas",
    "Noruega" : "Oslo"
}

# 12- Escribe un programa que combine dos diccionarios.
combinacion = paises | info
print(combinacion)

# 13- Crea un conjunto a partir de las claves de un diccionario.
new_set = set(combinacion.keys())
print(new_set)

# 14- Escribe un programa que imprima la longitud de cada clave en un diccionario.
for clave in combinacion.keys():
    longitud = len(clave)
    print(f"La clave: {clave}, tiene una longitud de: {longitud} letras")
    
# 15- Crea un programa que determine si dos conjuntos son disjuntos(si no tienen ningun elemento en comun).
con_1 = {1, 2, 86, 63, 4, 8}
con_2 = {1, 22, 6, 63, 4, 8}
print(con_1.isdisjoint(con_2))

#### fibonacci
def fibonacci(n):
    a = 0
    b = 1
    fibo = []
    for x in range(n):
        fibo.append(a)
        a, b = b, b + a
    return fibo
dato = fibonacci(15)
print(dato)

#### anagrama: 2 frases son anagramas cuando tienen las mismas letras pero son palabras distintas
import re
def anagramas(frase1, frase2):
    lista1 = list(sorted(re.sub(r"[ ,.]","",frase1.lower())))
    lista2 = list(sorted(re.sub(r"[ ,.]","",frase2.lower())))
    return lista1 == lista2
datos = anagramas("mani,", "iman")
print(datos)

#### palindromo: una palabra o frase es palindromo cuando significa lo mismo alderecho y al revez
def palindromo(palabra):
    palabra_1 = re.sub(r"[ ,.\d]","",palabra.lower())
    palabra_2 = palabra_1[::-1]
    return palabra_1 == palabra_2
dato = palindromo("apipa")
print(dato)

# Mini Proyectos:
# Desarrolla un programa que gestione una lista de contactos utilizando diccionarios.
class Contactos:
    def __init__(self):
        self.agenda = {}
        pass

    def agregar_contactos(self):
        try:
            nombre = input("Ingrese el nombre: ")
            numero = int(input("Ingrese el numero: "))
            self.agenda.setdefault(nombre.capitalize(), numero)
            return "Muchas gracias por agregar el numero"
        except TypeError as e:
            return f"Ingrese valores correctos y no: {e}"

    def mostrar_contactos(self):
        try:
            if not self.agenda:
                return "no hay ningun numero"
            contacts = []
            for c, v in self.agenda.items():
                contacto = f"Nombre: {c.capitalize()} y numero: {v}"
                contacts.append(contacto)
            return "\n".join([f"{i}- {informacion}"for i, informacion in enumerate(contacts, start=1)])
        except TypeError as e:
            return f"Ingrese valores correctos y no: {e}"
        
    def eliminar(self):
        try:
            nombre = input("Ingrese el nombre que quiera borrar: ")
            if nombre.capitalize() not in self.agenda:
                raise KeyError("El contacto no existe.")
            self.agenda.pop(nombre.capitalize())
            return "Contacto borrado"
        except (TypeError, KeyError) as e:
            return f"Ingrese un valor valido {e}"
        
espacio = Contactos()
while True:
    print(
        "\n Bienvenido a mi agenda de contactos \n"
        "1- Agregar Contactos\n"
        "2- Mostrar Contactos\n"
        "3- Eliminar Contactos\n"
        "4- Salir de Agenda\n"
    )
    number = int(input("Ingrese el numero de la accion que desea realizar: "))
    if number == 1:
       print(espacio.agregar_contactos())

    elif number == 2:
        print(espacio.mostrar_contactos())

    elif number == 3:
        print(espacio.eliminar())

    elif number == 4:
        print("Muchas Gracias por usar mi agenda")
        break
    else:
        print("Numero equivocado, ingrese uno valido del 1 al 4")

# Crea un programa que cuente la frecuencia de palabras en un texto utilizando un diccionario.
def frecuencia_palabras(word):
    import re 
    frecuency = {}
    for palabra in re.findall(r"\b\w+\b", word.lower()):
        if palabra in frecuency:
            frecuency[palabra] += 1
        else:
            frecuency[palabra] = 1
    return frecuency

dato = frecuencia_palabras("hola mundo; Soy Helen Edwards Calvin de recursos humanos, hola tengo: 23 años")
print(dato)

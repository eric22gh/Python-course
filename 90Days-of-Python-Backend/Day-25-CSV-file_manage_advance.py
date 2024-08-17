# Día 25: Manejo de Archivos avnzado con CSV

# Definición del Tema
# Manejo de archivos CSV (valores separados por comas) en Python, aprendiendo cómo leer, escribir 
# y manipular datos en este formato.

# Tips del Tema
# - CSV es un formato comúnmente utilizado para almacenar datos tabulares, donde cada fila representa un registro y las 
# columnas están separadas por comas.
# - Python proporciona el módulo csv para trabajar con archivos CSV de manera fácil y eficiente.
# - El módulo csv proporciona funciones para leer y escribir archivos CSV, así como para procesar datos en formato CSV.

import csv
# Escribir 
datos = [
    # lista de listas
    ["Nombre", "Edad", "Correo"],
    ["Juan", 30, "juan@example.com"],
    ["María", 25, "maria@example.com"],
    ["Eric", 28, "Eric@example.com"]
]

with open("datos.csv", "w", newline="", encoding= "utf-8") as archivo:
    escritor_csv = csv.writer(archivo)
    # escritor_csv.writerow(datos) lo escribe todo como en una lista
    escritor_csv.writerows(datos)
#     - El método csv.writer() crea un objeto que se utiliza para escribir en archivos CSV.
#     - writerows() se utiliza para escribir varias filas a la vez, donde cada fila es una lista.

#Leer datos 
with open("datos.csv", "r") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
#     - El método csv.reader() crea un objeto que se utiliza para leer el contenido del archivo CSV.
#     - Un bucle for se utiliza para iterar sobre las filas del archivo CSV y se imprimen.

# Avanzado: Lectura y Filtrado de Datos
# Leer datos desde un archivo CSV y filtrar por edad mayor a 25

with open("datos.csv", "r") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        nombre, edad, correo = fila
        if edad.isdigit() and int(edad) > 25:
#     - Se verifica si la columna edad es un número y si es mayor a 25.
            print(f"{nombre} tiene {edad} años y su correo es {correo}")
print("eric")
with open("datos.csv", "r") as file:
    read = csv.reader(file)
    for x in read:
        nombre, edad, correo = x
        if edad.isdigit() and int(edad) <= 25:
            print(f"{nombre} tiene {edad} años y su correo es {correo}")

# # Manejo de DictReader y DictWriter

# Usar DictWriter para escribir un archivo CSV
campos = ["Nombre", "Edad", "Correo"]
datos = [
    # lista de diccionarios
    {"Nombre": "Juan", "Edad": 30, "Correo": "juan@example.com"},
    {"Nombre": "María", "Edad": 25, "Correo": "maria@example.com"},
    {"Nombre": "Alex", "Edad": 20, "Correo": "Alex@example.com"}
]

with open("datos.csv", "w", newline="", encoding= "utf-8") as archivo:
# - DictWriter: Permite escribir un archivo CSV utilizando diccionarios, donde las claves corresponden a los nombres de las columnas.
    escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
#   writeheader: permite escribir los encabezados
    escritor_csv.writeheader()
# - writerows() se utiliza para escribir varias filas a la vez, donde cada fila es una lista.
    escritor_csv.writerows(datos) 

# Usar DictReader para leer un archivo CSV
with open("datos.csv", "r") as archivo:
    lector_csv = csv.DictReader(archivo)
# - DictReader: Permite leer un archivo CSV en forma de diccionarios, facilitando el acceso a los valores por nombres de columnas.
    for fila in lector_csv:
        print(f"{fila['Nombre']} tiene {fila['Edad']} años y su correo es {fila['Correo']}")

# Práctica Sugerida
# 1. Ejercicio de Filtrado Avanzado: Crea un programa que lea un archivo CSV de productos, 
# filtre aquellos que tienen un precio mayor a $50, y guarde los resultados en un nuevo archivo CSV.
capos = ["nombre", "precio"]
datoss = [
    {"nombre": "pala", "precio": 100},
    {"nombre": "tornillo", "precio": 10},
    {"nombre": "taladro", "precio": 500},
    {"nombre": "martillo", "precio": 50},
    {"nombre": "varilla", "precio": 10},
    {"nombre": "varilla", "precio": 1000},
    {"nombre": "panel", "precio": 80}
]
with open("productos.csv", "w", newline="", encoding= "utf-8") as file:
    product = csv.DictWriter(file, fieldnames=capos)
    product.writeheader()
    product.writerows(datoss)

with open("productos.csv", "r") as file:
    reading = csv.DictReader(file)
    productos_filtrados = [] # agregar cuando se ocupa un filtro

    for x in reading:
        precio = int(x['precio'])
        nombre = x['nombre']

        if precio > 50:
            productos_filtrados.append({'nombre': nombre, 'precio': precio})

with open("new_list.csv", "w", newline="", encoding= "utf-8") as new_data:
    product = csv.DictWriter(new_data, fieldnames=capos)
    product.writeheader()
    product.writerows(productos_filtrados)

# 2. Ejercicio de Agregación: Crea un programa que lea un archivo CSV de ventas, calcule el total de ventas por producto, 
# y guarde los totales en un nuevo archivo CSV.
with open("productos.csv", "r") as ventas:
    productos = csv.DictReader(ventas)
    filtro = {}
    suma_precio = 0
    for x in productos:
        price = float(x['precio'])
        suma_precio += price
        name = x['nombre']
        if name in filtro:
            filtro[name] += price
        else:
            filtro[name] = price
resultado = [{'nombre': nombre, 'precio': precio} for nombre, precio in filtro.items()]

with open("new_prod.csv", "w", newline="", encoding="utf-8") as file:
    prod = csv.DictWriter(file, fieldnames=capos)
    prod.writeheader()
    prod.writerows(resultado)

# Ejercicios
# Ejercicio 1: Escribe un programa que lea un archivo CSV con datos de estudiantes (nombre, edad y promedio) y muestre la información de cada estudiante.
hearders = ["nombre", "edad", "promedio"]
datos2 =[
    {"nombre":"eric", "edad":25, "promedio": 78 },
    {"nombre":"alex", "edad":20, "promedio": 88 },
    {"nombre":"luis", "edad":21, "promedio": 98 },
    {"nombre":"maria", "edad":22, "promedio": 68 },
    {"nombre":"marta", "edad":23, "promedio": 84 }
]
with open ("estudiantes.csv", "w", encoding= "utf-8", newline="") as file:
    alumos = csv.DictWriter(file, fieldnames=hearders)
    alumos.writeheader()
    alumos.writerows(datos2)

with open("estudiantes.csv", "r") as read:
    info = csv.DictReader(read)
    for notas in info:
        print(f"Este alumno: {notas['nombre']} tiene una edad de: {notas['edad']} y un promedio de: {notas['promedio']}")

# Ejercicio 2: Escribe un programa que lea un archivo CSV con datos de productos (nombre, precio y cantidad) y calcule el valor total de inventario.
hearders = ["nombre", "precio","cantidad"]
data = [
    {"nombre":"pala", "precio":500, "cantidad": 100},
    {"nombre":"tornillo", "precio":50, "cantidad": 1000},
    {"nombre":"cierra", "precio":5000, "cantidad": 18},
    {"nombre":"cerrucho", "precio":100, "cantidad": 200},
    {"nombre":"lamina", "precio":1500, "cantidad": 80},
    {"nombre":"martillo", "precio":18, "cantidad": 980},
]
with open("articulos.csv", "w", encoding="utf-8", newline="") as file:
    productos = csv.DictWriter(file, fieldnames=hearders)
    productos.writeheader()
    productos.writerows(data)
with open("articulos.csv", "r") as reads:
    info = csv.DictReader(reads)
    suma = 0
    for inventario in info:
        valor = int(inventario['cantidad'])
        suma += valor
print(f"el inventario total es de: {suma} productos")

# Ejercicio 3: Escribe un programa que lea un archivo CSV con datos de articulos (producto, cantidad y precio) y calcule el total de ventas.
with open("articulos.csv", "r") as ventas:
    total = csv.DictReader(ventas)
    venta_total = 0
    for vendidos in total:
        precio = float(vendidos['precio'])
        cantidad = int(vendidos['cantidad'])
        venta_total += precio * cantidad
print(f"Si la tienda logra vender todos los artículos, tendría una venta total de: ${venta_total}")
        
# Ejercicio 4: Escribe un programa que lea un archivo CSV con datos de empleados (nombre, salario y departamento) y muestre el nombre del empleado con el salario más alto.
hearders = ["nombre", "salario","departamento"]
data = [
    {"nombre":"alex", "salario":50000, "departamento": "ventas"},
    {"nombre":"vanessa", "salario":600000, "departamento": "ventas"},
    {"nombre":"maria", "salario":500000, "departamento": "dev"},
    {"nombre":"gellen", "salario":100000, "departamento": "test"},
    {"nombre":"luis", "salario":1500000, "departamento": "produccion"},
    {"nombre":"marcos", "salario":180000, "departamento": "test"}
]
with open("empleados.csv", "w", newline="", encoding="utf-8") as datos:
    planilla = csv.DictWriter(datos, fieldnames=hearders) 
    planilla.writeheader()
    planilla.writerows(data)

with open("empleados.csv","r") as plan:
    lista = csv.DictReader(plan)
    suma_salario = 0
    salario_mayor = {}
    for salarios in lista: 
        monto = float(salarios["salario"])
        if monto > suma_salario:
            suma_salario = monto
            salario_mayor = salarios
print(f"el salario mas alto es de: {suma_salario} y pertenese a: {salario_mayor['nombre']}")

# Ejercicio 5: Escribe un programa que lea un archivo CSV con datos de películas (título, año y género) y muestre el título de la película más antigua.
# cuando se busca el menor de una lista tengo que poner un techo(numero) que se mas alto o igual que el numero mas grande de la lista
# y cuando se busca el maximo no, porque el va agregando
hearders = ["titulo", "year", "genero"]
datos = [
    {"titulo": "aorca", "year":2024, "genero": "drama"},
    {"titulo": "datos", "year":2004, "genero": "terror"},
    {"titulo": "asalto", "year":2000, "genero": "accion"},
    {"titulo": "saw", "year":2005, "genero": "gore"},
    {"titulo": "while", "year":1995, "genero": "accion"}
]

with open("peliculas.csv", "w", encoding="utf-8", newline="") as file:
    peliculas = csv.DictWriter(file, fieldnames=hearders)
    peliculas.writeheader()
    peliculas.writerows(datos)

with open ("peliculas.csv","r") as data:
    pelicula = csv.DictReader(data)
    suma_pelicula = float('inf') # buscan el mínimo o máximo de un conjunto de valores
    peli = {}
    for x in pelicula:
        vieja = int(x["year"])
        if vieja < suma_pelicula:
            suma_pelicula = vieja
            peli = x
print(f"la pelicula mas vieja es: {peli['titulo']} del año: {suma_pelicula}")

# Ejercicio 6: Escribe un programa que lea un archivo CSV con datos de clientes (nombre, correo y teléfono) 
# y encuentre el cliente con el correo electrónico más largo.
hearders = ["titulo", "correo", "teléfono"]
datos = [
    {"titulo": "alex", "correo":"alex59@hotmail.com", "teléfono": 58965341},
    {"titulo": "irma", "correo":"irma508905@hotmail.com", "teléfono": 78456321},
    {"titulo": "pedro", "correo":"ped589@hotmail.com", "teléfono": 56324178},
    {"titulo": "sofia", "correo":"sofia@hotmail.com", "teléfono": 8974562130},
    {"titulo": "walter", "correo":"walter589@hotmail.com", "teléfono": 7896452130}
]

with open("clientes.csv", "w", encoding="utf-8", newline="") as file:
    peliculas = csv.DictWriter(file, fieldnames=hearders)
    peliculas.writeheader()
    peliculas.writerows(datos)

with open("clientes.csv", "r") as data:
    clientes = csv.DictReader(data)
    correo = {}
    inicio = 0
    for client in clientes:
        p = client["correo"]
        conteo = len(p)
        if conteo > inicio:
            inicio = conteo
            correo = client
print(f"El correo mas largo es el de: {correo['titulo']} con: {inicio} caracteres")

# Ejercicio 7 (Teoría): Explica qué es un archivo CSV, por qué es útil y cuáles son algunas de sus características.
# Archivos CSV (Comma-Separated Values) son archivos de texto plano que almacenan datos tabulares en formato de filas y columnas, 
# donde los campos están separados por comas. Son útiles para almacenar, intercambiar y analizar datos de manera simple y accesible. 
# Su integración con el módulo csv en Python permite la manipulación eficiente de estos archivos.

# Ejercicio 8 (Práctica): Escribe un programa que lea un archivo CSV con datos de ventas (nombre y precio) 
# y encuentre el producto de más valor.
with open("productos.csv", "r") as data:
    productos = csv.DictReader(data) 
    prod = {}
    suma_prod = 0
    for x in productos:
        valor = float(x['precio'])
        if valor > suma_prod:
            suma_prod = valor
            prod = x
print(f"el producto de mas valor es: {prod['nombre']} con un valor de: {suma_prod}")

# Ejercicio 9: Escribe un programa que lea un archivo CSV con datos de estudiantes (nombre, edad y promedio) 
# y encuentre el estudiante con el promedio más alto.
with open("estudiantes.csv","r") as data:
    alumos = csv.DictReader(data)
    promedio = {}
    suma_promedio = 0
    for estudiantes in alumos:
        prod_alto = float(estudiantes['promedio']) 
        if prod_alto > suma_promedio:
            suma_promedio = prod_alto
            promedio = estudiantes
print(f"el estudiante: {promedio['nombre']} tiene el promedio mas alto que es de: {suma_promedio}")

# Ejercicio 10: Escribe un programa que lea un archivo CSV con datos de libros (título, autor y páginas) 
# y muestre el título del libro más largo.
hearders = ["titulo", "autor", "paginas"]
datos = [
    {"titulo": "cronicas de una muerte", "autor":"alex", "paginas": 589},
    {"titulo": "100", "autor":"irma", "paginas": 784},
    {"titulo": "dark", "autor":"ped", "paginas": 563},
    {"titulo": "fallout", "autor":"sofia", "paginas": 897},
    {"titulo": "libertados", "autor":"walter", "paginas": 789}
]
with open("libros.csv", "w", encoding="utf-8", newline="") as data:
    libros = csv.DictWriter(data, fieldnames=hearders)
    libros.writeheader()
    libros.writerows(datos)
with open("libros.csv", "r") as read:
    libros = csv.DictReader(read)
    suma_libros = 0
    libro_largo = {}
    for l in libros:
        titulo = l['titulo']
        conteo = len(titulo)
        if conteo > suma_libros:
            suma_libros = conteo
            libro_largo = l
print(f"el libro: {libro_largo['titulo']} tiene el titulo mas largo con: {suma_libros} caracteres")
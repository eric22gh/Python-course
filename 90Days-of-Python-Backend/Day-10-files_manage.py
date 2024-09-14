# Día 10: Manejo de Archivos
# Manejar archivos en Python, incluyendo cómo leer y escribir datos.

# Tips del Tema
# Abrir archivos: Se utiliza la función open() para abrir archivos en varios modos:
# 'r' : Modo lectura (por defecto).
# 'w' : Modo escritura (crea un archivo nuevo o sobreescribe uno existente).
# 'a' : Modo append (agregar al final del archivo).
# 'r+': Modo lectura/escritura

# ############### leer 
# archivo = open('mi_archivo.txt', 'r')  # Abre el archivo en modo lectura

# with open('mi_archivo.txt', 'r') as archivo:
#     contenido_completo = archivo.read()  # Lee el archivo completo
#     print(contenido_completo)

# with open('mi_archivo.txt', 'r') as archivo:
#     for linea in archivo:
#         print(linea.strip())  # Lee y muestra línea por línea

# ################## escribir
# with open('mi_archivo.txt', 'w') as archivo:
#     archivo.write("Hola, mundo!\n")
#     archivo.write("Este es un archivo de mi_archivo.\n")

# with open('mi_archivo.txt', 'a') as archivo:
#      archivo.write("Añadiendo una nueva línea al final.\n")

# ################# cerrar: es importante cerrar el arcivo
# archivo = open('mi_archivo.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()  # Cierra el archivo manualmente

# # Usar 'with' para manejo automático de cierre
# with open('mi_archivo.txt', 'r') as archivo:
#     contenido = archivo.read()

# ################

# # Crear y escribir en un archivo, sobre escribe el contenido anterior
# with open('mi_archivo.txt', 'w') as archivo:
#     archivo.write("Esta es la primera línea.\n")
#     archivo.write("Esta es la segunda línea.\n")

# # Leer el archivo completo
# with open('mi_archivo.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print("Contenido completo del archivo:")
#     print(contenido)

# # Agregar una nueva linea al archivo
# with open('mi_archivo.txt', 'a') as archivo:
#     archivo.write("Añadiendo una tercera línea.\n")
#     archivo.write("Añadiendo una cuarta línea.\n")

# # Leer el archivo línea por línea
# with open('mi_archivo.txt', 'r') as archivo:
#     print("Leyendo línea por línea:")
#     for linea in archivo:
#         print(linea.strip())

# ######################## Ejercicios
# # Ejercicio 1: Crea un archivo de texto y escribe en él tu nombre y edad.
# with open("texto.txt", "w") as archivo:
#     archivo.write("mi nombre es: Eric Hernandez.\n")
#     archivo.write("tengo una edad de: 30 años.\n")

# with open("texto.txt", "w") as archivo:
#     archivo.write("mi nombre es: Eric Hernandez.\n"
#                   "tengo una edad de: 30 años.\n")

# # Ejercicio 2: Abre el archivo creado en el ejercicio 1 y lee su contenido.
# with open("texto.txt","r") as archivo:
#     leer = archivo.read()
#     print(leer)

# # Ejercicio 3: Añade una nueva línea con tu ciudad en el archivo creado en el ejercicio 1.
# with open("texto.txt","a") as archivo:
#     archivo.write("mi nombre es: Eric Hernandez.\n"
#                   "tengo una edad de: 30 años.\n"
#                   "vivo en la ciudad de madrid.\n")
    
# # Ejercicio 4: Lee el archivo línea por línea y muestra cada línea.
# with open("texto.txt","r") as archivo:
#     rea = archivo.readlines(100)
#     print(rea) # end " " significa que se va a ser print al final de cada linea.

# # Ejercicio 5: Define una función que lea un archivo y cuente el número de líneas.
# def leer_file(archivo):
#     with open("texto.txt","r") as archivo:
#         contar = archivo.readlines()
#         return len(contar)
# archivo = "texto.txt"
# print(f'El archivo tiene {leer_file(archivo)} líneas.')

# # Ejercicio 6: Define una función que lea un archivo y cuente el número de palabras.
# def read_file(file):
#     with open("texto.txt","r") as file:
#         contar = file.read()
#         palabras = contar.split()
#         return len(palabras)
# file = "texto.txt"
# print(f"el archivo tiene: {read_file(file)} palabras")

# # Ejercicio 7: Define una función que tome un nombre de archivo y una cadena, y escriba la cadena en el archivo.
# def write_string(archivos,cadena):
#     with open(archivos,"w") as files:
#         escribir = files.write(cadena)
# archivos = "texto.txt"
# write_string(archivos,"hola soy costa.")
# print("Cadena escrita en el archivo.")

# # Ejercicio 8: Define una función que tome un nombre de archivo y un número, y añada tantas líneas al archivo con el texto "Línea X".
# def añadir(nombre_archivo, cantidad):
#     with open(nombre_archivo, "w") as app:
#         for i in range(1, cantidad + 1):
#             app.write(f"Linea {i}.\n")

# archivo = "miapp.txt"
# añadir(archivo, 5)

# # Ejercicio 9 (Teoría): ¿Cuál es la diferencia entre los modos de apertura de archivos r, w, a, y r+?
# # el modo r es solo para lectura, el w para escritura, el a para agregar mas lineas al archivo y el r+ permite escribir y en el archivo

# # Ejercicio 10 (Práctica): Escribe un programa que pida al usuario un nombre de archivo y un texto, y escriba el texto en el archivo. 
# # Si el archivo ya existe, añade el texto en lugar de sobrescribirlo.
# nombre_archivo = str(input("ingresa el nombres del archivo con .txt: "))
# texto = str(input("ingresa el texto ") + "\n")
# with open(nombre_archivo,"w") as eric:
#         escribir = eric.write(texto)
#         if nombre_archivo:
#             eric.write(texto) # todas las operaciones de escritura tienen que estar en el bloque with.
#         else:
#             print(escribir)

# Ejercicio 11: Crea un archivo llamado "datos.txt" y escribe en él 5 números enteros separados por espacios en una sola línea.
with open("datos.txt", "w") as file:
    for x in range(1, 6):
        dato = file.write(str(f"{x} "))

########## otra forma
with open("dato.txt", "w") as file:
    file.write(" ".join(str(x) for x in range(1, 6)))

# Ejercicio 12: Abre el archivo "datos.txt" y calcula la suma de los números enteros que contiene.
with open("datos.txt", "r") as read:
    cadenas = read.read()
    numeros = [int(n) for n in cadenas.split()]
    print(f"La suma de todos los numeros del archivo es: {sum(numeros)}")
   
# Ejercicio 13: Crea un archivo "multiplicacion.txt" que contenga las tablas de multiplicar del 1 al 10, con cada tabla en una nueva línea.
with open("multiplicacion.txt", "w") as file1:
    for tabla in range(1, 11):
        for numero in range(1, 11):
            file1.write(f"{tabla} x {numero} = {tabla * numero}\n")
        file1.write("\n")  # espacio entre tablas

# Ejercicio 14: Escribe un programa que copie el contenido de un archivo llamado "origen.txt" a un archivo nuevo llamado "copia.txt".
with open("origen.txt", "w") as file:
    data = file.write("eric hernandez edwards\n")
# si el archivo ya esta creado se puede avanzar de aqui en adelantes para no sobreescribir el archivo ya que se pueden perder datos.
with open("origen.txt", "r") as file2:
    data = file2.read()

with open("copia.txt", "w") as file3:
    data1 = file3.write(data)

# Ejercicio 15: Define una función que tome como entrada un archivo de texto y reemplace todas las vocales con la letra 'x', escribiendo el resultado en un nuevo archivo.
def replace_vocals(file):
    with open(file, "r") as eric:
        datu = eric.read()
    with open("eric.txt", "w") as eric2:
        #remplazo_cadenas = datu.replace("a","x").replace("e","x").replace("i","x").replace("o","x").replace("u","x")
        remplazo_cadenas = datu.translate(str.maketrans("aeiou", "xxxxx"))
        new = eric2.write(remplazo_cadenas)

    print("Las vocales fueron reemplazadas exitosamente.")

replace_vocals("copia.txt")

# Ejercicio 16: Crea un archivo "poema.txt" con 3 líneas de texto. Después, escribe un programa que lea el archivo e imprima cuántas palabras tiene cada línea.
with open("poema.txt", "w") as fill:
    datos = fill.write("eric alexander hernandez edwards\n"
                       "helen calvin brenes\n"
                       "diego hernandez edwards\n"
                       )

with open("poema.txt", "r") as read:
    leido = read.readlines()
for i, linea in enumerate(leido, 1):
    conteo = len(linea.split())
    print(f"la linea numero {i} tiene: {conteo} palabras")
    
# Ejercicio 17: Crea un programa que abra un archivo llamado "numeros.txt" y muestre solo las líneas que contienen números pares.
with open("numeros.txt", "w") as num:
    numeross = num.writelines("2 4 6 8\n"
                         "3 5 7 9\n"
    )
with open("numeros.txt", "r") as reads:
 for linea in reads:  
        numeros = [int(n) for n in linea.split()] 
        for par in numeros:
            if par % 2 == 0:  
                print(par)

# Ejercicio 18: Define una función que tome dos nombres de archivo, lea el contenido de ambos, y los combine en un archivo nuevo llamado "combinado.txt".
def combinar_archivos(file1, file2, output_file="combinado.txt"):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            contenido1 = f1.read()
            contenido2 = f2.read()

        with open(output_file, "w") as combinado:
            combinado.write(contenido1 + contenido2)
        
        print(f"Archivos combinados correctamente en {output_file}.")

    except FileNotFoundError as e:
        print(f"Error: No se pudo encontrar el archivo - {e}")
        
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

combinar_archivos("poema.txt", "origen.txt")

# Ejercicio 19: Escribe un programa que abra un archivo llamado "reverso.txt" y escriba en él el contenido invertido de otro archivo llamado "origen.txt".
with open("origen.txt", "r") as fil:
    read = fil.read()
with open("reverso.txt", "w") as wr:
    wrote = wr.write(read[::-1]) 

# Ejercicio 20: Escribe un programa que tome una lista de nombres de archivos y verifique si cada uno existe o no. 
# Para los archivos que existen, imprime su tamaño en bytes.
import os # os para Operaciones con Archivos y Directorios
archivos = ["combinado.txt", "copia.txt", "datos.txt", "erics.txt"]
for files in archivos:
    if os.path.exists(files):
        tamaño = os.path.getsize(files)
        print(f"el archivo: {files} existe y su tamaño es: {tamaño}bytes")
    else:
        print(f"el archivo: {files} no existe")


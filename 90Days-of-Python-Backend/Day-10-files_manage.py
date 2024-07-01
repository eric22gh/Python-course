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



######################## Ejercicios
# Ejercicio 1: Crea un archivo de texto y escribe en él tu nombre y edad.
with open("texto.txt", "w") as archivo:
    archivo.write("mi nombre es: Eric Hernandez.\n")
    archivo.write("tengo una edad de: 30 años.\n")

with open("texto.txt", "w") as archivo:
    archivo.write("mi nombre es: Eric Hernandez.\n"
                  "tengo una edad de: 30 años.\n")

# Ejercicio 2: Abre el archivo creado en el ejercicio 1 y lee su contenido.
with open("texto.txt","r") as archivo:
    leer = archivo.read()
    print(leer)

# Ejercicio 3: Añade una nueva línea con tu ciudad en el archivo creado en el ejercicio 1.
with open("texto.txt","a") as archivo:
    archivo.write("mi nombre es: Eric Hernandez.\n"
                  "tengo una edad de: 30 años.\n"
                  "vivo en la ciudad de madrid.\n")
    

# Ejercicio 4: Lee el archivo línea por línea y muestra cada línea.
with open("texto.txt","r") as archivo:
    rea = archivo.readlines(100)
    print(rea) # end " " significa que se va a ser print al final de cada linea.


# Ejercicio 5: Define una función que lea un archivo y cuente el número de líneas.
def leer_file(archivo):
    with open("texto.txt","r") as archivo:
        contar = archivo.readlines()
        return len(contar)
archivo = "texto.txt"
print(f'El archivo tiene {leer_file(archivo)} líneas.')

# Ejercicio 6: Define una función que lea un archivo y cuente el número de palabras.
def read_file(file):
    with open("texto.txt","r") as file:
        contar = file.read()
        palabras = contar.split()
        return len(palabras)
file = "texto.txt"
print(f"el archivo tiene: {read_file(file)} palabras")

# Ejercicio 7: Define una función que tome un nombre de archivo y una cadena, y escriba la cadena en el archivo.
def write_string(archivos,cadena):
    with open(archivos,"w") as files:
        escribir = files.write(cadena)
archivos = "texto.txt"
write_string(archivos,"hola soy costa.")
print("Cadena escrita en el archivo.")

# Ejercicio 8: Define una función que tome un nombre de archivo y un número, y añada tantas líneas al archivo con el texto "Línea X".
def añadir(nombre_archivo, cantidad):
    with open(nombre_archivo, "w") as app:
        for i in range(1, cantidad + 1):
            app.write(f"Linea {i}.\n")

archivo = "miapp.txt"
añadir(archivo, 5)

# Ejercicio 9 (Teoría): ¿Cuál es la diferencia entre los modos de apertura de archivos r, w, a, y r+?
# el modo r es solo para lectura, el w para escritura, el a para agregar mas lineas al archivo y el r+ permite escribir y en el archivo

# Ejercicio 10 (Práctica): Escribe un programa que pida al usuario un nombre de archivo y un texto, y escriba el texto en el archivo. 
# Si el archivo ya existe, añade el texto en lugar de sobrescribirlo.

nombre_archivo = str(input("ingresa el nombres del archivo con .txt: "))
texto = str(input("ingresa el texto ") + "\n")
with open(nombre_archivo,"w") as eric:
        escribir = eric.write(texto)
        if nombre_archivo:
            eric.write(texto) # todas las operaciones de escritura tienen que estar en el bloque with.
        else:
            print(escribir)

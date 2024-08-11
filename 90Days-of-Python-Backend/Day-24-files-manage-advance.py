# Día 24: Manejo de Archivos

# Definición del Tema
# Abrir, leer, escribir y archivos de texto, binarios, csv, pdf y json.

# Tips del Tema
# - Python proporciona funciones y métodos integrados para trabajar con archivos.
# - El modo de apertura de un archivo determina si se puede leer, escribir o ambos.
# - Es importante cerrar un archivo después de terminar de trabajar con él para liberar recursos.
# 'r' : Modo lectura (por defecto).
# 'w' : Modo escritura (crea un archivo nuevo o sobreescribe uno existente).
# 'a' : Modo append (agregar al final del archivo).
# 'r+': Modo lectura/escritura
# 'w+': Modo lectura/escritura
# 'a+': Modo append(agregar al final del archivo)lectura/escritura

# (write) escribir contenido en él archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola mundo!\n")
    archivo.write("hola, eric hernandez\n") # segunda linea del archivo
    
# Añadir texto a un Archivo Existente
with open("archivo.txt", "a") as archivo:
    archivo.write("Tercera línea añadida.\n")

# (read) leer un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read() # no es recomendable usar readlines para archivos grandes ya que guarda en memoria
    print(contenido)

# archivo.close()  # Cierra el archivo manualmente

# Lectura de Archivos de Texto Línea por Línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina los espacios en blanco al inicio y final de cada línea

############################
# # Escribir un archivo binario (copiar una imagen)
# with open("imagen.png", "wb") as archivo:
#     archivo.write("contenido_binario") # hay que escribirlo en binario

# # Abrir un archivo en modo binario y leer su contenido
# with open("imagen.png", "rb") as archivo:
#     contenido = archivo.read()
#     print(contenido)
###############################

########## Archivos de Texto (CSV, JSON, etc.)     
#Archivos CSV
import csv
# Escribir en un archivo CSV
with open("salida.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad", "Ciudad"])
    escritor.writerow(["Alice", 30, "Madrid"])
    escritor.writerow(["Bob", 25, "Barcelona"])
    escritor.writerow(["Eric", 30, "Costa Rica"])

# Leer archivo CSV
# with open("salida.csv", "r") as archivo:
#     read = csv.reader(archivo) # esta variable devuelve un objeto iterable x eso no se puede con print
#     print(read)
### leer linea x linea
with open("salida.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# Archivos JSON
import json
# Escribir en un archivo JSON
nuevos_datos = {"nombre": "Carlos", "edad": 28, "ciudad": "Sevilla", "Carrera": "Informatica"}
with open("datos.json", "w") as archivo:
    json.dump(nuevos_datos, archivo) # json.dump pasa los datos en python a JSON

# Leer archivo JSON
with open("datos.json", "r") as archivo:
    datos = json.load(archivo) # json.load lee datos JSON
    print(datos)

# Comprimir Archivos en un ZIP
import zipfile # hay que crear el archivo que se quiere comprimir

with open("file.txt", "w") as file:
    leer = file.write("Eric hernandez edwards")

with zipfile.ZipFile("file.zip", "w") as archivo_zip:
    archivo_zip.write("file.txt") # poner el nombre del file que quiere comprimir

# Descomprimir Archivos de un ZIP
with zipfile.ZipFile("file.zip", "r") as archivo_zip:
    archivo_zip.extractall("/Desktop/Python-course/90Days-of-Python-Backend")

# Manejo Avanzado de Archivos
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se encontró.")
except IOError:
    print("Hubo un problema al leer el archivo.")

import os # os para Operaciones con Archivos y Directorios
# Listar archivos en el directorio que estas
archivos = os.listdir(".")
print(archivos)

# Comprobar si un archivo existe
if os.path.exists("fil.txt"):
    print("El archivo existe.")
else:
    print("El archivo no existe.")

# Renombrar un archivo
#os.rename("file.txt", "archivo_renombrado.zip")
#os.rename("file.zip", "data.txt") # solo renombra el archivo en caso de el anterior este comprimido y con datos, ala hora de renombrarlo
# no va a poder verse los datos
# os.rename("file.txt", "datoss.txt") 

# Eliminar un archivo
# os.remove("archivo_renombrado.zip")

# # Manejo de archivos JSON: Intenta leer datos de un archivo JSON, modificarlos y escribir los cambios de vuelta en un nuevo archivo JSON.
datos = {"nombre":"alex", "edad": 56, "ciudad": "limon"}
with open("eric.json", "w") as file:
    json.dump(datos, file)

with open("eric.json", "r") as file:
   files = json.load(file)

new_datos = {"nombre":"eric", "edad": 6, "ciudad": "cartago"}
files.update(new_datos)

with open("eric.json", "w") as file:
    json.dump(files, file, indent=3)

###### ejercicios 
# Ejercicio 1: Escribe un programa que lea el contenido de un archivo de texto y cuente el número de palabras en él.
with open("file.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"En el archivo hay: {word_count} palabras")

# Ejercicio 2: Escribe un programa que lea el contenido de un archivo de texto y cuente el número de líneas en él.
with open("file.txt", "r") as txt:
    c = txt.readlines()
    print(len(c))

with open("eric.json", "r") as jsons:
    x = sum(1 for linea in jsons)
    print(x)

with open("salida.csv", "r") as CSa:
    a =  csv.reader(CSa)
    print(len(a))

################### o
def contar_lineas(archivo):
    with open(archivo, "r") as file:
        line_count = sum(1 for _ in file) 
    return line_count

lineas_txt = contar_lineas("file.txt")
print(f"file.txt tiene {lineas_txt} líneas.")

lineas_json = contar_lineas("eric.json")
print(f"eric.json tiene {lineas_json} líneas.")

lineas_csv = contar_lineas("salida.csv")
print(f"salida.csv tiene {lineas_csv} líneas.")

# Ejercicio 3: Escribe un programa que lea el contenido de un archivo de texto y cuente el número de caracteres alfabéticos en él.
def contar_caracteres_alfabeticos(archivo):
    with open(archivo, "r") as file:
        contenido = file.read()
        caracteres_alfabeticos = [char for char in contenido if char.isalpha()] 
        return len(caracteres_alfabeticos)

caracteres_alfabeticos = contar_caracteres_alfabeticos("archivo.txt")
print(f"El archivo contiene {caracteres_alfabeticos} caracteres alfabéticos.")

# Ejercicio 4: Escribe un programa que lea el contenido de un archivo CSV (valores separados por comas) y convierta cada fila en una lista de elementos.
def csv_como_listas(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lector_csv = csv.reader(archivo) 
        filas = [fila for fila in lector_csv] 
    return filas

filas_csv = csv_como_listas("salida.csv")
for fila in filas_csv:
    print(fila) 

# Ejercicio 5: Escribe un programa que lea el contenido de un archivo de texto y cree un nuevo archivo con todas las letras en mayúsculas.
with open("archivo.txt", "r") as pop:
    d = pop.read()
new = d.upper()
with open("new_file.txt", "w") as n:
    l = n.write(new)

# Ejercicio 6: Escribe un programa que lea el contenido de un archivo de texto y cree un nuevo archivo con todas las palabras en minúsculas.
############# en formato txt
with open("archivo.txt", "r") as p:
    f = p.read()
new = f.lower()
with open("coto.txt", "w") as file:
    new_datos = file.write(new)

###### en formato JSON
with open("eric.json", "r") as json_fole:
    leer = json.load(json_fole)
minuscula = {}
for nombre, valor in leer.items():
    clave = nombre.lower() # la primera clave siempre va a ser un string, pero la segunda no siempre, depende de la condicion
    if isinstance(valor, str): # revisa con isinstance si valor es un str
        valor_minuscula = valor.lower()  
    else:
        valor_minuscula = valor  
    minuscula[clave] = valor_minuscula
with open("archivo.json", "w") as new: # crea un nuevo archivo con las letras en minuscula
    json.dump(minuscula, new, indent=2)

# Ejercicio 7 (Teoría): Explica cómo abrir, leer, escribir y cerrar archivos en Python, 
# y menciona algunas consideraciones importantes al trabajar con archivos.
# Con el manejo de archivos en python se puede abrir, leer y escribir en archivos como .txt, csv o json es muy util en cierto campos, 
# sin embargo se tiene que tomar siertas cosideraciones a la hora de hacer esta operaciones: tomar encuenbta que r = leer, w = escribir, a = agregar
# r+ = escribir y leer el nombre del archivo = file.txt, csv o json... Dada las consideraciones anteriores la sintaxis seria la siguientre 
# with open("file.txt", "r") as new
# leer = new.read() # para poner leer el archivo

# Ejercicio 8 (Práctica): Escribe un programa que lea el contenido de un archivo de texto y elimine todas las líneas en blanco.
with open("coto.txt","r") as top:
    archivo = top.read()
    print(archivo.replace(" ",""))

# Ejercicio 9: Escribe un programa que lea el contenido de un archivo de texto y cuente el número de veces que aparece cada palabra en él.
with open("coto.txt", "r") as leido:
    file = leido.read()
import re 
cadena = file
patron = r"hola"
palabra = re.findall(patron, cadena)
conteo = len(palabra)
print(f"el numero de veces que aparece la palabra: {patron}, son: {conteo} veces")
####################################################################
from collections import Counter
# import re
with open("coto.txt", "r") as leido:
    file = leido.read()

file = file.lower()
palabras = re.findall(r'\b\w+\b', file) # un re para encontrar todas las palabras
conteo_palabras = Counter(palabras)

for palabra, cantidad in conteo_palabras.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces.")

# Ejercicio 10: Escribe un programa que lea el contenido de un archivo binario y muestre su contenido en hexadecimal.
def leer_archivo_binario_y_mostrar_hex(archivo_binario):
    with open(archivo_binario, "rb") as archivo: 
        contenido = archivo.read()
        contenido_hex = contenido.hex() # pasarlo a hexadecimal
        print(contenido_hex)

leer_archivo_binario_y_mostrar_hex("nombre_del_archivo.bin")

# Día 23: Expresiones Regulares

# Definición del Tema
# ES una herramienta poderosa para buscar y manipular cadenas de texto con patrones específicos.

# Tips del Tema
# - Las expresiones regulares son patrones de búsqueda utilizados para encontrar coincidencias dentro de cadenas de texto.
# - Python proporciona el módulo `re` para trabajar con expresiones regulares.
# - Los patrones de expresiones regulares se definen utilizando una sintaxis especial que incluye metacaracteres como `.`, `*`, `+`, `?`, `[ ]`, `{ }`, entre otros.

# 1. Buscar un patrón en una cadena
import re
cadena = "¡Hola mundo!"
patron = r"Hola" 
resultado = re.search(patron, cadena)
if resultado:
    print("Se encontró una coincidencia.")
else:
    print("No se encontró ninguna coincidencia.")

# 2. Buscar todas las ocurrencias de un patrón en una cadena
cadena = "Python es un lenguaje de programación. Python es fácil de aprender."
patron = r"Python"
resultados = re.findall(patron, cadena)
print("Se encontraron", len(resultados), "ocurrencias de 'Python' en la cadena.")

cadena1 = "los juegos olimpicos 2024 son los mejores, ya que estos juegos a diferencia de otros juegos"
patron1 = r"juegos"
result = re.findall(patron1, cadena1)
print("se encontraron:", len(result),"resultados")

# 3. Sustituir un patrón por otro en una cadena
cadena = "Los gatos son adorables. Los perros también son adorables."
patron = r"adorables"
nueva_cadena = re.sub(patron, "increíbles", cadena)
patron2 = r"perros"
new = re.sub(patron2, "pajaros", cadena)
print(new)

# Conceptos Avanzados
# Símbolos Básicos en Expresiones Regulares
# . : Coincide con cualquier carácter excepto una nueva línea.
# ^ : Coincide con el comienzo de una línea.
# $ : Coincide con el final de una línea.
# * : Coincide con 0 o más repeticiones del carácter o grupo anterior.
# + : Coincide con 1 o más repeticiones del carácter o grupo anterior.
# ? : Coincide con 0 o 1 repeticiones del carácter o grupo anterior (opcionalidad).
# {n} : Coincide con exactamente n repeticiones del carácter o grupo anterior.
# {n,} : Coincide con n o más repeticiones del carácter o grupo anterior.
# {n,m} : Coincide con entre n y m repeticiones del carácter o grupo anterior.
# [] : Define un conjunto de caracteres; coincide con cualquiera de los caracteres en el conjunto.
# | : Operador OR; coincide con el patrón antes o después del operador.
# () : Agrupa subexpresiones; se usa para aplicar operadores a subexpresiones o para capturar coincidencias.
# \ : Escapa el siguiente carácter especial, permitiendo que se use como carácter literal.

# Secuencias de Escape Comunes
# \d : Coincide con cualquier dígito (equivalente a [0-9]).
# \D : Coincide con cualquier carácter que no sea un dígito.
# \w : Coincide con cualquier carácter de palabra (equivalente a [a-zA-Z0-9_]).
# \W : Coincide con cualquier carácter que no sea una palabra.
# \s : Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, nuevas líneas).
# \S : Coincide con cualquier carácter que no sea un espacio en blanco.
# \b : Coincide con una frontera de palabra.
# \B : Coincide con cualquier lugar que no sea una frontera de palabra.

# Ejemplos de Expresiones Regulares Comunes
# Dirección de correo electrónico: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
# Número de teléfono (formato (123) 456-7890): ^\(\d{3}\) \d{3}-\d{4}$
# Fecha en formato DD/MM/YYYY: ^\d{2}/\d{2}/\d{4}$
# Número de tarjeta de crédito (4 grupos de 4 dígitos): ^\d{4} \d{4} \d{4} \d{4}$
# URL básica: ^(https?|ftp)://[^\s/$.?#].[^\s]*$
# ip4: \b(?:\d{1,3}\.){3}\d{1,3}\b

# Ejemplo de metacaracteres:
cadena = "abbb ac abb abc"
patron = r"a.b"
resultados = re.findall(patron, cadena)
print("Patrones encontrados:", resultados)

# 5. Grupos y Rango de Caracteres
# Grupos
cadena = "Fecha: 2024-08-07"
patron = r"(\d{4})-(\d{2})-(\d{2})"
resultado = re.search(patron, cadena)
if resultado:
    print("Año:", resultado.group(1))
    print("Mes:", resultado.group(2))
    print("Día:", resultado.group(3))

# Rango de caracteres
cadena = "La casa número 123 está en la calle 456, del pais 20 de lista de PID" # buscar numeros en esa string
patron = r"[0-9]+" # numeros del 0  al 9 y mas
resultados = re.findall(patron, cadena)
print("Números encontrados:", resultados)

# 6. Fronteras de Palabras y Conjuntos Negativos
# Fronteras de palabras: \b
cadena = "hola hola123 123hola"
patron = r"\bhola\b"
resultados = re.findall(patron, cadena)
print("Palabras 'hola' encontradas:", resultados)

# Conjuntos negativos: [^ ]
cadena = "abc123 def456"
patron = r"[^0-9]+"
resultados = re.findall(patron, cadena)
print("Subcadenas sin números:", resultados)

# 7. Funciones avanzadas de `re`
# re.match() - Coincidencia al inicio de la cadena
cadena = "Python es genial"
patron = r"Python"
resultado = re.match(patron, cadena)
if resultado:
    print("Coincidencia al inicio de la cadena encontrada.")

# re.split() - Dividir una cadena según un patrón
cadena = "Python,Java,C++,JavaScript"
patron = r","
resultados = re.split(patron, cadena)
print("Cadena dividida:", resultados)

# 8. Compilación de Expresiones Regulares
# Compilar una expresión regular para mejorar el rendimiento
patron = re.compile(r"\d+")
cadena = "Hay 123 manzanas y 456 naranjas."
resultados = patron.findall(cadena)
print("Números encontrados (compilado):", resultados)

# 9. Flags en Expresiones Regulares
# Flags para modificar el comportamiento de las expresiones regulares:
# re.IGNORECASE - Ignorar mayúsculas y minúsculas
# re.MULTILINE - Tratamiento de múltiples líneas
# re.DOTALL - Hacer que el punto (.) coincida con cualquier carácter, incluyendo nueva línea

cadena = "Python es GENIAL. PYTHON es divertido."
patron = re.compile(r"python", re.IGNORECASE)
resultados = patron.findall(cadena)
print("Coincidencias ignorando mayúsculas/minúsculas:", resultados)

####### Ejercicios
# Ejercicio 1: Escribe una expresión regular para encontrar todas las direcciones de correo electrónico en un texto dado.
cadena5 = "alex@gmail.com, luis@gmail.com, maria@gmail.com, maria@hotmail.com"
patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
res = re.findall(patron, cadena5)
print(f"Se encontraron {len(res)} correos en el archivo: {res}")

# Ejercicio 2: Escribe una expresión regular para validar números de teléfono en el formato (123) 456-7890.
caden = "(123) 456-7890, (12) 456-78, (12) 456-7893, (023) 22-7890, (923) 106-7890, (124) 456-7890"
patron = r"\(\d{3}\)\s\d{3}-\d{4}"
r = re.findall(patron, caden)
print("se encontraron", len(r), f"los cuales son: {r}")

# Ejercicio 3: Escribe una expresión regular para encontrar todas las palabras que empiezan con la letra "a" en un texto.
strins = "anoche soñe que arturo armaba un Atico, hernandez"
patron4 = r"\b[aA]\w*\b"
a = re.findall(patron4, strins)
print(a)

# Ejercicio 4: Escribe una expresión regular para validar direcciones IPv4.
string = "192.56.0.0/18, 192.22.10.0/32, 200.250.23.0/25, 22.56.4/2, 192.56./30, 10.22.12.56"
patron = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ip = re.findall(patron, string)
print(ip)

# Ejercicio 5: Escribe una expresión regular para validar contraseñas que contengan al menos una letra mayúscula, una letra minúscula, un número y un carácter especial.
password = "Password123!"
patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(patron, password):
    print("contraseña segura")

else:
    print("contraseña muy debil")

# Ejercicio 6: Escribe una expresión regular para encontrar todas las fechas en formato DD/MM/AAAA en un texto.
texto = "04/02/2030, 10/02/2000, 04/01/2025"
patron = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"
fecha = re.findall(patron, texto)
print(fecha)

# Ejercicio 7 (Teoría): Explica qué son las expresiones regulares y cómo se utilizan en Python para buscar patrones en cadenas de texto.
# son secuencias de caracteres que definen un patrón de búsqueda. En Python, se utilizan para encontrar, reemplazar y manipular cadenas de texto
# mediante el módulo re

# Ejercicio 8 (Práctica): Escribe una expresión regular para validar direcciones de correo electrónico según las reglas estándar.
correos = "pop@gmail.com, pita.com, eric.rh@hotmail.com"
patron = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
validar = re.findall(patron, correos)
print(validar)

# Ejercicio 9: Escribe una expresión regular para encontrar todas las apariciones de una palabra específica en un texto, ignorando mayúsculas y minúsculas.
texto = "Python es increíble. Me gusta programar en python."
patron = r"\bpython\b"
resultados = re.findall(patron, texto, re.IGNORECASE)
print(resultados)

# Ejercicio 10: Escribe una expresión regular para validar números de teléfono en cualquier formato común (p. ej., (123) 456-7890, 123-456-7890, 123.456.7890, etc.).
telefonos = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890",
    "123 456 7890",
    "1234567890",
    "(123)-456-7890",
    "(+506) 61-04-56-50"
]

# patron = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
patron = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
for telefono in telefonos:
    if re.match(patron, telefono):
        print(f"{telefono} es válido.")
    else:
        print(f"{telefono} no es válido.")

# Ejercicio 11
# Escribe una expresión regular para encontrar todas las palabras que terminan con "ción" en un texto.
import re
patron = r"\b\w*ción\b" # explicacion de esta expresion:\b es un borde de palabra y \w* es cualquier palabra sin espacios.
string_cion = "una canción de una orquestacion se escucha en el concierto"
resultados = re.findall(patron, string_cion)
print(resultados)

# Ejercicio 12
# Escribe una expresión regular para validar códigos postales en formato 12345 o 12345-6789.
codigo_postal = "12345-6789", "12345"
patron = r"\b\d{5}(-\d{4})?\b" # explicacion de esta expresion:\b es un borde de palabra, \d{5} es cualquiera con 5 digitos y -\d{4} es un guion y cualquiera con 4 digitos
for cp in codigo_postal:
    if re.fullmatch(patron, cp):
        print(f"{cp} es válido")
    else:
        print(f"{cp} no es valido")

# Ejercicio 13
# Escribe una expresión regular para encontrar todas las palabras que contienen al menos una vocal.
vocales_en_palabras = "hola, como estas, que tal, estan bien"
patron = r"\b\w*[aeiou]\w*\b"
resultados = re.findall(patron, vocales_en_palabras)
print(resultados)

# Ejercicio 14
# Escribe una expresión regular para validar fechas en formato YYYY-MM-DD.
validar_fechas = "2023-01-01, 2023-02-28, 2023-04-30, 205-01-89"
patron = r"\b\d{4}-\d{2}-\d{2}\b" # \b es un borde de palabra, \d{4} es cualquiera con 4 digitos y -\d{2} es un guion y cualquiera con 2 digitos
resultados = re.findall(patron, validar_fechas)
print(resultados)

# Ejercicio 15
# Escribe una expresión regular para extraer todas las URL de un texto dado.
url_validas = "https://www.ejemplo.com", "https://otra.ejemplo.com", "http://www.otra22.com", "http://otra.1ejemplo."
patron = r"\bhttps?://\S+\.[A-Z|a-z]{2,7}\b" # \b es un borde de palabra, https?:// es cualquiera con https o http y \S+ es cualquiera sin espacios
patron1 = r"\bhttps?://[^\s/$.?#].[^\s]*\.[A-Za-z]{2,7}\b"
for url in url_validas:
    if re.findall(patron1, url):
        print(f"{url} es una URL valida")
    else:
        print(f"{url} no es una URL")

# Ejercicio 16
# Escribe una expresión regular para encontrar todas las palabras que tienen exactamente 5 letras.
palabras_con_5_letras = "hola, como estas, que tal las tareas, estan excelentes ?"
patron = r"\b\w{5}\b"
resultados = re.findall(patron, palabras_con_5_letras)
print(resultados)
###### mas de 5 letras
patron = r"\b\w{5,}\b"
resultados = re.findall(patron, palabras_con_5_letras)
print(resultados)

# Ejercicio 17
# Escribe una expresión regular para validar números decimales (con o sin signo).
numeros_decimales = "1.234", "12.345", "123.456", "1234.567", "12345.678", "123", "10"
patron = r"\b\d+\.\d+\b" # \b es un borde de palabra, \d+ es cualquiera con 1 o mas digitos y .\d+ es un punto y cualquiera con 1 o mas digitos
for num in numeros_decimales:
    if re.findall(patron, num):
        print(f"{num} es un número decimal")
    else:
        print(f"{num} no es un número decimal")

# Ejercicio 18
# Escribe una expresión regular para encontrar todas las ocurrencias de palabras que comienzan y terminan con la misma letra.
palabras = "Oro","rar", "Somos", "murcielago", "hola mundo", "otro"
patron = r"\b(\w)\w*\1\b" # \b es un borde de palabra, (\w): Captura la primera letra de la palabra, \w*: Coincide con cualquier número de caracteres de palabra (cero o más).
# \1: Captura la primera coincidencia, \b: Coincide con un borde de palabra.
for palabra in palabras:
    if re.findall(patron, palabra.lower()):
        print(f"Esta palabra: {palabra} empieza y termina con la misma letra.")
    else:
        print(f"Esta palabra: {palabra} no empieza y termina con la misma letra.")

# Ejercicio 19
# Escribe una expresión regular para validar un formato de fecha en español (DD de Mes de AAAA).
fecha_valida = "01 de Enero de 2023", "10 de Febrero de 2023", "31 de Marzo de 2023", "30/04/2023"
patron = r"\b\d{1,2} de (Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre) de \d{4}\b"
 # \b es un borde de palabra, \d{1,2} es cualquiera con 1 o 2 digitos y \d{4} es cualquiera con 4 digitos
for fecha in fecha_valida:
    if re.findall(patron, fecha):
        print(f"Esta fecha:{fecha} es valida")
    else:
        print(f"ESta fecha:{fecha} no es valida")

# Ejercicio 20
# Escribe una expresión regular para encontrar todas las combinaciones de letras mayúsculas en un texto.
mayusculas = "Este Texto Tiene ALGUNAS Letras MAYÚSCULAS."
patron = r"[A-Z]+"
resultados = re.findall(patron, mayusculas)
print(resultados)


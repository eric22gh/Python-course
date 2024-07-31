###### expresiones regulares; inpecionar si una cadena de texto tiene cosas.

import re 

texto = " hola eric, como esta.... este es mi profesor numero 1 _"
resultado = re.search("hola", texto) # encontrar palabras dentro del texto.
print(resultado)   

res = re.match("mi", texto)
print(res)

resultado1 = re.findall("hola", texto) # encontra todos los holas
print(resultado1)

#####buscar digitos numericos
resultado2 = re.findall(r"\d", texto) # encontra numeros en el texto
print(resultado2)

resultado3 = re.findall(r"\D", texto) # encontrar todo menos numeros
print(resultado3)

resultado4 = re.findall(r"\w", texto) # encontrar caracteres alfanumericos, python considera el _ como un alfanumerico
print(resultado4)

resultado5 = re.findall(r"\s", texto) # encontrar espacios, tabs, saltos de linea
print(resultado5)


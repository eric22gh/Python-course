##### strings
my_var = "edwards"
my_var2 = "ed"

print(len(my_var))
print(len(my_var2))
print(len(my_var + my_var2))

my_name = "eric\nhernandez\nedwards" # salto de linea al imprimir
print(my_name)

name, surname, age = "eric", "edwards", 30
print(" mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(" mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(" mi nombre es" " " + name + " " + surname + " " "y mi edad es" " " + str(age)) # son mejores las anteriores opciones xk es mas facil para el programa
print(f" mi nombre es {name} {surname} y mi edad es {age}") # la mejor

#### reverse
funciones = "hernandez"
print(funciones.capitalize())
print(funciones.upper())
print(funciones.count("h"))
print(funciones.isnumeric())
print("1".isnumeric())
print(funciones.lower())
print(funciones.lower().isupper())
print(funciones.startswith("nan"))

########## 
sourse = "gelboness"
sor = ("gelboness,hernandez")

print(dir(sourse)) # ver las cosas que puedo hacer, es una funcion de python

rest = sourse.upper()
rest1 = "gelboness".upper() # todo a mayuscula
rest1 = "gelboness".lower() # todo a minuscula
rest1 = "gelboness".capitalize() # primera letra a mayuscula
rest1 = sourse.find("b") # buscar algo, los espacios tambien se cuentan
rest1 = sourse.index("s") # buscar algo igual q find pero la diferencia es que si index no encuentra la letra nos da error
rest1 = sourse.isnumeric() # si hay un numerio en la cadena nos da true
rest1 = sourse.isalpha() # letras de la a la x sin espacios, sin caracteres especiales, sin numeros
rest1 = sourse.count("s") # cuantas veces sale esta letra o palabra en el strings
rest10 = len(sourse) # cuantos caracteres hay en una cadena
rest1 = sourse.startswith("gel") # si la cadena empieza con el parametro q le pasamos, devuelve true
rest1 = sourse.endswith("ss") # si la cadena termina  con el parametro q le pasamos 
rest1 = sourse.replace("gel","gael") # si encuentra una parte de la cadena que digas, la reemplaza por otra que quieras
rest11 = sor.split(",") # se parar cadenas con el parametro que le pasemos y las combierte en una lista 

print(type(rest11))
print(rest11[1])
print(rest10)









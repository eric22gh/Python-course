#tipos de datos:
# listas [] conjunto de datos, son mutables
# tuplas () conjunto de valores, son inmutables, no se pueden cambiar
# sets {}  son una lista pero son inmutables, estructura fija de valores, no es ordenado, admite repetidos, no hay indice
# diccionario {"x": 25} # se accede al dato por medio de la llave

my = set()
my_othe = {}
print(type(my_othe))
my_othe = {"eric", "edwards", 30} # se declara como un diccionario, pero apenas tengo datos cambia a set x la forma de introducir datos
print(type(my_othe))
print(type(my))
print(len(my_othe)) # con tar cuantosdatos hay hay una 

my_othe.add("hernandez")
print(my_othe)

print("eric" in my_othe)
print("er" in my_othe) # comprobar si un dato esta en el set


# covertir un set en una lista

my_set = {"eric", "edwards", 30}
my_list = list(my_set)
print(my_list[1])
print(my_list)
print(type(my_list))

############### sets son elementos no son ordenados pero pueden cambiar, admite repeditos

lost_set = {"dalto", "soy eric", 36, True, 36} # solo va a dar una vez 36 porque no admite duplicado,
# se usa en python para eliminar datos duplicados, de lista a set y de set a list
print(lost_set)
# lost_set[0] = "eric" # da error porque son inmutables
print(lost_set)



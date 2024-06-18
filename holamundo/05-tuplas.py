#tipos de datos:
# listas [] conjunto de datos, son mutables
# tuplas () conjunto de valores, son inmutables, no se pueden cambiar
# sets {} 
# diccionario {"x": 25} # se accede al dato por medio de la llave

####### tuplas {}
my_tuples = ()
# o
my_oyher_yuple = tuple()
my_oyher_yuple = (22.5, "hernandez")

my_tuples = (30, "nehro", 56, "edwards", "edwards")
print(type(my_tuples))
print(my_tuples[0])

print(my_tuples.count("nehro")) # cuantas veces esta esto en la tupla
print(my_tuples.count("edwards"))
print(my_tuples.index(56)) # en que posicion esta en la tupla

#### da error por son inmutables, se quedan con el valor dado la primera vez
# my_tuples[1] = "eric"
# print(my_tuples)

print(my_tuples + my_oyher_yuple)
# o
tuple = my_tuples + my_oyher_yuple
print(tuple)

#### convertir una tupla inmutable en una lista mutable

my_tup = (30, "nehro", 56, "edwards", "edwards")
print(type(my_tup))
my_eric = list(my_tup) # se declara una variable para cambiar la tuplan a lista
print(my_eric)
print(type(my_eric))
print(type(my_tup))

my_eric[4] = "eric"
my_eric.insert(2, 22) # añadir a la lista
print(my_eric)

# my_eric = tuple(my_tup) # convertir la lista en tupla
# print(type(my_eric))
del my_tup # la elimina momentaneamente del codigo, no como el clear que lo borra de una vez

######## la tupla no puede modificar recordar

lost_tuple = ("dalto", "soy eric", 36, True, 55, 10.5) 
print(lost_tuple[1])

# lost_tuple[2] = 22 va a dar error porque son inmutables
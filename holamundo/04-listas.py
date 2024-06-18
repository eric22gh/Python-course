####  estructuras de datos: listas es un conjunto de datos, son mutables
#tipos de datos:
# listas [] conjunto de datos
# tuplas () conjunto de valores, son inmutables, no se pueden cambiar
# sets {} 
# diccionario {"x": 25} # se accede al dato por medio de la llave

my_list = []
my_lost = [30, 1.75, "eric", "edawrds"]
print(len(my_list))
my_list = [12, 35, 65, 98, 23, 10]
print(my_list)
print(len(my_list)) # 6 elementos
print(my_lost)
print(type(my_lost))

print(my_lost[-1])
print(my_lost[1])
print(my_lost[-2])
print(my_lost[2])
print(my_lost.count("eric")) # contar elementos dentro de la propia lista
age, altura, name, surname = my_lost
print(name) # desempaquetar una lista
print(age)
print(my_lost + my_list) # suma el contenido
#print(my_lost - my_list) 

my_Lis = [] # lista
my_Lis = "edwards" # ahora es una variables

my_list.append("edwards") # añade elementos al final
my_list.insert(0, "alex") # insertar algo en la lista en la posicion que dice el numero
my_list.remove(98) # eliminar algo en la lista
del my_list[2] # otra formar de elimina x indice, directanmente el numero o objeto sin verlo
my_list.pop() # quita el ultimo elemenmto de la lista
my_list.pop(2) # quita el elemento 2 de la lista
print(my_list.pop(2))
print(my_list)
my_list.clear() # limpiar toda la lista
my_eric = my_lost.copy() # hacer una variable y copiarle los datos de una lista
print(type(my_eric))
print(my_list) # esta vacia x el clear que le dimos arriba
print(my_eric)
my_eric.reverse() # poner alrevez la lista
# my_eric.sort() # ordena la lista, no ordena ni floats y str
print(my_eric)

##### como hacer sublistas
print(my_eric[1:3]) # da los datos que estan en medio de la posicion de esos numeros
#####################

lost = ["dalto", "soy eric", 36, True] # estoy es un array
print(lost)
print(lost[2])
print(lost[3])
print(lost[0])

lost[2] = 22
print(lost)



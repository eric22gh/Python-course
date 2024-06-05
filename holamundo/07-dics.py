#tipos de datos:
# listas [] conjunto de datos, son mutables
# tuplas () conjunto de valores, son inmutables, no se pueden cambiar
# sets {}  son una lista pero son inmutables, estructura fija de valores, no es ordenado, admite repetidos, no hay indice
# diccionario {"x": 25} # se accede al dato por medio de la llave

#####diccionarios 

my_dict = dict()
my_other = {1, 1, "eric"}
print(my_other) # no acepta duplicados set, es {} igual a dic, pero cuando tiene codigo dentro del parentecis se convierte en set
print(type(my_dict))
print(type(my_other))

my_pop = {"nombre":"eric", "edad":30, "apellido":"edwards", "nick":"memin", 1.2:"python"} # diccionario "x":"y"
print(my_pop)
print(type(my_pop))

my_po = {"nombre":"eric", 
        "edad":30, 
        "apellido":"edwards",
        "nick":"memin", 
        "lenguaje":{"python","GO", "JAVA", "django"}
           
} # diccionario "x":"y"
print(my_po)
print(my_po["apellido"]) # se puede imprimir lo que hay en ese campo

#### actualizar
print(my_po["edad"])
my_po["edad"] = 31
print(my_po["edad"])
print(my_po)

###agregar un nuevo campo
print(my_po)
my_po["calle"] = "calle edwrads"
print(my_po)

del my_po["lenguaje"] # solo de esta forma se puede eliminar
print(my_po)

print("edad" in my_po) # el busca por clave y por valor

print(my_po.items()) # listados de todo
print(my_po.keys()) # listado de todos las claves
print(my_po.values()) # listado de los valores
#crear una nueva tabla con un solo valor de otra tabla
my_rop = my_po.fromkeys(("edad",31))
print(my_rop)


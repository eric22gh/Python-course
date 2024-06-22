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
#######################
j_son = {
    "nombre" : "eric",
    "name" : "edwards",
    "edad" : 30,
    "ciudad" : "limom",
    "estado": "soltero"

}
print(j_son)
print(j_son["nombre"])

j_son["edad"] = 55
j_son["edad"] += 2

print(j_son)

####### metodos

Bone = {
    "name" : "eric",
    "surname" : "perez",
    "age" : 30,
    "apodo" : "memim",
    "lenguaje" : {"patua", "español", "ingles"}
}

claves = Bone.items() # da los indices con su valor, con ese metodo se puede iterar este dic, con print(bone) da lo mismo pero no se puede iterar
print(claves)

Bone.get("name") # da el valor de ese indice

op = Bone.keys() # nos da los indices
print(op)

Bone.pop("name", "age") # borra elementos del dic x medio del indice

eric = Bone.fromkeys("surname", "alex")

print(eric)
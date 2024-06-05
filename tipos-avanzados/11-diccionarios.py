###### diccionarios; coleccion de datos q se encuentran agrupados por una llave y un valor age = 29
# como llave solo acepta strings y valor puede ser cualquier cosa
#tipos de datos:
# listas []
# tuplas ()
# sets {} 
# diccionario {"x": 25} # se accede al dato por medio de la llave

dic = {"x": 25, "y": 30}
print(dic)
print(dic["y"])
dic["z"] = 45
print(dic)

print(dic.get("z"))
del dic["y"] # para eliminar un dato del diccionario

###### si no se los valores de los dicionarios
for valor in dic:
    print(valor, dic[valor])

##### oo

# for llave, valor in dic.items:
#     print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "eric"},
    {"id": 2, "nombre": "carlos"},
    {"id": 3, "nombre": "pop"},
    {"id": 4, "nombre": "alex"}
]

# print(usuarios)
for user in usuarios:
    print(user["nombre"])
#print(user)
mascotas = ["pulgas", "perros", "sapo","eric", "chancho", "eric"] # el string eric no estaba ateriormente

print(mascotas.index("sapo"))
# print(mascotas.index("eric"))  si no esta da error
# para que no de error hay que buscarlo con if
if "eric" in mascotas:
    print(mascotas.index("eric"))
else:
    print("palabra no encontrada")

# encontrar cuantas veces esta ese string dentro de esa lista

print(mascotas.count("eric"))

#tipos de datos:
# listas []
# tuplas ()
# diccionario {} 
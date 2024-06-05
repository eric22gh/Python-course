######
#tipos de datos:
# listas []
# tuplas ()
# sets {} 
# diccionario {"x": 25} # se accede al dato por medio de la llave
lista = [1, 2, 3, 4]
print(*lista)
print(1, 2, 3, 4)
lista2 = [5, 6, 7]
combinada = [*lista, *lista2 ]
print(combinada)
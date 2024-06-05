#tipos de datos:
# listas []
# tuplas ()
# diccionario {} 

# ordenando
num = [55, 1000, 5, 6, 10, 3, 4, 8, 1, 2, 8, 22]
print(num)
num.sort() # ORDENARLOS
print(num)
num.sort(reverse=True) # PONERLOS ALRVEZ
num2 = sorted(num) #este igual ordena pero el anterior ordena la misma lista, este en cambio crea otra lista con los mismo datos pero ordenada
print(num)
print(num2)

# ordenar listas dentro de listas
user = [[4, "perro"], [1, "edawrds"], [5, "perros"]]
user.sort()
print(user)
############### ordenar x como nosotros queramos
user2 = [["perro", 4], ["edawrds", 1], ["perros", 5]]
print(user2)
def odernar(user2):
    return user2[1]
user2.sort(key=odernar)
user2.sort(key=odernar, reverse=True) # opcion de ordenado al revez #1
print(user2)

user2.sort(key=lambda el: el[1], reverse=True) # opcion de ordenado al revez #2
print(user2)

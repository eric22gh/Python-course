#### son lo mismo que las listas, pero los elementos no se pueden modificar
#tipos de datos:
# listas []
# tuplas ()
# diccionario {} 
numeros = (1, 2, 3) + (5, 6, 8)
print(numeros)
# covertir una lista en tuola
point = tuple([1, 3])
print(point)
points = numeros[:2]
print(points)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

#numeros[0] = 5

## como modificar una tupla, aunq no se dbe de hacer, por sola las listas se modifican
list = list(numeros)
list[0] = "edwards"
print(list)
# se hizo una lista embase a una tupla
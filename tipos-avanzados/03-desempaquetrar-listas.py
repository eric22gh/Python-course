num = [1, 2, 3, 4, 5, 6, 7]

# lo siguiente no se hace  
# primero = num[1]
# sehundo = num[2]
# tercero = num[3]

primero, segundo, tercero, cuarto, quinto, sexto, septimo = num
print(primero, segundo, tercero)
print(tercero)
#####
num = [1, 2, 3, 4, 5, 6, 7]
primero, *otros, ultimo = num
print(primero, otros)
print(primero, otros, ultimo)


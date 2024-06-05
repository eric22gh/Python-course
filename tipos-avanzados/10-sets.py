#### set: grupo o conjunto, no se pueden repetir y tampoco estan ordenados
#tipos de datos:
# listas []
# tuplas ()
# sets {} 
# diccionario 

primer = {1, 1, 2, 2, 5, 89, 9, 100}
primer.add(22)
primer.remove(1)
print(primer) # no me va tirar los numeros repetidos
second = [1, 2, 3]
#######
sec = set(second) # transformar una lista en un set
print(sec)
print(sec | primer ) # este operador | se llama union, igual no va a imprimir los numeros duplicados
print(sec & primer ) # este operador se llama intersepcion, devuelve los elementos q este en los 2 sets
print(sec - primer ) # este operador se llama diferencia, quita los elementos q estan en los 2 sets, se los quita al set 1
print(sec ^ primer ) # este operador se llama diferencia simetrica, compara y quita los elementos duplicados con los q se encuentra y solo deja los no duplicados
if 2 in second:
    print(" hola, encontre el numero")
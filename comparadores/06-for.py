## bucle for; iterar una lista de elementos,
## sirven para buscar elementos, operaciones matematicas
## range ()

# for numero in range(10): # da una lista de numeros en consolo, inicia desde el 0
# # numero va a tomar el valor de cada uno de esos numeros en esa lista
#     print(numero * 2) # imprime los numeros de la lista 
#     break
 
num1 = 22

for numero in range(11): 
    print(numero)
    if numero == num1:
        print("detente encontre el numero", num1)
        break
else:
    print("no encontre el numero")

#########
eric = 500
for number in range(600):
    print(number)
    if number == eric:
        print("encontre la plata")
else:
    print("no encontre el numero")


### iterables ##### range () es un iterable

for ric in "Eric Hernandez":
    print("ric")

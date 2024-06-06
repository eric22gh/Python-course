#### loops o for; no sirve para iterar(pasar por el mismo codigo varias veces)


#### while
my = 0
while my <= 10:
    print(my) ## va a imprimir 0 infinitas veces
    my += 2 # ingrementar el valor de my, asi tambien se sacan numeros pares
    if my == 6:
        print("este es el numero que esta buscando el:",my,)
else:
    print(" mi condicion es mayor que 10")
print("se termino el bucle")

eric = 0
while eric <= 15:
    print(eric)
    eric += 1
    if eric == 11:
        print("este es el numero que esta buscando el:",eric,)
        break
    print("la ejecucion sigue")


##### bucle for nos sirve para iterar un grupo de elementos y se va a iterar la misma cantidad de elemteos q tenga la lista

my_list = [12, 35, 65, 98, 23, 10]

for ele in my_list:
    print(ele)
        

my_tuples = (30, "nehro", 56, "edwards", "edwards")
for tup in my_tuples:
    print(tup)

my_othe = {"eric", "edwards", 30} # se declara como un diccionario, pero apenas tengo datos cambia a set x la forma de introducir datos
for top in my_othe:
    print(top)

my_pop = {"nombre":"eric", "edad":30, "apellido":"edwards", "nick":"memin", 1.2:"python"} # diccionario "x":"y"
for nam in my_pop:
    print(nam)
    if nam == "edad":
        print("encontre la edad")
        break
else:
    print("terminado")


for nam in my_pop.values():
    print(nam)
else:
    print("se detuvo la ejecucion")
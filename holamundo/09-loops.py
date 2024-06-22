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


# un bucle q crea una variable que cada vez que da vuelta va a varle el valor de esa variable

animales = ["perro", "gato", "sapo", "tigre", "culebra"]
number = [55, 55, 10, 6, 7]

for animal in animales:
    print(f"Ahora la variable animal es: {animal}")

for num in number:
    print(num * 10)

# iterar 2 listas, tienen que tener los mismos elementos
for animal,num in zip(animales,number):
    print(f"objetos de la lista {animal}")
    print(f"objetos de la lista {num}")

### recorer una lista
for nom in enumerate(number):
    indice = nom[0]
    valor = nom[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    #print(nom) # devuelve el indice y valor


#### recorrer dicionarios

Bone = {
    "name" : "eric",
    "surname" : "perez",
    "age" : 30,
    "apodo" : "memim",
    "lenguaje" : {"patua", "español", "ingles"}
}

for key in Bone:
    print(key) # solo da el indice
    
for key in Bone.items(): # asi da indice y valor
    idice = key[0]
    valor = key[1]
    print(f"el indice es: {idice} y el valor es: {valor}")
    #print(key) 

frutas = ["banao", "mango", "papaya", "sandia", "melon", "pipa", "pera"]

for frut in frutas:
    if frut == "pipa":
        continue # se salta pipa
    print(f"me voy a comer una {frut}")


for frut in frutas:
    print(f"me voy a comer una {frut}")
    if frut == "mango":
        break
print(f"nme duele la panza por comer {frut} ya no voy a comer mas")

numeros = [5, 10, 5, 6]
numeros_dupli = [x*2 for x in numeros]
print(numeros_dupli)
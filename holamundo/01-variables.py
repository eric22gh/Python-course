###### variables 
my_var = "Terraform"
#my_var2 = "Terraform" + 2 # da error no se puede sumar 
my_var2 = "Terraform" * 2 # este si se puede
my_int = 22
my_int2 = 22 - 8
my_bool = True
my_float = 2.5
my_com = 3 + 5j 
eric = my_bool
print(my_com)
print(my_int2)
print(my_var)
print(my_var, my_bool, my_float) # concatenar variables
print(eric)
#### covertir
print(type(my_int))
my_eric = str(my_int)
print(type(my_eric))
#print(type(my_var, my_bool, my_float)) # da error

###### funciones del sistema
print(len(my_var)) # len cuenta cuantas letras tiene la var

#### varaibles en una sola linea
name, age, apellido, alias = "eric", 30, "edwards", "negro"
print(alias)
print(age)
print("Mi nombre es:", name, "Mi apellido es:", apellido, "Tengo", age, "años", "y mi alias es:", alias)
#### inputs
firts_name = input(" cual es tu nombre:")
años = input(" cual es tu edad:")
print("Tu nombre es:", firts_name)
print("Tienes una edad de:", años,"años")


lista = [22, "eric", "hernandez"] # desempaquetar listas o tuplas
edad, nombre, surname = lista
print(surname)
print(edad)
print(nombre)

## otra forma de hacer tuplas 

tupla = "dato1", "dato2"
tupla = "dato1", # con un solo dato


print(type(tupla))

########### conjuntos dentro de otro conjunto
conjunto1 = frozenset(["dato3", "dato4"])
conjunto2  = {conjunto1, "dato5"}
print(conjunto2)

rop = conjunto2.issubset(conjunto1) # si conjunto1 esta en conjunto2
print(rop)





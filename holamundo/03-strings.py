##### strings
my_var = "edwards"
my_var2 = "ed"

print(len(my_var))
print(len(my_var2))
print(len(my_var + my_var2))

my_name = "eric\nhernandez\nedwards" # salto de linea al imprimir
print(my_name)

name, surname, age = "eric", "edwards", 30
print(" mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(" mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(" mi nombre es" " " + name + " " + surname + " " "y mi edad es" " " + str(age)) # son mejores las anteriores opciones xk es mas facil para el programa
print(f" mi nombre es {name} {surname} y mi edad es {age}") # la mejor

#### reverse
funciones = "hernandez"
print(funciones.capitalize())
print(funciones.upper())
print(funciones.count("h"))
print(funciones.isnumeric())
print("1".isnumeric())
print(funciones.lower())
print(funciones.lower().isupper())
print(funciones.startswith("nan"))







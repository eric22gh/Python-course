##### operadores
# operadores aritmeticos
print(3+8)
print(3-8)
print(3/8) # siempre nos devuelve un float
print(3//8) # nos devuelve un int, da un datos pero lo redondea hacia abajo y asi es un int: division baja
print(3*8)
print(3**8) 
print(3%8) # modulo: para saber si n¿hay un multiplo, devuelve el resto, lo que sobra de la division

print("hola" + "eric")
print("hola" + str(5))
print("hola" * 5)
print("hola" * (2 + 5))
#print("hola" * 5.5) # da error porque es un float
my_t = 5.5
print(type(my_t))
print("edwards" * int(my_t))

######### operadores comparativos, nos devuelven true o false ##########

print(3 > 5) # mayor que
print(3 < 5) # menor que
print(3 == 5) # igual a
print(3 != 5) # distinto
print(3 >= 5) # mayor igual
print(3 <= 5) # menor igual
print(3 < 5 == 5)
##### comprueba con la ordenacion alfabetica
print("hola" > "zython") 
print("hola" < "python") 
print("hola" == "hola") 
print("hola" != "hola") 
print("hola" >= "python") 
print("hola" <= "python") 

########## operadores logicos

print(3 > 5  and "hola" > "zython" ) # si las 2 se cumplen &
print(3 > 5  or "hola" > "zython" ) # si una se cumple nos devuelve verdadero | , cuando las 2 son iguales nos de false, si hay 2 false o true
print(not(3 > 5)) # negando la operacion
print(not(2 > 10)) # va a dar true















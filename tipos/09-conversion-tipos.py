##### conversion de tipos ##### 

x = input("") 
# int () trasformar un dato a integer
# str () trasformar un dato a string
# float () trasformar un dato a float
# bool () trasformar un dato a boolean, este podria tener problemas: porque todo lo pasa a true o false
# truthy y falsy: para un tipo de dato(falsy: ""/ 0 / none) devuelve false
print(bool(""))
print(bool(0))
print(bool(None))
print(bool("0"))
print(bool(" "))
#####
x = str(7)
y = 7

#print(8 + x) # da error porque x es un string
print(8 + y) # aqui no da error porque  Y tiene de valor un integer
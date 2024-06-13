##### exception handling #######
# si el programa da un error y nosotros no hacemos nada con ese error, la app muere
num1, num2, num3 = 10, 56, "100"

print(num1 + num2)
#print(num1 + num3) # error 


#print(5 + "10") # python no puede sumar un integer con string

try:
    print(num1 + num3) # cuando da error salta a except
    print("todo bien")
except:
    print("se ha profucido un error")

# with else

try:
    print(num1 + num2) 
    print("todo bien")
except:
    print("se ha profucido un error")
else:
    print("la ejecucion continua")

###### with finally


try:
    print(num1 + num2) 
    print("todo bien")
except:
    print("se ha profucido un error")
else: # else y finally son opcionales
    print("la ejecucion continua")
finally: # se ejecuta siempre pase lo que pase
    print("la ejecucion sigue")

###### ecepciones por tipo

try:
    print(num1 + num3) # cuando da error salta a except
    print("todo bien")
except ValueError as error : # solo capture errores value, ponerle el resultado de error a una variable
    print("se ha producido un valuerror")
    print(error) # es una variable local  
except TypeError: 
    print("se ha producido un typerror")
except Exception as ex: 
    print(ex)
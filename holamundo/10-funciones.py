### funciones 

def my_func ():
    print("esto es una funcion")
    #my_func () # si lo dejo se hace un bucle infinito

my_func () # llamar a la funcion
my_func () 
my_func () 

#my_func("hola eric" + (my_func))

def sum (a: int, b: int):
    print(a + b)
sum("10","123")
sum(10,12)
sum(1.2,22.5)

def suma (a: int, b: int):
    return a + b
suma(55, 56)

eric = suma(55, 56)
print(eric)

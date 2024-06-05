# imprimir una variable con print fuera de una funcion no se puede, nos va a dar error porque una funcion solo tiene alcance dentro de ella
# siempre hay que definir una variable antes de llamarla
saludo = "hola peru" # variable global, es una mala practica usarlas, es mejor usarlas dentro de funciones, por que
# si el dia de mañana tenemos un error con una variable tendriamos que buscar en todo el codigo.
def hello():
    saludo = "hola eric"
    print(saludo)


def hola ():
    saludo = "hola edwards"
    print(saludo)

def hell():
    global saludo # aqui aque este dentro de una funcion, le estamos indicando que es la var global, es la manera correta
    print(saludo)

hola()
hello()
print(saludo) # aqui imprime hola peru porque el saludo de las funciones solo tiene dominio dentro de las funciones
hell()
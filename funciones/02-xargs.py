#####XARGS pasarles multiples argumentos
def suma (a, b, c):
    print(a+b+c)

suma(3, 6, 10)
#suma(30, 52, 10, 6, 52, 10) # esto da error ´porque solo puede sumar 3 numeros
##### una manera es
def sum (*numeros): # va a sumas todos los numeros del parametro numeros
    resultado = 0 # estamos declarando una variable q vale 0, va a guadar la suma que encuentre en numeros
    for numero in numeros: # numero es una var temporal q guarda lo que encontro en numeros
        resultado += numero # suma el valor de numero a resultado y luego guarda el nuevo valor en resultado.
    print(resultado)
sum(3, 6, 10)
sum(30, 52, 10, 6, 52, 10)


##### practice

def multiply (*numeros):
    resultado = 1 # porque ningun numero se puede multiplicar x cero
    for numero in numeros:
        resultado *= numero
    print(resultado)
multiply(3, 6, 10)
multiply(30, 52, 10, 6, 52, 10)

# operadores de asignación compuesta son útiles porque hacen que el código sea más conciso y a menudo más fácil de leer.
#+= (Suma y asignación):
x = 5
x += 3  # Ahora x es 8 (5 + 3)
#-= (Resta y asignación):
x = 5
x -= 3  # Ahora x es 2 (5 - 3)
# *= (Multiplicación y asignación):
x = 5
x *= 3  # Ahora x es 15 (5 * 3)
# /= (División y asignación):
x = 5
x /= 2  # Ahora x es 2.5 (5 / 2)
#%= (Módulo y asignación):
x = 5
x %= 3  # Ahora x es 2 (5 % 3)
# **= (Exponenciación y asignación)
x = 5
x **= 3  # Ahora x es 125 (5 ** 3)

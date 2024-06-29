### funciones 

def my_func ():
    print("esto es una funcion")
    #my_func () # si lo dejo se hace un bucle infinito

my_func () # llamar a la funcion
#my_func("hola eric" + (my_func))

def sum_d(a: int, b: int):
    print(a + b)
sum_d(10,12)
sum_d(1.2,22.5)

def suma (a: int, b: int):
    return a + b
suma(55, 56)

eric = suma(55, 56)
print(eric)

def s(*numeros): # suma todos los parametros
    return sum(numeros)
resul = s(1, 55, 5, 65, 89, 100)
print(resul)

def hello(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "caballero"
    else:
        adjetivo = "amor"
    print(f"mi nombre es: {nombre}, hola {adjetivo}")
hello("eric","hombre")
hello("lucia","mujer")
hello("alex","nose")

########################################
import random # para seleccionar caracteres aleatorios.
import string # para acceder a conjuntos de caracteres como letras y dígitos.

def generar_contrasena(longitud):
    # Definir los caracteres que se pueden utilizar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar una contraseña aleatoria utilizando los caracteres definidos
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    return contrasena

longitud_deseada = 10
contrasena_generada = generar_contrasena(longitud_deseada)
print(f"Contraseña generada: {contrasena_generada}")

 ################## funciones build-in(por defecto en python)

numeros = [1, 55, 5, 65, 89, 100]

numero_alto = max(numeros)
print(numero_alto)

numero_bajo = min(numeros)
print(numero_bajo)

num = round(12.3656,0) # redondear un numero, despues de la coma poner el numero de decimales que imprime en la consola.
print(num)

bool = bool(1.2) #  devuelve false: 0, vacio,false y none /// true: number disto de 0, true, string, datos no vacios
print(bool)

all = all([1, False, "JNKJFD", True]) # comprueba false o true en toda una lista
print(all)

numer = [1, 55, 5, 65, 89, 100]
sumas = sum(numer)  # suma todos los valores
print(sumas)

################ funciones lambda: crea funciones anonimas

multi_plicar = lambda x : x * 2
print(multi_plicar(5))

numeros1 = [1, 2, 6, 8, 16, 24, 55]
numeros_pares = filter(lambda numero:numero%2 == 0, numeros1) # numeros pares con funciones lambda, filter ejecuta cada valor de un iterable(lista)
print(list(numeros_pares))

### lista de compañeros en una lista
def obtener_compa(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero: ")
        edad = input("ingrese la edad del compañero: ")
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[0])
    return compañeros
compa = obtener_compa(cantidad=2)
print(compa)

####### mostrar la serie de fibonacci del 0 a un numero
def fibonacci(num):
    a,b = 0,1
    fibo_lista = []
    for i in range(num):
        if b > num: return fibo_lista
        else: 
            fibo_lista.append(b)
            a,b = b,a+b # clave de fibonacci
    
resultado = fibonacci(20)
print(resultado)
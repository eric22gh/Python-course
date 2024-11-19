# Día 30: Estructuras de control (if, for, while)
# Teoría:
# Las estructuras de control permiten tomar decisiones en el código. La instrucción if se usa para ejecutar bloques de código condicionalmente. 
# Los bucles for y while permiten iterar sobre colecciones o ejecutar un bloque de código repetidamente.

# Ejemplos:
# Sistema de Recomendación:
productos = ['Laptop', 'Teléfono', 'Tablet', 'Auriculares']
presupuesto = 500
for producto in productos:
    if producto == 'Laptop':
        precio = 800
    elif producto == 'Teléfono':
        precio = 300
    elif producto == 'Tablet':
        precio = 400
    else:
        precio = 150

    if precio <= presupuesto:
      print(f'Puedes comprar: {producto}')

# Contador de Números:
# Contar hasta un número ingresado
numero = int(input("Ingresa un número: "))
contador = 1
while contador <= numero:
    print(contador)
    contador += 1

# Juego de Adivinanza:
# import random
# numero_secreto = random.randint(1, 1000)
# intento = 0
# while intento != numero_secreto:
#     intento = int(input("Adivina el número entre 1 y 100: "))
#     if intento < numero_secreto:
#         print("Demasiado bajo!")
#     elif intento > numero_secreto:
#         print("Demasiado alto!")
#     else:
#         print("¡Correcto!")

# Tips y Buenas Prácticas:
# Utiliza elif para manejar múltiples condiciones en lugar de anidar múltiples if.
# Usa bucles for cuando conozcas de antemano cuántas veces necesitas iterar.
# Asegúrate de que las condiciones en tus estructuras de control sean claras y fáciles de entender.

# Ejercicios:
# 1- Escribe un programa que verifique si un número es positivo, negativo o cero.
try:
    number = 0
    if isinstance(number, (int, float)): # verifica si es int o float
        if number < 0:
            print(f"El numero: {number} es negativo")
        elif number == 0:
            print(f"El numero: {number} es igual a 0")
        else:
            print(f"El numero: {number} es positivo")
except Exception as n:
    print(f"{n} tipo de dato incorrecto")

# 2- Crea un bucle for que imprima los números del 1 al 10.
for n in range(11):
    print(n)

# 3- Escribe un programa que use un bucle while para contar hasta 5.
counter = 0
while counter <= 5:
    print(counter)
    counter += 1

# 4- Crea un programa que imprima los números pares del 1 al 20.
num = 1
while num <= 20:
    if num % 2 == 0:
        print(f"{num} es un numero par")
    num += 1

# 5- Escribe un programa que sume todos los números en una lista.
lista_numeros = sum([n for n in range(1, 50)])
print(f"La suma de los numeros de la lista es: {lista_numeros}")

# 6- Crea un programa que imprima la tabla de multiplicar de un número ingresado.
def tabla_multiplicar(n):
    if n == 0 :
        print("no se multiplica por 0")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

    try:
        dato = tabla_multiplicar(int(input("ingrese la tabla de el numero que quiera: ")))
    except ValueError as j:
        print(f"dato no valido: {j}")

# 7- Escribe un programa que encuentre todos los divisores de un número dado.
def divisores(n):
    lista = []
    for i in range(1, n):
        if n % i == 0: # no es lo mismo i % n que n % i
            lista.append(i)
    return lista
dato = divisores(15)
print(dato)

# 8- Crea un programa que imprima el factorial de un número usando un bucle.
def factorial(n):
    if n == 0:
        return "El numero tiene que ser mayor que 0."
    resultado = 1
    for o in range(1, n + 1):
        resultado *= o
    return resultado
dato = factorial(5)
print(dato)

# 9- Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz".
for numeros in range(1, 101):
    if numeros % 3 == 0 and numeros % 5 == 0:
        print(f"El numero: {numeros} a sido reemplazado por: FizzBuzz")
    elif numeros % 3 == 0:
        print(f"El numero: {numeros} a sido reemplazado por: Fizz")
    elif numeros % 5 == 0:
        print(f"El numero: {numeros} a sido reemplazado por: Buzz")
    else:
        print(numeros)

# 10- Crea un programa que calcule la suma de los dígitos de un número.
nu = 568
digito = str(nu)
sumar = 0
for d in digito:
    sumar += int(d)
print(f"La suma de los digitos:{nu}, es: {sumar}")   

# 11- Escribe un programa que determine si un número es primo.
# un número es primo, necesitas verificar si es divisible por cualquier número entre 2 y la raíz cuadrada del número.
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 7
if es_primo(number):
    print(f"{number} es un número primo.")
else:
    print(f"{number} no es un número primo.")

# 12- Crea un programa que imprima la secuencia de Collatz para un número dado.
# La secuencia de Collatz es una serie de números que empiezas a generar con cualquier número positivo, 
# si el número es par, se divide entre 2, y si es impar, se multiplica por 3 y se suma 1.
def collatz(n):
    while n != 1: # cuando llega a uno se detiene
        print(n, end=" -> ") #end= lo que va a ir al final de cada operacion o iteracion
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
dato = collatz(6)

# 13- Escribe un programa que solicite al usuario un número y encuentre el número más cercano en una lista.
# La función abs() devuelve el valor absoluto de un número: es su distancia desde el cero en la recta numérica.
numero_1 = 52
lista_1 = [22, 0, 56, 45, 23, 69]
cercano = min(lista_1, key= lambda x : abs(x - numero_1)) # en este caso la recta numerica es numero_1
print(f"El numero de la lista mas cercano a: {numero_1}, es: {cercano}")

# 14- Crea un programa que imprima los primeros 10 números de la serie Fibonacci.
def fibonacci(n):
    a = 0
    b = 1
    lis = []
    for x in range(n):
        lis.append(a)
        a, b = b, b + a
    return lis
dato = fibonacci(10)
print(dato)

# 15- Escribe un programa que imprima los elementos de una lista que son mayores que un número dado.
import random
lista_elementos = [random.randint(1, 50)for i in range(5)]
numero_dado = 25
mayores = [x for x in lista_elementos if x > numero_dado]
print(mayores)

##### anagrama; 2 palabras son anagramas cuando tienen significado distinto, pero tienen las mismas letras
def anagrama(word1, word2):
    try:
        import re
        word_1 = re.sub(r"[ ,;.:]","", word1.lower())
        word_2 = re.sub(r"[,;.:]","", word2.lower())
        frase1 = list(sorted(word_1))
        frase2 = list(sorted(word_2))
        if frase1 == frase2:
            return F"Las 2 palabras:{word1} y {word2} son anagramas"
        else:
            return F"Las 2 palabras:{word1} y {word2} no son anagramas"
    except (ValueError, TypeError) as e:
        return f"ERROR: {e}"

dato = anagrama("iman", "mani")
print(dato)
### palindromo: una palabra es palindorma cuando se lee igual al derecho y al revez
def palindromo(word):
    try:
        import re
        word_1 = re.sub(r"[ ,;.:]","", word)
        word_2 = word[::-1]
        if word_1 == word_2:
            return "Esta palabra o frase, si es palindroma"
        else:
            return "Esta palabra o frase, no es palindroma"
    except (ValueError, TypeError) as r:
        return f"Error: {r}"
    
dato = palindromo("amor")
print(dato)

# Mini Proyectos:
# Desarrolla un programa que simule un sistema de votación.
# El programa debe solicitar al usuario que ingrese el nombre de un candidato y luego mostrar el total de votos para ese candidato.
import re
class Votacion:
    def __init__(self):
        self.candidatos = {}
    def votar(self, candidato):
        try:
            if candidato in self.candidatos:
                self.candidatos[candidato] += 1
                print(f"Gracias por su voto hacia: {candidato}")
            else:
                self.candidatos[candidato] = 1
                print(f"Gracias por su voto hacia: {candidato}")
        except (ValueError, TypeError) as e:
            print(f"ERROR: {e}")
    def mostrar_resultados(self):
        for candidato, votos in self.candidatos.items():
            print(f"{candidato}: {votos} votos")

votacion = Votacion()
while True:
    print("\n Menu de Sistema de Votación\n"
          "1- Votar\n"
          "2- Resultados\n"
          "3- Salir\n"
          )
    menu = (int(input("Ingrese una opcion: ")))
    if menu == 1:
        print("\n Candidatos disponibles\n"
                "1- luis \n"
                "2- eric \n"
                "3- helen \n"
                "4- alex \n")
        candidato = input("Ingrese el nombre del candidato: ").capitalize()
        candidato = re.sub(r"[ ,;.:\d]","", candidato)
        votacion.votar(candidato)
    elif menu == 2:
        votacion.mostrar_resultados()
    elif menu == 3:
        print("Gracias por participar")
        break
    else:
        print("Numero equivocado, ingrese uno valido del 1 al 3")

# Crea un juego de adivinanza de números que permita múltiples intentos.
import re
opciones = [random.randint(1, 10) for x in range(1)]
intentos = 3
while intentos > 0:
    num_ganador = int(input(f"ingrese el numero ganador, te quedan {intentos} intentos: "))
    if num_ganador in opciones:
        print(f"Felicidades {num_ganador} es el numero ganador")
        break
    elif num_ganador not in opciones :
        intentos -= 1
        print(f"Sigue intentandolo, te quedan: {intentos} oportunidades")
        if intentos == 0:
            print(f"Ya no te quedan mas oportunidades")
            break
    else:
        print("Valor equivocado")

# # Estructuras de Control (If, Else, Elif)
# # Definición del tema:
# # Las estructuras de control permiten que el programa tome decisiones y ejecute diferentes bloques de código según ciertas condiciones.

# # Tips:
# # Las condiciones se evalúan como verdaderas o falsas.
# # Usa indentación consistente (4 espacios o un tab) para definir bloques de código.
# # Usa operadores de comparación (==, !=, >, <, >=, <=) para evaluar condiciones.

# #ejemplo:
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# # La estructura 'if' verifica si la condición 'edad >= 18' es verdadera.
# # Si la condición es verdadera, se ejecuta el bloque de código debajo de 'if'.
# # Si la condición es falsa, se ejecuta el bloque de código debajo de 'else'.

# # Ejercicios:

# # Escribe un programa que verifique si una persona es mayor de edad.

A = 10
if A >= 18:
    print("es mayor o tiene 18")
else:
    print("No es mayor de edad")

# # Añade una condición adicional para verificar si una persona es adolescente (13-19 años).

b = 13
if b >= 13 and 19 >= b:
    print("es adolescente")
else:
    print(" no tienes edad")

# # Modifica el programa para que imprima un mensaje personalizado para niños, adolescentes y adultos.

persona = int(input("escriba su edad:"))
if persona <= 10:
    print("Bievenido niño")
elif persona >= 11 and 17 >= persona:
    print("Bienvenido adolescente")
else:
    print("Bienvenido Adulto")

# # Escribe un programa que solicite al usuario una temperatura y diga si hace frío, calor o está templado.

temperatura = int(input("Ingrese la temperatura"))
if temperatura <= 10:
    print("hace mucho frio, la temperatura esta a:",temperatura,"grados celsius")
elif temperatura >= 11 and 19 >= temperatura:
    print("El clima esta templado, la temperatura esta a:",temperatura,"grados celsius")
else:
    print("hace mucho calor, la temperatura esta a:",temperatura,"grados celsius")
    
# [Teoría] Explica cómo funcionan los bloques de código en Python.
# los bloques de código son secciones de código que se agrupan y se ejecutan juntos. 
# Los bloques de código en Python se utilizan para definir la estructura y el flujo del programa.

# [Práctica] Escribe un programa que solicite al usuario una nota (0-100) y devuelva una calificación (A, B, C, D, F).
nota = int(input("escribe tu nota"))
if nota >= 80 and 100 >= nota:
    print("tienes una calificacion tipo A")
elif nota >= 60 and 79 >= nota:
    print("tienes una calificacion tipo B")
elif nota >= 40 and 59 >= nota:
    print("tienes una calificacion tipo C")
elif nota >= 20 and 39 >= nota:
    print("tienes una calificacion tipo D")
elif nota >= 1 and 19 >= nota:
    print("tienes una calificacion tipo f")
else:
    print("Nota erroronea")



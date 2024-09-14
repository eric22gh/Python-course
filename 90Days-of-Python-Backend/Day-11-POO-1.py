# Día 11: Programación Orientada a Objetos (POO) - Introducción
# Es un paradigma de programación que organiza el código en torno a objetos y clases. 
# Este enfoque permite modelar entidades del mundo real como objetos con características (atributos) y acciones (métodos).

# permite:
# Reutilización de Código: Las clases y objetos pueden ser reutilizados en diferentes partes del programa.
# Modelado de Problemas Complejos: Permite representar entidades del mundo real y sus interacciones de manera más natural.
# Abstracción y Modularidad: Facilita la organización del código en componentes que pueden ser desarrollados y mantenidos de manera independiente.

# Tips del Tema
# Clases y Objetos: Las clases son plantillas que definen la estructura y el comportamiento de los objetos. 
# Los objetos son instancias específicas de esas clases. LOS VARIABLES=ATRIBUTOS(CARACTERISTICAS) ASOCIADAS A LOS OBJETOS Y ELLOS ESTAN DENTRO DE LAS CLASES.

# Atributos y Métodos: Los atributos son variables asociadas a los objetos que representan sus características.
#  Los métodos son funciones que pertenecen a las clases u objetos y permiten realizar acciones sobre los datos. 
# LOS METODOS PERMITEN QUE LAS CLASES Y LOS OBJETOS HAGAN FUNCIONES

# Encapsulación: principio que permite ocultar los detalles internos de un objeto y exponer solo la interfaz necesaria para interactuar con él. 
# Se logra definiendo atributos como públicos, protegidos o privados.

# # Definición de una clase/ nota es una buena practica que las clases comiencen con letra mayuscula.
# class Perro: # clase
#     def __init__(self, nombre, edad): # metodos, selft es para q el entre a los atributos o metdos
#         self.nombre = nombre  # Atributo público
#         self.edad = edad      

#     def ladrar(self): # metodo
#         print(f"{self.nombre} está ladrando.")

# # Creación de un objeto o instancia de una clase
# mi_perro = Perro("Fido", 3)
# print(mi_perro.nombre)  # Salida: Fido
# print(mi_perro.edad)    # Salida: 3
# mi_perro.ladrar()       # Salida: Fido está ladrando.

# # Perro es una clase que define la estructura y comportamiento de los objetos de tipo Perro.
# # __init__ es un método especial llamado constructor que inicializa los atributos (nombre y edad) cuando se crea un nuevo objeto de la clase.
# # self es una referencia al objeto actual y se utiliza para acceder a los atributos y métodos del objeto dentro de la clase.
# # mi_perro es una instancia u objeto específico de la clase Perro. Al llamar mi_perro.ladrar(), se ejecuta el método ladrar() definido en la clase.

# class gato:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def maullar(self):
#         print(f"el gato, {self.name} con {self.age} de edad, se escucha por todo lado")
# mi_gato = gato("gaara", 14)
# mi_gato.maullar()

# my_cat = gato("neji",22)
# my_cat.maullar()

# class horse:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#     def blood(self):
#         print(f"El  caballo {self.name} con tipo de raza {self.breed} esta entrado a la subasta")
# mi_horse = horse("liniker","Brama")
# mi_horse.blood()

# mi_horse2 = horse("kit","shepard")
# mi_horse2.blood()

# ####################Ejercicios
# # Ejercicio 1: Define una clase Coche con atributos marca y modelo, y un método arrancar que imprima un mensaje.
# class coche:
#     def __init__(self,marca,modelo):
#         self.marca = marca
#         self.modelo = modelo
#     def arrancar(self):
#         print(f"el carro marca {self.marca} del modelo {self.modelo} esta arrancando")
# llave = coche("jaguar","2024")
# llave.arrancar()

# # Ejercicio 2: Crea dos objetos de la clase Coche y llama al método arrancar para cada uno.
# clase1 = coche("hyuday","2023")
# clase1.arrancar()

# clase2 = coche("toyota","2025")
# clase2.arrancar()

# # Ejercicio 3: Añade un método detener a la clase Coche que imprima un mensaje y pruébalo con los objetos creados.
# class coche:
#     def __init__(self,marca,modelo):
#         self.marca = marca
#         self.modelo = modelo
#     def arrancar(self):
#         print(f"el carro marca {self.marca} del año {self.modelo} esta arrancando")
#     def detener(self):
#         print(f"el carro marca {self.marca} del año {self.modelo} se esta deteniedo")
        
# llave = coche("jaguar","2024")
# llave.detener()
# clase2 = coche("toyota","2025")
# clase2.detener()

# # Ejercicio 4: Define una clase Alumno con atributos nombre y nota, y un método aprobar que devuelva True si la nota es mayor o igual a 5.
# class alumno:
#     def __init__(self,name,nota ):
#         self.name = name
#         self.nota  = nota 
#     def aprobar(self):
#         if self.nota  >= 5:
#             print(f"la nota de {self.name} es mayor o igual a 5")
#             print(True)
#         else:
#             print(f"la nota de {self.name} es menor que 5")
#             print(False)
            
# calificacion = alumno("alex",5)
# calificacion.aprobar()
            
# # Ejercicio 5: Crea una lista de objetos Alumno y escribe un programa que cuente cuántos alumnos han aprobado.
# class aprobado:
#     def __init__(self,alumno, nota):
#         self.alumno = alumno
#         self.nota = nota
#     def aprobado(self):
#         if self.nota >= 70:
#             contar = self.nota
#             alum = self.alumno
#             print(F"El alumno {alum} con la nota {contar} estan aprobados")

# calificacion = aprobado("victor",65)
# calificacion.aprobado()
# calificacion = aprobado("vicka",75)
# calificacion.aprobado()
# calificacion = aprobado("viquez",85)
# calificacion.aprobado()
# calificacion = aprobado("vyk",55)
# calificacion.aprobado()
# ############# otra forma
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def aprobado(self):
#         return self.nota >= 70

# # lista de Alumno
# alumnos = [
#     Alumno("Victor", 65),
#     Alumno("Vicka", 75),
#     Alumno("Viquez", 85),
#     Alumno("Vyk", 55),
#     Alumno("Alex", 4),
#     Alumno("Elarya", 3)
# ]

# # Contar cuántos alumnos han aprobado
# aprobados = 0
# for alumno in alumnos:
#     if alumno.aprobado():
#         aprobados += 1

# print(f"Cantidad de alumnos aprobados: {aprobados}")

# # Ejercicio 6: Añade un atributo curso a la clase Alumno y modifica el método aprobar para que incluya el nombre del curso en el mensaje de aprobación.
# class alumno:
#     def __init__(self,name,nota ,curso):
#         self.name = name
#         self.nota  = nota 
#         self.curso = curso
#     def aprobar(self):
#         if self.nota  >= 5:
#             print(f"la nota del alumno {self.name} del curso {self.curso} es mayor o igual a {self.nota} Aprobado.")
#             return True
#         else:
#             print(f"la nota del alumno {self.name} del curso {self.curso} es menor que {self.nota} Reprobado")
#             return False
            
# calificacion = alumno("alex",5,"ciencias")
# calificacion.aprobar()

# # Ejercicio 7: Define una clase rectangulo con atributos ancho y alto, y métodos para calcular el área y el perímetro.
# class rectangulo:
#     def __init__(self, alto, ancho):
#         self.ancho = ancho
#         self.alto = alto
#     def area(self):
#         area = self.alto * self.ancho
#         return area
#         # print(f"el resultado del area del rectangulo es {area}")
#     def perimetro(self):
#         perimetro = (self.alto*2 + self.ancho*2)
#         print(f"el resultado del perimetro del rectangulo es {perimetro}")
# figura = rectangulo(10,20)
# figura.area()
# figura.perimetro()

# # Ejercicio 8: Crea una lista de objetos rectangulo y escribe un programa que calcule el área total de todos los rectángulos.
# rectangulos = [
#     rectangulo(11, 15),
#     rectangulo(5, 12),
#     rectangulo(2, 9),
#     rectangulo(8, 13)
# ]

# # Calcular el área total de todos los rectángulos
# area_total = 0
# for rectangulo in rectangulos:
#     area_total += rectangulo.area()

# print(f"El área total de todos los rectángulos es {area_total}")

# # Ejercicio 9 (Teoría): ¿Qué es una clase en POO y cómo se diferencia de un objeto?
# # Una clase es un modelo o plantilla que define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán. 
# # La clase actúa como un blueprint que especifica qué datos y comportamientos (métodos) tendrán los objetos.

# # Un objeto es una instancia de una clase. Es una entidad individual que contiene datos específicos y puede utilizar los métodos definidos en la clase.
# # En otras palabras, un objeto es un ejemplar concreto de una clase con valores particulares.

# # Ejercicio 10 (Práctica): Escribe un programa que defina una clase Persona con atributos nombre y edad, y métodos para mostrar su información y verificar si es mayor de edad.
# class persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#     def mayor(self):
#         if self.edad >= 18:
#             print(f"El señor(a) {self.nombre} con una edad de {self.edad} años es mayor de edad")
#         else:
#             print(f"El señor(a) {self.nombre} con una edad de {self.edad} años no es mayor de edad")

# personas = persona("eduardo",25) 
# personas2 = persona("alep",17) 
# personas.mayor()
# personas2.mayor()

# Ejercicio 11
# Define una clase `Calculadora` con métodos para sumar, restar, multiplicar y dividir. Crea un objeto de la clase y realiza algunas operaciones.
class Calculadora:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
    def sumar(self):
        return self.numero_1 + self.numero_2
    def resta(self):
        return self.numero_1 - self.numero_2
    def multiplicar(self):
        return self.numero_1 * self.numero_2
    def dividir(self):
        if self.numero_2 == 0: # no se puede dividir un numero entre 0
            return "Error: División por cero no permitida"
        return self.numero_1 / self.numero_2
 
dato = Calculadora(5, 56)
print(dato.sumar())
print(dato.resta())
print(dato.dividir())
print(dato.multiplicar())

# Ejercicio 12
# Define una clase `Libro` con atributos `titulo`, `autor` y `genero`.Añade un método `es_novel` que devuelva `True` si el género del libro es "novela".
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    
    def es_novel(self):
        if self.genero == "novela":
            return True
        else:
            return False

dato = Libro("el cuervo", "marquez", "novela")
print(dato.es_novel())

# Ejercicio 13
# Crea una clase `CuentaAhorros` que herede de `CuentaBancaria`. Añade un atributo `interes`y un método `calcular_interes` que calcule el interés sobre el saldo.
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        pass
class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldo, interes):
        self.interes = interes # super() permite invocar métodos
        super().__init__(saldo)
    def calcular_interes(self):
        return f" El interes sobre el saldo: {self.saldo} colones es de: {self.saldo * self.interes} colones"
    
dato = CuentaAhorros(250000, 0.15)
print(dato.calcular_interes())

# Ejercicio 14
# Define una clase `Producto` con atributos `nombre`, `precio` y `cantidad`.Añade un método `actualizar_stock` que modifique la cantidad del producto.
class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    def actualizar_stock(self, venta):
        if venta > self.cantidad:
            return "No se puede realizar la venta, stock insuficiente."
        self.cantidad -= venta  # Actualizar el stock en el sistema
        ganancia = venta * self.precio
        return f"Se vendieron {venta} productos. Stock restante: {self.cantidad}. Ganancia total: {ganancia} colones."
dato = Producto("papas",250, 100)
print(dato.actualizar_stock(10))

# Ejercicio 15
# Crea una clase `Triangulo` con atributos `lado1`, `lado2`, y `lado3`.Añade un método `es_equilatero` que devuelva `True` si todos los lados son iguales.
class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            return True
        else:
            return False
dato = Triangulo(10, 10, 10)
print(dato.es_equilatero())

# Ejercicio 16
# Define una clase `Profesor` con atributos `nombre`, `materia`, y `años_experiencia`.Añade un método `es_experto` que devuelva `True` 
# si los años de experiencia son mayores o iguales a 10.
class Profesor():
    def __init__(self, nombre, materia, años_experiencia):
        self.nombre = nombre
        self.materia = materia
        self.años_experiencia = años_experiencia
    
    def es_experto(self):
        return self.años_experiencia >= 10
       
profesor1 = Profesor("Alex", "Ciencias", 5)
profesor2 = Profesor("Sofía", "Español", 11)
profesor3 = Profesor("Carlos", "Física", 6)
print(profesor1.es_experto())  
print(profesor2.es_experto())  
print(profesor3.es_experto())

# Ejercicio 17
# Crea una clase `Fecha` con atributos `dia`, `mes`, y `año`.Añade un método `es_bisiesto` que determine si el año es bisiesto.
class Fecha():
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def es_bisiesto(self):
        if (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0):
            return f"el año: {self.año} si es un año bisiesto"

        else:
            return f"el año: {self.año} no es un año bisiesto"
        
dato = Fecha(22, 5, 2024)
print(dato.es_bisiesto())

# Ejercicio 18
# Define una clase `Empleado` con atributos `nombre`, `salario`, y `puesto`.Añade un método `aumento` que aplique un porcentaje de aumento al salario.
class Empleado():
    def __init__(self, nombre, salario, puesto):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto
    
    def aumento(self, porcentaje):
        aumento = self.salario * porcentaje
        salario_nuevo = self.salario + aumento
        return f"El porcentaje de aumento salarial del empleado: {self.nombre} es de: {aumento:.0f} y ahora su salario es de: {salario_nuevo:.0f}"
dato = Empleado("eric", 500000, "ventas")
print(dato.aumento(0.050))

# Ejercicio 19
# Crea una clase `CocheDeportivo` que herede de `Coche` (del ejercicio anterior).Añade un atributo `velocidad_maxima`
# y un método `es_rapido` que devuelva `True` si la velocidad máxima es mayor a 200 km/h.
class Coche:
    def __init__(self, carro, velocidad_maxima):
        self.carro = carro
        self.velocidad_maxima = velocidad_maxima
    def es_rapido(self):
        return self.velocidad_maxima > 200
class CocheDeportivo(Coche):
    def __init__(self, carro, velocidad_maxima):
        super().__init__(carro, velocidad_maxima)

deportivo = CocheDeportivo("Toyota Supra", 201)

if deportivo.es_rapido():
    print(f"El {deportivo.carro} es un coche rápido con una velocidad máxima de {deportivo.velocidad_maxima} km/h.")
else:
    print(f"El {deportivo.carro} no es un coche rápido, su velocidad máxima es de {deportivo.velocidad_maxima} km/h.")

# Ejercicio 20
# Define una clase `Ruta` con atributos `origen` y `destino`.Añade un método `distancia` que calcule la distancia entre los dos puntos dados 
# (puedes asumir una distancia fija para simplificar).
class Ruta():
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
    def distancia(self):
        diferencia = abs(self.destino - self.origen) # abs asegura que la distancia sea siempre positiva
        return f"La distancia en km entre el punto de origen: {self.origen}km y punto de destino {self.destino}km es de: {diferencia}km"
dato = Ruta(152, 855)
print(dato.distancia())


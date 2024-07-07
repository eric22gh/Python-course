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

# Definición de una clase/ nota es una buena practica que las clases comiencen con letra mayuscula.
class Perro: # clase
    def __init__(self, nombre, edad): # metodos, selft es para q el entre a los atributos o metdos
        self.nombre = nombre  # Atributo público
        self.edad = edad      # Atributo público

    def ladrar(self): # metodo
        print(f"{self.nombre} está ladrando.")

# Creación de un objeto o instancia de una clase
mi_perro = Perro("Fido", 3)
print(mi_perro.nombre)  # Salida: Fido
print(mi_perro.edad)    # Salida: 3
mi_perro.ladrar()       # Salida: Fido está ladrando.

# Perro es una clase que define la estructura y comportamiento de los objetos de tipo Perro.
# __init__ es un método especial llamado constructor que inicializa los atributos (nombre y edad) cuando se crea un nuevo objeto de la clase.
# self es una referencia al objeto actual y se utiliza para acceder a los atributos y métodos del objeto dentro de la clase.
# mi_perro es una instancia u objeto específico de la clase Perro. Al llamar mi_perro.ladrar(), se ejecuta el método ladrar() definido en la clase.

class gato:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def maullar(self):
        print(f"el gato, {self.name} con {self.age} de edad, se escucha por todo lado")
mi_gato = gato("gaara", 14)
mi_gato.maullar()

my_cat = gato("neji",22)
my_cat.maullar()

class horse:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def blood(self):
        print(f"El  caballo {self.name} con tipo de raza {self.breed} esta entrado a la subasta")
mi_horse = horse("liniker","Brama")
mi_horse.blood()

mi_horse2 = horse("kit","shepard")
mi_horse2.blood()



####################Ejercicios
# Ejercicio 1: Define una clase Coche con atributos marca y modelo, y un método arrancar que imprima un mensaje.
class coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print(f"el carro marca {self.marca} del modelo {self.modelo} esta arrancando")
llave = coche("jaguar","2024")
llave.arrancar()

# Ejercicio 2: Crea dos objetos de la clase Coche y llama al método arrancar para cada uno.
clase1 = coche("hyuday","2023")
clase1.arrancar()

clase2 = coche("toyota","2025")
clase2.arrancar()

# Ejercicio 3: Añade un método detener a la clase Coche que imprima un mensaje y pruébalo con los objetos creados.
class coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print(f"el carro marca {self.marca} del año {self.modelo} esta arrancando")
    def detener(self):
        print(f"el carro marca {self.marca} del año {self.modelo} se esta deteniedo")
        
llave = coche("jaguar","2024")
llave.detener()
clase2 = coche("toyota","2025")
clase2.detener()

# Ejercicio 4: Define una clase Alumno con atributos nombre y nota, y un método aprobar que devuelva True si la nota es mayor o igual a 5.
class alumno:
    def __init__(self,name,nota ):
        self.name = name
        self.nota  = nota 
    def aprobar(self):
        if self.nota  >= 5:
            print(f"la nota de {self.name} es mayor o igual a 5")
            print(True)
        else:
            print(f"la nota de {self.name} es menor que 5")
            print(False)
            
calificacion = alumno("alex",5)
calificacion.aprobar()
            
# Ejercicio 5: Crea una lista de objetos Alumno y escribe un programa que cuente cuántos alumnos han aprobado.
class aprobado:
    def __init__(self,alumno, nota):
        self.alumno = alumno
        self.nota = nota
    def aprobado(self):
        if self.nota >= 70:
            contar = self.nota
            alum = self.alumno
            print(F"El alumno {alum} con la nota {contar} estan aprobados")

calificacion = aprobado("victor",65)
calificacion.aprobado()
calificacion = aprobado("vicka",75)
calificacion.aprobado()
calificacion = aprobado("viquez",85)
calificacion.aprobado()
calificacion = aprobado("vyk",55)
calificacion.aprobado()
############# otra forma
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        return self.nota >= 70

# Crear una lista de objetos Alumno
alumnos = [
    Alumno("Victor", 65),
    Alumno("Vicka", 75),
    Alumno("Viquez", 85),
    Alumno("Vyk", 55),
    Alumno("Alex", 4),
    Alumno("Elarya", 3)
]

# Contar cuántos alumnos han aprobado
aprobados = 0
for alumno in alumnos:
    if alumno.aprobado():
        aprobados += 1

print(f"Cantidad de alumnos aprobados: {aprobados}")

# Ejercicio 6: Añade un atributo curso a la clase Alumno y modifica el método aprobar para que incluya el nombre del curso en el mensaje de aprobación.
class alumno:
    def __init__(self,name,nota ,curso):
        self.name = name
        self.nota  = nota 
        self.curso = curso
    def aprobar(self):
        if self.nota  >= 5:
            print(f"la nota del alumno {self.name} del curso {self.curso} es mayor o igual a {self.nota} Aprobado.")
            return True
        else:
            print(f"la nota del alumno {self.name} del curso {self.curso} es menor que {self.nota} Reprobado")
            return False
            
calificacion = alumno("alex",5,"ciencias")
calificacion.aprobar()

# Ejercicio 7: Define una clase rectangulo con atributos ancho y alto, y métodos para calcular el área y el perímetro.
class rectangulo:
    def __init__(self, alto, ancho):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        area = self.alto * self.ancho
        return area
        # print(f"el resultado del area del rectangulo es {area}")
    def perimetro(self):
        perimetro = (self.alto*2 + self.ancho*2)
        print(f"el resultado del perimetro del rectangulo es {perimetro}")
figura = rectangulo(10,20)
figura.area()
figura.perimetro()

# Ejercicio 8: Crea una lista de objetos rectangulo y escribe un programa que calcule el área total de todos los rectángulos.
rectangulos = [
    rectangulo(11, 15),
    rectangulo(5, 12),
    rectangulo(2, 9),
    rectangulo(8, 13)
]

# Calcular el área total de todos los rectángulos
area_total = 0
for rectangulo in rectangulos:
    area_total += rectangulo.area()

print(f"El área total de todos los rectángulos es {area_total}")

# Ejercicio 9 (Teoría): ¿Qué es una clase en POO y cómo se diferencia de un objeto?
# Una clase es un modelo o plantilla que define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán. 
# La clase actúa como un blueprint que especifica qué datos y comportamientos (métodos) tendrán los objetos.

# Un objeto es una instancia de una clase. Es una entidad individual que contiene datos específicos y puede utilizar los métodos definidos en la clase.
# En otras palabras, un objeto es un ejemplar concreto de una clase con valores particulares.

# Ejercicio 10 (Práctica): Escribe un programa que defina una clase Persona con atributos nombre y edad, y métodos para mostrar su información y verificar si es mayor de edad.
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mayor(self):
        if self.edad >= 18:
            print(f"El señor(a) {self.nombre} con una edad de {self.edad} años es mayor de edad")
        else:
            print(f"El señor(a) {self.nombre} con una edad de {self.edad} años no es mayor de edad")

personas = persona("eduardo",25) 
personas2 = persona("alep",17) 
personas.mayor()
personas2.mayor()
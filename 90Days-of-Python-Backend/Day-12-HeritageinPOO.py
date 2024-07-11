# Día 12: Herencia en POO
# La herencia en la Programación Orientada a Objetos (POO) es un concepto fundamental que permite 
# a una clase nueva (llamada clase derivada o subclase) heredar atributos y métodos de otra clase existente 
# (llamada clase base o superclase).Esto fomenta la reutilización del código y facilita la creación de jerarquías de clases 
# que modelan de manera efectiva la relación "es-un".

# Tips del Tema

# Herencia: Permite que una clase herede atributos y métodos de otra clase.

# Clase base y clase derivada: La clase base es la clase original de la que se hereda, 
# y la clase derivada es la nueva clase que extiende la clase base.

# Sobrescritura: Las clases derivadas pueden redefinir métodos de la clase base para cambiar o extender su comportamiento 
# según sea necesario.

# La herencia permite organizar el código de manera jerárquica, facilitando la extensión y la modificación de clases base según las necesidades del programa. 

########### ejemplos

# Definición de una clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas

# Definición de clases derivadas
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Creación de objetos de las clases derivadas
mi_perro = Perro("Rex")
mi_gato = Gato("Felix")

# Llamada a los métodos de las clases derivadas
mi_perro.hacer_sonido()  
mi_gato.hacer_sonido()   

class Persona:
    def __init__(self, lugar, persona):
        self.lugar = lugar # atributos
        self.persona = persona

    def Nacionalidad(self): # metodos
        pass # para que funcione la herencia

class Mueble(Persona): # clase mueble va a heredar funciones de la clase persona
    def Nacionalidad(self):
        print(F"este mueble es de {self.lugar} y su dueño es {self.persona}")

class Caballo(Persona):
    def Nacionalidad(self):
        print(F"este caballo es de {self.lugar}")

Mueble = Mueble("costarica","edwards")    # objetos
Caballo = Caballo("costarica","bhrama")
Mueble.Nacionalidad()
Caballo.Nacionalidad()



# ######################Ejercicios
# Ejercicio 1: Define una clase base Vehiculo con un atributo marca y un método arrancar. 
# Luego, define una clase derivada Coche que sobrescriba el método arrancar.
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    def arrancar(self):
        print(f"esta marca de carros: {self.marca} si arranca")
        pass
class Coche(Vehiculo):
    def arrancar(self):
        print(f"esta marca de coches {self.marca} no arranca")
mi_Coche = Coche("toyota") # no pueden a ver 2 objetos iguales
mi_Coche.arrancar()

# Ejercicio 2: Crea objetos de las clases Vehiculo y Coche, y llama al método arrancar para cada uno.
Vehiculo_2 = Vehiculo("hyundai")
Vehiculo_2.arrancar()

mi_Coche2 = Coche("byd")
mi_Coche2.arrancar()

# Ejercicio 3: Define una clase base Persona con atributos nombre y edad, y un método presentarse. 
# Luego, define una clase derivada Estudiante que sobrescriba el método presentarse y añada un atributo curso.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso): # se añade un atributo mas
        super().__init__(nombre, edad) # super() para llamar al constructor de la clase base.
        self.curso = curso

    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy del curso de {self.curso}")

mi_estudiante = Estudiante("Eric", 22, "Ciencias")
mi_estudiante.presentarse()

# Ejercicio 4: Crea un objeto de la clase Estudiante y llama al método presentarse.
student = Estudiante("alex",20,"español")
student.presentarse()

# Ejercicio 5: Define una clase base Figura con un método area que devuelva 0. Luego, 
# define una clase derivada Circulo que sobrescriba el método area para calcular el área del círculo.
import math

class Figura:
    def area(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2) # fórmula del area de un circulo: π * radio².

mi_circulo = Circulo(5)
print(f"El área del círculo es: {mi_circulo.area()}")


# Ejercicio 6: Crea una lista de objetos Figura y Circulo, y escribe un programa que muestre el área de cada figura.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        formula = math.pi * (self.radio ** 2)
        return formula

figura = [
    Circulo(5), # para que la clase lo tome como datos individuales hay que pasarlo por un for
    Circulo(12),
    Circulo(10),
    Circulo(22)
]

for i,figuras in enumerate(figura, start=1):
    resultado = figuras.area()
    print(f"el resultado del area del circulo numero {i} es: {resultado}")


# Ejercicio 7: Define una clase base Empleado con atributos nombre y salario, y un método mostrar_salario. 
# Luego, define una clase derivada Gerente que añada un atributo bono y sobrescriba el método mostrar_salario para incluir el bono.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_salario(self):
        print(f"Este es el salario: {self.salario} del empleado: {self.nombre}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def mostrar_salario(self):
        salario_total = self.salario + self.bono
        print(f"Este es el salario bruto: {salario_total} del gerente: {self.nombre} (incluye bono de {self.bono})")

manager = Gerente("Alex", 20000, 55)
manager.mostrar_salario()


# Ejercicio 8: Crea objetos de las clases Empleado y Gerente, y llama al método mostrar_salario para cada uno.
empleado = Empleado("Carlos", 30000)
empleado.mostrar_salario()

manager = Gerente("luis", 50000, 500)
manager.mostrar_salario(100)

# Ejercicio 9 (Teoría): ¿Qué es la herencia en POO y cuáles son sus beneficios?
# es una forma poderosa de reutilizar codigo de una forma eficaz, heredando metodos y atributos ah objetos o metodos en otras partes del codigo...
# una de sus ventajas en la organizacion de codigo y editar facilmente metodos.

# Ejercicio 10 (Práctica): Escribe un programa que defina una clase base Instrumento con un método tocar. 
# Luego, define clases derivadas Guitarra y Piano que sobrescriban el método tocar para mostrar mensajes específicos para cada instrumento. 
# Crea objetos de Guitarra y Piano y llama al método tocar para cada uno.
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
    def tocar(self):
        print(f"este instrumentos hace phhhs!!!!")

class Guitarra(Instrumento):
    def tocar(self, sonido):
        self.sonido = sonido
        print(f"este instrumento de nombre {self.nombre} hace de sonido {self.sonido}")
class Piano(Instrumento):
    def tocar(self, sound):
        self.sound = sound
        print(f"este instrumento del almacen y de nombre {self.nombre} hace un sonido {self.sound}")

guitar = Guitarra("guitarra")
guitar.tocar("thhhhhh")

piane = Piano("piane")
piane.tocar("fhhhhhhhhs")

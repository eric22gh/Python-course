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

# Ejercicio 11: Define una clase base Mascota con atributos nombre y edad. Luego, define una clase derivada Perro que tenga 
# un método adicional jugar que imprima un mensaje usando el nombre de la mascota.
class Mascota():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        pass
class Perro(Mascota):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def jugar(self):
        print(f"{self.nombre} está jugando y tiene {self.edad} años.")

# instancia o objeto de Perro
dato = Perro("toby", 10)
dato.jugar()

# Ejercicio 12: Crea una clase base Persona con un método hablar que imprima "Hablando...". Luego, crea una clase derivada 
# Profesor que sobrescriba el método hablar para que también mencione la materia que enseña.
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        pass

    def hablar(self):
        print(f"esta persona: {self.nombre} hablando")

class Profesor(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia
    def hablar(self):
        super().hablar()  # Llamar al método de la clase  y que se impriman los 2 textos( clase base y herededad)
        print(f"Además, está enseñando la materia de {self.materia}.")

dato = Profesor("carlos", "ciencias")    
dato.hablar() 

# Ejercicio 13: Define una clase base Vehiculo con atributos tipo y marca. Luego, crea dos clases derivadas, 
# Motocicleta y Coche, que añadan un atributo velocidad_maxima y sobrescriban un método mostrar_informacion.
class Vehiculo():
    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca

    def mostrar_informacion(self):
        print(f"Vehículo tipo: {self.tipo}, marca: {self.marca}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, velocidad_maxima):
        super().__init__("Motocicleta", marca)
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        print(f"Motocicleta marca: {self.marca}, velocidad máxima: {self.velocidad_maxima} km/h")

class Coche(Vehiculo):
    def __init__(self, marca, velocidad_maxima):
        super().__init__("Coche", marca) # cuando el atributo es fijo se puede poner en strings
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        print(f"Coche marca: {self.marca}, velocidad máxima: {self.velocidad_maxima} km/h")

moto = Motocicleta("Yamaha", 350)
moto.mostrar_informacion()

coche = Coche("Toyota", 220)
coche.mostrar_informacion()

vehiculo = Vehiculo("Bicicleta", "GT")
vehiculo.mostrar_informacion()

# Ejercicio 14: Crea una clase base FiguraGeometrica con un método calcular_area que devuelva 0. Luego, 
# define dos clases derivadas: Cuadrado y Triangulo. Cada una debe sobrescribir el método calcular_area con la fórmula adecuada.
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, medida):
        self.medida = medida
        pass
    @abstractmethod
    def calcular_area(self):
        return 0

class Cuadrado(FiguraGeometrica):
    def __init__(self, medida):
        super().__init__(medida)

    def calcular_area(self):
        return f"el area del cuadrado es: {self.medida ** 2}"

class Triangulo(FiguraGeometrica):
    def __init__(self, medida, altura):
        super().__init__(medida)
        self.altura = altura

    def calcular_area(self):
        area_triangulo = (self.medida * self.altura) / 2 
        return f"el area del triangulo es: {area_triangulo:.0f}"

dato = Cuadrado(5)
print(dato.calcular_area())
dato1 = Triangulo(5, 7)
print(dato1.calcular_area())

# Ejercicio 15: Define una clase base Electrodomestico con atributos marca y modelo. Luego, crea una clase derivada Lavadora 
# que añada un atributo capacidad y sobrescriba un método mostrar_detalle para incluir la capacidad.
class Electrodomestico():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    @abstractmethod
    def mostrar_detalle(self):
        return f"este es la info de este electrodimestico marca: {self.marca} y modelo: {self.modelo}"
        pass
class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad

    def mostrar_detalle(self):
        return f"{super().mostrar_detalle()}, y capacidad: {self.capacidad} kilos" # evitar la reutilizacion del codigo de return arriba

dato = Lavadora("oster", 1998, 100)
print(dato.mostrar_detalle())

# Ejercicio 16: Crea una clase base DispositivoElectronico con un método encender que imprima un mensaje. Luego, define dos clases derivadas, 
# Telefono y Ordenador, que sobrescriban el método encender para mostrar mensajes específicos de cada dispositivo.
class DispositivoElectronico():
    def __init__(self, nombre):
        self.nombre = nombre
        pass

    def encender(self):
        print(f"El dispositivo {self.nombre} se está encendiendo.")

class Telefono(DispositivoElectronico):
    def __init__(self, nombre):
        super().__init__(nombre)

    def encender(self):
        print(f"El teléfono {self.nombre} está encendido.")
class Ordenador(DispositivoElectronico):
    def __init__(self, nombre):
        super().__init__(nombre)

    def encender(self):
        print(f"El ordenador {self.nombre} está encendido.")

dato2 = Telefono("Samsung Galaxy")
dato2.encender()
dato2 = Ordenador("Windows PC")
dato2.encender()

# Ejercicio 17: Define una clase base Producto con atributos nombre y precio. Luego, define una clase derivada Libro 
# que añada un atributo autor y sobrescriba el método mostrar_informacion para incluir el autor.
class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}.")
        pass
class Libro(Producto):
    def __init__(self, nombre, precio, autor):
        super().__init__(nombre, precio)
        self.autor = autor
    def mostrar_informacion(self):
        print(f"Este libro tiene esta informacion: nombre: {self.nombre}, precio: {self.precio} y su autor: {self.autor}")
    
dato1 = Libro("El cuervo", 19500, "Gabriel García Márquez")
dato1.mostrar_informacion()

# Ejercicio 18: Crea una clase base Transporte con un atributo capacidad. Luego, define dos clases derivadas, Autobus y Tren, 
# que sobrescriban un método mostrar_capacidad para mostrar la capacidad con un mensaje diferente en cada caso.
class Transporte():
    def __init__(self, capacidad):
        self.capacidad = capacidad
    def mostrar_capacidad(self):
        print(f"Capacidad de transporte: {self.capacidad} pasajeros.")
        pass

class Autobus(Transporte):
    def __init__(self, capacidad):
        super().__init__(capacidad)

    def mostrar_capacidad(self):
        print(F"Esta es la capacidad completa de este autobus: {self.capacidad} pasajeros")

class Tren(Transporte):
    def __init__(self, capacidad):
        super().__init__(capacidad)

    def mostrar_capacidad(self):
        print(F"Esta es la capacidad completa de este Tren: {self.capacidad} pasajeros")

dato = Autobus(52)
dato.mostrar_capacidad()
dato = Tren(5)
dato.mostrar_capacidad()

# Ejercicio 19: Define una clase base Animal con un método hacer_sonido. Luego, crea dos clases derivadas, Vaca y Caballo, 
# que sobrescriban el método hacer_sonido con un sonido específico para cada animal.
class Animal():
    def __init__(self, animal):
        self.animal = animal
    def hacer_sonido(self):
        print(F"este animal: {self.animal} hace un sonido")
        pass

class Vaca(Animal):
    def __init__(self, animal):
        super().__init__(animal) 
    def hacer_sonido(self):
        print(f"este animal: {self.animal} hace muuuu")

class Caballo(Animal):
    def __init__(self, animal):
        super().__init__(animal) 
    def hacer_sonido(self):
        print(f"este animal: {self.animal} hace jhhhh") 

dato5 = Vaca(" BU") 
dato5.hacer_sonido()

# Ejercicio 20: Crea una clase base Herramienta con atributos tipo y material. Luego, define una clase derivada Martillo 
# que sobrescriba un método golpear que imprima un mensaje usando el tipo y material de la herramienta.
class Herramienta():
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material
        pass
class Martillo(Herramienta):
    def __init__(self, tipo, material):
        super().__init__(tipo, material)

    def golpear(self):
        print(f"Se está usando un martillo de tipo: {self.tipo}, hecho de: {self.material} para golpear.")
dato = Martillo("Largo", "metal")
dato.golpear()
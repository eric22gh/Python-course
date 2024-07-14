# Día 13: Polimorfismo en POO

# Definición del Tema
# El polimorfismo es un principio de la Programación Orientada a Objetos (POO) que permite tratar objetos de diferentes clases 
# de manera uniforme a través de una interfaz común. Esto significa que un mismo método puede comportarse de diferentes maneras 
# según el tipo de objeto que lo esté utilizando.
# varios comportamientos de un metodo dependiendo de que objeto lo utilice.
# trabajar con varios objetos a la vez.

# Tips del Tema

# Polimorfismo: Es la habilidad de usar una interfaz común para diferentes tipos de objetos. 
# Permite que objetos de diferentes clases respondan al mismo método de manera diferente.

# Métodos sobrescritos: Clases derivadas pueden tener métodos con el mismo nombre que en la clase base, 
# pero con comportamientos específicos para cada clase.

# Uso de polimorfismo: Facilita la extensión y mantenibilidad del código, ya que permite escribir código que actúa sobre objetos genéricos 
# y se adapta automáticamente al tipo específico de objeto que se está manipulando.

############## ejemplos

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

# Uso de polimorfismo
animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()  # Salida: ¡Guau! ¡Miau!

###############

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

# Definición de clases derivadas
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío!"

# Función que usa polimorfismo
def hacer_sonido_de_animales(animales):
    for animal in animales:
        print(animal.hacer_sonido())

# Creación de objetos de las clases derivadas
mi_perro = Perro()
mi_gato = Gato()
mi_pajaro = Pajaro()

# Uso de polimorfismo
animales = [mi_perro, mi_gato, mi_pajaro]
hacer_sonido_de_animales(animales)

################ Ejercicios
# Ejercicio 1: Define una clase base Figura con un método area. Define clases derivadas Circulo y Cuadrado que sobrescriban el método area para calcular el área correspondiente.
import math

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado): # iniciar el atributo
        self.lado = lado

    def area(self):
        return self.lado ** 2

circulo = Circulo(5)
print(f"El área del círculo es: {circulo.area()}")

cuadrado = Cuadrado(10)
print(f"El área del cuadrado es: {cuadrado.area()}")

# Ejercicio 2: Crea una lista de objetos Circulo y Cuadrado, y escribe un programa que muestre el área de cada figura usando polimorfismo.
figuras = [
    Circulo(10),
    Circulo(15),
    Circulo(19),
    Circulo(22),
    Cuadrado(22),
    Cuadrado(5),
    Cuadrado(20),
    Cuadrado(7)
]

for i, figura in enumerate(figuras, start=1):
    print(f"El área de la figura {i} es: {figura.area()}")

# Ejercicio 3: Define una clase base Empleado con un método calcular_pago. Define clases derivadas Asalariado y Freelancer que sobrescriban el método calcular_pago.
class Empleado:
    def calcular_pago(self):
        pass

class Asalariado(Empleado):
    def __init__(self, pago):
        if pago <= 0:
            raise ValueError("El pago debe ser un valor positivo.")
        self.pago = pago

    def calcular_pago(self):
        return self.pago - (self.pago * 0.25)

class Freelancer(Empleado):
    def __init__(self, pago):
        if pago <= 0:
            raise ValueError("El pago debe ser un valor positivo.")
        self.pago = pago

    def calcular_pago(self):
        return self.pago - (self.pago * 0.13)

empleados = [
    Asalariado(20000),
    Freelancer(20000)
]

for empleado in empleados:
    print(f"El pago para el empleado es de {empleado.calcular_pago()}")

# Ejercicio 4: Crea una lista de objetos Asalariado y Freelancer, y escribe un programa que calcule el pago de cada empleado usando polimorfismo.
# Asalaria = [
#     Asalariado(30000),
#     Asalariado(40000),
#     Asalariado(20000),
#     Asalariado(50000)
# ]
# freelance = [
#     Freelancer(20000),
#     Freelancer(10000),
#     Freelancer(60000),
#     Freelancer(80000)
# ]
# for i, salary in enumerate(Asalaria, start=1):
#     resul = salary.calcular_pago()
#     print(F"el salario del empleado numero {i} es de {resul} colones")
# for i, salaries in enumerate(freelance, start=1):
#     result = salaries.calcular_pago()
#     print(f"El pago del empleado freelance numero {i} es de {result}")

###### otra manera ##############

Asalaria = [
    Asalariado(30000),
    Asalariado(40000),
    Asalariado(20000),
    Asalariado(50000),
    Freelancer(20000),
    Freelancer(10000),
    Freelancer(60000),
    Freelancer(80000)
]
for i, salary in enumerate(Asalaria, start=1):
    resul = salary.calcular_pago()
    print(F"el salario del empleado numero {i} es de {resul} colones")

# Ejercicio 5: Define una clase base Transporte con un método mover. Define clases derivadas Coche y Bicicleta que sobrescriban el método mover.
class Transporte:
    def mover(self):
        pass

class Coche(Transporte):
    def __init__(self, tipo):
        self.tipo = tipo

    def mover(self):
        return f"{self.tipo} está en movimiento."

class Bicicleta(Transporte):
    def __init__(self, tipo):
        self.tipo = tipo

    def mover(self):
        return f"{self.tipo} no se mueve."

coche = Coche("coche")
print(coche.mover())

bicicleta = Bicicleta("bicicleta")
print(bicicleta.mover())
   
# Ejercicio 6: Crea una lista de objetos Coche y Bicicleta, y escribe un programa que llame al método mover para cada Transporte usando polimorfismo.
coches = [
    Coche("bicileta"),
    Coche("patineta"),
    Coche("cuadraciclo"),
    Coche("motocicleta")
]
bicicletas = [
    Bicicleta("patines"),
    Bicicleta("tren"),
    Bicicleta("avion"),
    Bicicleta("jet")
]

for i, cars in enumerate(coches, start=1):
    res = cars.mover()
    print(F"el Transporte numero {i} {res}")

for i, bicycle in enumerate(bicicletas, start=1):
    rest = bicycle.mover()
    print(f"el Transporte numero {i} de tipo {rest}")
    
# Ejercicio 7: Define una clase base Electrodomestico con un método encender. Define clases derivadas Televisor y Lavadora que sobrescriban el método encender.
class Electrodomestico:
    def encender(self):
        pass

class Televisor(Electrodomestico):
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        return f"{self.tipo} y está encendido."

class Lavadora(Electrodomestico):
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        return f"{self.tipo} y está encendida."

electrodomestico1 = Televisor("televisor de 50 pulgadas")
print(f"Compramos un {electrodomestico1.encender()}")
                      
electrodomestico2 = Lavadora("lavadora de 18kg")
print(f"Compramos una {electrodomestico2.encender()}")

# Ejercicio 8: Crea una lista de objetos Televisor y Lavadora, y escribe un programa que llame al método encender para cada electrodoméstico usando polimorfismo.
linea_blanca = [
    Televisor("tv de 50 pulgadas"),
    Televisor("tv de 100 pulgadas"),
    Televisor("tv de 40 pulgadas"),
    Televisor("tv de 32 pulgadas"),
    Lavadora("lavadora de 18kg"),
    Lavadora("lavadora de 28kg"),
    Lavadora("lavadora de 8kg"),
    Lavadora("lavadora de 58kg")
]

for i, tele in enumerate( linea_blanca, start=1):
    electro = tele.encender()
    print(f"compramos una {electro}")

# Ejercicio 9 (Teoría): ¿Qué es el polimorfismo y cómo mejora la flexibilidad del código en POO?
# permite que diferentes clases implementen el mismo método, respondiendo de manera diferente según la clase. 
# Esto mejora la flexibilidad del código al permitir la creación de interfaces y funciones que pueden trabajar con diferentes tipos de objetos de manera uniforme, 
# facilitando el mantenimiento y la expansión del código.

# Ejercicio 10 (Práctica): Escribe un programa que defina una clase base Animals con un método hacer_sonido, y clases derivadas Perro, Gato, y Pajaro 
# que sobrescriban el método hacer_sonido. Crea una lista de estos animales y llama al método hacer_sonido para cada uno usando polimorfismo.
class Animals:
    def hacer_sonido(self):
        pass
class Perro(Animals):
    def __init__(self, dog):
        self.dog = dog
    def hacer_sonido(self):
        return f"un perro llamado {self.dog}"

class Gato(Animals):
    def __init__(self, cat):
        self.cat = cat
    def hacer_sonido(self):
        return f"un gato llamado {self.cat}"
    
class Pajaro(Animals):
    def __init__(self, bird):
        self.bird = bird
    def hacer_sonido(self):
        return f"un pajaro de especie {self.bird}"
    
animaless = [
    Perro("snoppy"),
    Perro("rex"),
    Perro("max"),
    Gato("lulu"),
    Gato("luna"),
    Gato("mia"),
    Pajaro("colibri"),
    Pajaro("alvatros"),
    Pajaro("condor"),
]

for criaturas in animaless:
    nombre = criaturas.hacer_sonido() # mismo metodo pero reacciona diferente segun la clase, basicamente eso es polimorfismo
    print(f"esta es mi mascota {nombre}")

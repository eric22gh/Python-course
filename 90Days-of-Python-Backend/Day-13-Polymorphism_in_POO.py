# Día 13: Polimorfismo en POO

# Definición del Tema
# El polimorfismo es un principio de la Programación Orientada a Objetos (POO) que permite tratar objetos de diferentes clases 
# de manera uniforme a través de una interfaz común. Esto significa que un mismo método puede comportarse de diferentes maneras 
# según el tipo de objeto que lo esté utilizando.
# polimorfismo: un metodo reacciona diferente dependiendo de que objeto lo utilice.
# trabajar con varios objetos a la vez.

# Tips del Tema

# Polimorfismo: Es la habilidad de usar una interfaz común para diferentes tipos de objetos. 
# Permite que objetos de diferentes clases respondan al mismo método de manera diferente.

# Métodos sobrescritos: Clases derivadas pueden tener métodos con el mismo nombre que en la clase base, 
# pero con comportamientos específicos para cada clase.

# Uso de polimorfismo: Facilita la extensión y mantenibilidad del código, ya que permite escribir código que actúa sobre objetos genéricos 
# y se adapta automáticamente al tipo específico de objeto que se está manipulando.

############## ejemplos

# class Animal:
#     def hacer_sonido(self):
#         raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

# class Perro(Animal):
#     def hacer_sonido(self):
#         print("¡Guau!")

# class Gato(Animal):
#     def hacer_sonido(self):
#         print("¡Miau!")

# # Uso de polimorfismo
# animales = [Perro(), Gato()]

# for animal in animales:
#     animal.hacer_sonido()  # Salida: ¡Guau! ¡Miau!

# ###############

# class Animal:
#     def hacer_sonido(self):
#         raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

# # Definición de clases derivadas
# class Perro(Animal):
#     def hacer_sonido(self):
#         return "¡Guau!"

# class Gato(Animal):
#     def hacer_sonido(self):
#         return "¡Miau!"

# class Pajaro(Animal):
#     def hacer_sonido(self):
#         return "¡Pío!"

# # Función que usa polimorfismo
# def hacer_sonido_de_animales(animales):
#     for animal in animales:
#         print(animal.hacer_sonido())

# # Creación de objetos de las clases derivadas
# mi_perro = Perro()
# mi_gato = Gato()
# mi_pajaro = Pajaro()

# # Uso de polimorfismo
# animales = [mi_perro, mi_gato, mi_pajaro]
# hacer_sonido_de_animales(animales)

# ################ Ejercicios
# # Ejercicio 1: Define una clase base Figura con un método area. Define clases derivadas Circulo y Cuadrado que sobrescriban el método area para calcular el área correspondiente.
# import math

# class Figura:
#     def area(self):
#         pass

# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio

#     def area(self):
#         return math.pi * (self.radio ** 2)

# class Cuadrado(Figura):
#     def __init__(self, lado): # iniciar el atributo
#         self.lado = lado

#     def area(self):
#         return self.lado ** 2

# circulo = Circulo(5)
# print(f"El área del círculo es: {circulo.area()}")

# cuadrado = Cuadrado(10)
# print(f"El área del cuadrado es: {cuadrado.area()}")

# # Ejercicio 2: Crea una lista de objetos Circulo y Cuadrado, y escribe un programa que muestre el área de cada figura usando polimorfismo.
# figuras = [
#     Circulo(10),
#     Circulo(15),
#     Circulo(19),
#     Circulo(22),
#     Cuadrado(22),
#     Cuadrado(5),
#     Cuadrado(20),
#     Cuadrado(7)
# ]

# for i, figura in enumerate(figuras, start=1):
#     print(f"El área de la figura {i} es: {figura.area()}")

# # Ejercicio 3: Define una clase base Empleado con un método calcular_pago. Define clases derivadas Asalariado y Freelancer que sobrescriban el método calcular_pago.
# class Empleado:
#     def calcular_pago(self):
#         pass

# class Asalariado(Empleado):
#     def __init__(self, pago):
#         if pago <= 0:
#             raise ValueError("El pago debe ser un valor positivo.")
#         self.pago = pago

#     def calcular_pago(self):
#         return self.pago - (self.pago * 0.25)

# class Freelancer(Empleado):
#     def __init__(self, pago):
#         if pago <= 0:
#             raise ValueError("El pago debe ser un valor positivo.")
#         self.pago = pago

#     def calcular_pago(self):
#         return self.pago - (self.pago * 0.13)

# empleados = [
#     Asalariado(20000),
#     Freelancer(20000)
# ]

# for empleado in empleados:
#     print(f"El pago para el empleado es de {empleado.calcular_pago()}")

# # Ejercicio 4: Crea una lista de objetos Asalariado y Freelancer, y escribe un programa que calcule el pago de cada empleado usando polimorfismo.
# # Asalaria = [
# #     Asalariado(30000),
# #     Asalariado(40000),
# #     Asalariado(20000),
# #     Asalariado(50000)
# # ]
# # freelance = [
# #     Freelancer(20000),
# #     Freelancer(10000),
# #     Freelancer(60000),
# #     Freelancer(80000)
# # ]
# # for i, salary in enumerate(Asalaria, start=1):
# #     resul = salary.calcular_pago()
# #     print(F"el salario del empleado numero {i} es de {resul} colones")
# # for i, salaries in enumerate(freelance, start=1):
# #     result = salaries.calcular_pago()
# #     print(f"El pago del empleado freelance numero {i} es de {result}")

# ###### otra manera ##############

# Asalaria = [
#     Asalariado(30000),
#     Asalariado(40000),
#     Asalariado(20000),
#     Asalariado(50000),
#     Freelancer(20000),
#     Freelancer(10000),
#     Freelancer(60000),
#     Freelancer(80000)
# ]
# for i, salary in enumerate(Asalaria, start=1):
#     resul = salary.calcular_pago()
#     print(F"el salario del empleado numero {i} es de {resul} colones")

# # Ejercicio 5: Define una clase base Transporte con un método mover. Define clases derivadas Coche y Bicicleta que sobrescriban el método mover.
# class Transporte:
#     def mover(self):
#         pass

# class Coche(Transporte):
#     def __init__(self, tipo):
#         self.tipo = tipo

#     def mover(self):
#         return f"{self.tipo} está en movimiento."

# class Bicicleta(Transporte):
#     def __init__(self, tipo):
#         self.tipo = tipo

#     def mover(self):
#         return f"{self.tipo} no se mueve."

# coche = Coche("coche")
# print(coche.mover())

# bicicleta = Bicicleta("bicicleta")
# print(bicicleta.mover())
   
# # Ejercicio 6: Crea una lista de objetos Coche y Bicicleta, y escribe un programa que llame al método mover para cada Transporte usando polimorfismo.
# coches = [
#     Coche("bicileta"),
#     Coche("patineta"),
#     Coche("cuadraciclo"),
#     Coche("motocicleta")
# ]
# bicicletas = [
#     Bicicleta("patines"),
#     Bicicleta("tren"),
#     Bicicleta("avion"),
#     Bicicleta("jet")
# ]

# for i, cars in enumerate(coches, start=1):
#     res = cars.mover()
#     print(F"el Transporte numero {i} {res}")

# for i, bicycle in enumerate(bicicletas, start=1):
#     rest = bicycle.mover()
#     print(f"el Transporte numero {i} de tipo {rest}")
    
# # Ejercicio 7: Define una clase base Electrodomestico con un método encender. Define clases derivadas Televisor y Lavadora que sobrescriban el método encender.
# class Electrodomestico:
#     def encender(self):
#         pass

# class Televisor(Electrodomestico):
#     def __init__(self, tipo):
#         self.tipo = tipo

#     def encender(self):
#         return f"{self.tipo} y está encendido."

# class Lavadora(Electrodomestico):
#     def __init__(self, tipo):
#         self.tipo = tipo

#     def encender(self):
#         return f"{self.tipo} y está encendida."

# electrodomestico1 = Televisor("televisor de 50 pulgadas")
# print(f"Compramos un {electrodomestico1.encender()}")
                      
# electrodomestico2 = Lavadora("lavadora de 18kg")
# print(f"Compramos una {electrodomestico2.encender()}")

# # Ejercicio 8: Crea una lista de objetos Televisor y Lavadora, y escribe un programa que llame al método encender para cada electrodoméstico usando polimorfismo.
# linea_blanca = [
#     Televisor("tv de 50 pulgadas"),
#     Televisor("tv de 100 pulgadas"),
#     Televisor("tv de 40 pulgadas"),
#     Televisor("tv de 32 pulgadas"),
#     Lavadora("lavadora de 18kg"),
#     Lavadora("lavadora de 28kg"),
#     Lavadora("lavadora de 8kg"),
#     Lavadora("lavadora de 58kg")
# ]

# for i, tele in enumerate( linea_blanca, start=1):
#     electro = tele.encender()
#     print(f"compramos una {electro}")

# # Ejercicio 9 (Teoría): ¿Qué es el polimorfismo y cómo mejora la flexibilidad del código en POO?
# # permite que diferentes clases implementen el mismo método, respondiendo de manera diferente según la clase. 
# # Esto mejora la flexibilidad del código al permitir la creación de interfaces y funciones que pueden trabajar con diferentes tipos de objetos de manera uniforme, 
# # facilitando el mantenimiento y la expansión del código.

# # Ejercicio 10 (Práctica): Escribe un programa que defina una clase base Animals con un método hacer_sonido, y clases derivadas Perro, Gato, y Pajaro 
# # que sobrescriban el método hacer_sonido. Crea una lista de estos animales y llama al método hacer_sonido para cada uno usando polimorfismo.
# class Animals:
#     def hacer_sonido(self):
#         pass
# class Perro(Animals):
#     def __init__(self, dog):
#         self.dog = dog
#     def hacer_sonido(self):
#         return f"un perro llamado {self.dog}"

# class Gato(Animals):
#     def __init__(self, cat):
#         self.cat = cat
#     def hacer_sonido(self):
#         return f"un gato llamado {self.cat}"
    
# class Pajaro(Animals):
#     def __init__(self, bird):
#         self.bird = bird
#     def hacer_sonido(self):
#         return f"un pajaro de especie {self.bird}"
    
# animaless = [
#     Perro("snoppy"),
#     Perro("rex"),
#     Perro("max"),
#     Gato("lulu"),
#     Gato("luna"),
#     Gato("mia"),
#     Pajaro("colibri"),
#     Pajaro("alvatros"),
#     Pajaro("condor"),
# ]

# for criaturas in animaless:
#     nombre = criaturas.hacer_sonido() # mismo metodo pero reacciona diferente segun la clase, basicamente eso es polimorfismo
#     print(f"esta es mi mascota {nombre}")

# Ejercicio 11: 
# Define una clase base Instrumento con un método tocar. 
# Luego, define clases derivadas Guitarra y Bateria que sobrescriban el método tocar para mostrar el sonido específico de cada instrumento.
class Instrumento():
    def __init__(self, nombre_instrumento):
        self.nombre_instrumento = nombre_instrumento
        pass
    def tocar(self):
        return f"este instrumento: {self.nombre_instrumento} hace un sonido"

class Guitarra(Instrumento):
    def __init__(self, nombre_instrumento):
        super().__init__(nombre_instrumento)
    def tocar(self):
        return F"{super().tocar()} y es: tututu"
    
class Bateria(Instrumento):
    def __init__(self, nombre_instrumento):
        super().__init__(nombre_instrumento)
    def tocar(self):
        return f"{super().tocar()} y hace: tum tum tum"
    
dato = Guitarra("guitarra electrica")
print(dato.tocar())
dato1 = Bateria("Bateria")
print(dato1.tocar())

# Ejercicio 12: 
# Define una clase base Juego con un método iniciar. 
# Luego, crea clases derivadas Futbol y Ajedrez que sobrescriban el método iniciar con la forma en que comienza cada juego.
class Juego():
    def __init__(self, nombre_juego):
        self.nombre_juego = nombre_juego
        pass
    def iniciar(self):
        return f"este juego: {self.nombre_juego} ya inicio"

class Futbol(Juego):
    def __init__(self, nombre_juego):
        super().__init__(nombre_juego)
    def iniciar(self):
        return F"{super().iniciar()}, sin embargo inicio emocionante"
    
class Ajedrez(Juego):
    def __init__(self, nombre_juego):
        super().__init__(nombre_juego)
    def iniciar(self):
        return f"{super().iniciar()}, sin embargo inicio poco emocionante"
dato2 = Ajedrez("ajedrez")
print(dato2.iniciar())
dato3 = Futbol("futbol americano")
print(dato3.iniciar())

# Ejercicio 13: 
# Crea una clase base Empleado con un método calcular_bono. 
# Define clases derivadas Gerente y Diseñador, cada una sobrescribiendo el método para calcular el bono específico para ese tipo de empleado.
class Empleado():
    def __init__(self, nombre_empleado, bono, salario):
        self.nombre_empleado = nombre_empleado
        self.bono = bono
        self.salario = salario
        pass
    def calcular_bono(self):
        total_bono = self.salario * self.bono
        return f"este empleado: {self.nombre_empleado} y tiene un monto bono de: {total_bono} colones"
    
class Gerente(Empleado):
    def __init__(self, nombre_empleado, bono, salario):
        super().__init__(nombre_empleado, bono, salario)

    def calcular_bono(self):
        return F"{super().calcular_bono()} y es del departamento de gerencia"
    
class Diseñador(Empleado):
    def __init__(self, nombre_empleado, bono, salario):
        super().__init__(nombre_empleado, bono, salario)
    def calcular_bono(self):
        return F"{super().calcular_bono()} y es del departemento de diseño"
    
dato7 = Gerente("eric", 0.12, 250000)
print(dato7.calcular_bono())
dato8 = Diseñador("alex", 0.15, 250000)
print(dato8.calcular_bono())

# Ejercicio 14: 
# Define una clase base Dispositivo con un método encender. 
# Luego, crea clases derivadas Laptop y Smartphone que sobrescriban el método encender para mostrar cómo se enciende cada dispositivo.
class Dispositivo():
    def __init__(self, nombre_dispositivo):
        self.nombre_dispositivo = nombre_dispositivo
        pass
    def encender(self):
        return f"este dispositivo: {self.nombre_dispositivo} se ha encendido"

class Laptop(Dispositivo):
    def __init__(self, nombre_dispositivo):
        super().__init__(nombre_dispositivo)
    def encender(self):
        return f"{super().encender()} de manera lenta"   
    
class Smartphone(Dispositivo):
    def __init__(self, nombre_dispositivo):
        super().__init__(nombre_dispositivo)

    def encender(self):
        return F"{super().encender()} de manera rapida"
    
dato = Laptop("HP")
print(dato.encender())
dato1 = Smartphone("Samsung Galaxy")
print(dato1.encender())

# Ejercicio 15: 
# Define una clase base Vehiculo con un método mover. 
# Luego, crea clases derivadas Auto y Bicicleta que sobrescriban el método mover para mostrar cómo se desplaza cada tipo de vehículo.

class Vehiculo():
    def __init__(self, nombre_vehiculo):
        self.nombre_vehiculo = nombre_vehiculo
        pass
    def mover(self):
        return f"este vehiculo: {self.nombre_vehiculo} se esta desplazando"
class Auto(Vehiculo):
    def __init__(self, nombre_vehiculo):
        super().__init__(nombre_vehiculo)

    def mover(self):
        return F"{super().mover()} en cuatro ruedas y de una manera rapida"

class  Bicicleta(Vehiculo):
    def __init__(self, nombre_vehiculo):
        super().__init__(nombre_vehiculo)

    def mover(self):
        return f"{super().mover()} en dos ruedas y de una manera lenta"
    
dato = Auto("toyota")
print(dato.mover())
dato5 = Bicicleta("GT")
print(dato5.mover())

# Ejercicio 16: 
# Define una clase base Animal con un método hacer_sonido. 
# Luego, crea clases derivadas Perro y Gato que sobrescriban el método hacer_sonido para mostrar el sonido específico de cada animal.
class Animal():
    def __init__(self, nombre_animal):
        self.nombre_animal = nombre_animal
        pass
    def hacer_sonido(self):
        return f"este animal: {self.nombre_animal} hace un sonido"
    
class Perro(Animal):
    def __init__(self, nombre_animal):
        super().__init__(nombre_animal)

    def hacer_sonido(self):
        return F"{super().hacer_sonido()} y es: Guau Guau"
class Gato(Animal):
    def __init__(self, nombre_animal):
        super().__init__(nombre_animal)
    def hacer_sonido(self):
        return f"{super().hacer_sonido()} y es: Miau Miau"
    
animal1 = Perro("perro")
print(animal1.hacer_sonido())
animal2 = Gato("gato")
print(animal2.hacer_sonido())
    
# Ejercicio 17: 
# Define una clase base Electrodomestico con un método encender. 
# Luego, crea clases derivadas Refrigerador y Microondas que sobrescriban el método encender con el comportamiento específico de cada electrodoméstico.
class Electrodomestico():
    def __init__(self, nombre_Electrodomestico):
        self.nombre_Electrodomestico = nombre_Electrodomestico
        pass
    def encender(self):
        return F"este: {self.nombre_Electrodomestico} es un Electrodomestico"

class Refrigerador(Electrodomestico):
    def __init__(self, nombre_Electrodomestico):
        super().__init__(nombre_Electrodomestico)
    def encender(self):
        return f"{super().encender()} y se enciende lentamente"
class Microondas(Electrodomestico):
    def __init__(self, nombre_Electrodomestico):
        super().__init__(nombre_Electrodomestico)

    def encender(self):
        return f"{super().encender()} y se enciende rapidamente"
    
dato1 = Refrigerador("refrigeradora samsung")
print(dato1.encender())
dato2 = Microondas("microondas LG")
print(dato2.encender())
         
# Ejercicio 18: 
# Crea una clase base Figura con un método calcular_area. 
# Luego, define clases derivadas Circulo y Triangulo que sobrescriban el método calcular_area para calcular el área de cada figura.
import math
class Figura():
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area_circulo = math.pi * (self.radio ** 2)
        return f"El área del círculo es: {area_circulo:.0f}"

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area_triangulo = (self.base * self.altura) / 2
        return f"El área del triángulo es: {area_triangulo:.0f}"

figura1 = Circulo(6)
print(figura1.calcular_area())
figura2 = Triangulo(4, 8)
print(figura2.calcular_area())

# Ejercicio 19: 
# Define una clase base Transporte con un método capacidad. 
# Luego, crea clases derivadas Autobus y Moto que sobrescriban el método capacidad para mostrar la cantidad de pasajeros que puede llevar cada tipo de transporte.
class Transporte():
    def __init__(self, cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre
    def capacidad(self):
        pass
class Autobus(Transporte):
    def __init__(self, cantidad, nombre):
        super().__init__(cantidad, nombre)
    def capacidad(self):
        return f"este es un: {self.nombre} y tiene una capacidad de: {self.cantidad} pasajeros"
class Moto(Transporte):
    def __init__(self, cantidad, nombre):
        super().__init__(cantidad, nombre)

    def capacidad(self):
        return f"este es un: {self.nombre} y tiene una capacidad de: {self.cantidad} pasajeros"

tr1 = Autobus(25, "Bus")
print(tr1.capacidad())
tr2 = Moto(2, "motocicleta")
print(tr2.capacidad())

# Ejercicio 20: 
# Define una clase base Persona con un método saludar. 
# Luego, crea clases derivadas Estudiante y Profesor que sobrescriban el método saludar para mostrar cómo saluda cada tipo de persona.
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return f"esta persona: {self.nombre} saluda"
        pass
class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def saludar(self):
        return f"{super().saludar()} de una forma alegre, por que es un estudiante"
    
class Profesor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def saludar(self):
        return f"{super().saludar()} de una forma amarga, ya que es un profesor"
    
persona = Estudiante("Alex")
print(persona.saludar())
persona1 = Profesor("Carlos")
print(persona1.saludar())

########## otra manera ############
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def saludar(self):
        return f"Esta persona: {self.nombre} saluda"

class Estudiante(Persona):
    def saludar(self):
        return f"{super().saludar()} de una forma alegre, porque es un estudiante"
    
class Profesor(Persona):
    def saludar(self):
        return f"{super().saludar()} de una forma amarga, ya que es un profesor"

persona = Estudiante("Alex")
print(persona.saludar())
persona1 = Profesor("Carlos")
print(persona1.saludar())
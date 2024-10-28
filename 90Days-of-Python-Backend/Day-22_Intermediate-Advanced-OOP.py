### Día 22: Programación Orientada a Objetos (POO) nivel: intermedio-avanzado

#### Definición del Tema
#Programación orientada a objetos (POO) en Python, incluyendo clases, objetos, métodos, herencia, polimorfismo y conceptos más avanzados de POO.

#### Tips del Tema
# - **Clases:** Plantillas para crear objetos (instancias de clase). Definen atributos y métodos.
# - **Objetos:** Instancias de clases que pueden tener sus propios valores de atributos.
# - **Métodos:** Funciones definidas dentro de una clase que operan sobre sus atributos.
# - **Herencia:** Mecanismo para crear una nueva clase usando atributos y métodos de una clase existente.
# - **Polimorfismo:** Capacidad de usar una sola interfaz para representar diferentes tipos de datos.
# - **Encapsulación:** Agrupación de datos y métodos que operan sobre los datos dentro de una única unidad, restringiendo el acceso a algunos de los componentes del objeto.

# Definir una clase
class Perro:
    # Método inicializador
    def __init__(self, nombre, edad):
        self.nombre = nombre # atributo
        self.edad = edad

    # Método de instancia
    def ladrar(self):
        return f"{self.nombre} está ladrando." # metodo

# objetos de la clase
mi_perro = Perro("Firulais", 5)
otro_perro = Perro("Rex", 3)

print(mi_perro.nombre)      
print(mi_perro.ladrar())     
print(otro_perro.nombre)     
print(otro_perro.ladrar())  

# Definir una clase Persona con atributos nombre, edad y métodos para presentarse y celebrar_cumpleaños que aumente la edad en 1.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

    def celebrar_cumpleaños(self):
        self.edad += 1
        return f"Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años."

# Crear un objeto de la clase
persona = Persona("Alice", 30)
print(persona.presentarse())          
print(persona.celebrar_cumpleaños())  

# Implementa una jerarquía de clases con Forma como clase base y Rectangulo y Circulo como clases derivadas. 
# Incluir métodos para calcular el área y el perímetro de cada forma.
class Forma:
    def area(self):
        raise NotImplementedError("La subclase debe implementar el método abstracto")

    def perimetro(self):
        raise NotImplementedError("La subclase debe implementar el método abstracto")

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.alto * self.ancho

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio

rect = Rectangulo(10, 20)
circulo = Circulo(5)

print(f"Área del rectángulo: {rect.area()}")        
print(f"Perímetro del rectángulo: {rect.perimetro()}")  
print(f"Área del círculo: {circulo.area()}")         
print(f"Perímetro del círculo: {circulo.perimetro()}")   

# Crear una clase Empleado con atributos nombre, posición, salario y métodos para promocionar (aumentando el salario) y degradar (disminuyendo el salario).
class Empleado:
    def __init__(self, nombre, posicion, salario):
        self.nombre = nombre
        self.posicion = posicion
        self.salario = salario

    def promocionar(self, cantidad):
        self.salario += cantidad # hacer la suma y actualizar el valor de self.salario
        return f"{self.nombre} ha sido promovido. Nuevo salario: {self.salario}"

    def degradar(self, cantidad):
        self.salario -= cantidad
        return f"{self.nombre} ha sido degradado. Nuevo salario: {self.salario}"

# Crear un objeto de la clase
empleado = Empleado("John", "Desarrollador", 50000)
print(empleado.promocionar(5000))
print(empleado.degradar(3000))   

# Conceptos Avanzados de POO
# Métodos de Clase y Métodos Estáticos

# Metodo clase: Un método de clase es un método que está vinculado a la clase y no a la instancia del objeto. 
# Esto significa que puede acceder y modificar el estado de la clase.

# Metodo estatic: no está vinculado a la clase o la instancia. No puede modificar el estado de la clase o de la instancia.

class OperacionesMatematicas:
    # Método de clase
    @classmethod
    def sumar(cls, a, b):
        return a + b

    # Método estático
    @staticmethod
    def multiplicar(a, b):
        return a * b

# Usar el método de clase
print(OperacionesMatematicas.sumar(10, 20))  

# Usar el método estático
print(OperacionesMatematicas.multiplicar(10, 20))  


##### Propiedades
class Rectangulo:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    @property
    def area(self):
        return self.__ancho * self.__alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self.__ancho = valor
        else:
            print("El ancho debe ser positivo")

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self.__alto = valor
        else:
            print("El alto debe ser positivo")

rect = Rectangulo(10, 20)
print(rect.area)  
rect.ancho = 15
print(rect.area)  
rect.alto = -10  
############# ejercicios
# Ejercicio 1: Define una clase Coche con atributos marca, modelo y año. Crea dos objetos de la clase y muestra sus atributos.
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar(self):
        print(f"Este carro: {self.marca}, modelo: {self.modelo} y del año: {self.año} esta en mi garage")
    
carro = Coche("toyota", "Supra", 2005)
carro1 = Coche("HYundai", "tucson", 2008)
carro1.mostrar()
carro.mostrar()

# Ejercicio 2: Añade un método acelerar a la clase Coche que imprima un mensaje indicando que el coche está acelerando. 
# Usa este método en los objetos creados en el ejercicio 1.
#técnica conocida como "monkey patching".agregando métodos o modificando atributos existentes, aunque no es una buena practica es mejor añadir todos los metodos.
# a la hora de construir la clase.
def acelerar(self): # crear el metodo para la clase
    print(f"este carro: {self.marca} esta acelerando")
Coche.acelerar = acelerar # añadir el metodo a la clase
carro.acelerar() # usar los objetos de la clase anterior con el nuevo metodo 

def inventario(self):
    print(f"este modelo: {self.año} si esta en el inventario")
Coche.inventario = inventario
carro.inventario()

def precio(self):
    print(f"este modelo: {self.modelo} esta en oferta")
Coche.precio = precio
carro.precio()

# Ejercicio 3: Define una clase Persona con atributos nombre y edad. Añade un método saludar que imprima un saludo con el nombre de la persona.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"hola mucho gusto me llamo: {self.nombre} y tengo: {self.edad}")
dato = Persona("Alex", 30)
dato.saludar()

# Ejercicio 4: Define una clase Estudiante que herede de la clase Persona del ejercicio 3. Añade un atributo curso y un método estudiar 
# que imprima un mensaje indicando que el estudiante está estudiando en su curso.
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"el estudiante: {self.nombre}, esta estudiando el curso: {self.curso}")

materia = Estudiante("rodri", 45, "informatica")
materia.estudiar()

# Ejercicio 5: Define una clase Rectangulo con atributos base y altura. Añade métodos para calcular el área y el perímetro del rectángulo.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):
        area = self.altura * self.base
        print(f"el area del rectangulo es: {area}")
    
    def perimetro_rectangulo(self):
        perimetro = 2 * (self.altura + self.base)
        print(f"el perimetro del rectangulo es: {perimetro}")

dato_area = Rectangulo(2, 8)
dato_area.area_rectangulo()
dato_area.perimetro_rectangulo()
        
# Ejercicio 6: Define una clase Círculo con atributo radio. Añade métodos para calcular el área y la circunferencia del círculo.
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        pass
    def area_circulo(self):
        area = 3.14 * self.radio ** 2
        print(f"el area de este circulo es: {area}")

    def circunferencia_circulo(self):
        circunferencia = 2 * 3.14 * self.radio
        print(f"la circunferencia es de: {circunferencia}")
datos = Circulo(8)
datos.area_circulo()
datos.circunferencia_circulo()

# Ejercicio 7: Define una clase Triangulo con atributos lado1, lado2 y lado3. Añade métodos para calcular el área y el perímetro del triángulo.
# 3. area de triangulo b * a / 2 .... perimetro: lado1 + lado2 + lado3
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        pass
    def area_triangulo(self):
        # Usar la fórmula de Herón para calcular el área de cualquier triángulo
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        print(f"el area del triangulo es de: {area}")

    def perimetro_triangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        print(f"el perimetro del triangulo es de: {perimetro}")
numeros = Triangulo(4,8,4)
numeros.area_triangulo()
numeros.perimetro_triangulo()

# Ejercicio 8: Define una clase CuentaBancaria con atributos titular y saldo. Añade métodos para depositar, retirar y mostrar el saldo de la cuenta.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        pass
    def depositar(self, deposito):
        self.saldo += deposito
        return f"el titular: {self.titular} realizo un deposito de: {deposito} y su nuevo saldo es: {self.saldo}"
    def retirar(self, cantidad):
        self.saldo -= cantidad
        return f"el señor: {self.titular} retiro una suma de: {cantidad} colones y ahora su saldo es de {self.saldo} colones"
    def mostrar(self):
        return f"el saldo del titular: {self.titular}, es de: {self.saldo}"
    
persona = CuentaBancaria("alex", 195000)
print(persona.depositar(25000))
print(persona.retirar(50000))
print(persona.mostrar())

# Ejercicio 9 (Teoría): Explica qué es la herencia en la programación orientada a objetos y cuál es su utilidad.
# La herencia es un principio en la Programación Orientada a Objetos (POO) que permite a una clase, llamada subclase o clase derivada, 
# heredar atributos y métodos de otra clase, conocida como superclase o clase base. La herencia facilita la reutilización del código, 
# permitiendo que las subclases reutilicen y extiendan las funcionalidades de la superclase. También permite la creación de jerarquías de clases y el polimorfismo, 
# donde diferentes subclases pueden implementar métodos con el mismo nombre pero con comportamientos distintos.

# Ejercicio 10 (Práctica): Define una clase Empleado con atributos nombre, apellido y sueldo. 
# Define una clase Gerente que herede de Empleado y añade un atributo departamento. 
# Override el método de impresión para que muestre el nombre, apellido y departamento del gerente.
class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        pass
class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, departamento):
        super().__init__(nombre, apellido, sueldo)
        self.departamento = departamento
    def impresion(self):
        return f"Este empleado de nombre: {self.nombre} {self.apellido} es del depártamento de: {self.departamento}"
    
empleo = Gerente("eric", "edwards", 500000, "ventas")
print(empleo.impresion())

# Ejercicio 11
# Define una clase Libro con atributos titulo, autor y año_publicacion. Crea dos objetos de la clase y muestra sus atributos.
class Libro():
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def informacion(self):
        return f"El nombre del autor es: {self.autor} y el libro es: {self.titulo} y su año de publicacion es: {self.año_publicacion}"
informacio1 = Libro("El Cuervo", "Gabriel Garcia", 1985)
informacio2 = Libro("Sombras del pasado", "Eric Calvin", 1975)
print(informacio1.informacion())
print(informacio2.informacion())

##################################
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def __str__(self):
        return f"{self.titulo} de {self.autor}, publicado en {self.año_publicacion}"

informacio1 = Libro("El Cuervo", "Gabriel Garcia", 1985)
informacio2 = Libro("Sombras del pasado", "Eric Calvin", 1975)
print(informacio1)
print(informacio2)

# Ejercicio 12
# Añade un método resumir a la clase Libro que imprima un resumen del libro en el formato: "El libro 'titulo' fue escrito por autor en el año año_publicacion."
def resumir(self):
    return f"El libro {self.autor} fue escrito por autor en el año: {self.año_publicacion}"
Libro.resumir = resumir # añadir este metodo a la clase anterior, sin embargo no es una buena practica
print(informacio1.resumir())

# Ejercicio 13
# Define una clase Animal con un método hacer_sonido que imprima un sonido genérico. Luego, crea una clase Gato que herede de Animal y
# sobrescriba el método hacer_sonido para que imprima "Miau".
class Animal():
    def __init__(self, animal):
        self.animal = animal
    def hacer_sonido(self):
        return f"El animal hace un sonido"
        
class Gato(Animal):
    def __init__(self, animal):
        super().__init__(animal)
    def hacer_sonido(self):
        super().hacer_sonido()
        return f"{super().hacer_sonido()} y es Miau"
    
info = Gato("Felix")
print(info.hacer_sonido())

# Ejercicio 14
# Crea una clase Vehiculo con atributos marca, modelo y año. Define un método info que devuelva una cadena con la información del vehículo. 
# Luego, crea una clase Camion que herede de Vehiculo y añada un atributo capacidad_carga.
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def informacion_vehiculo(self):
        return f"Este vehiculo de marca: {self.marca}, modelo: {self.modelo} y del año: {self.año}"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def informacion_vehiculo(self):
        return f"{super().informacion_vehiculo()}, tiene una capacidad de carga de: {self.capacidad_carga} toneladas"
    
dato = Camion("Mac", "bost", 2001, 18000)
print(dato.informacion_vehiculo())

# Ejercicio 15
# Define una clase Cuenta con atributos titular y saldo. Añade métodos para depositar, retirar y mostrar_saldo. 
# Asegúrate de que no se pueda retirar más de lo que hay en el saldo.
class Cuenta():
    def __init__(self, Titular, Saldo):
        self.Titular = Titular
        self.Saldo = Saldo

    def depositar(self, Monto):
        self.Saldo += Monto 
        return f"El nuevo saldo despues de el deposito es: {self.Saldo}"
    
    def retirar(self, Monto):
        if Monto > self.Saldo:
            return "El monto a retirar es mayor que el saldo en su cuenta, ingrese un monto valido"
        else:
            self.Saldo -= Monto
            return f"El nuevo saldo despues de el retiro es: {self.Saldo}"
    
    def mostrar_saldo(self):
        return f"El saldo en tu cuenta bancaria es de: {self.Saldo}"
    
dato = Cuenta("Eric Hernandez", 250000)
print(dato.depositar(2500))
print(dato.retirar(1000000))
print(dato.mostrar_saldo())

# Ejercicio 16
# Crea una clase Producto con atributos nombre, precio y stock. Añade métodos para vender (disminuyendo el stock) y reabastecer (aumentando el stock).
class Producto():
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            return "No hay suficiente stock para realizar la venta."
        self.stock -= cantidad
        return f"Después de la venta, el stock se ha disminuido y ahora es de: {self.stock}"
    
    def reabastecer(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a reabastecer debe ser mayor que cero."
        self.stock += cantidad
        return f"El stock ha aumentado y ahora es de: {self.stock}"
    
dato = Producto("Taladro", 250000, 25)
print(dato.vender(10))
print(dato.reabastecer(2))

# Ejercicio 17
# Define una clase Curso que tenga atributos nombre, codigo y estudiantes. Añade un método para inscribir_estudiante que añada 
# un estudiante a la lista de estudiantes.
class Curso():
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []
    
    def inscribir_estudiante(self, nombre_estudiante):
        if nombre_estudiante.lower() in self.estudiantes: # para evitar el duplicado de nombres
            return f"El estudiante {nombre_estudiante} ya está inscrito."
        self.estudiantes.append(nombre_estudiante)
        return F"esta es la lista de estudiantes: {self.estudiantes}"
    
dato = Curso("Ciencias", 21)
print(dato.inscribir_estudiante("helen"))
print(dato.inscribir_estudiante("alex"))
print(dato.inscribir_estudiante("Helen"))

# Ejercicio 18
# Crea una clase Ordenador con atributos marca, modelo y ram. Define un método que imprima las especificaciones del ordenador. 
# Luego, crea una subclase Portatil que añada un atributo peso.
class Ordenador():
    def __init__(self, marca, modelo, ram):
        if ram <= 0:
            raise ValueError("La RAM debe ser un número positivo.")
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
    
    def especificaciones(self):
        return f"Este ordenador de marca: {self.marca}, modelo: {self.modelo}, tiene una memoria ram de: {self.ram} GB"

class Portatil(Ordenador):
    def __init__(self, marca, modelo, ram, peso):
        super().__init__(marca, modelo, ram)
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        self.peso = peso

    def especificaciones(self):
        return F"{super().especificaciones()} y tambien tiene un peso de: {self.peso} gramos"
    
dato = Ordenador("HP", "LX", 18)
dato2 = Portatil("HP", "LX", 18, 1000)
print(dato.especificaciones())
print(dato2.especificaciones())

# Ejercicio 19
# Define una clase Empleado con atributos nombre, apellido y sueldo. Crea un método que calcule el sueldo anual. 
# Luego, crea una clase Vendedor que herede de Empleado y añada un atributo comision.
class Empleado():
    def __init__(self, nombre, apellido, sueldo):
        if sueldo < 0:
            raise ValueError("El sueldo debe ser un número positivo.")
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def sueldo_anual(self):
        nuevo_sueldo = self.sueldo * 12
        return f"El empleado: {self.nombre} {self.apellido} tiene un sueldo añual de: {nuevo_sueldo:.0f} colones"

class Vendedor(Empleado):
    def __init__(self, nombre, apellido, sueldo, comision):
        super().__init__(nombre, apellido, sueldo)
        if comision < 0:
            raise ValueError("La comisión debe ser un número positivo.")
        self.comision = comision

    def sueldo_anual(self):
        sueldo_anual_base = self.sueldo * 12
        sueldo_total = sueldo_anual_base + (sueldo_anual_base * self.comision / 100)
        return f"{super().sueldo_anual()} más una comisión del: {self.comision}% que totaliza: {sueldo_total:.0f} colones"
    
dato = Vendedor("Eric", "Calvin", 850000, 10)
print(dato.sueldo_anual())

# Ejercicio 20
# Crea una clase Juego con un método iniciar. Luego, define una clase JuegoDeMesa que herede de Juego 
# y sobrescriba el método iniciar para incluir un mensaje que indique que el juego de mesa ha comenzado.
class Juego():
    def __init__(self, juego):
        self.juego = juego
    def Iniciar(self):
        pass
class JuegoDeMesa(Juego):
    def __init__(self, juego):
        super().__init__(juego)

    def Iniciar(self):
        return f"El juego de mesa {self.juego} ha comenzado."
    
dato = JuegoDeMesa("domino")
print(dato.Iniciar())
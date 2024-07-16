# Día 14: Encapsulación y Abstracción en POO

# La encapsulación y la abstracción son dos principios clave de la POO que permiten:
# Encapsulación: Controlar el acceso a los datos dentro de un objeto, protegiendo su estado interno y solo exponiendo lo necesario a través de métodos públicos.
# Abstracción: Proporcionar una interfaz simplificada para interactuar con objetos sin revelar su implementación interna, lo que facilita su uso y mantenimiento.

# Tips del Tema
# 1-Encapsulación: Permite que los detalles internos de un objeto estén ocultos. 
# Esto se logra mediante el uso de atributos privados y métodos que actúan como la interfaz del objeto.
# 2-Abstracción: Simplifica la interacción con los objetos al proporcionar solo los métodos relevantes y ocultar el funcionamiento interno.
# 3-Accesibilidad: En Python, los atributos privados se indican con un guion bajo simple _ y los protegidos con dos guiones bajos __. 
# Esto es una convención que sugiere que esos atributos no deben ser accedidos directamente desde fuera de la clase.

################## Beneficios de la Encapsulación y Abstracción

# Seguridad: Al encapsular los datos, se protege la integridad del estado interno del objeto, previniendo modificaciones indeseadas.
# Mantenibilidad: Facilita el mantenimiento del código, ya que los cambios en la implementación interna no afectan a los usuarios de la clase, 
# siempre que la interfaz pública permanezca constante.
# Simplicidad: Proporciona una interfaz clara y simple, lo que facilita la comprensión y uso de la clase por otros desarrolladores.

##################### ejemplo

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular          # Atributo público
        self.__saldo = saldo            # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad      # Modifica el saldo interno

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:  # Verifica que el retiro sea válido
            self.__saldo -= cantidad        # Modifica el saldo interno

    def obtener_saldo(self):
        return self.__saldo                # Proporciona acceso al saldo

# Uso de encapsulación
cuenta = CuentaBancaria("Alice", 1000)
cuenta.depositar(500)                  # Deposita 500
cuenta.retirar(200)                    # Retira 200
print(cuenta.obtener_saldo())          # Salida: 1300

############### 

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca                 # Atributo público
        self.__modelo = modelo             # Atributo privado

    def mostrar_info(self):
        return f"{self.marca} - {self.__modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)   # Llama al constructor de la clase base
        self.__puertas = puertas           # Atributo privado

    def mostrar_info(self):
        return f"{super().mostrar_info()} - {self.__puertas} puertas"

# Uso de encapsulación y abstracción
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.mostrar_info())         # Salida: Toyota - Corolla - 4 puertas

# ############### ejerciios
# Ejercicio 1: Define una clase Persona con atributos públicos nombre y edad, y un atributo privado __saldo. 
# Añade métodos para modificar y obtener el saldo.
class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo
    
    def modificar(self):
        self.__saldo -= self.__saldo * 0.13 # -= resta y asignar
        return f"este es el saldo mofidificado: {self.__saldo} de la persona de nombre {self.nombre}"
    
    def obtener(self):
        salario = self.__saldo
        return f"esta persona: {self.nombre} tiene un saldo de {salario}"
    
saldos = [
    Persona("eric", 25, 320000),
    Persona("alex", 28, 320000)
]
for sal in saldos:
    salt = sal.modificar()
    saol = sal.obtener()
    print(salt)
    print(saol)

# Ejercicio 2: Crea un objeto de la clase Persona y prueba los métodos para modificar y obtener el saldo.
objeto = Persona("edwards", 30, 50000)
print(objeto.modificar())
print(objeto.obtener())

# Ejercicio 3: Define una clase Producto con atributos públicos nombre y precio, y un atributo privado __stock. 
# Añade métodos para modificar y obtener el stock.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock

    def modificar(self):
        cantidad = 5
        if self.__stock >= cantidad:
            self.__stock -= cantidad
            return f"Después de la modificación, el stock es {self.__stock}"
        else:
            return "No hay suficiente stock para realizar la modificación"
    
    def obtener_stock(self):
        return f"El producto {self.nombre} tiene un stock de {self.__stock} "
        
    
cosas = Producto("llave francesa", 22500, 100)
print(cosas.modificar())
print(cosas.obtener_stock())

# Ejercicio 4: Crea una lista de objetos Producto y escribe un programa que muestre el stock de cada producto usando los métodos definidos.
lista = [
    Producto("pala", 22500, 500),
    Producto("pico", 22800, 50),
    Producto("puño", 28500, 20),
    Producto("cemento", 29500, 100)
]

for ferre in lista:
    inventory = ferre.obtener_stock()
    # print(f"Producto: {ferre.nombre} - {inventory}")
    print(f"{inventory}") 

# Ejercicio 5: Define una clase Vehiculo con atributos públicos marca y modelo, y un atributo privado __kilometraje. 
# Añade métodos para modificar y obtener el kilometraje.
class Vehiculo:
    def __init__(self, marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = kilometraje
    def modificar(self):
        tiempo_de_circulacion = 2024 - self.modelo
        return f"El vehiculo de marca {self.marca} tiene {tiempo_de_circulacion} años de circulacion"
    def obtener_kilometraje(self):
        return f"Este Vehiculo {self.marca} tiene {self.__kilometraje} kilometros de kilometraje"
carro = Vehiculo("maserati", 2012, 8000)
print(carro.modificar())
print(carro.obtener_kilometraje())
        
# Ejercicio 6: Crea una lista de objetos Vehiculo y escribe un programa que muestre el kilometraje de cada vehículo usando los métodos definidos.
vehiculos = [
    Vehiculo("toyota", 2022, 20000),
    Vehiculo("bently", 2023, 10000),
    Vehiculo("ford", 2016, 8000),
    Vehiculo("subaru", 2020, 5000)
]
for car in vehiculos:
    print(car.obtener_kilometraje())

# Ejercicio 7: Define una clase Empleado con atributos públicos nombre y puesto, y un atributo privado __salario. Añade métodos para modificar y obtener el salario.
class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.__salario = salario
    
    def modificar(self):
        self.__salario = self.__salario * 0.13
        return f"El empleado {self.nombre} tiene una modificacion en el salario de {self.__salario}"
    
    def obtener_el_salario(self):
        return f"El empleado {self.nombre} tiene un salario bruto de {self.__salario}"
    
salary = Empleado("alexander", "ventas", 500000)
print(salary.modificar())
print(salary.obtener_el_salario())

# Ejercicio 8: Crea una lista de objetos Empleado y escribe un programa que muestre el salario de cada empleado usando los métodos definidos.
planilla = [
    Empleado("alex", "RRHH", 320000),
    Empleado("rosa", "ventas", 720000),
    Empleado("luis", "Desarrollo", 520000),
    Empleado("maria", "Seguridad", 420000)
]
for plan in planilla:
    print(plan.obtener_el_salario())

# Ejercicio 9 (Teoría): ¿Qué es la encapsulación y cómo mejora la seguridad y mantenibilidad del código en POO?
# la encapsulacion es un metodo de seguridad en POO, previene el acceso no autorizado a los datos con eso le brinda seguridad aun atributo, 
# ya que estos por defecto son publicos y esto no es una buena buena practica dependiendo de la situacion. 
# Este proceso se realiza con __ despues del sefl. asi protejemos los datos de ese atributo.

# Ejercicio 10 (Práctica): Escribe un programa que defina una clase CuentaBancaria con atributos privados __titular y __saldo, y métodos para depositar, 
# retirar y obtener el saldo. Crea un objeto de CuentaBancaria y prueba los métodos definidos.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self):
        self.__saldo += self.__saldo + 0.20
        return f"El empleado {self.__titular} va a depositar ala CuentaBancaria un 20% de su pagol, osea su nuevo saldo es: {self.__saldo} mil colones"

    def retirar(self):
        cantidad = 10000
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"{self.__titular} ha retirado {cantidad} mil colones. Nuevo saldo: {self.__saldo} mil colones."
        else:
            return f"No se puede retirar {cantidad} mil colones. Saldo insuficiente."

    def obtener_el_saldo(self):
        return f"El empleado {self.__titular} sabe que su saldo en CuentaBancaria es de {self.__saldo} mil colones"
    
estado = CuentaBancaria("Gregorio", 520000)
print(estado.depositar())
print(estado.retirar())
print(estado.obtener_el_saldo())
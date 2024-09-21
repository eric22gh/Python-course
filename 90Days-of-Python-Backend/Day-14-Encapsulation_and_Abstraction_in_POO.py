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
        self.__saldo = saldo            # Atributo protegido _ atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad      # Modifica el saldo interno

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:  # Verifica que el retiro sea válido
            self.__saldo -= cantidad        # Modifica el saldo interno

    def obtener_saldo(self):
        return self.__saldo                

# encapsulación
cuenta = CuentaBancaria("Alice", 1000)
cuenta.depositar(500)                  
cuenta.retirar(200)                    
print(cuenta.obtener_saldo())          

############### 

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca                 # Atributo público
        self.__modelo = modelo             # Atributo privado

    def mostrar_info(self):
        return f"{self.marca} - {self.__modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)   # Llamar al constructor de la clase base
        self.__puertas = puertas           

    def mostrar_info(self):
        return f"{super().mostrar_info()} - {self.__puertas} puertas"

# encapsulación y abstracción
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.mostrar_info())        

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

# Ejercicio 11: 
# Define una clase Libro con atributos públicos título y autor, y un atributo privado __precio.
# Añade métodos para modificar y obtener el precio.
class Libro():
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio
    
    def modificar(self, descuento):
        if 0 <= descuento <= 1:
            monto = self.__precio * descuento
            self.__precio -= monto
            return f"Este es el precio modificado del libro: {self.__precio:.0f} colones del autor: {self.autor}"
          
        else:
            return "Descuento no válido"
    
    def obtener(self):
        return f"El libro '{self.titulo}' tiene un precio de {self.__precio} colones"
    
dato1 = Libro("el cuervo", "Gabriel", 25000)
print(dato1.modificar(0.15))
dato2 = Libro("cronicas","homero", 20000)
print(dato2.obtener())

# Ejercicio 12:
# Crea una lista de objetos Libro y escribe un programa que muestre el precio de cada libro usando los métodos definidos.
lista = [
    Libro("el cuervo", "Gabriel", 25000),
    Libro("Monster", "Rodrigo perez", 24000),
    Libro("Cronicas", "Gabriel marquez", 20000),
    Libro("Homero", "socrates", 26000),
    Libro("El principito", "frida khalo", 21000)
]
for precio in lista:
    print(precio.obtener())

# Ejercicio 13:
# Define una clase Estudiante con atributos públicos nombre y edad, y un atributo privado __nota.
# Añade métodos para modificar y obtener la nota.
class Estudiante():
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.__nota = nota
    
    def modificar(self, puntos):
        if puntos < self.__nota:
            self.__nota -= puntos
        else:
            self.__nota = 0  # Evitar que la nota sea negativa
        return F"Esta es la nota modificada: {self.__nota}"
    
    def obtener(self):
        return f"Alumno: {self.nombre} esta es su nota: {self.__nota}"
    
alumno1 = Estudiante("eric", 25, 89)
print(alumno1.modificar(12))
alumno2 = Estudiante("alex", 22, 98)
print(alumno2.obtener())

# Ejercicio 14:
# Crea una clase Banco con atributos privados __nombre y __cuentas (una lista de objetos de tipo CuentaBancaria).
# Añade métodos para agregar cuentas y mostrar el saldo de todas las cuentas.
class Banco():
    def __init__(self, nombre, cuentas, saldo):
        self.__nombre = nombre
        self.__cuentas = cuentas
        self.__saldo = saldo

    def agregar_cuentas(self):
        lista1.append(Banco(self.__nombre, self.__cuentas, self.__saldo))

    def mostrar(self):
        return f"Este es el saldo: {self.__saldo} colones de esta cuenta: {self.__nombre}"
        
lista1 = [
    Banco("eric", "2568-6589-2", 250000),
    Banco("alice", "2568-6500-6", 19500),
    Banco("marcos", "2568-0001-2", 200000)
]
dato1 = Banco("beto", "5878-2345-5", 30000) 
dato1.agregar_cuentas()  

for saldo in lista1:
    print(saldo.mostrar())
        
# Ejercicio 15:
# Define una clase Casa con atributos públicos dirección y tamaño, y un atributo privado __precio.
# Añade métodos para modificar y obtener el precio.
class Casa():
    def __init__(self, direccion, tamaño, precio):
        self.direccion = direccion
        self.tamaño = tamaño
        self.__precio = precio
    def modificar(self, devaluacion):
        monto = self.__precio * devaluacion
        self.__precio -= monto
        return F"Este es el precio modificado con la devaluacion del area: {self.__precio:.0F} colones"
    def obtener(self):
        return f"Este es el precio: {self.__precio:.0F} colones de esta vivienda con tamaño de: {self.tamaño}"
    
casa1 = Casa("Ciudad de nueva york, contiguo al central park","100mts", 1000000)
print(casa1.modificar(0.15))
print(casa1.obtener()) # esto es polimorfismo, el mismo objeto reacciona diferente segun el metodo

# Ejercicio 16:
# Define una clase Juego con atributos públicos título y género, y un atributo privado __rating.
# Añade métodos para modificar y obtener el rating.
class Juego():
    def __init__(self, titulo, genero, rating):
        self. titulo = titulo
        self.genero = genero
        self.__rating = rating
    
    def modificar(self, puntos_negativos):
        self.__rating -= puntos_negativos
        if self.__rating >= 0:
            return f"Este es el nuevo ranting de este juego despues de la actualizacion es: {self.__rating}"
        else: 
            return F"El ranking no puede tener un numero negativo"
    
    def obtener(self):
        return f"Aqui tenemos el ranking: {self.__rating} de este juego: {self.titulo}"
    
juego1 = Juego("until Dawn", "suspenso", 10)
print(juego1.modificar(2))
print(juego1.obtener())

# Ejercicio 17:
# Crea una lista de objetos Juego y escribe un programa que muestre el rating de cada juego usando los métodos definidos.
lista_juegos = [
    Juego("Leaf for dead", "Zombies", 7),
    Juego("Horizon", "Aventura", 2),
    Juego("Mortal Kombat", "Peleas", 6),
    Juego("DB Budokai", "Peleas", 5),
    Juego("the evil within", "Terror", 9)
]
for Posicion in lista_juegos:
    print(Posicion.obtener())

# Ejercicio 18:
# Define una clase TarjetaCredito con atributos públicos número y titular, y un atributo privado __limite.
# Añade métodos para modificar y obtener el límite de crédito.
class TarjetaCredito():
    def __init__(self, numero, titular, limite):
        self.numero = numero
        self.titular = titular
        self.__limite = limite
    
    def modificar(self, ganancia_banco):
        if self.__limite -ganancia_banco >= 0: # validacion, para que no de negativo
            self.__limite -= ganancia_banco
            return f"Este es su limite de credito despues de la modificacion: {self.__limite}"
        else:
            return "No es posible modificar el limite, el valor resultante es negativo."
    
    def obtener(self):
        return f"Este es su credito total: {self.__limite} colones"

tarjeta = TarjetaCredito("1236-5698-8975", "Eric Edwards", 250000)
print(tarjeta.modificar(23000))
print(tarjeta.obtener())

# Ejercicio 19:
# Crea una clase Empresa con atributos privados __nombre y __salarios (una lista de objetos Empleado).
# Añade métodos para agregar empleados y mostrar los salarios de todos los empleados.
class Empresa():
    def __init__(self):
        self.__empleados = []

    def agregar_empleados(self, nombre, salario):
        self.__empleados.append(Empleado(nombre, salario))

    def mostrar_salarios(self):
        for empleado in self.__empleados:
            print(f"El empleado: {empleado.nombre} tiene un salario de: {empleado.salario} colones")

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

empresa = Empresa()
empresa.agregar_empleados("Eric Edwards", 520000)
empresa.agregar_empleados("Helen Brenes", 320000)
empresa.agregar_empleados("Carlos Mora", 820000)
empresa.mostrar_salarios()

# Ejercicio 20:
# Escribe un programa que defina una clase Dispositivo con atributos privados __marca, __precio y __modelo,
# y métodos para modificar y obtener la información del dispositivo.
class Dispositivo():
    def __init__(self, marca, precio, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    def modificar(self, devaluacion):
        if devaluacion > self.__precio:
            return "La devaluación no puede ser mayor que el precio."
        self.__precio -= devaluacion
        return f"El nuevo precio después de la devaluación es: {self.__precio} colones."
    
    def obtener(self):
        return f"Esta es la informacion de el siguiente dispositivo: {self.__marca}, modelo: {self.__modelo} y precio: {self.__precio}"
    
Dispositivo1 = Dispositivo("Samsung", 256000, "Galaxy L200")
print(Dispositivo1.modificar(32000))
print(Dispositivo1.obtener())
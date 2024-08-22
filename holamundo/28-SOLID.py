#### los principios de solid #####
# mantenibildad, reutilizabilidad, legibilidad, estensibilidad

# Los principios SOLID en Programación Orientada a Objetos (POO) son un conjunto de cinco directrices de diseño
# que ayudan a crear software más flexible, mantenible y escalable.

# 1- Single Responsibility Principle (SRP): Cada clase debe tener una única responsabilidad o razón para cambiar,
# es decir, debe estar enfocada en realizar una sola tarea.

# 2- Open/Closed Principle (OCP): Las clases deben estar abiertas a la extensión, pero cerradas a la modificación. 
# Esto significa que puedes agregar nuevas funcionalidades sin alterar el código existente.

# 3- Liskov Substitution Principle (LSP): Los objetos de una clase derivada deben poder sustituir a los objetos de su clase base 
# sin alterar el comportamiento del programa.

# 4- Interface Segregation Principle (ISP): Es preferible tener interfaces pequeñas y específicas que muchas clases implementen, 
# en lugar de una interfaz grande que obligue a las clases a implementar métodos que no utilizan.

# 5- Dependency Inversion Principle (DIP): Las clases deben depender de abstracciones (interfaces) y no de clases concretas. 
# Esto reduce el acoplamiento entre los módulos del software.

# ejemplo: # 1- Single Responsibility Principle (SRP) que cada clase haga solo una cosa y si una clase hace 2 se tiene que separar
class auto():
    def __init__(self, tanque) -> None:
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("ho hay combustible")

class TanqueDeCombustible:
    def __init__(self) -> None:
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanke = TanqueDeCombustible()
auto = auto(tanke)

# segundo principio, 2- Open/Closed Principle (OCP), agregar nuevas funcionalidades sin alterar el código existente.
# no es bueno moidificar el codigo de una clase, se parar el programa por partes pequeñas
class Notificar:
    def __init__(self, user, msj) -> None:
        self.user = user
        self.msj = msj
    # se ocupa notificar x correo y x msj entoces hay que dividir eso
    def notificar(self):
        raise NotImplementedError

class NotificarCorreo(Notificar):
    def notificar(self):
        print(f"se envio el msj por correo {self.user}")

class NotificarMsj(Notificar):
    def notificar(self):
        print(f"se envio el mensaje a {self.user}")

# tercer principio Liskov Substitution Principle (LSP); si b es una subclase de a, los objetos de la b puede usar la clase a
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "estoy volando"
class AveNovuela(Ave):
    pass

# cuarto principio Interface Segregation Principle (ISP): no depender de una interfaz para todo
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class durmiendo(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, durmiendo):

    def comer(self):
        print("el humano come")

    def trabajar(self):
        print("el humano trabaja")

    def dormri(self):
        print("el humano duerme")

class Robbot(Trabajador):

    def trabajar(self):
        print("el robbot trabaja")

robot = Robbot()
human = Humano()

robot.trabajar()
human.comer()
human.dormir()
human.trabajar()

# quinto principio solid, Dependency Inversion Principle (DIP): los modulos de alto nivel y bajo nivel, dependen de las adstracciones
# y no de ellos mismos y las abstraciones no depender de los detalles si no que alrevez.
# limitacion
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

class Application:
    def __init__(self):
        self.database = MySQLDatabase()

    def run(self):
        self.database.connect()
        print("Running application...")
        self.database.disconnect()
# la clase applicacion depende de la mysql y si hay otro tipo no va a poder
app = Application()
app.run()

################# correctamente
from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")
# applicacion depende de msql y postgre y no de database que es la clase principal
class Application:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        self.database.connect()
        print("Running application...")
        self.database.disconnect()

mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.run()

postgresql_db = PostgreSQLDatabase()
app = Application(postgresql_db)
app.run()

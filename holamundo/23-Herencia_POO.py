### henrencia en programacion orientada a objetos #####
## heredar los altributos de una clase ya hecha a otra clase distinta

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        pass
    def hablar(self):
        return f"hola, estoy hablando"

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario):
        super().__init__(nombre, edad, nacionalidad) # super() hace que herede los atributos de la clase anterior
        self.salario = salario
    pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, ubicacion):
        super().__init__(nombre, edad, nacionalidad) # super() hace que herede los atributos de la clase anterior
        self.ubicacion = ubicacion
    pass

roberto = Empleado("alex", 56, "argentino", 850000)
print(roberto.hablar())

############## herencia multiple ###

class Artitas:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad
        pass

    def mostrar(self):
        return f"mi habilidad es: {self.habilidad}"
    
class EmpleadoArtista(Persona, Artitas): # herencia multiple, varios metedos de otras clases a una sola clase
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artitas.__init__(self, habilidad)
        self.salario = salario

    def presentar(self):
        return f"hol soy: {self.nombre} y {super().mostrar()} y mi pais es: {self.nacionalidad}" # no solo se pueden retornar los datos, tambien los metodos de otras clases

dop = EmpleadoArtista("eric", 25, "mexicano", "cantar", 850000)
print(dop.presentar())

### verificar si X clase pertenece a una clase
herencia = issubclass(EmpleadoArtista, Estudiante)
instancia = isinstance(dop, EmpleadoArtista) # si ese dato o objeto pertenece a esa clase
print(instancia)

######## que pasa si 2 clases tiene el mismo nombre de metodo y atributo, cual de estos datos va a tomar el objeto
# esto se arregla con el MRO(movimento rectilineo uniforme) :orden en el que python busca metodos yb atributos en las clases

class A:
    def hablar(self):
        print("hola des A")
    pass

class B(A):
    # def hablar(self):
    #     print("hola des B")
    pass

class C(A):
    # def hablar(self):
    #     print("hola des C")
    pass
class F(A):
    # def hablar(self):
    #     print("hola des F")
        pass

class D(B, C, F): # asi tambien define la prioridad la primera es de D, si no existe el metodo pasa a B y si no lo encuentra pasa ah C y si no va a A
    # def hablar(self):
    #     print("hola des D")
    pass


d = F()
d.hablar()
print(D.mro())
F.hablar(A) # llamar a la clase F con el metodo de la clase A

#############

class Personas:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        pass # pasar sus atributos

    def mostrar_datos(self):
        return f"nombre: {self.nombre}"
        return f"edad: {self.edad}"
    
class Estudent(Personas):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        return f"mostrar grado: {self.grado}"
    
student = Estudent("luis", 28, "quinto año")
print(student.mostrar_grado())
print(student.mostrar_datos())

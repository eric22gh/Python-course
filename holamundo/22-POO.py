#### introduccion a programacion orientada a objetos, es una forma de programar #####
# ventajas: escalbilidad, modulacion; legibilidad, reutilizacion de codigo

#### objetos: entidades del mundo real = datos
#### clases: nos permite escribir las caracteristicas que va a tener el objeto
#### atributos: son variables que pertenecen a una clase
#### metodos: es una funcion que dentro de una clase se convierte en metodo

########### clases y objetos
class Celular:
    # atributos estaticos son modificables afuera de la clase
    marca = "samsung"
    modelo = "s24"
    camara = "48mp"

# objetos es una instancia de una clase
Celular1 = Celular()
Celular2 = Celular()
Celular3 = Celular()

print(Celular1.camara)
print(Celular2.marca)
print(Celular3.modelo)

##### atributos

class telefono:
    # atributos
    def __init__(self, marca, modelo, camara): # __init__ ejecuta la funcion o metodo constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

phone = telefono("samsung", "s25", "100mp")
phone1 = telefono("apple", "15", "10mp")
phone2 = telefono("huawei", "p60", "800mp")

print(phone.camara)
print(phone.marca)
print(phone.modelo)

print(phone1.camara)
print(phone1.marca)
print(phone1.modelo)

print(phone2.camara)
print(phone2.marca)
print(phone2.modelo)

############### metodos

class Phones:
    def __init__(self, telefono, persona):
        self.telefono = telefono
        self.persona = persona
        
    # metodosS
    def llamar(self):
        return f"esta perosna: {self.persona} llamo con el telefono: {self.telefono}"
    
    def cortar(self):
        return f"esta persona: {self.persona} corto la llamada"
    
dato = Phones("samsung", "alex")
print(dato.llamar())
print(dato.cortar())

class Estudiante:
    def __init__(self, nombre, curso, edad, modalidad):
        self.nombre = nombre
        self.curso = curso
        self.edad = edad
        self.modalidad = modalidad
    
    def estudiar(self):
        return f"el estudiante: {self.nombre}, con una edad de: {self.edad} lleva el curso de: {self.curso} en modalidad: {self.modalidad}"
    
datos = Estudiante("alex", "informatica", 23, "presencial")
datos1 = Estudiante("lucia", "ciencias", 25, "virtual")
datos2 = Estudiante("victor", "fisica", 20, "presencial")
print(datos.estudiar())
print(datos1.estudiar())
print(datos2.estudiar())

while True:
    estudiar = input("ingresa estudiar1, estudiar2 o estudiar3:")
    if (estudiar.lower() == "estudiar1"):
        print(datos.estudiar())

    elif (estudiar.lower() == "estudiar2"):
        print(datos1.estudiar())

    elif (estudiar.lower() == "estudiar3"):
        print(datos2.estudiar())

#### classes; todo lo que esta adentro de una clase va a responder a una logica.

class persona:
    pass  # declaración nula que no realiza ninguna acción
print(persona)

class mipersona:
    def __init__(self, name, surname): # para q mipersona reciva algun parametro
        self.name = name
        self.surname = surname


my = mipersona("eric", "edwards")
print(my.name)
print(my.surname)
print(f"{my.name}{my.surname}")
print(mipersona) # no va a imprimir los valores que tiene la clase, hay que declararle la variable y 
# especificar q atributo se quiere imprimir de esa variable

class mipersona:
    def __init__(self, name, surname, alias = "sin alias"): # para q mipersona reciva algun parametro, se puede declarar una var dentro de una clase
        self.full_name = f"({name}) {surname} {alias}"

    def walk (self):
         print(f"{self.full_name} esta caminado")

my_eric = mipersona("eri", "hernan")
print(my_eric.full_name)
my_eric.walk()

my_ed = mipersona("alex", "edawrads")
print(my_ed.full_name)
my_ed.walk()

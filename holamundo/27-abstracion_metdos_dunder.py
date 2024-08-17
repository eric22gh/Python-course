### abstracion ####
# una interfaz simple que oculte la interfaz complicada

class auto():
    def __init__(self) -> None:
        self._stado = "apagado"
        pass

    def encender(self):
        self._stado = "encendido"
        print("el auto esta encendido")

    def conducir(self):
        if self._stado == "apagado":
                self.encender()
        print("conduciendo el auto")

mi_auto = auto() 
mi_auto.conducir() # abstracion

######## classes abstractas, es una clase que no podemos instanciar, es como una plantilla para crear otras clases
# implemntar un metodo definir las estrucciones que va a tener el metodo

# from abc import ABC, abstractmethod 

# class Persina(ABC):
#     @abstractmethod
#     def __init__(self, nombre, edad, sexo) -> None:
#         self.nombre = nombre
#         self.edad = edad
#         self.sexo = sexo
#         # super().__init__()
#     @abstractmethod
#     def trabajar(self):
#          pass
    
#     def presentar(self):
#         print(f"hola me llamo: {self.nombre} y soy {self.sexo} y tengo: {self.edad} años")

# eric = Persina("eric", 22, "male")
# eric.trabajar()

############### metodos dunder funciones que tiene un  metodo especial

class Carros:
    def __init__(self) -> None: # construye el objeto
         pass
    
    def __str__(self) -> str: ##  devolver una representacion del objeto en una cadena de texto
         pass
    
    def __repr__(self) -> str: ### 
         pass
######### descoradores #########
# el decorador le agrega mas funcionabilidad a una funcion ya sea antes o despues de ejecutarla

def decorador(funtion):
    def funcion_moficada(): # se llama la funcion anterior y esa a a este
        print("antes de llamar a la funcion")
        funtion()
        print("despues de llamar a la funcion")
    return funcion_moficada # retorna los datos de essta funcion

def saludo():
    print("hola")

saludo_modificado = decorador(saludo)
saludo_modificado()

############ propiedades: 

class MIclase:
    def __init__(self, atras, frente, medio):
        self._atras = atras # atributo privado
        self.__frente = frente # atributo privado
        self.medio = medio # publico
    @property 
    def get_mostre(self):
        return self.__frente
    # getters para mostrar el valor de un atributo privado

objeto = MIclase("si", "no mienta", "si lo estoy")
nombre = objeto.get_mostre 
# print(objeto.get_mostre())
print(nombre)
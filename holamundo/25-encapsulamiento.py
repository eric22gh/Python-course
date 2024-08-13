###### encapsulamiento
# Encapsulación: Controlar el acceso a los datos dentro de un objeto, protegiendo su estado interno y solo exponiendo lo necesario a través de métodos públicos.

# class MIclase:
#     def __init__(self, atras, frente, medio) -> None:
#         self._atras = atras # atributo privado
#         self.__frente = frente # atributo privado
#         self.medio = medio # publico
#         pass

# objeto = MIclase("no", 55, 2) ## va a dar error porque el self.__frente es privado, se resuelve con get + nombre del metodo
# print(objeto.__frente())

#### setters y getters

class MIclase:
    def __init__(self, atras, frente, medio):
        self._atras = atras # atributo privado
        self.__frente = frente # atributo privado
        self.medio = medio # publico
    
    def mostre(self):
        return self.__frente
    
    def get_mostre(self):
        return self.__frente
    # getters para mostrar el valor de un atributo privado

    def set_atras(self, new):
        self._atras = new
    # setter para actualizar un valor

objeto = MIclase("si", "no mienta", "si lo estoy")
print(objeto.get_mostre())

das = objeto.set_atras("alex")
print(das)

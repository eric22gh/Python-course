#### polimorfismo en POO, un metodo puede comportarse de diferente manera segun el tipo de objeto

class Gato():
    def sonido(self):
        return "miauu"
    
class Perro():
    def sonido(self):
        return "guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()
# polimorfismo con el objeto
hacer_sonido(Perro())
hacer_sonido(Gato())


###polimorfismo con el metodo
print(gato.sonido())
print(perro.sonido())

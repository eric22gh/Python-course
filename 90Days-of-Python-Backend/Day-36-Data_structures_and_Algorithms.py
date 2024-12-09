# Día 36: Operaciones con conjuntos

# Teoría:
# Los conjuntos en Python son colecciones no ordenadas de elementos únicos. Se utilizan para realizar operaciones matemáticas como uniones, 
# intersecciones y diferencias. Un conjunto se define utilizando llaves {} o la función set().

# Algunas operaciones básicas incluyen:
# Unión: Combina dos conjuntos.
# Intersección: Retorna los elementos comunes entre dos conjuntos.
# Diferencia: Retorna los elementos que están en un conjunto pero no en otro.
# Diferencia simétrica: Retorna los elementos que están en uno u otro conjunto, pero no en ambos.
# Adición: Agrega un elemento al conjunto.
# Remisión: Elimina un elemento del conjunto.


# Tips y Buenas Prácticas:
# Utiliza conjuntos cuando necesites almacenar elementos únicos y realizar operaciones de conjunto.
# Recuerda que los conjuntos no mantienen el orden de los elementos.
# Evita usar listas como elementos de un conjunto, ya que son mutables y causarán un error.

# Ejemplos:
# Operaciones de Conjuntos:
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión
union = conjunto_a | conjunto_b
print("Unión:", union)

# Intersección
interseccion = conjunto_a & conjunto_b
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto_a - conjunto_b
print("Diferencia (A - B):", diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto_a ^ conjunto_b
print("Diferencia simétrica:", diferencia_simetrica)

# Adición
conjunto_a.add(5)
print("Conjunto A con 5:", conjunto_a)

# Remisión
conjunto_b.remove(4)
print("Conjunto B sin 4:", conjunto_b)

# Discard
conjunto_a.discard(2)
print("Conjunto A sin 2:", conjunto_a)

# interseccion de dos conjuntos
conjunto_a.intersection_update(conjunto_b)
print("Conjunto A intersección de conjunto B:", conjunto_a)

# diferencia de dos conjuntos
conjunto_a.difference_update(conjunto_b)
print("Conjunto A diferencia de conjunto B:", conjunto_a)

# diferencia simétrica de dos conjuntos
conjunto_a.symmetric_difference_update(conjunto_b)
print("Conjunto A diferencia simétrica de conjunto B:", conjunto_a)

# isdisjoint
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
print("conjunto_a y conjunto_b son disjuntos:", conjunto_a.isdisjoint(conjunto_b))

# issubset
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print("conjunto_a es un subconjunto de conjunto_b:", conjunto_a.issubset(conjunto_b))

# issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print("conjunto_a es un superconjunto de conjunto_b:", conjunto_a.issuperset(conjunto_b))

# pop
conjunto_a = {1, 2, 3}
elemento = conjunto_a.pop()
print("Elemento eliminado:", elemento)

# union
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_unido = conjunto_a.union(conjunto_b)
print("Conjunto unido:", conjunto_unido)

# update
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_a.update(conjunto_b)
print("Conjunto A actualizado:", conjunto_a)

# Ejercicios:
# 1- Crea dos conjuntos y realiza la unión entre ellos.
con_1 = {1, 89, 580}
con_2 = {"eric", "alex"}
new = con_1 | con_2 # con_2.union(con_1)
print(new)

# 2- Encuentra la intersección de dos conjuntos de números.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print(conjunto_a.intersection(conjunto_b))

# 3- Crea un conjunto de frutas y elimina una fruta específica.
frutas = {"bananos", "manzana", "pipas", "fresas", "aguacate"}
frutas.remove("pipas")
print(frutas)

# 4- Realiza la diferencia entre dos conjuntos de letras.
conjunto_a = {"h", "a", "z", "o"}
conjunto_b = {"h", "j", "z", "i"}
print(conjunto_a.difference(conjunto_b))

# 5- Crea un conjunto de números y verifica si un número específico está presente.
import random
numeros = {random.randint(1, 100) for n in range(10)}
print(2 in numeros)

# 6- Realiza la diferencia simétrica entre dos conjuntos de colores.
colores_1 = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "blanco", "gris"}
colores_2 = {"azul", "amarillo", "naranja", "morado", "rosa", "negro", "blanco", "gris"}
print(colores_1.symmetric_difference(colores_2))

# 7- Crea un conjunto con los primeros 10 números y otro con los números del 5 al 15, luego encuentra la intersección.
num_1 = {n for n in range(1, 10)}
num_2 = {n for n in range(5, 15)}
print(num_1.intersection(num_2))

# 8- Crea un conjunto de palabras y cuenta cuántas palabras únicas hay.
colores_1 = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "blanco", "gris", "negro", "amarillo"}      
print(f"en el conjunto hay: {len(colores_1)} palabras unicas")

# 9- Escribe un programa que combine dos conjuntos y elimine duplicados.
def eliminar_duplicados(set_1, set_2):
    neW = colores_1 | colores_2
    return neW
print(eliminar_duplicados({"rojo", "verde", "azul", "amarillo", "naranja", "negro", "blanco", "gris"}, {"azul", "amarillo", "naranja", "morado", "rosa", "negro", "blanco", "gris"}))

# 10- Crea un conjunto de estudiantes y verifica si un estudiante está en el conjunto.
def verificacion(set, estudiante):
    verificar =  estudiante in set
    return verificar
print(verificacion({"alex", "eric", "greivin", "rad", "carlos"}, "helen"))

# 11- Realiza una unión de tres conjuntos diferentes.
union_3 = colores_1 | num_1 | conjunto_a
print(union_3)

# 12-Crea un conjunto de elementos y muestra su longitud.
elementos = {"alex", "eric", "greivin", "rad", "carlos"}
print(f"La longitud de este conjunto es de: {len(elementos)} palabras")

# 13- Escribe un programa que convierta una lista a un conjunto.
def list_set(lista):
    convert = set(lista)
    return convert
print(list_set(["eric", 25, 36, "helen", 89, "edwards"]))

# 14- Crea un conjunto de números y encuentra el número máximo y mínimo.
import random
numbers = {random.randint(1, 250) for n in range(10)}
print(f"El numero maximo de el conjunto es: {max(numbers)} y el minimo es: {min(numbers)}")

# 15- Desarrolla un programa que imprima todos los elementos de un conjunto.
for i, elemento in enumerate(numbers, start=1):
    print(f"Elemento {i}, del conjunto: {elemento}")


# Mini Proyectos:
# Crea un programa que gestione una lista de contactos utilizando conjuntos para evitar duplicados.
class Contactos:
    def __init__(self):
        self.contacts = set()
    pass

    def agregar_contactos(self, nombre, numero):
        if type(nombre) == str and type(numero) == int:
            dato = (nombre.capitalize(), numero)
            self.contacts.add(dato)
            return "Contacto agregado, muchas gracias \n"
        else:
            return "Error de tipo, solo se acepta texto en nombre y en numero digitos  \n"

    def mostrar_contactos(self):
        if not self.contacts:
            return "Lista de contactos vacia  \n"
        return "\n".join((f"{i}- Nombre: {nombre} y Numero: {numero}")for i, (nombre, numero) in enumerate(self.contacts, start=1))

    def eliminar_contacto(self, info):
            try:
                self.contacts.remove(info)
                return "Contacto eliminado  \n"
            except KeyError as e:
                return "Contacto no encontrado \n"
            
admin = Contactos()
while True:
    print(
        "\n Bienvenidos a mis contactos \n"
        "1- Agregar contactos \n"
        "2- Mostrar contactos \n"
        "3- Eliminar contactos \n"
        "4- Salir \n"
    )
    accion = int(input("Ingrese la accion que desea realizar: \n"))
    if accion == 1:
        nombre = input("Ingrese el nombre de el contacto: \n")
        numero = int(input("Ingrese el numero de el contacto: \n"))
        print(admin.agregar_contactos(nombre, numero))
    elif accion == 2:
        print(admin.mostrar_contactos())
    elif accion == 3:
        print(admin.mostrar_contactos())
        print("Ingrese el nombre y numero de contacto que desea eliminar \n")
        nombre = input("Ingrese el nombre de el contacto: \n")
        numero = int(input("Ingrese el numero de el contacto: \n"))
        info = (nombre.capitalize(), numero)
        print(admin.eliminar_contacto(info))
        print("Contacto eliminado...muchas gracias \n")
    elif accion == 4:
        print("Muchas gracias....Saliendo")
        break
    else:
        print("Ingrese un valor de 1 a 4")

# Desarrolla un programa que analice dos listas de estudiantes y muestre los que están en ambas listas.
def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))
print(intersection(["alex", "maria", "greivin", "rad", "karla"], ["helen", "eric", "greivin", "rad", "carlos"]))
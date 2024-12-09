# Día 12: Métodos de conjuntos


# Teoría:
# Los conjuntos en Python tienen varios métodos útiles que permiten manipular y consultar sus elementos.
# Algunos de los métodos más comunes son:

# .add(elemento): Agrega un elemento al conjunto.
# .remove(elemento): Elimina un elemento del conjunto. Lanza un error si el elemento no está presente.
# .discard(elemento): Elimina un elemento del conjunto sin lanzar error si no está presente.
# .clear(): Elimina todos los elementos del conjunto.
# .pop(): Elimina y retorna un elemento aleatorio del conjunto.
# .union(otro_conjunto): Retorna un nuevo conjunto que es la unión de dos conjuntos.
# .intersection(otro_conjunto): Retorna un nuevo conjunto que es la intersección de dos conjuntos.

# Tips y Buenas Prácticas:
# Usa .discard() en lugar de .remove() si no estás seguro de que el elemento esté en el conjunto.
# Recuerda que los conjuntos son mutables, por lo que puedes agregar o eliminar elementos en cualquier momento.
# Evita realizar operaciones innecesarias en conjuntos grandes para mejorar el rendimiento.

# Ejemplos Reales:
# Uso de Métodos de Conjuntos:
conjunto = {1, 2, 3}

# Agregar un elemento
conjunto.add(4)
print("agregar 4 a lo ultimo de el conjunto:", conjunto)

# Eliminar un elemento
conjunto.remove(2)
print("eliminar 2 d el conjunto:", conjunto)

# Usar discard
conjunto.discard(5)  # No lanzará error
print("discard en 5 d el conjunto:", conjunto)

# Usar pop
conjunto.pop()
print("Elimina cualquier elemento:", conjunto)

# Unión de Conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
print("Union de conjuntos:", union)

# Intersección de Conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)
print("Interseccion de conjuntos:", interseccion)

# Limpiar el conjunto
conjunto.clear()
print("Después de limpiar:", conjunto)

# Ejercicios:
# Crea un conjunto y agrega varios elementos.
new_set = set()
for i in range(10):
    new_set.add(i)
print(new_set)

# Elimina un elemento de un conjunto utilizando .remove().
new_set.remove(5)
print(new_set)

# Utiliza .discard() para intentar eliminar un elemento que no está en el conjunto.
new_set.discard(15)
print(new_set)

# Crea un conjunto y limpia todos sus elementos.
prueba = {1, 2, 3, 4, 5}
prueba.clear()
print(prueba)

# Utiliza .pop() para eliminar un elemento aleatorio de un conjunto.
pru = {1, 2, 3, 4, 5}
pru.pop()
print(pru)

# Crea un conjunto y encuentra su longitud.
new = {1, 2, 3, 4, 5}
print(f"El conjunto tiene {len(new)} elementos")

# Agrega elementos de una lista a un conjunto.
lista = [1, 2, 3, 4, 5]
conjunto = set()
for i in lista:
    conjunto.add(i)
print(conjunto)

# Realiza operaciones de unión e intersección utilizando métodos.
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print("Union:", union)
print("Interseccion:", interseccion) # elementos en comun

# Crea un conjunto de nombres y elimina uno utilizando .remove().
nombres = {"Juan", "Pedro", "Maria"}
nombres.remove("Pedro")
print(nombres)

# Utiliza .add() para agregar un elemento que ya existe.
nombres = {"Juan", "Pedro", "Maria"}
nombres.add("Pedro") # no lo agrega porque los conjuntos no admiten elementos duplicados
print(nombres)

# Escribe un programa que combine dos conjuntos usando .union().
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
print(union)

# Crea un conjunto de números y utiliza .pop() para eliminar un elemento. 
numeros = {1, 2, 3, 4, 5}
numeros.pop()
print(numeros)

# Crea un conjunto y utiliza .clear() para vaciarlo.
conjunto = {1, 2, 3, 4, 5}
conjunto.clear()
print(conjunto)

# Utiliza .intersection() para encontrar elementos comunes entre dos conjuntos.
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

# Crea un conjunto y utiliza .add() para agregar un elemento existente.
conjunto = {1, 2, 3}
conjunto.add("hola")
print(conjunto)

# Mini Proyectos:
# Desarrolla un programa que gestione un registro de asistencia utilizando conjuntos para evitar duplicados.
class Asistencia:
    def __init__(self):
        self.asistentes = set()

    def agregar_asistente(self, nombre):
        try:
            self.asistentes.add(nombre.capitalize())
            return "Asistente agregado correctamente."
        except Exception as e:
            return f"Ha ocurrido un error: {e}"

    def mostrar_asistentes(self):
        if not self.asistentes:
            return "No hay asistentes registrados."
        return "\n".join({f"{i}- {asistente}" for i, asistente in enumerate(self.asistentes, start=1)})
    def eliminar_asistente(self, nombre):
        try:
            self.asistentes.remove(nombre.capitalize())
            return "Asistente eliminado correctamente."
        except KeyError:
            return "El asistente no estaba registrado."
        
    def buscar_asistente(self, nombre):
        if nombre.capitalize() in self.asistentes:
            return "El asistente está registrado."
        return "El asistente no está registrado."
    
administrador = Asistencia()

while True:
    print("1. Agregar asistente")
    print("2. Mostrar asistentes")
    print("3. Eliminar asistente")
    print("4. Buscar asistente")
    print("5. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del asistente: ")
        print(administrador.agregar_asistente(nombre))
    elif opcion == 2:
        print(administrador.mostrar_asistentes())
    elif opcion == 3:
        print(administrador.mostrar_asistentes())
        nombre = input("Ingrese el nombre del asistente a eliminar: ")
        print(administrador.eliminar_asistente(nombre))
    elif opcion == 4:
        nombre = input("Ingrese el nombre del asistente a buscar: ")
        print(administrador.buscar_asistente(nombre))
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

# Crea un programa que analice las preferencias de comida de un grupo de personas utilizando conjuntos.
class Preferencias:
    def __init__(self):
        self.preferencias = set()

    def agregar_preferencia(self, preferencia):
        try:
            self.preferencias.add(preferencia.capitalize())
            return "Preferencia agregada correctamente."
        except Exception as e:
            return f"Ha ocurrido un error: {e}"

    def mostrar_preferencias(self):
        if not self.preferencias:
            return "No hay preferencias registradas."
        return "\n".join({f"{i}- {preferencia}" for i, preferencia in enumerate(self.preferencias, start=1)})

    def eliminar_preferencia(self, preferencia):
        try:
            self.preferencias.remove(preferencia.capitalize())
            return "Preferencia eliminada correctamente."
        except KeyError:
            return "La preferencia no estaba registrada."
        
    def analizar_preferencia(self, preferencia):
        if preferencia.capitalize() in self.preferencias:
            return "La preferencia está registrada."
        return "La preferencia no está registrada."
    
preferencias = Preferencias()

while True:
    print("1. Agregar preferencia")
    print("2. Mostrar preferencias")
    print("3. Eliminar preferencia")
    print("4. Analizar preferencia")
    print("5. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        preferencia = input("Ingrese la preferencia: ")
        print(preferencias.agregar_preferencia(preferencia))
    elif opcion == 2:
        print(preferencias.mostrar_preferencias())
    elif opcion == 3:
        print(preferencias.mostrar_preferencias())
        preferencia = input("Ingrese la preferencia a eliminar: ")
        print(preferencias.eliminar_preferencia(preferencia))
    elif opcion == 4:
        preferencia = input("Ingrese la preferencia a analizar: ")
        print(preferencias.analizar_preferencia(preferencia))
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

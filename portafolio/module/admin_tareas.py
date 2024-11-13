class Tareas:
    def __init__(self, lista):
        self.lista = []
        pass

    def agregar_tareas(self, tarea):
        try:
            self.lista.append(tarea.capitalize())
            return "Tarea agregada"
        except TypeError:
            return "Solo se agrega texto"
    
    def eliminar_tarea(self, tarea):
       try:
           self.lista.remove(tarea.capitalize())
           return "Tarea eliminada"
       except ValueError:
           return "Tarea no encontrada"
       
    def mostrar_tareas(self):
        if not self.lista:
            return "No hay tareas pendientes"
        return "\n".join([f"{i}- {tareas}"for i, tareas in enumerate(self.lista, start=1)]) # se acomulan las tareas 
        
admin = Tareas([])
while True:
    print("\n Bienvenido al menu de tareas \n"
          "1- agregar tareas\n"
          "2- eliminar tareas\n"
          "3- mostrar tareas \n"
          "4- salir\n"
    )
    try:
        number = int(input("Ingrese un numero: "))
    except ValueError:
        print("Ingrese un numero valido")
        continue

    if number == 1:
        Task = input("agrega la tarea que deseas agregar: ")
        admin.agregar_tareas(Task)
        print("Tarea agregada")
        
    elif number == 2:
        Task = input("agrega la tarea que deseas eliminar: ")
        admin.eliminar_tarea(Task)
        print("Tarea eliminada")
        
    elif number == 3:
        print(admin.mostrar_tareas())

    elif number == 4:
        print("Gracias por usar el programa")
        break
        
    else:
        print("Ingrese un numero valido")
from module import admin_tareas
import tkinter as tk

# instancia de la clase Tareas
admin = admin_tareas.Tareas([])

# ventana principal de Tkinter
root = tk.Tk()
root.title("Administrador de tareas")

# Crear y agregar widgets a la ventana
label = tk.Label(root, text="Administrador de tareas")
label.pack()

button_agregar = tk.Button(root, text="Agregar tarea", command=lambda: print(admin.agregar_tareas("Nueva tarea")))
button_agregar.pack()

button_eliminar = tk.Button(root, text="Eliminar tarea", command=lambda: print(admin.eliminar_tarea("Tarea eliminada")))
button_eliminar.pack()

button_mostrar = tk.Button(root, text="Mostrar tareas", command=lambda: print(admin.mostrar_tareas()))
button_mostrar.pack()

button_salir = tk.Button(root, text="Salir", command=root.quit)
button_salir.pack()

# Iniciar la interfaz gráfica
root.mainloop()


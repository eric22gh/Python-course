with open("fof\\tex.txt", "r", encoding="UTF-8") as te: # encoding="UTF-8" para los carateres raros
    te.read()

nombres = ["lucas","alewx", "camila", "erwin"]
apellidos = ["edwards", "lopez", "vargas","pertez"]

##### registrar las listas en un archivo

with open("nombresyapellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"nombre: {n}\nApeliido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]
    #####
    
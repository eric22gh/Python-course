##### funciones 
#print("hola")

def hola (): 
    print("hola eric") 
    print("arquitecto de soluciones")

hola() # para llamar a la funcion, es un argumento

#### parametros y argumentos: darle una variable a la funcion y asi usarla en cualquier parte, reutilizar codigo

def hello (nombre): #parametro nombre de la varaible dentro de la funcion 
    print(F"hola {nombre}")
    print("arquitecto de soluciones")

hello("baiser") # argumento el valor que le estamos pasando, osea el puede cambiar

def hello (nombre, apellido): # parametro
    print(F"hola {nombre} {apellido}")
    print("arquitecto de soluciones")

hello("alex", "vazquez") # argumento
hello("gabriel", "lopez")
hello("Eric", "Edwards")

### argumentos opcionales, hacer que un argumento utilice un valor por defecto 

def pop (marca, dueño="luigi"):
    print(f"esta marca es {marca} y el dueño es {dueño}")
    print("purdy mptors")
pop("bently", "edwards")
pop("maserati")
pop("bently")
#######
def pap (brand="bayern", pastilla="hibu"): # guardar 2 por defecto, recordar esto es un parametro
    print(f"esta marca es {brand} y la partilla es {pastilla}")
    print("buen farmaco")
pap() # y adentro va el argumento que no esta aqui por esta por defecto en el parametro

####### cuando estamos muy adelantados en el codigo y no vemos el orden del parametro
pap (pastilla="paracetamol", brand="JYJ") # aqui esta desordenando, pero deja de importar si lo referencio0


#### practice
def star (name, nacionalidad):
    print("quie es el actriz")
    print(f"Es {name} de {nacionalidad}")
star ("Eric", "costa rica")
star ("alex", "Pero")
star ("luis", "brazil")
######### valor por defecto
def thor (dios="buri", mitologia="nordica"):
    print(F"este es {dios} el dios de la mitologia {mitologia}")
thor()
thor("balder", "nordica")
thor(mitologia="egipcia", dios="horus")# cuando esta en desorden 
thor("Rah")
######
x = int(input("ingrese el valor de x:"))
y = int(input("ingrese el valor de y:"))
def suma (x, y):
    print(x + y)
suma(x, y)









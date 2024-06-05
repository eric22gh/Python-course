## operadores logicos ##
## and cuando 2 cosas se cumplen: 5<10 and 2>1 resultado trues
## or solo una condicion se cumple
## not niega el resultado de una operacion 

gas = True
encendido = True
edad = 20 

## and cuando 2 cosas se cumple
if gas and encendido:
    print("puede llenar el tanque")
# solo una condicion se cumple
if gas or encendido:
    print("puedes avanzar")
# niega todo 
if not gas or encendido:
    print("correr")

if gas and (encendido and edad > 18): # siempre se evaluan primero los parentesis,
    # se ponen en una operacion asi porque python no sa be que va primero
    print("puedes sacar el id")


## operadores de corto circuito; 

if gas or encendido or edad > 18: #
    print("puedes sacar el id")
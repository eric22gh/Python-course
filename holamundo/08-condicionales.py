##### condicionales, decide si algo de nuestro codigo se va a ejecutar si o no

my = True
if my ==  False: # poner == false es redundande, pork con solo poner if my actomaticamente se tiene q cumplir la condicion
    # yo opino q encasos especiales si lo necesita, como la calcu que hice
    print("hola bucle")
else:
    print("el bucle continua")


eric = 35

if eric > 30:
    print("habiltado")
    
else:
    print("todavia no esta habiltado")


my_lol = 22
my_lal = 2

if my_lol > 5 and my_lal > 15: # tienen que cumplirce las 2 condiciones
    print("tienen edad suficiente")
else:
    print("no tienen edad todavia")

if my_lol == 5:
    print("es correcto")

elif my_lol == 2:
    print("hola nuemro 2")

elif my_lol == 22:
    print("hola, te encontre")
else:
    print("sige intentando")

string = "eric"
if string:
    print("hola eric")

###################

los = 5
if los >= 3:
    print("puedes pasar")
else:
    print("no puedes pasar")

################### if anidados

los = 5
if los == 3:
    print("puedes pasar")
    if los == 2:
        print("puedes pasar")
    elif los == 1:
        print("puedes pasar")
    else:
        print("eric")
else:
    print("no puedes pasar")
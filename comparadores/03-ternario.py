### ternario es para reducir y que se vea mejor un if o condicional en una sola linea

age = 2                                          #"es mayor" if age    >      18   else "es menor"
mensaje = "es mayor" if age > 18 else "es menor" # es mayor si age es mayor q 18 y si no es menor
# if edad > 17:
#     mensaje = "es mayor"
# else:
#     mensaje = " no es mayor"
print(mensaje)
#######
p = int(input("Ingrese el numero: "))
p = int(p)
eric =  "ya no eres un adolecente" if p >= 18 else "todavia te falta un año" if p == 17 else "todavia eres un ñino" if p == 16 else "vuelve a casa bebe" if p <= 15 else "vuelve a casa bebe"
print(p)

if p >= 18:
    print("ya no eres un adolecente")
elif p == 17:
    print("todavi te falta un año")
elif p == 16:
    print("todavia eres un ñino")
else:
    p <= 15
    print("vuelve a casa bebe")

#####
a = input("ingrese el numero")
msj = "esta disponible" if a > 20 else "no esta disponible"
print(msj)
# comando = "" # terminal virtual
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)


numero = 1
while numero < 512: # while es un bucle infinito, hay que ponerle un contador o aumentador
    # para que no se quede en infinito, en cambio el for si va aumentando
    print(numero)
    numero *= 2 # este es el contador, lo multiplica por 2

for number  in range(257):
    print(number)

## bucles infinitos

numero = 1
while numero < 512: # while es un bucle infinito, hay que ponerle un contador o aumentador
    # para que no se quede en infinito, en cambio el for si va aumentando
    print(numero)
    break # es para terminar el bucle infinito
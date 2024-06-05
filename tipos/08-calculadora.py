# #### calculadora basica #####

# n1 = input("ingresa el numero: ")   # nos permite optener datos del usuario
# n2 = input("ingresa el segundo numero: ")
# opera = input("ingresa el tipo de operacion: ")
# n1 = int(n1)
# n2 = int(n2)

# suma = n1 + n2
# resta = n1 - n2 
# multi = n1 * n2 
# div = n1 / n2 

# while True: # todo lo que esta dentro de un while va de bucle 
#     n1 = input("ingresa el primer numero: ")   
#     n2 = input("ingresa el segundo numero: ")
#     opera = input("ingresa el tipo de operacion: suma, resta, multi, div: ")
        
#     if opera == "suma":
#         print("El resustado de la suma es: ",suma)

#     elif opera == "resta":
#             print("El resultado de la resta es: ",resta)
            
#     elif opera == "multi":
#             print("El resultado de la multiplicacion es: ",multi)

#     elif opera == "div":
#             print("El resultado de la divicion es: ",div)
#             break # antes del else va un break, es para salir del bucle
#     else:
#         print("operacion no reconocida")
#         print("Ingrese otra operacion valida.")
    


while True:
        numero1 = input("Ingrese el primer numero: ")
        numero2 = input("Ingrese el segundo numero: ")
        opera = input("Ingrese el tipo de operacion suma, resta, multi, div, elevar: ")
        #####
        numero1 = int(numero1)
        numero2 = int(numero2)
        ####
        suma = numero1 + numero2
        resta = numero1 - numero2
        multi = numero1 * numero2
        div = numero1 / numero2
        elevar = numero1 ** numero2
        ####          
        if opera == "suma":
                print("El resustado de la suma es: ",suma)
                print("Operacion terminada")

        elif opera == "resta":
                print("El resultado de la resta es: ",resta)
                print("Operacion terminada")

        elif opera == "multi":
                print("El resultado de la multiplicacion es: ",multi)
                print("Operacion terminada")

        elif opera == "div":
                print("El resultado de la divicion es: ",div)
                print("Operacion terminada")

        elif opera == "elevar":
            print("El resultado de elevar un numero es: ",elevar)
            print("Operacion terminada")
            break 
        else:
             print(" Operacion no valida, ingrese otra operacion")


        







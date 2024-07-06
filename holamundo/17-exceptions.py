##### manejo de errores

def sumar_dos():
    while True:
        a = input("ingrse el numero 1: ")
        b = input("ingrse el numero 2: ") #### si ponemps un string en vez de numero va a dar error
        try:
            Resultado = int(a) + int(b)
            break
        except ValueError as e: # lo que va a salir si da error
            print("te pedi un numero, no cadenas")
            print(f"ERROR: {e}")
        else:
            break
        finally:
            print("Muchas gracias")
    return Resultado
print(sumar_dos())

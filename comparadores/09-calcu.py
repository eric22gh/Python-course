while True:
    print("Bienvenido(a) a mi calculadora")
    x = int(input("ingrese el primer numero: "))
    Y = int(input("ingrese el segundo numero: "))
    opera = input("ingrese la operacion: suma, resta, multi, div o salir: ")
    ####
    suma = x + Y 
    resta = x - Y 
    multi = x ** Y 
    div = x / Y 
    ####
    if opera.lower() == "suma":
        print("El resultado de la suma es:",suma)
    elif opera.lower() == "resta":
        print("El resultado de la resta es:",resta)
    elif opera.lower() == "multi":
        print("El resultado de la multiplicacion es:",multi)
    elif opera.lower() == "div":
        print("El resultado de la division es:",div)
    elif opera.lower() == "salir": # por si lo escriben en mayuzcula
        print("Saliendo de la calculadora")
        break
    else:
        print("Operacion no valida, ingrese operaciones validas.")




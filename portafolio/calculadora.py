 ###### calculadora basica #####

while True:
    print("Bienvenido(a) a mi Calculadora")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese el tipo de operacion: suma, resta, multi, division, elevado o Salir: ")
    #######
    # El int es importante porque el num1 entra como un string y si no se convierte a int va a dar error
    #######
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2
    elevado = num1 ** num2
    #######
    if operacion.lower() == "suma": # recuerda esto entre comillas
        print("El resultado de la suma es:", suma)

    elif operacion.lower() == "resta":
        print("El resultado de la resta es:", resta)

    elif operacion.lower() == "multi":
        print("El resultado de la multiplicacion es:", multi)

    elif operacion.lower() == "division":
        print("El resultado de la division es:", division)

    elif operacion.lower() == "elevado":
        print("El resultado de la elevacion es:", elevado)

    elif operacion.lower() == "salir":
        print("Saliendo de la Calculadora")
        break
    else:
        print("Vuelva a insertar una operacion valida")


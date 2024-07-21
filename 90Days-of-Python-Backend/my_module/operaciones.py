def suma(a, b):
    return a + b
suma(10, 5)

def resta(a, b):
    return a - b
resta(10, 5)

def multiplicar(a, b):
    return a * b
multiplicar(10, 5)

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
dividir(10, 5)



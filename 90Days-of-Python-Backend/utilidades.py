def contar_palabras(palabra):
    contar = len(palabra.split()) # Divide la cadena en una lista usando el delimitador especificado (por defecto, el espacio).
    return f"Esta cadena tiene: {contar} palabras"
contar_palabras("murcielagos estan en la montaña de sixaola")

def kilometros_millas(kilometros):
    millas = kilometros * 0.621371 # kilometros a millas, 1 kilometro es el 62% de una milla
    return f"A estos {kilometros} kilometros le caben: {millas} millas"
kilometros_millas(10)

def millas_kilometros(millas):
    kilometros = millas * 1.60934 # millas a kilometros, cuantas millas hay en X kilometros
    return f"A estas {millas} millas le caben: {kilometros} kilometros"
millas_kilometros(5)

def hora_actual(hora):
    import datetime
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    return f"esta es la hora actual {hora} segundos"
hora_actual("")

def fecha_actual(fecha):
    import datetime
    fecha = datetime.datetime.now().date()
    return f"esta es la fecha de hoy: {fecha}"
fecha_actual("")

def manipular_mayuzcula(cadena):
    mayuzcula = cadena.upper()
    return f"esta cadena: {mayuzcula} fue convetida toda a mayuscula."
manipular_mayuzcula("mUrCiElAgOs")

def manipular_minuscula(cadena):
    minuscula = cadena.lower()
    return f"esta cadena: {minuscula} fue convetida toda a minuscula."
manipular_minuscula("mUrCiElAgOs")

def manipular_letra_capital(cadena):
    letra_capital= cadena.capitalize()
    return f"esta cadena: {letra_capital} fue convetida toda a letra capital."
manipular_letra_capital("mUrCiElAgOs")

##### hacer un palindromo: es una palabra que se escribe igual alderecho y al revez
#radar, anilina, reconocer
def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para ignorar diferencias de mayúsculas y minúsculas
    palabra = palabra.lower() # ignora mayusculas y minusculas
    #palabra = palabra.no_space()
    
    # Invertir la palabra y compararla con la original
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Ejemplos de uso:
print(es_palindromo("Reconocer"))  # Esto debería imprimir True
print(es_palindromo("Python"))     # Esto debería imprimir False
print(es_palindromo("Radar"))      # Esto debería imprimir True
print(es_palindromo("anilina"))      # Esto debería imprimir True
print(es_palindromo("amo la paloma"))      # Esto debería imprimir True







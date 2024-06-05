#### como depurar nuestro codigo
def largo (texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado
print("hola edwards") # el punto rojo de debug se llama breakpoint
l = largo("hola mundo")
print(l)
### depurar nuestro codigo en run and debug
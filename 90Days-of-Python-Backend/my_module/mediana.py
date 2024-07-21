def calcular_mediana(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    medio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    else:
        return lista_ordenada[medio]
calcular_mediana(lista = [5, 10, 55, 69, 20, 56, 223])


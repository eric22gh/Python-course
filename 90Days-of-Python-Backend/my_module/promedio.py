def promedio_lista(lista):
    if not lista:
        raise ValueError("La lista está vacía") # para menejo de errores, si la lista esta vacia
    suma = sum(lista)
    promedio = suma / len(lista)
    return f"el promedio de la lista es: {promedio}"
promedio_lista(lista = [5, 10, 55, 69, 20, 56, 223])


##### list comprehension ###

my_original_list = [52, 10, 55, 63, 42, 22]

lista = [i for i in range(8)]
print(lista)

lista = [i for i in range(80) if i % 2 == 0] # crear una lista
print(lista)

lista = [i * 2 for i in range(8)]
print(lista)

lista = [i * i for i in range(8)]
print(lista)

def sum_numbre(number):
    return number + 5
lista = [  sum_numbre(i) for i in range(8)]
print(lista)

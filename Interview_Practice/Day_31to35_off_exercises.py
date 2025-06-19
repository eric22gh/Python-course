# Día 31

# Ejercicio 151: Crea una función que verifique si un número es un número primo.
# Conceptos: Matemáticas, funciones.
def Prime_number(n):
    if n < 2:
        return "It is not a prime number"
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return "It is not a prime number"
        return "It is a prime number"
print(Prime_number(11))

def prime(x):
    if x < 2:
        return "It is not a prime number"
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return "It is not a prime number"
            return "It is a prime number"
print(prime(8))
            
                        
# Ejercicio 152: Escribe un programa que imprima los números del 1 al 100 y marque los múltiplos de 13 como "Trece".
# Conceptos: Bucles, condicionales.
def Trece():
    for i in range(0, 101):
        if i % 13 == 0:
            print("Trece")
        print(i)
Trece()

# Ejercicio 153: Crea una función que reciba una lista y devuelva el elemento en la posición media.
# Conceptos: Listas, funciones.
def Medium_list(elements):
    medium = int(len(elements) // 2)
    if len(elements) % 2 != 0:
        return elements[medium]
    else:
        return elements[medium - 1], elements[medium]

print(Medium_list([78, 56, 1, 22, 6, 10]))

# Ejercicio 154: Escribe un programa que cuente la cantidad de espacios en blanco en una cadena.
# Conceptos: Manipulación de strings, funciones.
def Count_Space(String):
    aux = 0
    for space in String:
        if space == " ":
            aux += 1
    return aux
print(Count_Space("Hello, I am Eric Hernandez Edwards"))

# Ejercicio 155: Crea una función que encuentre el número de combinaciones posibles de un conjunto de n elementos.
# Conceptos: Combinatoria, funciones.
def Combinations(elements):
    from itertools import combinations
    comb = []
    for i in range(len(elements) + 1):
        comb.extend(combinations(elements, i)) 
        # extend agrega los elementos de un iterable a la lista, mientras que append agrega el iterable como un solo elemento
    return len(comb) - 1  # Subtract 1 to exclude the empty combination
print(Combinations([1, 2, 3]))


# Día 32
# Ejercicio 156: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 14 por "Catorce".
# Conceptos: Bucles, condicionales.
def Catorce():
    for i in range(1, 101):
        if i % 14 == 0:
            print("Catorce")
        else:
            print(i)

# Ejercicio 157: Crea una función que reciba una cadena y devuelva el número de caracteres especiales.
# Conceptos: Manipulación de strings, funciones.
def Special_Characters(string):
    import string as stg
    count = 0
    aux =  stg.ascii_letters
    for i in string:
        if i not in aux:
            count += 1
    return count
print(Special_Characters("eric .#,"))

# Ejercicio 158: Escribe un programa que imprima la suma de los cuadrados de los números del 1 al 10.
# Conceptos: Bucles, matemáticas.
def Sum_Square_10():
    aux = 0
    #sux = sum([x**2 for x in range(0, 11)])
    for i in range(0, 11):
        aux += i**2
    return aux
print(Sum_Square_10())

# Ejercicio 159: Crea una función que encuentre la longitud de la lista más larga en una lista de listas.
# Conceptos: Listas, funciones.
def Max_List_Lists(data):
    aux = []
    for elements in data:
        if len(elements) > len(aux):
            aux = elements
    return len(aux)
dux = [
    ["eric", "tree", 56, 10, 89, True, 1.0],
    ["eric", "tree", 56, 10, 89, True],
    ["eric", "tree", 56, 10, 89, True, 1.0, "C.S.", "voy", 56, 89, 22],
    ["eric", "tree", 56, 10, 89],
    ["eric", "tree", 56, 10, 89, True, 1.0, 56, "Helen"]
]
print(Max_List_Lists(dux))

# Ejercicio 160: Escribe un programa que imprima un cuadrado de números, donde cada fila contenga el mismo número.
# Conceptos: Bucles, impresión.
def Square_Numbers(n):
    for i in range(1, n + 1):
        Square = i ** 2
        print(f"{Square}, {i}")

Square_Numbers(5)



# Día 33
# Ejercicio 161: Crea una función que verifique si una cadena es un anagrama de otra.
# Conceptos: Manipulación de strings, funciones. 
# # anagrama es una palabra que reordenada forma otra palabra, pero sin agregar o quitar letras.
def Anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        return sorted(string1) == sorted(string2)
print(Anagram("amor", "roma")) 

# Ejercicio 162: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 16 por "Dieciséis".
# Conceptos: Bucles, condicionales.
def Dieciseis():
    for i in range(1, 101):
        if i % 16 == 0:
            print("Dieciséis")
        else:
            print(i)
Dieciseis()

# Ejercicio 163: Crea una función que reciba una lista y devuelva el tercer elemento más grande.
# Conceptos: Listas, funciones.
def Third_element(elements):
    if len(elements) < 3:
        return "The list must have at least three elements"
    elements.sort()
    return elements[-3]
print(Third_element([100, 1, 56, 23, 89, 10]))

# Ejercicio 164: Escribe un programa que cuente cuántas veces aparece una palabra en un texto.
# Conceptos: Manipulación de strings, funciones.
def Count_A_word(Phrase, word):
    count = 0
    for aux in Phrase.split():
        if aux.lower() == word.lower(): # no esta contando bien
            count += 1
    return count
print(Count_A_word("Hello, my name is Eric Edwards nice to meet, what is your name?", "name"))

# Ejercicio 165: Crea una función que reciba un número y devuelva su cubo.
# Conceptos: Funciones, matemáticas.
def Cube_Number(n):
    return n ** 3
print(Cube_Number(8))



# Día 34
# Ejercicio 166: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 17 por "Diecisiete".
# Conceptos: Bucles, condicionales.
def Multiples_17():
    for i in range(1, 101):
        if i % 17 == 0:
            print("Diecisiete")
        else:
            print(i)
Multiples_17()

# Ejercicio 167: Crea una función que encuentre el número de elementos en una lista que son mayores que un valor dado.
# Conceptos: Listas, funciones.
def Bigger_than_Value(numbers, value):
    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] > value:
            count += 1
    return count
print(Bigger_than_Value([89, 5, 1, 3, 45, 22, 0, 2], 10))

# Ejercicio 168: Escribe un programa que imprima la suma de los números impares del 1 al 50.
# Conceptos: Bucles, matemáticas.
def FiFty_Sum():
    count = 0
    for i in range(1, 51):
        if i % 2 != 0:
            count += i
    return count
FiFty_Sum()

# Ejercicio 169: Crea una función que reciba una cadena y devuelva la misma cadena sin vocales.
# Conceptos: Manipulación de strings, funciones.
def Replace_Vowels(String):
    sux, vowels = [], "aeiou"
    for i in String:
        if i not in vowels:
            sux.append(i)
    return str("".join(sux))
print(Replace_Vowels("murcielago"))

# Ejercicio 170: Escribe un programa que imprima un triángulo de números, donde cada fila contenga el número de la fila.
# Conceptos: Bucles, impresión.
def Triangule_Numbers(n):
    for i in range(1, n + 1):
        space = " " * (n )
        nums = str(i) * i
        print(space + nums)
Triangule_Numbers(5)


# Día 35
# Ejercicio 171: Crea una función que verifique si una lista contiene elementos duplicados.
# Conceptos: Listas, funciones.
def Duplicated_Elements(elements):
    seen = set()
    for element in elements:
        if element in seen:
            return True
        seen.add(element)
    return False
print(Duplicated_Elements([1, 2, 3, 4, 5, 2]))


# Ejercicio 172: Escribe un programa que imprima los números del 1 al 100 y reemplace los múltiplos de 18 por "Dieciocho".
# Conceptos: Bucles, condicionales.
def Dieciocho():
    for i in range(1, 101):
        if i % 18 == 0:
            print("Dieciocho")
        else:
            print(i)
Dieciocho()

# Ejercicio 173: Crea una función que reciba una lista y devuelva la lista ordenada en orden ascendente.
# Conceptos: Listas, funciones.
def ascendent(elements):
    if len(elements) == 0:
        return "the list is empty"
    for i in range(0, len(elements)):
        for j in range(0, len(elements) -i -1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements
print(ascendent([55, 89, 1, 56, 10, 2]))

# Ejercicio 174: Escribe un programa que cuente cuántos caracteres hay en una cadena sin contar los espacios.
# Conceptos: Manipulación de strings, funciones.
def Count_characters(Phrase):
    if Phrase is None:
        return "there is no phrase to count"
    count = 0
    for i in Phrase.replace(" ", ""):
        count += 1
    return count
print(Count_characters("Eric h y"))

# Ejercicio 175: Crea una función que encuentre el número más grande en una lista de listas.
# Conceptos: Listas, funciones.
def Max_number(elements):
    if len(elements) == 0:
        return "the list is empty"
    aux = 0
    for i in range(0, len(elements)):
        if elements[i] > aux:
            aux = elements[i]
    return aux
print(Max_number([2, 1, 56, 10, 450, 6]))
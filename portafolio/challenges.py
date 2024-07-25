##### fizz buzz ######

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0: # se empieza por el caso mas restrictivo, mas condiciones
            print("fizzBuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)

fizzbuzz()

####### anagramas: dos palabras tengan las mismas letras #####

def anagrama(word_1, word_2):
    if word_1.lower() == word_2.lower():
        return False
    return sorted(word_1.lower()) == sorted(word_2.lower())
print(anagrama("amor", "roma"))

####### succesion de fibonacci ######
def fibonacci():
    prev = 0
    next = 1
    for number in range(1, 11):
        print(number)
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

############ NUMERO PRIMO ##### numero divisible(%) entre el mismo y entre uno y da 0 ese es un numero primo

def primo():
    for number in range(1, 101):

        if number >= 2:
            is_divisible = False
        
            for index in range(2, number):
                if number % index == 0: 
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)
    
primo()


for prime in range(2, 51):
    is_prime = True
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{prime} es un numero primo")
#2 raiz numero

######### crear una funcion q reciba una cadena y la devuelva alrevez ####

def reverse(texto):
    text_len = len(texto)
    tex = " "
    for o in range(0, len(texto)):
        tex += texto[text_len - o - 1]
    return tex

print(reverse("hola mundo"))

    
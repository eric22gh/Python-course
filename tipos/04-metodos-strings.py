## un metodo es es una funcion q esta dentro un objeto: upper() ####
animal = "tiGre De bengAla"
animals = " tigre siberiano "
print(animal.upper())
print(animal.capitalize()) # Primera letra en mayuscula
print(animal.lower()) # ignorar diferencias entre mayusculas y minusculas
print(animal.title()) # da en mayuscula las primeras letras de cada palabras 
print(animals.strip().capitalize()) # strip() para quitarle los espacios en blanco " tiGre De bengAla "
print(animal.find("De")) # ENCONTRA LA LETRA Y EN QUE POSICION ESTA 
print(animal.replace("De", "b")) 
print("ben" in animal) # y ven si esos strings se encuentran en animal
print("ben" not in animal) # para negar el resultado
# lo anterior nos dan booleans
print(animal.capitalize())






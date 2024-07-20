# Muito usados: join(), split(), find(), replace() 

gameName = "Fifa 2021"
gameDescription = "Fifa 2021, jogo de futebol, lançado em 2020"

print(gameName.upper()) #Maiúsculo
print(gameName.lower()) # Minúsculo
print(gameName.capitalize()) #Apenas primeira letra maiúscula
print(gameName.title()) #Apenas primeira letra maiúscula
print(gameName.center(10, '-')) #Retorna a string centralizada
print(gameName.find("f"))
print(gameDescription.count('a')) #Conta quantos caracteres 
print(gameDescription.count('A')) #Conta quantos caracteres 
print(gameDescription.replace("Fifa", "Pes")) #Altera elementos
print(gameDescription.split(','))
print(gameName.join(['1', '2', '3'])) # Concatenates gameName between each element of the list
print(gameName.startswith('Fi')) # Checks if the string starts with 'Fi'
print(gameName.endswith('21')) # Checks if the string ends with '21'
print(gameName.isdigit()) # Checks if the string contains only digits
print(gameName.islower()) # Checks if the string is in lowercase
print(gameName.isupper()) # Checks if the string is in uppercase
print(gameName.strip()) # Removes leading and trailing whitespace
print(gameName.lstrip()) # Removes leading whitespace
print(gameName.rstrip()) # Removes trailing whitespace
print(gameName.swapcase()) # Swaps the case of the string
print(gameName.isnumeric()) # Checks if the string contains only numeric characters
print(gameName.isdecimal()) # Checks if the string contains only decimal characters


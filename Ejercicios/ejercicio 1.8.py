frase=input("Introduce una frase: ")

frase2 =frase.lower().replace(" ","")

if frase == frase2[::-1]:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")



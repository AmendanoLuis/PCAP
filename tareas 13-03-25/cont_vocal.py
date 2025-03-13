frase = str(input("Introduce una frase: "))

vocales = "aeiou"
cont_vocales = 0

for letra in frase:
    if letra in vocales:
        cont_vocales += 1
        
print(f"La frase tiene {cont_vocales} vocales")
print("Luis Augusto Procel Amendaño")


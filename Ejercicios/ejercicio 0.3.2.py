# Importamos el módulo random para generar números random
from random import randint

num = randint(0, 10)
intentos = 10

# Version 2.0

for i in range(intentos):
    guess = int(input("Adivína el número 0 - 10: "))
    
    if not(0 <= num <= 10):
        print("Número fuera de rango.")
        continue
            
    if guess == num:
        print(f"¡Correcto! El número era {num}")
        break
    else:
        intentos -= 1
        print(f"Incorrecto, te quedan {intentos} intentos")
    
else:
    print("Te has quedado sin intentos.")
        
            
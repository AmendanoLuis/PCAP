# Importamos el módulo random para generar números random
from random import randint

num = randint(0, 10)
guess = 11

acertado = True
count = 1

# Version 3.0
while(guess != num):
    guess = int(input("Adivína el número 0 - 10: "))
    
    if not(0 <= num <= 10):
        print("Número fuera de rango.")
        continue
    
    if guess == num:
        print(f"¡Correcto! El número era {num}")
        acertado = False
        break
    else:
        count += 1
        print("¡Incorrecto!")

if count > 0:
    print(f"Has necesitado, {count} intentos.")
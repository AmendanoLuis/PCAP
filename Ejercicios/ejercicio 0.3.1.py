# Importamos el módulo random para generar números random
from random import randint

num = randint(0, 10)
guess = int(input("Adivína el número 0 - 10: "))

# Version 1.0
if 0 <= num <= 10:
    if guess == num:
        print(f"Correcto, el número era {num}")
    else:
        print(f"Error, número {guess} incorrecto, el número era {num}")
else:
    print("Número fuera de rango.")

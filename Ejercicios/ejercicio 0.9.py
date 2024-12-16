import random

numero_secreto = random.randint(1, 100)

intentos = 0 

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 100.")

# Bucle que sigue hasta que el usuario adivine el número
while True:
    
    try:
        adivinanza = int(input("Adivina el número: "))
        intentos += 1 
    
    # Excepción en caso de un valor inválido
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    # Comprobamos si el número ingresado es correcto
    if adivinanza < numero_secreto:
        print("¡Demasiado bajo! Intenta con un número mayor.")
    
    elif adivinanza > numero_secreto:
        print("¡Demasiado alto! Intenta con un número menor.")
    
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
         
        # Salimos del bucle cuando se adivina correctamente
        break 

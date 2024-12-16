numeros_ganadores = []

print("Introduce los números ganadores de la lotería primitiva (6 números):")

for i in range(6):
    while True:
        try:
            num = int(input(f"Introduce el número {i + 1}: "))
            if 1 <= num <= 49:
                numeros_ganadores.append(num)
                break
            else:
                print("El número debe estar entre 1 y 49. Intenta de nuevo.")

        except ValueError:
            print("Por favor, introduce un número válido.")

# Ordenamos los números de mayor a menor
numeros_ordenados = numeros_ganadores.sort()

print("\n Los números ganadores de la lotería primitiva son: ")
print(numeros_ganadores)
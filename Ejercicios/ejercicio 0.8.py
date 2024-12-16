num1 = int(input("Ingresa un número: "))

# Variable que contendrá el resultado del factorial de num1
factorial = 1

for i in range(1,num1 + 1): # Rango de 1 a num1
    factorial *= i

print(f"Factorial de {num1} es: {factorial}")
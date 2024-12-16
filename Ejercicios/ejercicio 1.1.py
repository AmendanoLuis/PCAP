pesoUser = float(input("Dime tu peso: "))

 # Usamos upper() para manejar mayúsculas y minúsculas
unidadPeso = input("¿(K)g o (L)bs? ").upper() 

peso = 0
pesoK = 0.0
pesoL = 0.0

if unidadPeso == "K":
    pesoK = pesoUser
    pesoL = pesoK * 2.20462
elif unidadPeso == "L":
    pesoL = pesoUser
    pesoK = pesoL / 2.20462
else:
    print("Unidad de peso no válida. Debes ingresar 'K' para kilogramos o 'L' para libras.")
    
    # Si la unidad no es válida, terminamos el programa
    exit()

# Imprimir el resultado según la unidad ingresada
# Usamos :.2f para determinar la cantidad de decimales del número que se muestran a la hora de imprimir
if unidadPeso == "K":
    print(f"Su peso en libras es: {pesoL:.2f} lbs")
else:
    print(f"Su peso en kilogramos es: {pesoK:.2f} kg")

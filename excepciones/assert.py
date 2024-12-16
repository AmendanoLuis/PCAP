import math

try:
    x = float(input("Ingresa un número: "))
    assert x >= 0.0

except ValueError:
    print("Error: Debes ingresar un número válido.")
    exit(1)
except AssertionError:
    print("Error de valor permitido ingresado, ingresa un número mayor o igual a 0.")
    exit(1)


x = math.sqrt(x)

print(x)
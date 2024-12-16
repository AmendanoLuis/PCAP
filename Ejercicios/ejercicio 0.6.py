print("Ingresa 2 números (pueden contener decimales)")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if(num1 > num2):
    print(f"El primer número {num1} es mayor al segundo {num2}")
elif(num2> num1):
    print(f"El segundo número {num2} es mayor al primero {num1}")
else:
    print(f"¡¡Los números {num1} y {num2} son iguales!!")
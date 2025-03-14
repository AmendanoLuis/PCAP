try:
    
    accion = int(input("¿Qué deseas hacer, buscar archivo (0) o realizar una division (1) ?: "))
    
    if accion == 0:    
        nombre_archivo = input("Ingresa el nombre del archivo: ")
        with open(nombre_archivo, "r") as archivo:
            cont_file = archivo.read()
    elif accion == 1:            
        num= int(input("Ingresa un número a dividir: "))
        divisor = int(input("Ingresa un número divisor: "))

        resultado = num / divisor
        print("El resultado de la división es:", resultado)

except FileNotFoundError:
    print("Error: El archivo no existe.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar un valor válido.")

print("Luis Augusto Procel Amendaño")


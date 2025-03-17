try:
    print("Abriendo archivo...")
    
    with open("archivo_inexistente.txt", "r") as archivo:
        print("Leyendo archivo...")
        print(archivo.read())

except FileNotFoundError:
    print("Error: El archivo no existe")
finally:
    print("Finalizando programa...")
    
print("Luis Augusto Procel Amendaño")


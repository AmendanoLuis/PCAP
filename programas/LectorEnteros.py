def read_int(prompt, min, max):
    while True:
        entrada = input(prompt)
        
        try:
            v = int(entrada)
            
            if min < v > max:
                print("Error: El valor no está dentro del rango permitido.")
                continue    

            return v
            
        except ValueError:
            print("Error: Entrada incorrecta.")
            continue
        


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
    
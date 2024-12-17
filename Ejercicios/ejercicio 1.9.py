entrada = input("Escribe una palabra: ")
vocales = ['a','e','i','o','u']


try:
    palabra = str(entrada)
    contador = 0
        
    for letra in palabra:
        
        # Si la letra (en minuscula) existe en la lista VOCALES, el contador sumara 1
        if letra.lower() in vocales:
            contador +=1    
    
except ValueError:
    print("Escribe una palabra, recuerdalo.")
    
print(f"Cantidad de vocales: {contador}")
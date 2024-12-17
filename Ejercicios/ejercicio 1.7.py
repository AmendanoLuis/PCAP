abecedario = [chr(i) for i in range(ord('a'),ord('z') + 1)]

resultado = []

for i in range(len(abecedario)):
    i + 1  
    if i % 3 != 0:
        resultado.append(abecedario[i])

print(f"Lista resultante: {', '.join(resultado)}.")
    
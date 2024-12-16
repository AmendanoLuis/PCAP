lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

print(lista1)

lista1.append("a")

print(lista1)

# Extiende la lista con otro array
lista1.extend(lista2)

print(lista1)

# Inserta al inicio de la lista
lista1.insert(1,9090)

print(lista1)

# Sumar con operadores y añadir a una nueval lista
lista1y2= lista1 + lista2

print(lista1y2)

# Añadir en bucle
mi_lista = []
for i in range(3):
    mi_lista.append(i)  # Añadimos números 0, 1, 2
print(mi_lista)




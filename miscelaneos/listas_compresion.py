'''listas por compresion'''

lista_1 = []

'''Lista de potencias de 10(10^0 a 10^5)'''
for n in range(6):
    lista_1.append(10 ** n)

'''Idem, usando una lista por compresion'''
lista_2 = [10 ** n for n in range(6)]

print(lista_1)
print(lista_2)

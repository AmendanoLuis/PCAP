def ordena_positivos(lst):

    # Ordenamos los números postivos de la lista de forma descendente
    # y lo guardamos en forma de lista dentro de positivos
    positivos = iter(sorted([i for i in lst if i > 0], reverse=True))

    return [next(positivos) if i > 0 else i for i in lst]


print(ordena_positivos([1, 3, 2, 4]))

print(ordena_positivos([-1, -3, -2, -4]))

print(ordena_positivos([3, -1, 2, -5, 4]))

print(ordena_positivos([0, -1, 3, 0, 2]))

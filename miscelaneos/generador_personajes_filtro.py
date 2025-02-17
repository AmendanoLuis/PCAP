import random
nombres = ['Ezio', 'Generalt', 'Kratos', 'Lara', 'Samus']
clases = ['Guerrero', 'Mago', "Arquero"]

personajes = [{
    "nombre": random.choice(nombres),
    "clase": random.choice(clases),
    "nivel": random.randint(1, 10)}
    for _ in range(5)]


personaje_filtrado = filter(lambda pej: pej['nivel'] > 5, personajes)

print("Personajes poderosos:")
for personaje in personaje_filtrado:
    print(personaje)
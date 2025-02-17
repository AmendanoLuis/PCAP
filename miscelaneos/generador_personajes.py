import random
nombres = ['Ezio', 'Generalt', 'Kratos', 'Lara', 'Samus']
clases = ['Guerrero', 'Mago', "Arquero"]

personajes = [{
    "nombre": random.choice(nombres),
    "clase": random.choice(clases),
    "nivel": random.randint(1, 10)}
    for i in range(5)]

for personaje in personajes:
    
    print(personaje)
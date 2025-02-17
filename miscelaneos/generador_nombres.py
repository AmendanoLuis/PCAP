import random

def generador_nombres():
    nombres = ['Arthas','Carlos','Pablo','David','Laura']
    random.shuffle(nombres)
    
    for nombre in nombres:
        yield nombre
        
generador = generador_nombres()

for _ in range(5):
    print(next(generador))
import random

# Función para determinar el ganador
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

# Lista con las opciones posibles
opciones = ["piedra", "papel", "tijera"]

# Bucle principal del juego
while True:
    # Solicitar al jugador su elección
    jugador = input("Elige entre 'piedra', 'papel' o 'tijera': ").lower()
    
    # Validar que la elección del jugador sea válida
    if jugador not in opciones:
        print("Opción no válida. Por favor, elige entre 'piedra', 'papel' o 'tijera'.")
        continue
    
    # Generar la elección de la computadora
    computadora = random.choice(opciones)
    
    # Mostrar las elecciones
    print(f"Tu elección: {jugador}")
    print(f"Elección de la computadora: {computadora}")
    
    # Determinar el ganador
    resultado = determinar_ganador(jugador, computadora)
    print(resultado)
    
    # Preguntar si se desea jugar nuevamente
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
    if jugar_de_nuevo != "sí":
        print("¡Gracias por jugar!")
        break

def mal_asunto(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise ValueError  # Regenera la excepcion
try:
    mal_asunto(0)
except (ArithmeticError,ValueError):
    print("¡Ya veo!")
    exit(0)

print("EN-FIN.")
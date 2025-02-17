import random
ataques_base = [random.randint(30,100) for _ in range(5)]

ataques_fuertes = list(map(lambda x:int(x * 1.2) if x > 50 else x, ataques_base))

print(f"Ataques base: {ataques_base}")
print(f"Ataques mejorados: {ataques_fuertes}")
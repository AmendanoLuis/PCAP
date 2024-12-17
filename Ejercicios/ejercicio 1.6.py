asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]

suspensas = []

for asignatura in asignaturas:
    mensaje = f"¿Que nota has sacado en {asignatura}? "
    entrada = input(mensaje)
    
    try:
        nota = float(entrada)
        
        if nota < 5:
            suspensas.append(asignatura)
        
    except ValueError: 
        print("Error en la nota, escribe una nota entre 0 y 10.")
            
print(f"Asignaturas Totales: {asignaturas}")
print(f"Asignaturas Suspensas: {suspensas}")
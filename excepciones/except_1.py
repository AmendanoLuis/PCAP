# EXCEPT 1.0

try:
    y= 1/0
    
# Excepción más concreta
except ZeroDivisionError:
    print("¡División entre cero!")
# Excepción más abastracta
except ArithmeticError:
    print("¡Problema Aritmético!")

# Excepción sin nombre
except:
    print("¡Algo ha ido mal...!")

print("FIN.")


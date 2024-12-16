
# EXCEPT 2.0

try:
    y= 1 /0
# Excepción menos concreta, menos código, misma funcionalidad
except (ZeroDivisionError,ArithmeticError):
    print("Hubo un problema al realizar la operación.")
# Excepción sin nombre
except:
    print("¡Algo ha ido mal...!")

print("FIN.")
import subprocess

resultado = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)

print("Salida del comando:")
print(resultado.stdout)

print("Luis Augusto Procel Amendaño")
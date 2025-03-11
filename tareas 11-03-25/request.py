import requests # type: ignore

# URL de web
url = "https://www.google.com"

# Obtener contenido de la web
response = requests.get(url)

# Imprimir contenido
print(f"Inicio respuesta Google \n {response.text[:500]} \n")
print("Fin de respuesta Google")
print("Luis Augusto Procel Amendaño")

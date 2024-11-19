


fecha=''

while True:
    fecha=input("introduce tu fecha de nacimiento en formato ( AAAAMMDD)")
    if fecha.isnumeric():
        break
        print("debes introducir una fecha en formato AAAAMMDD")

digito=0
suma=0

for i in fecha:
    suma+=int(i)
    print(suma)



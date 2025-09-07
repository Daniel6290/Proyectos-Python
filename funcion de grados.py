
#funcion para convertir centigrados a Fahrenheit viceversa

def conversion(grados, nomenclatura):
    if nomenclatura == "C":
        return (grados*1.8)+32
    elif nomenclatura == "F":
        return (grados-32)/1.8
    else:
        return "Nomenclatura no valida"

grados = float(input("Favor ingrese la cantidad de grados que le gustaria convertir "))
nomenclatura = str(input("Favor indique (C) si es celcius o (F) si es fahrenheit ")).upper()
resultado = conversion(grados, nomenclatura)
if nomenclatura == "C":
    print(resultado,"Grados Fahrenheit")
elif nomenclatura == "F":
    print(resultado, "Grados Celcius")

#crear una funcion que rote 90 grados una pieza de tetris
#el for va a comvertir cada columna de la pieza original en una fina de la nueva pieza
def rotar_pieza(pieza_original):
    nueva_matriz = []
    for i in range(3):
        nueva_fila = []
        for j in range(2, -1, -1):
            nueva_fila.append(pieza_original[j][i])
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

pieza_original = [
    [' ', 'x', ' '],
    [' ', 'x', 'x'],
    [' ', ' ', 'x']
]
pieza_nueva = rotar_pieza(pieza_original)

for fila in pieza_nueva:
    print(fila)
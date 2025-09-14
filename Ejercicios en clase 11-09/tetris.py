import random

tablero = []

for i in range(10):
    filas = []
    for i in range(10):
        filas.append("0")
    tablero.append(filas)
print("")

for filas in tablero:
    print("".join(filas))

PIEZA_CUADRADO = [
    ["X", "X"],
    ["X", "X"]
    ]

PIEZA_L = [
    ["X", "O"],
    ["X", "X"]
    ]

PIEZAS = [PIEZA_CUADRADO, PIEZA_L]

while True:
    pieza_a_ubicar = random.choice(PIEZAS)

    print("La pieza a ubicar es:")
    for i in pieza_a_ubicar:
        print("".join(i))
    print("")

    print("Dónde desea ubicarla?")
    seleccion_fila = int(input("Fila: "))
    seleccion_columna = int(input("Columna: "))
    print("")

    colision = False
    for i in range(2):
        for j in range(2):
            if (tablero[seleccion_fila + i][seleccion_columna + j] == "X") and (pieza_a_ubicar[i][j] == "X"):
                print("Colisión!")
                colision = True
                break
            else:
                tablero[seleccion_fila + i][seleccion_columna + j] = pieza_a_ubicar[i][j]

    if colision == True:
        break
    else:
        print("Pieza ubicada: ")
        for filas in tablero:
            print(filas)


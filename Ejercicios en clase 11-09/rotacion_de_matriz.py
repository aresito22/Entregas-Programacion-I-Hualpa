import random

matriz = []

for i in range(5):
    fila = ["a", "b", "c", "d", "e"]
    matriz.append(fila)

print("Matriz creada:")
for fila in matriz:
    print(fila)

def rotar_90(matriz):
    matriz_90 = []

    for i in range(5):
        filas = []
        for j in range(5):
            filas.append(matriz[j][i])
        matriz_90.append(filas)
    return matriz_90

def rotar_180(matriz):
    matriz_180 = []

    for i in range(4, -1, -1):
        filas = []
        for j in range(4, -1, -1):
            n = matriz[i][j]
            filas.append(n)
        matriz_180.append(filas)
    return matriz_180

def rotar_270(matriz):
    matriz_90 = []

    for i in range(4, -1, -1):
        filas = []
        for j in range(4, -1, -1):
            filas.append(matriz[j][i])
        matriz_90.append(filas)
    return matriz_90

while True:
    print("")
    print("1 - Rotar 90 grados")
    print("2 - Rotar 180 grados")
    print("3 - Rotar 270 grados")
    print("")
    opt = int(input("Rotación: "))
    print("")

    if opt == 1:
        print("Matriz rotada 90 grados: ")
        print("")
        matriz_90 = rotar_90(matriz)
        for filas in matriz_90:
            print(filas)
    elif opt == 2:
        print("Matriz rotada 180 grados: ")
        print("")
        matriz_180 = rotar_180(matriz)
        for filas in matriz_180:
            print(filas)
    elif opt == 3:
        print("Matriz rotada 270 grados: ")
        print("")
        matriz_270 = rotar_270(matriz)
        for filas in matriz_270:
            print(filas)          
    else:
        print("")
        print("Opción inválida.")
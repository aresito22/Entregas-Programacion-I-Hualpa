import random

barcos = []

for i in range(5):
    fila_barcos = []
    for i in range(5):
        i = random.randint(0, 1)
        fila_barcos.append(i)
    barcos.append(fila_barcos)

disparos = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append("-")
    disparos.append(fila)

print("Tablero de barcos:")
for filas in barcos:
    print(filas)

while True:
    print("")
    print("Tablero de disparos:")
    for filas in disparos:
        print(filas)

    print("")
    print("Ingrese el disparo a realizar:")
    intento_fila = int(input("Fila: "))
    intento_columna = int(input("Columna: "))

    if intento_fila > 4 or intento_columna > 4:
        print("")
        print("Fuera de rango.")
    elif barcos[intento_fila][intento_columna] == 1:
        print("")
        print("Acierto!")
        # Reemplaza la coordenada del tablero de disparos con X
        disparos[intento_fila][intento_columna] = "X"
        # Reemplaza la coordenada del tablero de barcos con 0, para luego evaluar si el barco fue efectivamente atacado
        barcos[intento_fila][intento_columna] = 0
    elif barcos[intento_fila][intento_columna] == 0:
        print("")
        print("Fallo.")
        disparos[intento_fila][intento_columna] = "0"

    contador = 0
    for filas in barcos:
        for i in filas:
            if i == 1:
                contador += 1
    
    if contador == 0:
        break

print("")
print("Le diste a todos los barcos!")
for filas in disparos:
    print(filas)
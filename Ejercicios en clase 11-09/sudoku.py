import random

sudoku = []

# Crear tablero
for i in range(4):
    fila = []
    for i in range(4):
        numero = random.randint(1, 4)
        fila.append(numero)

    sudoku.append(fila)
    
# Mostrar tablero
for fila in sudoku:
    print(*fila)

def validar_num_en_fila(num, fila):
    contador = 0
    for i in range(len(fila)):
        if fila[i] == num:
            contador += 1
    if contador > 1:
        return False
    else:
        return True
    
def validar_num_en_columna(num, indice, sudoku):
    contador = 0
    for fila in sudoku:
        if num == fila[indice]:
            contador += 1
    if contador > 1:
        return False
    else:
        return True

for fila in sudoku:
    for indice, num in enumerate(fila):
        valido = validar_num_en_fila(num,fila)
        if not valido:
            break
        else:
            valido = validar_num_en_columna(num, indice, sudoku)
            if not valido:
                break
    if not valido:
        break

if valido == True:
    print("El tablero de sudoku es válido.")
else:
    print("El tablero de sudoku no es válido.")
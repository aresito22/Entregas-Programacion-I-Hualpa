import random

matriz = []

for i in range(5):
    filas = []
    for j in range(5):
        n = random.randint(1, 100)
        filas.append(n)
    matriz.append(filas)

print("Matriz creada:")
for fila in matriz:
    print(fila)
print("")

for indice, fila in enumerate(matriz):
    suma = 0
    for i in fila:
        suma = suma + i
    print(f"La suma de los números en la fila {indice+1} es {suma}")
print("")

for i in range(5):
    suma = 0
    for j in range(5):
        suma = suma + matriz[j][i]
    print(f"La suma de los números en la columna {i+1} es {suma}")
print("")

numero_mayor = 0
for indice_fila, fila in enumerate(matriz):
    for indice_columna, i in enumerate(fila):
        if i > numero_mayor:
            numero_mayor = i
            localizacion_fila = indice_fila + 1
            localizacion_columna = indice_columna + 1

print(f"El número más grande en la matriz es {numero_mayor}; se encuentra en la posición {localizacion_fila}, {localizacion_columna}")
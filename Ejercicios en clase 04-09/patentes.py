ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMERO = "0123456789"

numero_usuario = int(input("Ingrese el número a buscar: "))
print("")

contador = 0

for i in ABECEDARIO:
    for j in ABECEDARIO:
        for k in ABECEDARIO:
            for l in NUMERO:
                for m in NUMERO:
                    for n in NUMERO:
                        patente = i + j + k + l + m + n
                        contador += 1

                        if contador == numero_usuario:

                            print(f"La patente es {patente}")
                            break
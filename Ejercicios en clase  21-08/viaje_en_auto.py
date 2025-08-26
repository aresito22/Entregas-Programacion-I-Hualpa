distancia = float(input("Ingrese la distancia a recorrer en kilometros: "))
precio = float(input("Ingrese el precio de la gasolina por litro: "))

litros_requeridos = (distancia / 100) * 8
costo_de_viaje = litros_requeridos * precio
horas_de_viaje = distancia / 90

print(f"Para el viaje se requerirán {litros_requeridos} litros.")
print(f"El costo del viajé será de {costo_de_viaje} pesos.")
print(f"El viaje durará {round(horas_de_viaje, 2)} horas asumiendo una velocidad de 90 KM/H")
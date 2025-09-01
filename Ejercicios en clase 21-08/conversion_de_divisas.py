monto_usd = float(input("Ingrese un monto en dolares: "))

tasa_de_cambio_usd_cop = 4042.47
tasa_de_cambio_usd_ars = 1365.0
tasa_de_cambio_usd_eur = 0.86

monto_cop = monto_usd * tasa_de_cambio_usd_cop
monto_ars = monto_usd * tasa_de_cambio_usd_ars
monto_eur = monto_usd * tasa_de_cambio_usd_eur

print(f"{monto_cop} pesos colombianos")
print(f"{monto_ars} pesos argentinos")
print(f"{monto_eur} euros")
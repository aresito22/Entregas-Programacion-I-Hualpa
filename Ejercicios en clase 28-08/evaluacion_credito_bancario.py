from utiles_es import pedir_texto

nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)
while " " not in nombre_completo:
    print("Debe ingresar su nombre completo.")
    nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)

cuit = pedir_texto("CUIT (sin guiones): ", permitir_vacio = False)
while len(cuit) != 11 or len(cuit) != 10:
    print("Número de CUIT inválido")
    cuit = pedir_texto("CUIT (sin guiones): ", permitir_vacio = False)

ingresos = float(input("Ingrese su sueldo mensual: "))
while ingresos < 0:
    print("Ingresos inválidos - no pueden ser menor a 0")
ingresos = float(input("Ingrese su sueldo mensual: "))

antiguedad = int(input("Antigüedad laboral (en años): "))
while antiguedad < 0:
    print("Antigüedad laboral inválida")
    antiguedad = int(input("Antigüedad laboral (en años): "))

print("Ingrese su historial crediticio:")
print("1 - Bueno")
print("2 - Regular")
print("3 - Malo")
historial = int(input())

if historial == 3 or ingresos < 200000:
    prestamo = "Rechazado"
elif ingresos >= 200000 and antiguedad < 2:
    prestamo = "Máximo 500.000"
elif ingresos >= 200000 and antiguedad >= 2:
    if historial == 2:
        prestamo = "Máximo 1.000.000"
    elif historial == 1:
        prestamo = "Máximo 3.000.000"

print("**RESUMEN**")
print(f"Cliente: {nombre_completo}")
print(f"CUIT: {cuit}")
print(f"Ingresos: ${ingresos}")
print(f"Antigüedad: {antiguedad}")

if historial == 1:
    print(f"Historial: bueno")
elif historial == 2:
    print(f"Historial: regular")
elif historial == 3:
    print(f"Historial: malo")

print(f"Prestamo: {prestamo}")
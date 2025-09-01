from utiles_es import pedir_texto

nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)
while " " not in nombre_completo:
    print("Debe ingresar su nombre completo.")
    nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)

edad = int(input("Ingrese su edad: "))
while edad < 0:
    print("Edad inválida.")
    edad = int(input("Ingrese su edad: "))

promedio = float(input("Ingrese su promedio general: "))
while 10 < promedio < 0:
    print("Promedio inválido - Ingrese un número decimal entre 0 y 10")
    promedio = float(input("Ingrese su promedio general: "))

ingresos_familiares_mensuales = float(input("Ingrese los ingresos familiares mensuales: "))
while ingresos_familiares_mensuales < 0:
    print("Ingresos inválidos - no pueden ser menor a 0")
    ingresos_familiares_mensuales = float(input("Ingrese los ingresos familiares mensuales: "))

if promedio < 6:
    status_beca = "Rechazado"
else:
    if ingresos_familiares_mensuales < 300000:
        status_beca = "Beca completa"
    elif 300000 <= ingresos_familiares_mensuales <= 600000:
        status_beca = "Media beca"
    elif ingresos_familiares_mensuales > 600000:
        status_beca = "Rechazado"

print("**RESUMEN**")
print(f"{nombre_completo}, {edad} años")
print(f"Promedio: {promedio}")
print(f"Ingresos familiares mensuales: {ingresos_familiares_mensuales}")
print(f"Resultado: {status_beca}")